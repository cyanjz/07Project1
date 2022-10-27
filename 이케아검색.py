{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "f9aae00d",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\insoo\\AppData\\Local\\Temp\\ipykernel_13864\\1554418824.py:4: DeprecationWarning: executable_path has been deprecated, please pass in a Service object\n",
      "  driver = webdriver.Chrome(ChromeDriverManager().install())\n"
     ]
    }
   ],
   "source": [
    "from webdriver_manager.chrome import ChromeDriverManager\n",
    "from selenium import webdriver\n",
    "\n",
    "driver = webdriver.Chrome(ChromeDriverManager().install())\n",
    "\n",
    "URL = 'https://www.ikea.com/kr/ko/'\n",
    "driver.get(url=URL)\n",
    "\n",
    "driver.implicitly_wait(time_to_wait = 10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "6a71b214",
   "metadata": {},
   "outputs": [],
   "source": [
    "from selenium.webdriver.common.by import By\n",
    "from selenium.webdriver.common.keys import Keys"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "ce2c4b4e",
   "metadata": {},
   "outputs": [],
   "source": [
    "elem = driver.find_element(By.CSS_SELECTOR, 'body > header > div > div > div > div.hnf-header__search > div > div > form > div > div > input')\n",
    "elem.send_keys('침대')\n",
    "elem.send_keys(Keys.RETURN)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "03caeb4a",
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "ename": "NoSuchElementException",
     "evalue": "Message: no such element: Unable to locate element: {\"method\":\"css selector\",\"selector\":\"#content > div > div > div:nth-child(4) > div:nth-child(3) > div.show-more > a\"}\n  (Session info: chrome=106.0.5249.119)\nStacktrace:\nBacktrace:\n\tOrdinal0 [0x00A21ED3+2236115]\n\tOrdinal0 [0x009B92F1+1807089]\n\tOrdinal0 [0x008C66FD+812797]\n\tOrdinal0 [0x008F55DF+1005023]\n\tOrdinal0 [0x008F57CB+1005515]\n\tOrdinal0 [0x00927632+1209906]\n\tOrdinal0 [0x00911AD4+1120980]\n\tOrdinal0 [0x009259E2+1202658]\n\tOrdinal0 [0x009118A6+1120422]\n\tOrdinal0 [0x008EA73D+960317]\n\tOrdinal0 [0x008EB71F+964383]\n\tGetHandleVerifier [0x00CCE7E2+2743074]\n\tGetHandleVerifier [0x00CC08D4+2685972]\n\tGetHandleVerifier [0x00AB2BAA+532202]\n\tGetHandleVerifier [0x00AB1990+527568]\n\tOrdinal0 [0x009C080C+1837068]\n\tOrdinal0 [0x009C4CD8+1854680]\n\tOrdinal0 [0x009C4DC5+1854917]\n\tOrdinal0 [0x009CED64+1895780]\n\tBaseThreadInitThunk [0x7558FA29+25]\n\tRtlGetAppContainerNamedObjectPath [0x77417BBE+286]\n\tRtlGetAppContainerNamedObjectPath [0x77417B8E+238]\n",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNoSuchElementException\u001b[0m                    Traceback (most recent call last)",
      "Input \u001b[1;32mIn [42]\u001b[0m, in \u001b[0;36m<cell line: 3>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      8\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m i \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;28mrange\u001b[39m(\u001b[38;5;241m15\u001b[39m):\n\u001b[0;32m      9\u001b[0m     elem\u001b[38;5;241m.\u001b[39msend_keys(Keys\u001b[38;5;241m.\u001b[39mPAGE_DOWN)\n\u001b[1;32m---> 10\u001b[0m     \u001b[43mdriver\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mfind_element\u001b[49m\u001b[43m(\u001b[49m\u001b[43mBy\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mCSS_SELECTOR\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43m#content > div > div > div:nth-child(4) > div:nth-child(3) > div.show-more > a\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m)\u001b[49m\u001b[38;5;241m.\u001b[39mclick()\n\u001b[0;32m     11\u001b[0m     time\u001b[38;5;241m.\u001b[39msleep(\u001b[38;5;241m0.1\u001b[39m)\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\site-packages\\selenium\\webdriver\\remote\\webdriver.py:856\u001b[0m, in \u001b[0;36mWebDriver.find_element\u001b[1;34m(self, by, value)\u001b[0m\n\u001b[0;32m    853\u001b[0m     by \u001b[38;5;241m=\u001b[39m By\u001b[38;5;241m.\u001b[39mCSS_SELECTOR\n\u001b[0;32m    854\u001b[0m     value \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m'\u001b[39m\u001b[38;5;124m[name=\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;132;01m%s\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m]\u001b[39m\u001b[38;5;124m'\u001b[39m \u001b[38;5;241m%\u001b[39m value\n\u001b[1;32m--> 856\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mexecute\u001b[49m\u001b[43m(\u001b[49m\u001b[43mCommand\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mFIND_ELEMENT\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43m{\u001b[49m\n\u001b[0;32m    857\u001b[0m \u001b[43m    \u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43musing\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m:\u001b[49m\u001b[43m \u001b[49m\u001b[43mby\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    858\u001b[0m \u001b[43m    \u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mvalue\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m:\u001b[49m\u001b[43m \u001b[49m\u001b[43mvalue\u001b[49m\u001b[43m}\u001b[49m\u001b[43m)\u001b[49m[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mvalue\u001b[39m\u001b[38;5;124m'\u001b[39m]\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\site-packages\\selenium\\webdriver\\remote\\webdriver.py:429\u001b[0m, in \u001b[0;36mWebDriver.execute\u001b[1;34m(self, driver_command, params)\u001b[0m\n\u001b[0;32m    427\u001b[0m response \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mcommand_executor\u001b[38;5;241m.\u001b[39mexecute(driver_command, params)\n\u001b[0;32m    428\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m response:\n\u001b[1;32m--> 429\u001b[0m     \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43merror_handler\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mcheck_response\u001b[49m\u001b[43m(\u001b[49m\u001b[43mresponse\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    430\u001b[0m     response[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mvalue\u001b[39m\u001b[38;5;124m'\u001b[39m] \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_unwrap_value(\n\u001b[0;32m    431\u001b[0m         response\u001b[38;5;241m.\u001b[39mget(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mvalue\u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;28;01mNone\u001b[39;00m))\n\u001b[0;32m    432\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m response\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\site-packages\\selenium\\webdriver\\remote\\errorhandler.py:243\u001b[0m, in \u001b[0;36mErrorHandler.check_response\u001b[1;34m(self, response)\u001b[0m\n\u001b[0;32m    241\u001b[0m         alert_text \u001b[38;5;241m=\u001b[39m value[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124malert\u001b[39m\u001b[38;5;124m'\u001b[39m]\u001b[38;5;241m.\u001b[39mget(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m'\u001b[39m)\n\u001b[0;32m    242\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m exception_class(message, screen, stacktrace, alert_text)  \u001b[38;5;66;03m# type: ignore[call-arg]  # mypy is not smart enough here\u001b[39;00m\n\u001b[1;32m--> 243\u001b[0m \u001b[38;5;28;01mraise\u001b[39;00m exception_class(message, screen, stacktrace)\n",
      "\u001b[1;31mNoSuchElementException\u001b[0m: Message: no such element: Unable to locate element: {\"method\":\"css selector\",\"selector\":\"#content > div > div > div:nth-child(4) > div:nth-child(3) > div.show-more > a\"}\n  (Session info: chrome=106.0.5249.119)\nStacktrace:\nBacktrace:\n\tOrdinal0 [0x00A21ED3+2236115]\n\tOrdinal0 [0x009B92F1+1807089]\n\tOrdinal0 [0x008C66FD+812797]\n\tOrdinal0 [0x008F55DF+1005023]\n\tOrdinal0 [0x008F57CB+1005515]\n\tOrdinal0 [0x00927632+1209906]\n\tOrdinal0 [0x00911AD4+1120980]\n\tOrdinal0 [0x009259E2+1202658]\n\tOrdinal0 [0x009118A6+1120422]\n\tOrdinal0 [0x008EA73D+960317]\n\tOrdinal0 [0x008EB71F+964383]\n\tGetHandleVerifier [0x00CCE7E2+2743074]\n\tGetHandleVerifier [0x00CC08D4+2685972]\n\tGetHandleVerifier [0x00AB2BAA+532202]\n\tGetHandleVerifier [0x00AB1990+527568]\n\tOrdinal0 [0x009C080C+1837068]\n\tOrdinal0 [0x009C4CD8+1854680]\n\tOrdinal0 [0x009C4DC5+1854917]\n\tOrdinal0 [0x009CED64+1895780]\n\tBaseThreadInitThunk [0x7558FA29+25]\n\tRtlGetAppContainerNamedObjectPath [0x77417BBE+286]\n\tRtlGetAppContainerNamedObjectPath [0x77417B8E+238]\n"
     ]
    }
   ],
   "source": [
    "import time\n",
    "elem = driver.find_element(By.TAG_NAME, 'body')\n",
    "for i in range(15):\n",
    "    elem.send_keys(Keys.PAGE_DOWN)\n",
    "    driver.find_element(By.CSS_SELECTOR, '#content > div > div > div:nth-child(4) > div:nth-child(3) > div.show-more > a').click()\n",
    "    time.sleep(0.1)\n",
    "\n",
    "    for i in range(15):\n",
    "        elem.send_keys(Keys.PAGE_DOWN)\n",
    "        driver.find_element(By.CSS_SELECTOR, '#content > div > div > div:nth-child(4) > div:nth-child(3) > div.show-more > a').click()\n",
    "        time.sleep(0.1)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "415cd4bc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "찾은 이미지 개수: 475\n"
     ]
    }
   ],
   "source": [
    "links = []\n",
    "images = driver.find_elements(By.CSS_SELECTOR, '#search-results > div > a > img.product-fragment__image.product-fragment__image--alt')\n",
    "\n",
    "for image in images:\n",
    "    if image.get_attribute('src') is not None:\n",
    "        links.append(image.get_attribute('src'))\n",
    "        \n",
    "print('찾은 이미지 개수:', len(links))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "90d2b415",
   "metadata": {},
   "outputs": [],
   "source": [
    "#search-results > div:nth-child(403) > a > img.product-fragment__image.product-fragment__image--alt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1abab948",
   "metadata": {},
   "outputs": [],
   "source": [
    "#search-results > div:nth-child(404) > a > img.product-fragment__image.product-fragment__image--alt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "24fbb35c",
   "metadata": {},
   "outputs": [],
   "source": [
    "import urllib\n",
    "from urllib import request"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "309ffa38",
   "metadata": {},
   "outputs": [],
   "source": [
    "for k, i in enumerate(links):\n",
    "    url = i\n",
    "    urllib.request.urlretrieve(url, \"D:\\\\이케아가구\\\\3\"+'-'+str(k)+'.jpg')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "92eacac6",
   "metadata": {},
   "outputs": [],
   "source": [
    "1 책상\n",
    "2 의자\n",
    "3 침대\n",
    "4 서랍/수납장"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "08a7bc0d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a48e5f62",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "04d641db",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
