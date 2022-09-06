import pprint

from openai.embeddings_utils import cosine_similarity
from database import LexataDB
from error_codes import ErrorCodes

lb = LexataDB()
# lb.delete("GOOG")


# print(lb.upload(ticker="GOOG",
#                 company_info={
#                     "ticker": "GOOG",
#                     "name": "Google",
#                     "sector": "IT",
#                     "jurisdiction": "U.S.",
#                 },
#                 filing_info={
#                     "date": "2023-01-01",
#                     "link": "https://google.com",
#                 },
#                 contents=[
#                     {"header": "some header 1", "text": "some risk factor 1", "embeddings": [1, 2, 3]},
#                     {"header": "some header 2", "text": "some risk factor 2", "embeddings": [4, 5, 6]}]))

# print(lb.get_company_info("GOOG"))

# print(lb.get_top_k())
#
for i in lb.get_top_k(k=2,
                      comparator=lambda x, y: cosine_similarity([1, 2, 3], x) < cosine_similarity([1, 2, 3], y),
                      sectors=["IT"]):
    pprint.pprint(i)

# print(lb.get_top_k(k=3,
#              comparator=lambda x, y: cosine_similarity([1, 2, 3], x) < cosine_similarity([1, 2, 3], y),
#              sectors=["IT"]))
