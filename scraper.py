# Utility function for scraping
import requests, json
from requests import request
from bs4 import BeautifulSoup
import re
from PCH import pch

class ScrapImg:
    def __init__(self, catdict):
        self.catdict = catdict
    def NaverShopping(self, query : str, path : str, catdict : dict):
        if path[-1] != '/':
            path = path + '/'
        pch['params']['query'] = pch.NS['params']['origQuery'] = query
        cate = catdict[query]
        pch.NS['pagingIndex'] = 1

        while self.pch.NS['pagingIndex'] != None:
            resp = requests.get(pch.NS['seed'], params=pch.NS['params'], cookies=pch.NS['cookies'], headers=pch.NS['header'])
            temp = json.loads(resp.text)
            i = 1
            while i <= int(pch.NS['params']['pagingSize']):
                for _ in temp['shoppingResult']['products']:
                    url = _['imageUrl']
                    urlresp = requests.get(url)
                    a = re.search(r'(\w+)(?:\s)(.+)', _['productTitle'])
                    try:
                        brand_name = a.group(1)
                        product_name = a.group(2)
                    except:
                        pass

                    j = (pch.NS['pagingIndex'] - 1) * 40 + i
                    fileName = f'{cate}-{brand_name}-{product_name}-{j}' + '.jpg'

                    try:
                        with open(path + fileName, 'wb') as fp:
                            fp.write(urlresp.content)
                    except:
                        pass
                    i += 1
            pch.NS['pagingIndex'] += 1

    def WeMakePrice(self):
        seed = 'https://search.wemakeprice.com/api/wmpsearch/api/v3.0/wmp-search/search.json'


        params['keyword'] = input('검색어:')
        cate = int(input('카테고리 번호:'))
        params['page'] = 1

        while params['page'] != None:
            resp = get(seed, params=params, headers=headers)
            resp.headers
            dom = BeautifulSoup(resp.text, 'html.parser')
            temp = resp.json()
            i = 1
            for _ in temp['data']['deals']:
                url = _['largeImgUrl']
                urlresp = get(url)
                a = re.search(r'(\w+)(?:\s)([\w\s]+)(?:\s)([독립|본넬]?)', _['dispNm'])
                try:
                    brand_name = a.group(1)
                    product_name = a.group(2)
                except:
                    pass

                j = (params['page'] - 1) * 82 + i
                fileName = f'{cate}-{brand_name}-{product_name}-{j}' + '.jpg'

                try:
                    with open('./bed/' + fileName, 'wb') as fp:
                        fp.write(urlresp.content)
                except:
                    pass
                i += 1
            params['page'] += 1