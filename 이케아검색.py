#!/usr/bin/env python
# coding: utf-8

# In[40]:


from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

driver = webdriver.Chrome(ChromeDriverManager().install())

URL = 'https://www.ikea.com/kr/ko/'
driver.get(url=URL)

driver.implicitly_wait(time_to_wait = 10)


# In[18]:


from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# In[41]:


elem = driver.find_element(By.CSS_SELECTOR, 'body > header > div > div > div > div.hnf-header__search > div > div > form > div > div > input')
elem.send_keys('침대')
elem.send_keys(Keys.RETURN)


# In[42]:


import time
elem = driver.find_element(By.TAG_NAME, 'body')
for i in range(15):
    elem.send_keys(Keys.PAGE_DOWN)
    driver.find_element(By.CSS_SELECTOR, '#content > div > div > div:nth-child(4) > div:nth-child(3) > div.show-more > a').click()
    time.sleep(0.1)

    for i in range(15):
        elem.send_keys(Keys.PAGE_DOWN)
        driver.find_element(By.CSS_SELECTOR, '#content > div > div > div:nth-child(4) > div:nth-child(3) > div.show-more > a').click()
        time.sleep(0.1)


# In[43]:


links = []
images = driver.find_elements(By.CSS_SELECTOR, '#search-results > div > a > img.product-fragment__image.product-fragment__image--alt')

for image in images:
    if image.get_attribute('src') is not None:
        links.append(image.get_attribute('src'))
        
print('찾은 이미지 개수:', len(links))


# In[ ]:


#search-results > div:nth-child(403) > a > img.product-fragment__image.product-fragment__image--alt


# In[ ]:


#search-results > div:nth-child(404) > a > img.product-fragment__image.product-fragment__image--alt


# In[45]:


import urllib
from urllib import request


# In[46]:


for k, i in enumerate(links):
    url = i
    urllib.request.urlretrieve(url, "D:\\이케아가구\\3"+'-'+str(k)+'.jpg')


# In[ ]:


1 책상
2 의자
3 침대
4 서랍/수납장


# In[ ]:





# In[ ]:





# In[ ]:




