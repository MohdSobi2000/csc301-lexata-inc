"""
This module contains the class responsible for database interactions and processing, forming a Data Access Object. 

It connects with the Lexata instance of MongoDB. The `mongo-url` field must be specified in a .env file for this class 
to access the remote database. Please see the documentation to obtain the credentials.

** Supported functionalities: **

1) upload(). Uploads risk factor data to the database, under a given company's ticker. Compiles the company metadata
given, along with filing info, and creates a well-formatted collection for this company in the database. Each collection 
represents a single company, and contains a *single* company_info document. For each filing that has been uploaded, a 
filing_info document is included, and is indexed by a num_filings field for this company. Finally, each risk factor gets 
its own document, which references the id of a *specific* filing document. In this manner, we reduce redundancy in the
database while preserving all information associated with each risk factor.

2) delete(). Drops the collection associated with a company, thereby deleting it from the database.

3) get_top_k(). The main query function for the database. Our database requires support for ranking items based on a 
different search query each time, and thus there is no static way to compare items. We therefore require a custom 
comparator function to be passed in each time, to compare items. For example, this could be a function to compare items
based on how similar their embeddings are to the embeddings for a user's search query.

"""
from __future__ import annotations

import heapq
import logging
import os
import sys
from typing import Callable, Any

from bson import ObjectId
from dotenv import load_dotenv
from pymongo import MongoClient
from error_codes import ErrorCodes
from builders import *
from rf_handler import RiskFactorHandler

class LexataDB:

    # Initializer for the LexataDB class.
    def __init__(self) -> None:
        load_dotenv()       # load in the environment variables from a .env file
        self.logger = logging.getLogger("database")
        logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

    # Save a set of risk factors for a given company. The Company does not need to exist in the database yet.
    def upload(self, ticker: str, company_info: dict, filing_info: dict, contents: list[dict]) -> ErrorCodes:
        database = self._make_db_connection()
        if database is None:
            return ErrorCodes.DATABASE_CONNECTION_ERROR

        # find the existing metadata document, or create one
        result = database[ticker].find_one(company_info)
        if result is None:
            self.logger.info("company does not exist yet, creating collection")
            database[ticker].insert_one({"document_type": "company_info"} | build_c(company_info).to_dict())
        else:
            self.logger.info("company already exists")

        # find the existing filing document, or create one
        filing = database[ticker].find_one(filing_info)
        if filing is None:
            self.logger.info("filing does not exist yet")
            # get the existing company info doc, and reflect the addition of a new filing
            company_dict = database[ticker].find_one({"document_type": "company_info"})
            company = build_c(company_dict)
            company.add_filing()
            database[ticker].update_one({"_id": ObjectId(company_dict["_id"])}, {"$set": company.to_dict()})
            # create a new filing doc
            filing_id = company.get_num_filings()
            filing = build_f(filing_info | {"filing_id": filing_id})
            database[ticker].insert_one({"document_type": "filing_info"} | filing.to_dict())
        else:
            self.logger.warning("filing already exists, skipping upload")
            return ErrorCodes.UPLOAD_INVALID_CONTENTS_ERROR

        # collect and process data for upload
        data_to_upload = []
        for content in contents:
            risk_factor = build_rf(content)
            if risk_factor is None:
                self.logger.error("invalid contents, could not upload risk factor")
                return ErrorCodes.UPLOAD_INVALID_CONTENTS_ERROR
            data_to_upload.append(risk_factor)

        # upload the data
        database[ticker].insert_many([
            {
                "document_type": "risk_factor",
                "filing_id": filing_id
            } | data.to_dict() for data in data_to_upload])
        self.logger.info(f"uploaded risk factors for company {ticker}")
        return ErrorCodes.SUCCESS

    # A function to delete a given company's risk factors.
    def delete(self, ticker: str) -> ErrorCodes:
        database = self._make_db_connection()
        if database is None:
            return ErrorCodes.DATABASE_CONNECTION_ERROR

        results = database.drop_collection(ticker)
        if results["ok"] != 0:
            self.logger.info(f"deleted risk factors for company {ticker}")
            return ErrorCodes.SUCCESS
        self.logger.warning(results["errmsg"])
        return ErrorCodes.DELETE_ERROR

    # A function to get the top n items in the database using a custom function to compare documents. Here, k is an
    # integer, indicating the top-k results
    def get_top_k(self, k: int, comparator: Callable[[Any, Any], bool], sectors: list[str] = None) -> ErrorCodes | list:
        if k < 1:
            self.logger.error("invalid query")
            return []
        database = self._make_db_connection()
        if database is None:
            self.logger.error("issue with connecting to database")
            return []

        # get all items from the database for processing
        companies_in_sector = self._get_companies_in_sector(sectors) if sectors is not None \
            else database.list_collection_names()
        company_data = {}
        # filter by companies
        for company in companies_in_sector:
            company_data[company] = []
            c = build_c(database[company].find_one({"document_type": "company_info"}))
            # filter by filings
            for filing in database[company].find({"document_type": "filing_info"}):
                f = build_f(filing)
                # get all risk factors
                for risk_factor in database[company].find({
                    "document_type": "risk_factor",
                    "filing_id": f.get_filing_id()
                }):
                    rf = build_rf(risk_factor)
                    company_data[company].append(RiskFactorHandler(rf, f, c))

        # iterate over each returned item, each representing the info for a company, and look for the k-largest
        # we use a heap to accomplish this. we need to set and then unset the comparator before and after the operation
        heap = []
        RiskFactorHandler.set_rf_comparator(comparator)
        for company in company_data.keys():
            for risk_factor in company_data[company]:
                heapq.heappush(heap, risk_factor)
                if len(heap) > k:
                    heapq.heappop(heap)  # our heap will always contain k elements, if we go over, pop the smallest

        # the resulting heap contains the k-largest elements in the database (need to reverse the list)
        results = [rf.to_dict() for rf in sorted(heap, reverse=True)]
        RiskFactorHandler.unset_rf_comparator()
        return results

    # ===== helper functions =====

    # Return the sector of the given company.
    def _get_company_sector(self, ticker: str) -> dict:
        database = self._make_db_connection()
        return database[ticker].find_one({"document_type": "company_info"})

    # Returns the metadata of a company given a ticker.
    def _get_metadata(self, ticker: str, obj_id: str) -> dict:
        database = self._make_db_connection()
        return database[ticker].find_one({"_id": ObjectId(obj_id)}) | self._get_company_sector(ticker)

    # Returns a list of companies that are in a given sector.
    def _get_companies_in_sector(self, sectors: list[str]) -> list[str]:
        database = self._make_db_connection()
        return list(filter(lambda x: self._get_company_sector(x)["sector"].lower() in [i.lower() for i in sectors],
                           database.list_collection_names()))

    # Makes a connection to the database. Returns the MongoClient object on success, and None on failure.
    def _make_db_connection(self):
        try:
            client = MongoClient(os.environ.get("mongo-url"))
            self.logger.debug(client.server_info())
            return client["lexata"]
        except Exception as e:
            self.logger.error(e)
            return None
