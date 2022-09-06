"""
The script for parsing data from the U.S. Securities and Exchange Commission (SEC) into a machine-ready format for the
database and backend code to interact with.

"""

from bs4 import BeautifulSoup

def _get_text_from_html(html_divs):

    bold_underlined_text = []     
    for div in html_divs:
        # if no text, move on
        if not div.get_text():
            continue
        spans = div.find_all('span')
        # check if bold, underlined, italic (heading)
        if ('font-weight:700' in str(spans[0])) or ('font-style:italic' in str(spans[0])) or ('underline' in str(spans[0])): 
            bold_underlined_text.append(div.get_text())

    return bold_underlined_text


def parse_html(html, text):

    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.find_all('div')
    bold_underlined_text = _get_text_from_html(divs) 

    parsed_text = text.splitlines()

    parsed_text[:] = [x for x in parsed_text if x]  # remove empty strings

    risk_factors = []   # contains lists of header and paragraph(s) pairs for each risk factor
    temp_risk_factors = []
    heading_count = 0

    for paragraph in parsed_text:

        # Fixing badly formatted output from text endpoint of sec-api
        if " ." in paragraph:
            paragraph = paragraph.replace(" .", ".")
        if " ," in paragraph:
            paragraph = paragraph.replace(" ,", ",")
        if paragraph[len(paragraph)-1] == " ":
            paragraph = paragraph[:len(paragraph)-1]


        if len(paragraph) < 30: # removes page numbers and short text
            continue

        if (not paragraph[0].islower()) and (paragraph in ' '.join(bold_underlined_text)):     # heading

            heading_count +=1

            if temp_risk_factors == []:
                temp_risk_factors = [paragraph, ""]
            elif temp_risk_factors[1] != [] and temp_risk_factors[1] != "":   # we have finished a heading + risk factor
                risk_factors.append(temp_risk_factors)
                temp_risk_factors = [paragraph, ""]
            elif temp_risk_factors[1] != [] and temp_risk_factors[1] == "":     # second heading before the text
                temp_risk_factors[0] = paragraph

        else:
            if temp_risk_factors == []:
                continue
            elif temp_risk_factors[1] == "":
                temp_risk_factors[1] = paragraph
            elif paragraph[0].islower():
                temp_risk_factors[1] += paragraph
            elif not paragraph[0].isalpha():   
                temp_risk_factors[1] += '\n' + paragraph
            else:
                temp_risk_factors[1] += '\n\n' + paragraph
   
    risk_factors.append(temp_risk_factors)

    # for i in range(len(risk_factors)):
    #     print(risk_factors[i])
    #     print("------Header------")
    #     print(risk_factors[i][0])
    #     print("------Body------")
    #     print(risk_factors[i][1])
    #     print("\n")
    #     i += 1
    # print(len(risk_factors))
    # print(heading_count)

    return risk_factors
