import requests
from bs4 import BeautifulSoup
from urllib.robotparser import RobotFileParser

# Function to check if scraping is allowed
def is_scraping_allowed(url):
    # Parse the base URL to get the robots.txt URL
    base_url = '/'.join(url.split('/')[:3])  # Extract protocol and domain
    robots_url = f"{base_url}/robots.txt"
    
    rp = RobotFileParser()
    rp.set_url(robots_url)
    rp.read()
    
    return rp.can_fetch("*", url)

url = input("Enter the URL to scrape: ")

if not is_scraping_allowed(url):
    print("Scraping not allowed by robots.txt")
    exit()

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')
    
    headings = soup.find_all(['h1', 'h2', 'h3'])
    for heading in headings:
        print(heading.text.strip())

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
