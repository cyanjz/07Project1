# Utility function for scraping
import requests, json
from requests import request
from bs4 import BeautifulSoup
import re
import PCH

class ScrapImg:
    def __init__(self, catdict):
        self.pch = PCH.pch()
        self.catdict = catdict
    def NaverShopping(self, query : str, path : str, catdict : dict):
        if path[-1] != '/':
            path = path + '/'
        self.pch.nsp['query'] = self.pch.nsp['origQuery'] = query
        cate = catdict[query]
        self.pch.nsp['pagingIndex'] = 1

        while self.pch.nsp['pagingIndex'] != None:
            resp = requests.get(self.pch.nss, params=self.pch.nsp, cookies=self.pch.nsc, headers=self.pch.nsh)
            temp = json.loads(resp.text)
            i = 1
            while i <= int(self.pch.nsp['pagingSize']):
                for _ in temp['shoppingResult']['products']:
                    url = _['imageUrl']
                    urlresp = requests.get(url)
                    a = re.search(r'(\w+)(?:\s)(.+)', _['productTitle'])
                    try:
                        brand_name = a.group(1)
                        product_name = a.group(2)
                    except:
                        pass

                    j = (self.pch.nsp['pagingIndex'] - 1) * 40 + i
                    fileName = f'{cate}-{brand_name}-{product_name}-{j}' + '.jpg'

                    try:
                        with open(path + fileName, 'wb') as fp:
                            fp.write(urlresp.content)
                    except:
                        pass
                    i += 1
            self.pch.nsp['pagingIndex'] += 1

    def WeMakePrice(self):
        # In[ ]:

        seed = 'https://search.wemakeprice.com/api/wmpsearch/api/v3.0/wmp-search/search.json'
        params = {
            'searchType': 'DEFAULT',
            'search_cate': 'top',
            'keyword': None,
            'isRec': 1,
            '_service': 5,
            '_type': 3,
            'page': None
        }

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