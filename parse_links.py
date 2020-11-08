from bs4 import BeautifulSoup as bs
import json
from pprint import pprint

def get_soup():
    with open('links.html') as f:
        links = f.read()

    soup = bs(links, 'html.parser')
    return soup
# Basically I want a dict with all titles and links in an associated list

def get_between():
    soup = get_soup()
    nextNode = soup.find('p')
    regions_dict = {}
    while True:
        if nextNode is None:
            break
        elif nextNode.name == 'p' and nextNode.get_text()[:6] == 'Région':
            region_name = nextNode.get_text()
            regions_dict[region_name] = {}
            current_region = regions_dict[region_name]
        elif nextNode.name == 'p':
            departement = nextNode.get_text()
            current_region[departement] = []
            currentDep = current_region[departement]
        elif nextNode.name == 'ul':
            link_list = [link['href'] for link in nextNode.find_all('a')]
            currentDep.extend(link_list)
        nextNode = nextNode.nextSibling
    return regions_dict

def filter_recent(link_dict):
    for region, departments in link_dict.items():
        list_dep = [dep for dep in departments]
        list_dep.sort()
        last_dep = list_dep[0]
        for dep in list_dep[1:]:
            if dep.split(' ')[0] == last_dep.split(' ')[0]:
                departments.pop(last_dep)
            last_dep = dep
    return link_dict

def get_link_dict():
    return filter_recent(get_between())

if __name__ == '__main__':
    link_dict = get_link_dict()
    with open('links.json', 'w') as f:
        json.dump(link_dict, f, indent=4)
