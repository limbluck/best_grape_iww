import math
from bs4 import BeautifulSoup
import requests
import json
import csv
import os

# Setup headers to simulate browser
request_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0',
    'Accept': 'application/json'
}

# Get vintages IDs and years
with open('./cards_cleared.csv', 'r', encoding="utf8") as file:

    lines_amount = -3
    csv_file = csv.reader(file)
    for line in csv_file:
        lines_amount += 1

    file.seek(0)

    for line_index, line in enumerate(csv_file):

        # Skip header and empty row
        if (line_index < 2): continue

        # Iterate through review pages (50 is max number of reviews per page)
        page_last = math.ceil(int(line[13]) / 50)
        for page in range(1, page_last + 1):

            # Show status in console
            print(f'card-{line_index - 2}/{lines_amount} | page-{page}/{page_last} | id-{line[1]}')

            # Define request URL, insert id, page and year
            url = 'https://www.vivino.com/api/wines/' + line[1] + '/reviews?per_page=50&page=' + str(page) + '&year=' + line[12]

            # Reques json data and write in in a file
            request = requests.get(url, headers=request_headers)
            with open('reviews_raw-json/card-' + str(line_index - 2) + '-page-' + str(page) + '.json', 'w') as jsonfile:
                json.dump(request.json(), jsonfile)

            # Prepare for next loop
            page += 1

            # Clear status
            os.system('cls')
