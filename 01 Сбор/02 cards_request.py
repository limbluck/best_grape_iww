import requests
from bs4 import BeautifulSoup
import csv
import json

# Setup headers to simulate browser
request_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0',
    'Accept': 'text/html',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br'
}

# Open links file
with open('cards_links.csv', 'r') as csv_links:

    # Read link from links file
    links = csv.reader(csv_links)
    for link_index, link in enumerate(links):

        # Request page html
        page = requests.get(link[0], headers=request_headers)
        soup = BeautifulSoup(page.text, 'lxml')

        # Find a script tag with requred data
        scripts = soup.find_all('script')
        for script in scripts:
            if 'vintagePageInformation' in script.text:

                # Extract data from script test
                contents = str(script.text).split('window.__PRELOADED_STATE__')
                for content in contents:
                    if 'vintagePageInformation' in content:

                        # Transform data into JSON
                        start = content.index('{')
                        end = - content[::-1].index('}')
                        card = json.loads(content[start:end])

                        # Write data in a separate json file
                        with open('cards_raw-json/card-' + str(link_index) + '.json', 'w') as file:
                            json.dump(card, file)