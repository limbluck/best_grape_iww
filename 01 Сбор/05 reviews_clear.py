# file

# review_id     : rewiews.[0].id

# wine_id       : rewiews.[0].vintage.wine.id
# wine_year     : rewiews.[0].vintage.year

# review_rating : rewiews.[0].rating
# review_date   : rewiews.[0].created_at

import os
import json
import csv

class Review:
    def __init__(self, file, review_id, wine_id, wine_year, review_rating, review_date):
        self.file = file
        self.review_id = review_id
        self.wine_id = wine_id
        self.wine_year = wine_year
        self.review_rating = review_rating
        self.review_date = review_date

# Prepare CSV file
with open('./reviews_cleared.csv', 'w', encoding="utf8") as csvfile:
    fieldnames = [ 'file', 'review_id', 'wine_id', 'wine_year', 'review_rating', 'review_date' ]
    dw = csv.DictWriter(csvfile, fieldnames)
    dw.writeheader()

    # Iterate through files
    for file in os.listdir('./reviews_raw-json/'):
        with open(f'./reviews_raw-json/{file}', 'r', encoding='utf-8') as raw_json:
            json_data = json.load(raw_json)

            print(f'working on - {file}')

            # Check if file have reviews
            if (json_data.get('reviews') is not None):
                if (len(json_data['reviews']) > 0):

                    for review in json_data['reviews']:

                        # Create Review object
                        review = Review(
                            f'c{file.split('-')[1]}p{file.split('-')[3].split('.')[0]}',

                            review['id'],

                            review['vintage']['wine']['id'],
                            review['vintage']['year'],

                            review['rating'],
                            review['created_at'],
                        )

                        # Write data in csv
                        csvfile.write(str(review.file) + ',')
                        csvfile.write(str(review.review_id) + ',')
                        csvfile.write(str(review.wine_id) + ',')
                        csvfile.write(str(review.wine_year) + ',')
                        csvfile.write(str(review.review_rating) + ',')
                        csvfile.write(str(review.review_date) + '\n')

            os.system('cls')
