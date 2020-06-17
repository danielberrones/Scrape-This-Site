import requests
from bs4 import BeautifulSoup


def soupRequest():
    url = 'https://scrapethissite.com/pages/simple/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'lxml')
    return soup

def getCountryAndCapital(soupObject):
    countries = [i.text.strip() for i in soupObject.find_all("h3", class_="country-name")]
    capitals = [i.text.strip() for i in soupObject.find_all("span", class_="country-capital")]
    return dict(zip(countries,capitals))

def parseDict(countryAndCapital):
    'save text to local machine'
    with open("myData.txt","w") as f:
        for i, (k,v) in enumerate(countryAndCapital.items()):
            f.write(str(f"{i+1}\n\nCountry: {k}\nCapital: {v}\n\n"))

def main():
    parseDict(getCountryAndCapital(soupRequest()))


main()











# PRINT PARSED TEXT
# def parseDict(countryAndCapital):
    # 'print parsed text'
    #for i, (k,v) in enumerate(countryAndCapital.items()):
    #print(f"{i+1}\n\nCountry: {k}")
    #print(f"Capital: {v}\n\n")



