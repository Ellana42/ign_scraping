from download_files import download_file
import os
import json

def get_links():
    with open('links.json') as f:
        links = json.load(f)
    return links

def save_links(link_dict):
    with open('links.json', 'w') as f:
        json.dump(link_dict, f, indent=4)

def generate_filetree(link_dict):
    new_link_dict = link_dict
    MAIN_PATH = '/Users/Mathilde/statapp/ign_data/'
    for region, departments in link_dict.items():
        region_name = region.split(' ')[-1]
        folderpath = MAIN_PATH + region_name 
        if not os.path.exists(folderpath):
            os.mkdir(folderpath)
            print('Created region folder : {}'.format(region_name))
        for department, files in departments.items():
            dep_parts = department.split(' ')
            year = department.split(' PVA ')[-1][:4]
            dep_name = '_'.join([dep_parts[0], dep_parts[2], year])
            subfolderpath = folderpath + '/' + dep_name
            if not os.path.exists(subfolderpath):
                os.mkdir(subfolderpath)
            for file_url in files:
                filename = file_url.split('/')[-1]
                filepath = subfolderpath + '/' + filename
                download_file(file_url, filepath)
                print('{} for {} in {} was downloaded'.format(filename, dep_name, region_name))
                new_link_dict[region][department].remove(file_url)
                save_links(new_link_dict)
                print('Progress saved')

link_dict = get_links()
generate_filetree(link_dict)
