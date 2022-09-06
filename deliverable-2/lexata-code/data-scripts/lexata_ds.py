# This is a script to run the data scraping process from the SEC API.

import os
import sys
import csv

import openai
from openai.embeddings_utils import get_embedding
from sec_api import ExtractorApi
from pymongo import MongoClient
from dotenv import load_dotenv
from sec10kparser import parse_html
from env_classification import create_risk_embeddings, perform_env_classification
from application.backend.database import LexataDB

# environment variables
load_dotenv()
SEC_API_KEY = os.environ.get('sec-api-key')
OAI_API_KEY = os.environ.get('open-ai-api-key')
MONGO_URL = os.environ.get('mongo-url')


def get_and_save(all_companies, debug):
    # the endpoints of the sec-api we will be using
    extractor_api = ExtractorApi(api_key=SEC_API_KEY)

    # the database we will be using
    client = MongoClient(MONGO_URL)
    db = client.lexata

    # open AI's API key needs to be set
    openai.api_key = OAI_API_KEY

    # for each company, we will get the risk factors, calculate embeddings, and save to the database
    for company in all_companies:
        # get the urls from the metadata file
        with open('metadata.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == company:
                    ticker = row[0]
                    comp_name = row[1]
                    sector = row[2]
                    date = row[3]
                    link = row[4]
                    break

        section_html = extractor_api.get_section(link, '1A', 'html')
        section_text = extractor_api.get_section(link, '1A', 'text')
        
        # now, we use the extractor endpoint to get the actual html data, and parse it using the Beautiful Soup library
        # we want to extract out only the actual text (the text endpoint doesn't do a great job at this...)
        risk_factors = parse_html(section_html, section_text)

        # now perform env classification to find relevant risk factors
        risk_embeddings = create_risk_embeddings(risk_factors)
        env_risk_factors = perform_env_classification(risk_embeddings)

        # for each risk factor, we obtain the embeddings and save it to the database
        risk_count = 1
        for header in env_risk_factors:
            db[company].insert_one({
                'ticker' : ticker,
                'company' : comp_name,
                'sector' : sector,
                'link' : link,
                'ID' : f"{ticker}-{date}-RF-{risk_count}",
                'header' : header,
                'text': env_risk_factors[header],
                'embedding': get_embedding(header, engine='text-search-babbage-doc-001')
            })
            risk_count += 1

        if debug:
            print(f'extracted data for: {company}')


if __name__ == '__main__':

    # manual mode: insert companies as command line arguments; -m  must be the last flag given
    if '-m' in sys.argv:
        companies = sys.argv[(sys.argv.index('-m') + 1):]
    # file mode: specify the file from where to receive company tickers
    elif '-f' in sys.argv:
        filename = sys.argv[sys.argv.index('-f') + 1] if len(sys.argv) > sys.argv.index('-f') + 1 \
            else 'company_tickers.txt'
        with open(filename, 'r') as f:
            companies = [i.strip('\n').strip('"') for i in f.readlines()]
    else:
        print('Usage: (-v) -m <company1> <company2> ... OR -f <filename>')
        exit(0)

    get_and_save(companies, '-v' in sys.argv)
