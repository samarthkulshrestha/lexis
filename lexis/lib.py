from bs4 import BeautifulSoup as bs
import requests as req

E_URL = "https://www.etymonline.com/search?q="
W_URL = "https://en.wiktionary.org/wiki/Special:Search?go=Look+up&search="
I_URL = "https://wordinfo.info/results?searchString="


def search_eo(term):
    url = E_URL + str(term)
    source = req.get(url).text
    soup = bs(source, "lxml")

    wds = []

    word_cont = soup.find("div", class_="word--C9UPa word_4pc--2SZw8")
    word = word_cont.div.a.text
    meaning = word_cont.div.div.section.p
    wd = {"word": word, "meaning": meaning, "source": "etymonline"}
    wds.append(wd)

    # returns all responses
    # for word_cont in soup.find_all("div", class_="word--C9UPa word_4pc--2SZw8"):
    #     word = word_cont.div.a.text
    #     meaning = word_cont.div.div.section.p
    #     wd = {"word": word, "meaning": meaning, "source": "etymonline"}
    #     wds.append(wd)

    return wds

def search_wk(term):
    url = W_URL + str(term)
    source = req.get(url).text
    soup = bs(source, "lxml")

    wds = []

    word = soup.find("h1", class_="firstHeading").text
    meaning = soup.find("div", class_="mw-parser-output").p
    wd = {"word": word, "meaning": meaning, "source": "wiktionary"}
    wds.append(wd)

    return wds

def search_wi(term):
    url = I_URL + str(term)
    source = req.get(url).text
    soup = bs(source, "lxml")

    wds = []

    word = soup.find("div", class_="title").text
    meaning = soup.find("div", class_="definition")
    wd = {"word": word, "meaning": meaning, "source": "wordinfo"}
    wds.append(wd)

    return wds

def search_def(term):
    eo = search_eo(term)
    wk = search_wk(term)
    wi = search_wi(term)
    wds = eo + wk + wi

    return wds

if __name__ == "__main__":
    inp = input("enter word: ")
    print(search_def(inp))
