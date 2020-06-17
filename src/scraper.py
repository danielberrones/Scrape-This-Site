import requests
from bs4 import BeautifulSoup

url = 'https://scrapethissite.com/pages/simple/'

# TODO: store country and capitals into array, save to file

r = requests.get(url)

soup = BeautifulSoup(r.text,'lxml')
# myHTML = soup.html
# with open('scrapeThisSite.html','w') as f:
#     f.write(str(myHTML))
countries = [i.text.strip() for i in soup.find_all("h3", class_="country-name")]
# countryNames = [soup.find("div", class_="col-md-4 country")]
# strippedNames = [i.get_text() for i in countryNames]
# country-capital
capitals = [i.text.strip() for i in soup.find_all("span", class_="country-capital")]
combined = dict(zip(countries,capitals))

def parseDict():
    # i = 1
    for i, (k,v) in enumerate(combined.items()):
        print(f"{i+1}\n\nCountry: {k}")
        print(f"Capital: {v}\n\n")

parseDict()

# print(len(capitals))
# print(len(countries))
# parseText = [i for i in countryNames.split(" ")]
# print(parseText)
# for x in countryNames:
#     print(x.text.strip())
# print(countryNames[7]=="Angola")

