# Utility function for scraping
import requests, json
from requests import request
from bs4 import BeautifulSoup
import re
import PCH


class ScrapUtility():
    def build_header(self, headerstring):
      '''
      Make header dictionary automatically.
      header string format sould be :
        key: value
        key: value
      returns header(dict)
      '''
      header = dict()
      for line in headerstring.splitlines():
        if len(line) > 0 and line[0] != ':':
          kv = re.search('^(.+)?: (.*)', line)
          try:
            header[kv.group(1)] = kv.group(2)
          except:
            pass
      return header

    def set_cookies(self, session, c):
      '''
      set cookies for session
      '''
      for _ in c.splitlines():
        if len(_) > 1:
          kv = _.split('\t')
          session.cookies.set(kv[0],kv[1])
      return session

class ScrapImg:
    def __init__(self, catdict):
        self.pch = PCH.pch()

    def NaverShopping(self, query : str, path : str, catdict : dict):
        self.pch.nsp['query'] = self.pch.nsp['origQuery'] = query
        cate = cardict[query]
        self.pch.nsp['pagingIndex'] = 1

        while self.pch.nsp['pagingIndex'] != None:
            resp = requests.get(seed, params=params, cookies=cookies, headers=headers)
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
                        with open('./table/' + fileName, 'wb') as fp:
                            fp.write(urlresp.content)
                    except:
                        pass
                    i += 1
            self.nsp['pagingIndex'] += 1

