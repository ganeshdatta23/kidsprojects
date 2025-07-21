import requests
from bs4 import BeautifulSoup

def basic_web_scraper():
    print("Welcome to the Basic Web Scraper!")
    url = input("Enter the URL to scrape: ")

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')

        # Example: Extract all paragraph texts
        paragraphs = soup.find_all('p')
        print("\n--- Paragraphs ---")
        for p in paragraphs:
            print(p.get_text())

        # Example: Extract all links
        links = soup.find_all('a')
        print("\n--- Links ---")
        for link in links:
            print(link.get('href'))

    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    basic_web_scraper()
