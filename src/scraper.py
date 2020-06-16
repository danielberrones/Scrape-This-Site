import requests
from bs4 import BeautifulSoup

url = 'https://scrapethissite.com/pages/simple/'

# TODO: store country and capitals into array, save to file

r = requests.get(url)

soup = BeautifulSoup(r.text,'lxml')
# myHTML = soup.html

# with open('scrapeThisSite.html','w') as f:
#     f.write(str(myHTML))

countryNames = [i.text.strip() for i in soup.find_all("h3", class_="country-name")]
# countryNames = [soup.find("div", class_="col-md-4 country")]
# strippedNames = [i.get_text() for i in countryNames]

# parseText = [i for i in countryNames.split(" ")]

# print(parseText)

# for x in countryNames:
#     print(x.text.strip())

print(countryNames[7]=="Angola")