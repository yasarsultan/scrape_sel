from selenium import webdriver
from bs4 import BeautifulSoup

url = "https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787"
driver = webdriver.Chrome()
driver.get(url)

page = driver.page_source
soup = BeautifulSoup(page, "lxml")

driver.quit()

tables = soup.find("table", id="table_id")
body = tables.tbody
rows = body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    for col in cols:
        print(col.text)