from download_files import download_file
import json

def get_links():
    with open('links.json') as f:
        links = json.load(f)
    return links

def generate_filetree(filetree):
    MAIN_PATH = '~/projects/statapp/ign_data/'
    for region, departments in filetree.items():
        folderpath = MAIN_PATH + region 
        if not os.path.exists(folderpath):
            os.mkdir(folderpath)
        for department, files in departments.items():
            subfolderpath = folderpath + '/' + department
            if not os.path.exists(folderpath):
                os.mkdir(folderpath)
            for filename, file_url in files.items():
                filepath = subfolderpath + '/' + filename
                download_file(fileurl, filepath)

# generate_filetree(link_dict)
links = get_links()
print(links)
