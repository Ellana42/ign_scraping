from requests import Session
import requests
from tqdm import tqdm
import shutil
import urllib.request as request
from contextlib import closing

url = 'https://ORTHOIRC:ORTHOIRC@wxs.ign.fr/02v71g3hwl8yn8j5yf1nf08v/telechargement/inspire/BDORTHO-JP2-IRC_PACK_D003_2016-01-01%24BDORTHO_2-0_IRC-0M50_JP2-E080_LAMB93_D003_2016-01-01/file/BDORTHO_2-0_IRC-0M50_JP2-E080_LAMB93_D003_2016-01-01.7z.001'

def download_file(url, filepath):
    if url[:5] == 'https':
        download_https(url, filepath)
    elif url[:3] == 'ftp':
        download_ftp(url, filepath)
    else:
        print('Unknown format')
        print('Url : {}'.format(url))
        print('Path : {}'.format(filepath))
        raise

def download_https(url, filepath):
    headers = {'Host': 'piwik.ign.fr',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
        'Accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Dest': 'image',
        'Referer': 'https://geoservices.ign.fr/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-GB,en;q=0.9,ja-JP;q=0.8,ja;q=0.7,fr-FR;q=0.6,fr;q=0.5,ru-RU;q=0.4,ru;q=0.3,en-US;q=0.2'}
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        print('ongoing')
        with open(filepath, 'wb') as f:
            print('writing')
            for chunk in tqdm(r.iter_content(chunk_size=8192)): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)
    return filepath

def download_ftp(url, filepath):
    with closing(request.urlopen(url)) as r:
        print('ongoing ftp')
        with open(filepath, 'wb') as f:
            print('writing ftp')
            shutil.copyfileobj(r, f)

