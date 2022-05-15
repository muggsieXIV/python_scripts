from bs4 import BeautifulSoup
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import csv 


search_term = ''

url = f'https://edition.cnn.com/search?q={search_term}'
print(url)

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

driver.get(url)
time.sleep(4)

soup = BeautifulSoup(driver.page_source, 'html.parser')

found_articles = []
int = 0

for h3 in soup.select('h3.cnn-search__result-headline > a'):
    
    url=h3.get('href')
    int+=1 
    id = int

    data = [int, h3.text, 'https:'+ url]

    found_articles.append(data)


with open('rowVsWade.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    header = ['id', 'title', 'url']
    writer.writerow(header)

    # write the data
    for data in found_articles:
        writer.writerow([data[0], data[1], data[2]])
