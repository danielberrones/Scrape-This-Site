import requests
from bs4 import BeautifulSoup

url = 'https://scrapethissite.com/pages/simple/'

# TODO: store country and capitals into array, save to file

def soupRequest():
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'lxml')
    return soup

def getCountryAndCapital(soupObject):
    countries = [i.text.strip() for i in soupObject.find_all("h3", class_="country-name")]
    capitals = [i.text.strip() for i in soupObject.find_all("span", class_="country-capital")]
    return dict(zip(countries,capitals))

def parseDict(countryAndCapital):
    for i, (k,v) in enumerate(countryAndCapital.items()):
        print(f"{i+1}\n\nCountry: {k}")
        print(f"Capital: {v}\n\n")

def main():
    parseDict(getCountryAndCapital(soupRequest()))


main()