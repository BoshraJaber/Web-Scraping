# Lab17: Web Scraping

* Web scraping, web harvesting, or web data extraction is data scraping used for extracting data from websites. The web scraping software may directly access the World Wide Web using the Hypertext Transfer Protocol or a web browse
* Web scraping is the process of using bots to extract content and data from a website
* Unlike screen scraping, which only copies pixels displayed onscreen, web scraping extracts underlying HTML code and, with it, data stored in a database.
* Example: Use the API of the website (if it exists). For example, Facebook has the Facebook Graph API which allows retrieval of data posted on Facebook. Access the HTML of the webpage and extract useful information/data from it. This technique is called web scraping or web harvesting or web data extraction.

* It is not illegal unless it is mentioned in the term of services of the website

![](https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2018/11/Untitled-1-768x183.jpg)

# Library used:
* bs4
* beautiful soup from bs4

## how to asset if a website is good for scraping or not 
1. if there is a repeated info then It is better to web scrap it then to copy and paste it

## Steps to scraping:
1. Get the HTML: define the website and its elements
 * send http request in python
2. Parse HTML for element with its class
 * HTML parser (parsing is making sense of something)
3. Get text from h2 saved as title
4. Get text from div
5. save it as description
