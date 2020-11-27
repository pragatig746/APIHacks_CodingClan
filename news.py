import requests
import pandas as pd
from bs4 import BeautifulSoup

r = requests.get('https://www.un.org/en/climatechange/climate-solutions')
page = r.content
soup = BeautifulSoup(page, 'html5lib')
news = soup.find_all('h3')

d = {}
for i in range(1, 7):
    links = news[i].find_all('a')
    d[str(news[i].get_text())] = str(links[0]['href'])

df = pd.DataFrame
df = pd.DataFrame(list(d.items()), columns=["Headlines", "Links"])
df.set_index('Headlines',inplace=True)
print(df)