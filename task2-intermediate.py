import requests
from bs4 import BeautifulSoup


def web_scraper(url):
    """
    Scrapes data from a website using requests and BeautifulSoup.
    """
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract all paragraphs as example
        paragraphs = soup.find_all('p')
        
        print(f"\n--- Web Scraper Results for {url} ---")
        print(f"Status Code: {response.status_code}\n")
        
        if paragraphs:
            for i, p in enumerate(paragraphs[:5], 1):
                print(f"{i}. {p.get_text().strip()[:100]}...")
        else:
            print("No paragraphs found.")
            
        return soup
        
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None


if __name__ == "__main__":
    url = input("Enter the URL to scrape (press Enter for https://example.com): ").strip()
    if not url:
        url = "https://example.com"
    web_scraper(url)

