"""
The script for performing classification on Risk Factor headings.

Classification method: Zero-shot classification

Embeds short descriptions of each label (env, nonenv), then compare cosine distance between embeddings of samples and
label descriptions. The highest similarity label to the sample input is the predicted label.

"""

import openai
from openai.embeddings_utils import cosine_similarity, get_embedding
from dotenv import load_dotenv
import os

# environment variables
load_dotenv()
OAI_API_KEY = os.environ.get('open-ai-api-key')
FILE_ID = 'file-9MBwIDal5jkLtsOgZifvQZN9'

testing_db = {"Catastrophic events or geopolitical conditions may disrupt our business.": "Env",
      "Natural disasters and unusual weather conditions (whether or not caused by climate change), pandemic outbreaks or other health crises, political or civil unrest, acts of violence or terrorism, and disruptive global political events could disrupt business and result in lower sales and otherwise adversely affect our financial performance.": "Env",
      "Product liability, product recall or other product safety or labeling claims could adversely affect our business, reputation and financial performance.": "Non-env",
      "Our current insurance program may expose us to unexpected costs and negatively affect our financial performance.": "Non-env",
      "We may not successfully identify, complete, or realize the benefits from strategic acquisitions, alliances, divestitures, joint ventures, or other investments.": "Non-env",
      "We may not be able to successfully execute our strategic initiatives.": "Non-env",
      "Our international operations subject us to additional risks and costs and may cause our profitability to decline.": "Non-env",
      "Our intellectual property rights are valuable, and any inability to protect them could reduce the value of our products and brands.": "Non-env",
      "The Sponsors have substantial control over us and may have conflicts of interest with us in the future.": "Non-env",
      "We may be unable to realize the anticipated benefits from prior or future streamlining actions to reduce fixed costs, simplify or improve processes, and improve our competitiveness.": "Non-env",
      "Our level of indebtedness, as well as our ability to comply with covenants under our debt instruments, could adversely affect our business and financial condition.": "Non-env",
      "Additional impairments of the carrying amounts of goodwill or other indefinite-lived intangible assets could negatively affect our financial condition and results of operations.": "Non-env",
      "Our net sales and net income may be exposed to foreign exchange rate fluctuations.": "Non-env",
      "Commodity, energy, and other input prices are volatile and could negatively affect our consolidated operating results.": "Non-env",
      "Volatility in the market value of all or a portion of the derivatives we use to manage exposures to fluctuations in commodity prices may cause volatility in our gross profit and net income.": "Non-env",
      "Our compliance with laws and regulations, and related legal claims or regulatory enforcement actions, could expose us to significant liabilities and damage our reputation.": "Non-env",
      "A downgrade in our credit rating could adversely impact interest costs or access to future borrowings.": "Non-env",
      "The ability of suppliers to deliver raw materials, parts and components to our manufacturing facilities, and our ability to manufacture without disruption, could affect our results of operations.": "Env",
      "Global climate change and related regulations could negatively affect our business.": "Env",
      "We are subject to requirements relating to environmental and safety regulations and environmental remediation matters which could adversely affect our business, results of operation and reputation.": "Env",
      "Significant increases in prices for raw materials, energy, transportation or other necessary supplies or services, without corresponding increases in our selling prices, could adversely affect our financial results.": "Env",
      "Climate Change: Climate change-related risks and uncertainties, legal or regulatory responses to climate change and failure to meet the Company’s climate change commitments could negatively impact the Company’s results of operations, financial condition and/or reputation.": "Env",
      "The Company and certain of its suppliers and customers are experiencing difficulties obtaining certain raw materials and components, and the cost of most of the Company’s raw materials and components is increasing.": "Env",
      "Severe weather, natural disasters and other similar events could materially adversely affect us.": "Env",
      "Increasing activities and projects intended to advance new energy technologies could introduce new risks to our businesses.": "Env",
      "Conditions beyond our control can interrupt our supplies, increase our product costs and impair our ability to deliver products and services to our customers.": "Env",
      "Climate change and volatile adverse weather conditions could adversely affect our restaurant sales or results of operations.": "Env",
      "Climate change and severe weather may adversely affect our and our joint ventures’ facilities and ongoing operations.": "Env",
      "There are certain environmental hazards and risks inherent in our operations that could adversely affect those operations and our financial results.": "Env",
      "Natural or man-made disasters, an outbreak of highly infectious or contagious disease, political instability, civil unrest, terrorist activity or war could materially adversely affect the number of visitors to our facilities and disrupt our operations.": "Env"}

# returns a similarity vector 
def keyword_score(header_embedding, keyword_embeddings):
    header_score = []
    for keyword in keyword_embeddings:
        similarity = cosine_similarity(header_embedding, keyword)
        header_score.append(similarity)
    
    return header_score

# inputs a list of risk_factors: []
# returns risk_embeddings dict: {header_text: body_text}
def create_risk_embeddings(risk_factors, engine="text-similarity-babbage-001"):
    risk_embeddings = {}

    for risk_factor in risk_factors:
        header = risk_factor[0]
        body = risk_factor[1]
        embedding = get_embedding(header, engine)
        risk_embeddings[header] = (embedding, body)

    return risk_embeddings

def perform_env_classification(risk_factors, engine='text-similarity-babbage-001'):
    keywords = ['Paris Agreement', 
                'Scenario Analysis', 
                'GHG', 
                'Greenhouse gas emissions', 
                'Scope 3',
                'environment', 
                'climate change', 
                'TCFD', 
                'Task Force on Climate Related Financial Disclosure', 
                'International Sustainability Standards Board', 
                'Sustainability Accounting Standards Board', 
                'SASB', 
                'ISSB', 
                'natural disasters',
                'fossil fuels',
                'gas',
                'raw materials',
                'green energy']
        
    keyword_embeddings = []
    for keyword in keywords:
        keyword_embeddings.append(get_embedding(keyword, engine))
    
    env_risk_factor = {}
    for header in risk_factors:
        scores = keyword_score(risk_factors[header][0], keyword_embeddings)

        for score in scores:
            if score >= 0.70:
                print("ENV FOUND - ZERO-SHOT CLASSIFICATION")
                
                classification_result = openai.Classification.create(
                    file=FILE_ID,
                    query=header,
                    search_model='ada',
                    model='curie',
                    max_examples=3
                )

                # found env risk factor
                if classification_result["label"] == 'Env':
                    print("ENV FOUND - CLASSIFICATION ENDPOINT")
                    env_risk_factor[header] = risk_factors[header][1]

                break
    
    return env_risk_factor

if __name__ == '__main__':
    # perform classification
    # db_embeddings = create_risk_embeddings(testing_db)
    # classifications = perform_env_classification(db_embeddings)
    openai.api_key = OAI_API_KEY
    # upload training_data file 
    file = openai.File.create(
        file=open("training_data", encoding="utf8"),
        purpose="classifications"
    )

    print(file['id'])
