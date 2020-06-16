import requests
from bs4 import BeautifulSoup

url = 'https://scrapethissite.com/pages/simple/'

# TODO: store country and capitals into array, save to file


r = requests.get(url)

soup = BeautifulSoup(r.text,'lxml')
# myHTML = soup.html

# with open('scrapeThisSite.html','w') as f:
#     f.write(str(myHTML))

countryNames = [soup.find_all("h3", class_="country-name")]
# strippedNames = [i.get_text() for i in countryNames]

splitText = []