import argparse
import concurrent.futures
import requests
from bs4 import BeautifulSoup
import urllib.parse

def search_bing(dork, num_pages):
    urls = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    for page in range(num_pages):
        query = f"https://www.bing.com/search?q={urllib.parse.quote(dork)}&first={page*10}"
        response = requests.get(query, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        for a in soup.find_all('a'):
            url = a.get('href')
            if url and not url.startswith('/search') and 'http' in url:
                urls.append(url)
    return urls

def process_url(url):
    try:
        response = requests.get(url)
        if "error in your SQL syntax" in response.text:
            print(f"Potential SQL vulnerability found: {url}")
        else:
            print(f"No SQL vulnerability found: {url}")
    except requests.RequestException as e:
        print(f"Failed to process {url}: {e}")

def main():
    parser = argparse.ArgumentParser(description="SQL Dork Scanner")
    parser.add_argument("-d", "--dork", type=str, required=True, help="Dork query")
    parser.add_argument("-e", "--engine", type=str, choices=["google", "bing"], required=True, help="Search engine")
    parser.add_argument("-p", "--pages", type=int, default=1, help="Number of pages to fetch")
    parser.add_argument("-t", "--threads", type=int, default=1, help="Number of threads to use")
    args = parser.parse_args()

    dork = args.dork
    engine = args.engine
    pages = args.pages
    threads = args.threads

    print(f"Searching for dork: {dork} using {engine} engine for {pages} pages with {threads} threads...")

    if engine == "google":
        print("Google search engine is not supported at this moment due to bot protection issues. Switching to Bing...")
        engine = "bing"

    if engine == "bing":
        urls = search_bing(dork, pages)
    else:
        urls = []

    print(f"Found {len(urls)} URLs.")

    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(process_url, urls)

if __name__ == "__main__":
    main()
