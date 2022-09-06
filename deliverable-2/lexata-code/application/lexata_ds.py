"""
A script to run the data scraping process:

1) Obtain risk factor data from the U.S. Securities and Exchange Commission by calling provided API endpoints.
2) Parse the data into a machine-ready dictionary/JSON format using the sec10kparser script.
3) Perform classification on the risk factors obtained - keep only those relating to the environment.
4) Vectorize each piece of text by obtaining an embedding from OpenAI's babbage text search engine.
5) Upload the documents to the database.

** Usage Instructions: **

This file can be run with the following command: `python3 lexata_ds.py` , with the following flags:
-v: verbose; an optional flag to print debugging information and status updates.
-m <company1> <company2> ... : runs the script on a set of companies, given by the user at the command line. While there
is no limit on the number of companies provided in this manner, for bulk uploads you should use the -f option instead.
Note that this flag must come after all the others, since all remaining arguments will be interpreted as companies.
-f <filename>: runs the script on all the companies listed in the given file.

"""

import os
import sys
import csv

import openai
from openai.embeddings_utils import get_embedding
from sec_api import ExtractorApi
from dotenv import load_dotenv
from backend.data_scrape_scripts.sec10kparser import parse_html
from backend.data_scrape_scripts.env_classification import create_risk_embeddings, perform_env_classification
from backend.database import LexataDB
from backend.error_codes import ErrorCodes

# environment variables
load_dotenv()
SEC_API_KEY = os.environ.get('sec-api-key')
OAI_API_KEY = os.environ.get('open-ai-api-key')
MONGO_URL = os.environ.get('mongo-url')


def get_and_save(all_companies, debug):
    # the endpoints of the sec-api we will be using
    extractor_api = ExtractorApi(api_key=SEC_API_KEY)

    # open AI's API key needs to be set
    openai.api_key = OAI_API_KEY

    # for each company, we will get the risk factors, calculate embeddings,
    # and save to the database
    for company in all_companies:
        # get the urls from the metadata file
        with open('backend/data_scrape_scripts/metadata.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == company:
                    ticker = row[0]
                    comp_name = row[1]
                    sector = row[2]
                    date = row[3]
                    region = row[4]
                    link = row[5]
                    break
        attempts = 0
        call_api = True
        while call_api and attempts < 20:
            call_api = False
            attempts += 1
            print("another attempt")
            try:
                section_html = extractor_api.get_section(link, '1A', 'html')
                section_text = extractor_api.get_section(link, '1A', 'text')
            except TypeError:
                call_api = True


        # now, we use the extractor endpoint to get the actual html data,
        # and parse it using the Beautiful Soup library we want to extract
        # out only the actual text (the text endpoint doesn't do a great job
        # at this...)
        risk_factors = parse_html(section_html, section_text)

        # now perform env classification to find relevant risk factors
        risk_embeddings = create_risk_embeddings(risk_factors)
        env_risk_factors = perform_env_classification(risk_embeddings)

        # for each risk factor, we obtain the embeddings and save it to the
        # database
        lexata_db = LexataDB()
        to_upload = []
        for header in env_risk_factors:
            for risk_factor in env_risk_factors[header].split("\n\n"):
                to_upload.append({
                    "header": header,
                    "text": risk_factor,
                    "embeddings": get_embedding(risk_factor, "text-search-babbage-doc-001")
                })

        # upload each
        company_info = {
            "ticker": ticker,
            "company_name": comp_name,
            "sector": sector,
            "jurisdiction": "U.S."
        }
        filing_info = {
            "date_of_filing": date,
            "link_to_filing": link
        }

        ret = lexata_db.upload(ticker, company_info, filing_info, to_upload)
        if ret != ErrorCodes.SUCCESS and debug:
            print(ret)
        elif debug:
            print(f'extracted data for: {company}')


if __name__ == '__main__':

    # manual mode: insert companies as command line arguments; -m  must be
    # the last flag given
    if '-m' in sys.argv:
        companies = sys.argv[(sys.argv.index('-m') + 1):]
    # file mode: specify the file from where to receive company tickers
    elif '-f' in sys.argv:
        filename = sys.argv[sys.argv.index('-f') + 1] if len(sys.argv) > \
                                                         sys.argv.index('-f') \
                                                         + 1 \
            else 'company_tickers.txt'
        with open(filename, 'r') as f:
            companies = [i.strip('\n').strip('"') for i in f.readlines()]
    else:
        print('Usage: (-v) -m <company1> <company2> ... OR -f <filename>')
        exit(0)

    get_and_save(companies, '-v' in sys.argv)
