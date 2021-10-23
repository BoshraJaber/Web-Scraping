# Lab17: Web Scraping

* Web scraping, web harvesting, or web data extraction is data scraping used for extracting data from websites. The web scraping software may directly access the World Wide Web using the Hypertext Transfer Protocol or a web browse
* Web scraping is the process of using bots to extract content and data from a website
* Unlike screen scraping, which only copies pixels displayed onscreen, web scraping extracts underlying HTML code and, with it, data stored in a database.
* Example: Use the API of the website (if it exists). For example, Facebook has the Facebook Graph API which allows retrieval of data posted on Facebook. Access the HTML of the webpage and extract useful information/data from it. This technique is called web scraping or web harvesting or web data extraction.

* It is not illegal unless it is mentioned in the term of services of the website

![](https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2018/11/Untitled-1-768x183.jpg)

# Library used:
* requests
* beautifulsoup4
* json

## how to asset if a website is good for scraping or not 
1. if there is a repeated info then It is better to web scrap it then to copy and paste it

## Steps to scraping:
1. Get the HTML: define the website and its elements
 * send http request in python using **requests** HTTP library
2. Parse HTML for element with its class
 * HTML parser (parsing is making sense of something) with Beautiful Soup library
3. Get text from h2 saved as title
4. Get text from div
5. save it as description

## How to code it:
1. `response = requests.get(bayt_url).text`
2.  `soup = BeautifulSoup(response, 'html.parser') `
    `result = soup.find('div', id='results_inner_card')`
    `jobs = result.find_all('li', class_='has-pointer-d')`
3. Loop over jobs to get what we want : ` title = job.find('h2').text.strip()`
4. Creating a dictionary: `cleaned_jobs = [clean_job(job) for job in jobs]` , calling the function for each element
5. dealing with the data: stoing it in a json file: `json_data = json.dumps(cleaned_jobs)`


## Useful Sources:
* [Requests: HTTP Library for Humans](https://docs.python-requests.org/en/latest/)
* [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/)