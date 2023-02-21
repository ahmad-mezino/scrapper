from scrapingant_client import ScrapingAntClient
import requests
import json
from bs4 import BeautifulSoup

API_KEY = "2894f7e9ccc24cb28b7e1d7ae108c6ff"

# search_url = "https://www.linkedin.com/jobs/search/?keywords=python&location=United%20States"
# scrapingant_url = f"https://api.scrapingant.com/v2/extended?url={search_url}&x-api-key={API_KEY}"
# scrapingant_url = f"https://api.scrapingant.com/v2/general?url={search_url}&x-api-key={API_KEY}"

scrapingant_url='https://api.scrapingant.com/v2/extended?url=https://www.linkedin.com/jobs/search/?keywords=React js&location=United%20States&x-api-key=2894f7e9ccc24cb28b7e1d7ae108c6ff'


# Send a GET request to the ScrapingAnt API endpoint to retrieve the rendered LinkedIn job search page HTML
response = requests.get(scrapingant_url)

# Parse the JSON response from the ScrapingAnt API into a Python dictionary
data = json.loads(response.text)
print(data)

# Check if the API response contains the expected content key
# if "content" not in data:
#     print("ScrapingAnt API failed to render the page correctly. Response:", data)
#     exit()

# # Extract the HTML content of the LinkedIn job search page from the dictionary
html = data["text"]

# Use BeautifulSoup to parse the HTML and extract job listings
soup = BeautifulSoup(html, "html.parser")
print(soup)

# Find all the job listings on the page
listings = soup.find_all("li", {"class": "result-card"})
print("listing")
print(listings)


for listing in listings:

    job_title = listing.find("h3", {"class": "result-card__title"}).text.strip()
    print("Job Title:", job_title)
    
    job_description = listing.find("div", {"class": "result-card__contents job-result-card__contents"}).text.strip()
    print("Job Description:", job_description)
    
    company_name = listing.find("a", {"class": "result-card__subtitle-link job-result-card__subtitle-link"}).text.strip()
    print("Company Name:", company_name)
    
    company_link = listing.find("a", {"class": "result-card__subtitle-link job-result-card__subtitle-link"})["href"]
    print("Company Link:", company_link)
    
    company_location = listing.find("span", {"class": "job-result-card__location"}).text.strip()
    print("Company Location:", company_location)
    


