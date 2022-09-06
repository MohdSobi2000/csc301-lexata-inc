# This is a script to run the data scraping process from the SEC API.

from datetime import datetime
import os

from sec_api import QueryApi, ExtractorApi
from dotenv import load_dotenv
import csv
from codes import CODES

load_dotenv()

# environment variables
SEC_API_KEY = os.environ.get('sec-api-key')
COMPANIES = []
SECTORS = []


def extract_meta():
    # the endpoints of the sec-api we will be using
    queryApi = QueryApi(api_key=SEC_API_KEY)

    # using CSV writer, open document for writing
    with open('metadata.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Ticker', 'Company Name', 'Sector', 'Date', 'Incorporation Region', 'Filing Link'])
        for i in range(len(COMPANIES)):
            query = {
                'query': {'query_string': {
                    'query': f'ticker:{COMPANIES[i]} AND formType:\"10-K\"'
                }},
                'from': '0',
                'size': '1',
                'sort': [{'filedAt': {'order': 'desc'}}]
            }
            filings = queryApi.get_filings(query)
            try:
                country = filings['filings'][0]['entities'][0]['stateOfIncorporation']
            except:
                country = "XX"
            date = datetime.fromisoformat(filings['filings'][0]['filedAt']).strftime('%Y-%m-%d')
            link = filings['filings'][0]['linkToFilingDetails']
            company_name = filings['filings'][0]['companyName']
            data = [COMPANIES[i], company_name, SECTORS[i], date, CODES[country], link]
            writer.writerow(data)
            print(f'extracted data for: {company_name}')


# Populates the list of companies using the file provided of company tickers
def populate_companies():
    tickers = open('../data-scripts/companies.txt', 'r')
    for line in tickers:
        comp_str = line.split(",")
        COMPANIES.append(comp_str[0].strip('"'))
        SECTORS.append(comp_str[4].strip('"'))

if __name__ == '__main__':
    populate_companies()
    extract_meta()

