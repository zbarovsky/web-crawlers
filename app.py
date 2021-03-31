from bs4 import BeautifulSoup, Tag
import requests

def get_discography():
    page = requests.get("https://en.wikipedia.org/wiki/Dave_Grohl_discography")
    soup = BeautifulSoup(page.text, "html.parser")

    discography = soup.find('h3').next_siblings
    print(discography)

    for elem in discography:
        if isinstance(elem, Tag):
            if elem.name == "h2":
                return
            if elem.name == 'ul':
                for item in elem:
                    if isinstance(item, Tag) and isinstance(item.contents[0], Tag):
                        title = item.contents[0].get_text()
                        print(title)

    return "Error"

get_discography()
