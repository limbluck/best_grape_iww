from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

# Open browser
driver = Chrome()

# Open catalog page with filters setted up
url = 'https://www.vivino.com/explore?e=eJwdizEKgDAQBH-zdSJYXuMTBCsROeMZAkblEqL-3mAzUwwTlSxiOMgg8kO2aY2Be6kf4Co6XLX7jQprkMw7Tl1pleRwLi8p53D4NHMRZS-48zhRU_9UHTJ-fkD1IYQ%3D'
driver.get(url)

# Find how much cards needs to load
wines_required = int(driver.find_element(By.XPATH, '//h2[@class="querySummary__querySummary--39WP2"]').text[8:12])
print('required - ' + str(wines_required))

# Load wine cards
wines_got = 0
while(wines_got < wines_required):
    driver.execute_script('window.scrollTo(0, document.documentElement.scrollHeight)')
    wines_got = len(driver.find_elements(By.XPATH, '//div[@class="wineCard__wineCard--2dj2T wineCard__large--1tkVl"]'))
    print('got - ' + str(wines_got))
    time.sleep(1)

# Write links in file
soup = BeautifulSoup(driver.page_source, 'lxml')
cards = soup.find_all('div', {'class' : 'wineCard__wineCard--2dj2T wineCard__large--1tkVl'})
with open('cards_links.csv', 'w') as csvfile:
    for card in cards:
        csvfile.write('https://www.vivino.com' + card.find('a').get('href'))
        csvfile.write('\n')
