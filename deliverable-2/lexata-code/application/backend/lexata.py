"""
This module provides the main entry point into the Lexata backend code, and is accessed by the server or other outside
code. It is responsible for providing an interface into the functionalities provided by the backend.

This class is also the point of interaction between the backend code (most notably the database.py file), and OpenAI.
It calls the babbage text search engine to obtain a vector embedding of the user's query. This matches the engine used
by the data scraping tool that embedded the items in the database to be searched from.

** Supported Functionalities: **

1) get_closest_to(). Receives a plain text query and obtains a text embedding vector from OpenAI. Then, calls the
methods provided by the LexataDB class in database.py to perform a search; ranking items in the database by how similar
their embeddings are to the query's. Returns the top-k results.

"""

import os
import openai

from openai.embeddings_utils import get_embedding, cosine_similarity
from dotenv import load_dotenv
from datetime import datetime
from database import LexataDB

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
