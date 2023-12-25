import requests
from bs4 import BeautifulSoup
import time

def search_google(query):
    google_url = f"https://www.google.com/search?q={query}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    response = requests.get(google_url, headers=headers)

    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch search results for query: {query}")
        return None

def extract_top_result_url(html):
    soup = BeautifulSoup(html, 'html.parser')
    result_div = soup.find('div', {'class': 'tF2Cxc'})
    if result_div:
        link = result_div.find('a')['href']
        return link
    else:
        return None

def extract_text_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()
        return text
    else:
        print(f"Failed to fetch content from URL: {url}")
        return None

def main():
    with open("unique_titles_1.txt", "r", encoding="utf-8") as file:
        titles = [title.strip() for title in file.readlines()]

    for i, title in enumerate(titles, start=1):
        print(f"Processing Title {i}: {title}")
        
        # Construct a Google search query
        query = f"{title} full text archive.org"
        
        # Search Google
        search_results_html = search_google(query)
        
        # Extract the top result URL
        top_result_url = extract_top_result_url(search_results_html)

        if top_result_url:
            # Extract text from the top result URL
            text_content = extract_text_from_url(top_result_url)

            if text_content:
                # Save the text content to a file
                filename = f"khasi_text_{i}.txt"
                with open(filename, "w", encoding="utf-8") as output_file:
                    output_file.write(text_content)

                print(f"Text content saved to {filename}")
        else:
            print("No relevant result found.")

        # Be respectful and avoid overloading the server
        time.sleep(5)

if __name__ == "__main__":
    main()
