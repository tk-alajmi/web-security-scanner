import requests
from bs4 import BeautifulSoup

def get_links(url):
    """Extract all links from a given URL"""
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        links = [a['href'] for a in soup.find_all('a', href=True)]
        return links

    except requests.RequestException as e:
        print(f"Error fetching links: {e}")
        return []

if __name__ == "__main__":
    url = input("Enter target URL: ")
    found_links = get_links(url)
    print("Found URLs:")
    for link in found_links:
        print(link)
