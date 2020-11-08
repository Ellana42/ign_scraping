from bs4 import BeautifulSoup as bs
from bs4 import NavigableString, Tag

with open('donnees_ign.html') as f:
    page = f.read()

soup = bs(page, 'html.parser')

def get_between(header):
    nextNode = header
    links = ''
    while True:
        nextNode = nextNode.nextSibling
        if nextNode.name == 'h1':
            break
        links += str(nextNode)
    return links

header = soup.find(id='orthoirc--50cm-et-hr-sous-licence-ouverte') 
link_page = get_between(header)

with open('links.html', 'w') as f:
    f.write(link_page)
