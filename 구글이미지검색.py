#!/usr/bin/env python
# coding: utf-8

# In[2]:


# !pip install selenium
# !pip install webdriver-manager


# In[3]:


from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

driver = webdriver.Chrome(ChromeDriverManager().install())

URL = 'https://www.google.co.kr/imghp'
driver.get(url=URL)

driver.implicitly_wait(time_to_wait = 10)


# In[4]:


from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# In[5]:


elem = driver.find_element(By.CSS_SELECTOR, 'body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input')
elem.send_keys('동서가구 침대')
elem.send_keys(Keys.RETURN)


# In[6]:


import time
elem = driver.find_element(By.TAG_NAME, 'body')
for i in range(60):
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.1)
try:
    driver.find_element(By.CSS_SELECTOR, '#islmp > div > div > div.tmS4cc.blLOvc.snjnxc > div.gBPM8 > div.qvfT1 > div.YstHxe > input').click()
    for i in range(60):
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.1)
except:
    pass


# In[5]:


links = []
images = driver.find_elements(By.CSS_SELECTOR, '#islrg > div.islrc > div > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img')

for image in images:
    if image.get_attribute('src') is not None:
        links.append(image.get_attribute('src'))
        
print('찾은 이미지 개수:', len(links))


# In[103]:


from urllib import request

for k, i in enumerate(links):
    url = i
    urllib.request.urlretrieve(url, "D:\\가구\\4"+'-'+str(k)+'.jpg') # 설치 경로 변경


# In[83]:


1 책상
2 의자
3 침대
4 서랍/수납장

