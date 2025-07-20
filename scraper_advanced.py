import requests
from bs4 import BeautifulSoup

def run():
    url = "https://example.com"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    print("[Scraper] Title:", soup.title.string)
