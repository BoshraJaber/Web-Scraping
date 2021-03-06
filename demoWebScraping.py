# Demo: scraping Bayt web app

import requests
from bs4 import BeautifulSoup
######## step 1 ###############
domain ='https://www.bayt.com'
bayt_url = f'{domain}/en/jordan/jobs/python-jobs/'
response = requests.get(bayt_url)

# print(response.headers)
# response.content , response.status_code, response.headers

html_text = response.text # will print the html page as it is

# The following code will create a file with the content
# with open("file.html",'w') as file:
#     file.write(html_text)
# print(html_text)


######## step 2 ###############
soup = BeautifulSoup(html_text, 'html.parser')
# print(soup.prettify())
result = soup.find('div', id='results_inner_card')
jobs = result.find_all('li', class_='has-pointer-d')
# print(len(jobs))
# print(jobs[0])

# title = jobs[0].find('h2').text.strip()
# company = jobs[0].find('b').text.strip()
# desc = jobs[0].find('p').text.strip()
# link = f"{domain}{jobs[0].find('a').get('href')}"

# print(title)
# print(company)
# print(desc)
# print(link)

# cleaned_jobs = []
# for job in jobs:
#     title = job.find('h2').text.strip()
#     company = job.find('b').text.strip()
#     desc = job.find('p').text.strip()
#     link = f"{domain}{job.find('a').get('href')}"
#     cleaned_job = {"title":title, 'company':company, 'desc':desc, 'link':link}
#     cleaned_jobs.append(cleaned_job)

def clean_job(dirty_job):
    title = dirty_job.find('h2').text.strip() # we use strip to remove any spaces
    company = dirty_job.find('b').text.strip()
    desc = dirty_job.find('p').text.strip()
    link = f"{domain}{dirty_job.find('a').get('href')}"
    return {"title":title, 'company':company, 'desc':desc, 'link':link}

######## step 3 ###############
cleaned_jobs = [clean_job(job) for job in jobs]

# print(cleaned_jobs)

import json

######## step 4 ###############
json_data = json.dumps(cleaned_jobs)
# print(json_data)

######## step 5 ###############
with open('json_data.json','w') as file:
    file.write(json_data)