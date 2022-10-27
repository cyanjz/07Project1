#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from requests import request,get,post
from bs4 import BeautifulSoup
import re


# In[ ]:


headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33'}


# In[ ]:


seed='https://search.wemakeprice.com/api/wmpsearch/api/v3.0/wmp-search/search.json'
params={
'searchType': 'DEFAULT',
'search_cate': 'top',
'keyword': None,
'isRec': 1,
'_service': 5,
'_type': 3,
'page': None
}

params['keyword']=input('검색어:')
cate=int(input('카테고리 번호:'))
params['page']=1

while params['page']!=None:
    resp=get(seed,params=params,headers=headers)
    resp.headers
    dom=BeautifulSoup(resp.text,'html.parser')
    temp=resp.json()
    i=1
    for _ in temp['data']['deals']:
        url=_['largeImgUrl']
        urlresp=get(url)
        j=(params['page']-1)*82+i
        fileName=f'{cate}-{j}'+'.jpg'
        with open('./bed1/'+fileName,'wb') as fp:
            fp.write(urlresp.content)
        i+=1
    params['page']+=1

