# Utility function for scraping
import requests, json
from bs4 import BeautifulSoup
import re
from PCH import pch

class ScrapImg:
    def __init__(self, catdict : dict):
        self.catdict = catdict
    def NaverShopping(self, query : str, path : str):
        if path[-1] != '/':
            path = path + '/'
        pch.nsp['query'] = pch.nsp['origQuery'] = query
        cate = catdict[query]
        pch.nsp['pagingIndex'] = 1

        while pch.nsp['pagingIndex'] != None:
            resp = requests.get(pch.nss, params=pch.nsp, cookies=pch.nsc, headers=pch.nsh)
            temp = json.loads(resp.text)
            i = 1
            while i <= int(pch.nsp['pagingSize']):
                for _ in temp['shoppingResult']['products']:
                    url = _['imageUrl']
                    imgresp = requests.get(url)
                    a = re.search(r'(\w+)(?:\s)(.+)', _['productTitle'])
                    try:
                        brand_name = a.group(1)
                        product_name = a.group(2)
                    except:
                        pass

                    j = (pch.nsp['pagingIndex'] - 1) * 40 + i

                    fileName = f'{cate}-{brand_name}-{product_name}-{j}' + '.jpg'

                    try:
                        with open(path + fileName, 'wb') as fp:
                            fp.write(imgresp.content)
                    except:
                        pass
                    i += 1
            pch.nsp['pagingIndex'] += 1

    def WeMakePrice(self, query : str, path : str):
        if path[-1] != '/':
            path = path + '/'
        pch.wmpp['keyword'] = query
        cate = self.catdict[query]
        pch.wmpp['page'] = 1

        while pch.wmpp['page'] != None:
            resp = requests.get(pch.wmps, params=pch.wmpp, headers=pch.wmph)
            resp.headers
            dom = BeautifulSoup(resp.text, 'html.parser')
            temp = resp.json()
            i = 1
            for _ in temp['data']['deals']:
                url = _['largeImgUrl']
                imgresp = requests.get(url)
                a = re.search(r'(\w+)(?:\s)([\w\s]+)(?:\s)([독립|본넬]?)', _['dispNm'])
                try:
                    brand_name = a.group(1)
                    product_name = a.group(2)
                except:
                    pass

                j = (pch.wmpp['page'] - 1) * 82 + i
                fileName = f'{cate}-{brand_name}-{product_name}-{j}' + '.jpg'

                try:
                    with open(path + fileName, 'wb') as fp:
                        fp.write(imgresp.content)
                except:
                    pass
                i += 1
            pch.wmpp['page'] += 1