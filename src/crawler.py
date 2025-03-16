from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Mozilla/5.0"}

def get_links(url):
    """Extract all absolute links from a given URL, ignoring JavaScript links."""
    try:
        response = requests.get(url, headers=HEADERS, timeout=5)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        links = set()

        for a in soup.find_all('a', href=True):
            href = a['href']
            if not href.startswith("javascript:"):  # Ignore JavaScript links
                absolute_url = urljoin(url, href)
                links.add(absolute_url)

        return list(links)

    except requests.RequestException as e:
        print(f"Error fetching links: {e}")
        return []

