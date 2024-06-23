# number                   : index

# wine_id                  : card.vintage.wine.id
# wine_name                : card.vintage.wine.name
# wine_alcohol             : card.vintage.wine.alcohol
# wine_region              : card.vintage.wine.region.name
# wine_country             : card.vintage.wine.region.country.name
# wine_grape1              : card.vintage.wine.grapes[1].name
# wine_grape2              : card.vintage.wine.grapes[2].name
# wine_grape3              : card.vintage.wine.grapes[3].name
# wine_grape4              : card.vintage.wine.grapes[4].name
# wine_grape5              : card.vintage.wine.grapes[5].name

# vintage_name             : card.vintage.name
# vintage_year             : card.vintage.year
# vintage_reviews-count    : card.vintage.statistics.ratings_count

# style_name               : card.vintage.wine.style.name
# style_region             : card.vintage.wine.style.region.name
# style_country            : card.vintage.wine.style.region.country.name

# price_amount             : card.price.amount
# price_currency           : card.price.currency.code

# winery_name              : card.vintage.wine.winery.name
# winery_region            : card.vintage.wine.winery.region.name
# winery_country           : card.vintage.wine.winery.region.country.name
# winery_business          : card.vintage.wine.winery.business_name

import json
import csv
import os

# Define vintage card class
class Vintage:
    def __init__(
            self,
            number,
            wine_id,
            wine_name,
            wine_alcohol,
            wine_region,
            wine_country,
            wine_grape1,
            wine_grape2,
            wine_grape3,
            wine_grape4,
            wine_grape5,
            vintage_name,
            vintage_year,
            vintage_reviewsCount,
            style_name,
            style_region,
            style_country,
            price_amount,
            price_currency,
            winery_name,
            winery_region,
            winery_country,
            winery_business
    ):
        self.number = number
        self.wine_id = wine_id
        self.wine_name = wine_name
        self.wine_alcohol = wine_alcohol
        self.wine_region = wine_region
        self.wine_country = wine_country
        self.wine_grape1 = wine_grape1
        self.wine_grape2 = wine_grape2
        self.wine_grape3 = wine_grape3
        self.wine_grape4 = wine_grape4
        self.wine_grape5 = wine_grape5
        self.vintage_name = vintage_name
        self.vintage_year = vintage_year
        self.vintage_reviewsCount = vintage_reviewsCount
        self.style_name = style_name
        self.style_region = style_region
        self.style_country = style_country
        self.price_amount = price_amount
        self.price_currency = price_currency
        self.winery_name = winery_name
        self.winery_region = winery_region
        self.winery_country = winery_country
        self.winery_business = winery_business

# Open csv file and create header
with open('./cards_cleared.csv', 'w', encoding="utf8") as csvfile:
    fieldnames = [ 'number', 'wine_id', 'wine_name', 'wine_alcohol', 'wine_region', 'wine_country', 'wine_grape1', 'wine_grape2', 'wine_grape3', 'wine_grape4', 'wine_grape5', 'vintage_name', 'vintage_year', 'vintage_reviewsCount', 'style_name', 'style_region', 'style_country', 'price_amount', 'price_currency', 'winery_name', 'winery_region', 'winery_country', 'winery_business' ]
    dw = csv.DictWriter(csvfile, fieldnames)
    dw.writeheader()

    # Count number of cards 
    for card_index, card_file in enumerate(os.listdir('./cards_raw-json')):

        with open(f'./cards_raw-json/card-{card_index}.json', 'r', encoding="utf8") as card_json:
            card_raw = json.load(card_json)
            card = Vintage(
                card_index,

                card_raw['vintage']['wine']['id'],
                card_raw['vintage']['wine']['name'],
                card_raw['vintage']['wine']['alcohol'],
                card_raw['vintage']['wine']['region']['name'],
                card_raw['vintage']['wine']['region']['country']['name'],
                card_raw['vintage']['wine']['grapes'][0]['name'] if len(card_raw['vintage']['wine']['grapes']) > 0 else '',
                card_raw['vintage']['wine']['grapes'][1]['name'] if len(card_raw['vintage']['wine']['grapes']) > 1 else '',
                card_raw['vintage']['wine']['grapes'][2]['name'] if len(card_raw['vintage']['wine']['grapes']) > 2 else '',
                card_raw['vintage']['wine']['grapes'][3]['name'] if len(card_raw['vintage']['wine']['grapes']) > 3 else '',
                card_raw['vintage']['wine']['grapes'][4]['name'] if len(card_raw['vintage']['wine']['grapes']) > 4 else '',

                card_raw['vintage']['name'],
                card_raw['vintage']['year'],
                card_raw['vintage']['statistics']['ratings_count'],

                card_raw['vintage']['wine']['style']['name'],
                card_raw['vintage']['wine']['style']['region']['name'],
                card_raw['vintage']['wine']['style']['region']['country']['name'],

                card_raw['price']['amount'],
                card_raw['price']['currency']['code'],

                card_raw['vintage']['wine']['winery']['name'],
                card_raw['vintage']['wine']['winery']['region']['name'],
                card_raw['vintage']['wine']['winery']['region']['country']['name'],
                card_raw['vintage']['wine']['winery']['business_name']
                )

        csvfile.write(str(card.number) + ',')
        csvfile.write(str(card.wine_id) + ',')
        csvfile.write(str(card.wine_name) + ',')
        csvfile.write(str(card.wine_alcohol) + ',')
        csvfile.write(str(card.wine_region) + ',')
        csvfile.write(str(card.wine_country) + ',')
        csvfile.write(str(card.wine_grape1) + ',')
        csvfile.write(str(card.wine_grape2) + ',')
        csvfile.write(str(card.wine_grape3) + ',')
        csvfile.write(str(card.wine_grape4) + ',')
        csvfile.write(str(card.wine_grape5) + ',')
        csvfile.write(str(card.vintage_name) + ',')
        csvfile.write(str(card.vintage_year) + ',')
        csvfile.write(str(card.vintage_reviewsCount) + ',')
        csvfile.write(str(card.style_name) + ',')
        csvfile.write(str(card.style_region) + ',')
        csvfile.write(str(card.style_country) + ',')
        csvfile.write(str(card.price_amount) + ',')
        csvfile.write(str(card.price_currency) + ',')
        csvfile.write(str(card.winery_name) + ',')
        csvfile.write(str(card.winery_region) + ',')
        csvfile.write(str(card.winery_country) + ',')
        csvfile.write(str(card.winery_business) + '\n')

        print(str(card_index) + ' - ' + card.wine_name)