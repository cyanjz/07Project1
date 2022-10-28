#to specify cookies, parameters and headers for scraping

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

class pch():
    nss = 'https://search.shopping.naver.com/api/search/all'
    nsc = {
        '_ga_7VKFYR6RV1': 'GS1.1.1633001955.6.1.1633001963.52',
        '_ga': 'GA1.2.429413694.1608041921',
        'NNB': '243UWQ65ZFMWG',
        'nid_inf': '1354423238',
        'NID_AUT': 'fnF/vVzivT5nQsPKRQ0oIZvnzXFs8cp+/J/eZRICyZBPf1b6yp1vWiGUx3RP9AQX',
        'NID_JKL': '7CnD1edRJ2sGkbrVYP/FH0f+Qyv3VmrNiUT5atx6AsA=',
        'NID_SES': 'AAABb852KskcogCiplJo/ZeGT/cvJf+zBYphX7+fxIugHwXBauozcTfZdIgBhg2aq88A/WYGj5NigmVSRI4iWiJ6NslPGH1cegn4Veg8WOFFX4UJDClFcMgkjm74INi+sVPgb8CQZtbqeFCPvuU8jacEpbrnaxC5vo/oC2w/cKR1J9pgmBQ82FuW60XskHzPAFcKbvvOTgYel4XLQZViWAfwzSf184SKHZ+pS/o0FKUvDGn9CHLvEyViLvC9FqRB+oJTHQxCuxuQXWmfFQ83fMnEMQJMplJfj3a1pXd7Dc+CZJLnQ5Uy+SX4bhwa/c4WbKvNm2a3nE/+KYSnZx0wealsvmQi4nCNHDJA/hAYb3rcAkWodchzCK1M6GBjM0g9UVqhHElu8RMb2/9qrBexXiSfPpiyp+HbAiQN79Ju4Bl7Nu3WaH3u56AeLhnrk7B3HHszQHGkqUavDMzqRI8tHSG1F0pCgsPZ609oR9yacmQYjdh7',
        'sus_val': 'W5VMnuZC7w/6G5v1v0j6gbFh',
        'autocomplete': 'use',
        'AD_SHP_BID': '26',
        'spage_uid': '',
    }
    nsh = {
        'authority': 'search.shopping.naver.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ko,en;q=0.9,en-US;q=0.8,zh-CN;q=0.7,zh;q=0.6',
        'cache-control': 'no-cache',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_ga_7VKFYR6RV1=GS1.1.1633001955.6.1.1633001963.52; _ga=GA1.2.429413694.1608041921; NNB=243UWQ65ZFMWG; nid_inf=1354423238; NID_AUT=fnF/vVzivT5nQsPKRQ0oIZvnzXFs8cp+/J/eZRICyZBPf1b6yp1vWiGUx3RP9AQX; NID_JKL=7CnD1edRJ2sGkbrVYP/FH0f+Qyv3VmrNiUT5atx6AsA=; NID_SES=AAABb852KskcogCiplJo/ZeGT/cvJf+zBYphX7+fxIugHwXBauozcTfZdIgBhg2aq88A/WYGj5NigmVSRI4iWiJ6NslPGH1cegn4Veg8WOFFX4UJDClFcMgkjm74INi+sVPgb8CQZtbqeFCPvuU8jacEpbrnaxC5vo/oC2w/cKR1J9pgmBQ82FuW60XskHzPAFcKbvvOTgYel4XLQZViWAfwzSf184SKHZ+pS/o0FKUvDGn9CHLvEyViLvC9FqRB+oJTHQxCuxuQXWmfFQ83fMnEMQJMplJfj3a1pXd7Dc+CZJLnQ5Uy+SX4bhwa/c4WbKvNm2a3nE/+KYSnZx0wealsvmQi4nCNHDJA/hAYb3rcAkWodchzCK1M6GBjM0g9UVqhHElu8RMb2/9qrBexXiSfPpiyp+HbAiQN79Ju4Bl7Nu3WaH3u56AeLhnrk7B3HHszQHGkqUavDMzqRI8tHSG1F0pCgsPZ609oR9yacmQYjdh7; sus_val=W5VMnuZC7w/6G5v1v0j6gbFh; autocomplete=use; AD_SHP_BID=26; spage_uid=',
        'logic': 'PART',
        'pragma': 'no-cache',
        'referer': 'https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery=%EC%B9%A8%EB%8C%80&pagingIndex=2&pagingSize=40&productSet=total&query=%EC%B9%A8%EB%8C%80&sort=rel&timestamp=&viewType=list',
        'sec-ch-ua': '"Chromium";v="106", "Microsoft Edge";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52',
    }
    nsp = {
        'sort': 'rel',
        'pagingIndex': None,
        'pagingSize': '40',
        'viewType': 'list',
        'productSet': 'total',
        'deliveryFee': '',
        'deliveryTypeValue': '',
        'frm': 'NVSHATC',
        'query': '침대',
        'origQuery': '침대',
        'iq': '',
        'eq': '',
        'xq': '',
    }

    wmph = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33'}

    wmps = 'https://search.wemakeprice.com/api/wmpsearch/api/v3.0/wmp-search/search.json'

    wmpp = {
            'searchType': 'DEFAULT',
            'search_cate': 'top',
            'keyword': None,
            'isRec': 1,
            '_service': 5,
            '_type': 3,
            'page': None
        }
