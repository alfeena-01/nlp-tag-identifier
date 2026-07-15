from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

def scrape_wikipedia(url):
    """
    Scrape paragraph text from a Wikipedia page.
    Returns the combined text as a string.
    """
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(req)
    html = response.read()
    soup = BeautifulSoup(html, 'html5lib')
    text = " ".join([p.get_text() for p in soup.find_all('p')])
    return text
