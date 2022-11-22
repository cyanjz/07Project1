import numpy as np
from requests import request
from PCH import ScrapUtility
from bs4 import BeautifulSoup
import pandas as pd

# headers = ScrapUtility.build_header('''accept: */*
#     accept-encoding: gzip, deflate, br
#     accept-language: ko-KR,ko;q=0.9
#     cache-control: no-cache
#     origin: https://www.enex.co.kr
#     pragma: no-cache
#     referer: https://www.enex.co.kr/
#     sec-ch-ua: "Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"
#     sec-ch-ua-mobile: ?0
#     sec-ch-ua-platform: "Windows"
#     sec-fetch-dest: empty
#     sec-fetch-mode: cors
#     sec-fetch-site: cross-site
#     user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36''')
# params = [{'page':'1', 'cateCd' : '005003'}, {'page' : '1', 'cateCd' : '004007'},
#          {'page' : '1', 'cateCd' : '002001'}, {'page' : '1', 'cateCd' : '002003'}]
# root = 'https://www.enex.co.kr/goods/goods_list.php?'
#
# resp = request('GET', root + ScrapUtility.set_params(params[0]), headers=headers)
# dom = BeautifulSoup(resp.text, 'html5lib')
# list1 = dom.select('div.container > div.goods_list > div.goods_list_cont > div.item_gallery_type > ul > li > div.item_cont > div.item_photo_box > a > img')
# list2 = dom.select('div.goods-best.bg > div.container > div.best_item_view > div.goods_list > div.goods_list_cont'
#                                         ' > div.item_gallery_type.dd > ul > li > div.item_cont > div.item_photo_box > a > img')
# list3 = dom.select('div.goods-best.bg > div.container > div.best_item_view > div.goods_list > div.goods_list_cont'
#                                         ' > div.item_gallery_type.dd > ul > li > div.item_cont > div.item_info_cont > div.item_money_box > strong.item_price'
#                    '> span')
# list4 = dom.select('div.container > div.goods_list > div.goods_list_cont > div.item_gallery_type > ul > li > div.item_cont > div.item_info_cont'
#                    ' > div.item_money_box > strong.item_price > span')
# print(len(list1), len(list4), len(list2), len(list3))
# print(list4[0].getText())
# 'https://www.enex.co.kr'
# 'https://www.enex.co.kr/data/goods/21/02/05//1000000388/1000000388_detail_032.jpg'


def EnexDbBuilder(params : list):
    X = pd.DataFrame(columns=['img', 'title', 'price', 'url'])

    root = 'https://www.enex.co.kr/goods/goods_list.php?'
    seed = 'https://www.enex.co.kr'
    headers = ScrapUtility.build_header('''accept: */*
    accept-encoding: gzip, deflate, br
    accept-language: ko-KR,ko;q=0.9
    cache-control: no-cache
    origin: https://www.enex.co.kr
    pragma: no-cache
    referer: https://www.enex.co.kr/
    sec-ch-ua: "Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"
    sec-ch-ua-mobile: ?0
    sec-ch-ua-platform: "Windows"
    sec-fetch-dest: empty
    sec-fetch-mode: cors
    sec-fetch-site: cross-site
    user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36''')

    for i, p in enumerate(params):
        print(f'{i}-th params')

        while True:
            resp = request('GET', root + ScrapUtility.set_params(p), headers=headers)
            dom = BeautifulSoup(resp.text, 'html5lib')

            if p['page'] == '1':
                bestseller = dom.select(
                    'div.goods-best.bg > div.container > div.best_item_view > div.goods_list > div.goods_list_cont'
                    ' > div.item_gallery_type.dd > ul > li > div.item_cont')
                bsimgs = pd.DataFrame([seed + bb.select('div.item_photo_box > a > img')[0]['src'] for bb in bestseller])
                bsprices = pd.DataFrame([bb.select('div.item_info_cont > div.item_money_box > strong.item_price > span')[0].getText() for
                            bb in bestseller])
                bslinks = pd.DataFrame([seed + bb.select('div.item_photo_box > a')[0]['href'][2:] for bb in bestseller])
                bstitles = pd.DataFrame([bb.select('div.item_info_cont > div.item_tit_box > a > strong.item_name')[0].getText() for bb in
                            bestseller])
                Y = pd.concat([bsimgs, bstitles, bsprices, bslinks], axis = 1)
                Y.columns = ['img', 'title', 'price', 'url']
                X = pd.concat([X, Y], ignore_index=True, axis = 0)

            products = dom.select('div.container > div.goods_list > div.goods_list_cont > div.item_gallery_type > ul > li > div.item_cont')
            if len(products) == 0:
                break
            pimgs = pd.DataFrame([seed + bb.select('div.item_photo_box > a > img')[0]['src'] for bb in products])
            pprices = pd.DataFrame([bb.select('div.item_info_cont > div.item_money_box > strong.item_price > span')[0].getText() for
                        bb in products])
            plinks = pd.DataFrame([seed + bb.select('div.item_photo_box > a')[0]['href'][2:] for bb in products])
            ptit = pd.DataFrame([bb.select('div.item_info_cont > div.item_tit_box > a > strong.item_name')[0].getText() for bb in
                        products])
            Y = pd.concat([pimgs, ptit, pprices, plinks], axis = 1)
            Y.columns = ['img', 'title', 'price', 'url']
            X = pd.concat([X, Y], ignore_index=True, axis=0)

            p['page'] = f'{int(p["page"]) + 1}'
    return X

X = EnexDbBuilder(params)
X.to_csv('D:\Workspace\SW_academy\Project1_DB\X.csv', encoding = 'euc-kr')


# item_info_box > , item_photo_box -> 제목, image
