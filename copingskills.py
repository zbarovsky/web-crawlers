from bs4 import BeautifulSoup, Tag
import requests

def get_coping_skills():
    page = requests.get("https://www.thepathway2success.com/100-coping-strategies-for-anger-anxiety-and-more/")
    soup = BeautifulSoup(page.text, "html.parser")
    doc = open('cs_list.txt', 'w')

    for sibling in soup.find('strong').parent.next_siblings:
        if isinstance(sibling, Tag):
            if sibling.name == 'div':
                return
            if sibling.name == 'p':
                skill = sibling.get_text()
                doc.write(f'{skill}\n')
    doc.close()

get_coping_skills()
