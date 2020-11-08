from requests import Session
import requests
from tqdm import tqdm

# headers = GET /piwik/piwik.php?link=https%3A%2F%2Fwxs.ign.fr%2Fenlf5fc2u11becs9p951mrzi%2Ftelechargement%2Fprepackage%2FORTHOHR-JP2_PACK_D014_2016-01-01%24ORTHOHR_1-0_RVB-0M20_JP2-E080_LAMB93_D014_2016-01-01%2Ffile%2FORTHOHR_1-0_RVB-0M20_JP2-E080_LAMB93_D014_2016-01-01.7z.001&idsite=42&rec=1&r=364841&h=11&m=49&s=27&url=https%3A%2F%2Fgeoservices.ign.fr%2Fdocumentation%2Fdiffusion%2Ftelechargement-donnees-libres.html%23orthoirc--50cm-et-hr-sous-licence-ouverte&_id=939d6a31670610b5&_idts=1604674428&_idvc=4&_idn=0&_refts=0&_viewts=1604684646&pdf=1&qt=0&realp=0&wma=0&dir=0&fla=0&java=0&gears=0&ag=0&cookie=1&res=1440x900&gt_ms=567 HTTP/1.1


url = 'https://ORTHOIRC:ORTHOIRC@wxs.ign.fr/02v71g3hwl8yn8j5yf1nf08v/telechargement/inspire/BDORTHO-JP2-IRC_PACK_D003_2016-01-01%24BDORTHO_2-0_IRC-0M50_JP2-E080_LAMB93_D003_2016-01-01/file/BDORTHO_2-0_IRC-0M50_JP2-E080_LAMB93_D003_2016-01-01.7z.001'

def download_file(url, filepath):
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
    return local_filename
