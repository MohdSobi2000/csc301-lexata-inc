import os
import openai

from openai.embeddings_utils import get_embedding, cosine_similarity
from dotenv import load_dotenv
from datetime import datetime
from .database import LexataDB


# The main python module for Lexata. Connects to the database and provides methods to perform searches, given a query.
# Uses the OpenAI library to rank and compare items in the database.
class Lexata:

    # Initializes an instance of a Lexata object. Needs an api key to be provided to access OpenAI.
    def __init__(self) -> None:
        load_dotenv()
        openai.api_key = os.environ.get('open-ai-api-key')
        self._db = LexataDB()
        self.timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # Given a query string, calculate cosine similarity with all other items in the database & return the closest.
    def get_closest_to(self, query: str, k: int = 1, sectors: list = None) -> dict:
        qe = get_embedding(query, engine='text-search-babbage-query-001')
        top_k = []
        for risk_factor in self._db.get_top_k(
                k=k,
                comparator=lambda x, y: cosine_similarity(qe, x) < cosine_similarity(qe, y),
                sectors=sectors
        ):
            top_k.append(risk_factor)
        return {i + 1: j for i, j in enumerate(top_k)}
