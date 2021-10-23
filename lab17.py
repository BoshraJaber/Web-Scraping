import requests
from bs4 import BeautifulSoup
import json

# Your web scraper should report the number of citations needed.
# Count function must be named get_citations_needed_count
# get_citations_needed takes in a url and returns an integer

url = 'https://en.wikipedia.org/wiki/History_of_Mexico'
def get_citations_needed_count(url):
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'html.parser')
    citations_needed = soup.find_all('span',text="citation needed" )
    return len(citations_needed)
    
    

get_citations_needed_count(url)

# Your web scraper should identify those cases AND include the relevant passage.
# E.g. Citation needed for “lorem spam and impsum eggs”
# Consider the “relevant passage” to be the parent element that contains the passage, often a paragraph element.
# Report function must be named get_citations_needed_report
# get_citations_needed_report takes in a url and returns a string
# the string should be formatted with each citation needed on own line, in order found.

def get_citations_needed_report(url):
    result = ''
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'html.parser')
    citations_needed = soup.find_all('span',text="citation needed" )
    for span in citations_needed:
        result += f"""{span.parent.parent.parent.parent.text}\r\n"""
    return result
    
 
relevant_passages = get_citations_needed_report(url) 

print(relevant_passages)

json_passages = json.dumps(relevant_passages)
with open('json_passages.json','w') as file:
    file.write(json_passages)