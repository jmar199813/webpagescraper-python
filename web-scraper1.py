import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Main_Page'  # Replace with the target URL

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
