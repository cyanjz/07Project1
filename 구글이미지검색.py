{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "ea11de30",
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting webdriver-manager\n",
      "  Downloading webdriver_manager-3.8.4-py2.py3-none-any.whl (27 kB)\n",
      "Requirement already satisfied: requests in c:\\users\\minji\\anaconda3\\lib\\site-packages (from webdriver-manager) (2.27.1)\n",
      "Requirement already satisfied: tqdm in c:\\users\\minji\\anaconda3\\lib\\site-packages (from webdriver-manager) (4.64.0)\n",
      "Collecting python-dotenv\n",
      "  Downloading python_dotenv-0.21.0-py3-none-any.whl (18 kB)\n",
      "Requirement already satisfied: charset-normalizer~=2.0.0 in c:\\users\\minji\\anaconda3\\lib\\site-packages (from requests->webdriver-manager) (2.0.4)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\minji\\anaconda3\\lib\\site-packages (from requests->webdriver-manager) (2021.10.8)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\\users\\minji\\anaconda3\\lib\\site-packages (from requests->webdriver-manager) (1.26.9)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\minji\\anaconda3\\lib\\site-packages (from requests->webdriver-manager) (3.3)\n",
      "Requirement already satisfied: colorama in c:\\users\\minji\\anaconda3\\lib\\site-packages (from tqdm->webdriver-manager) (0.4.4)\n",
      "Installing collected packages: python-dotenv, webdriver-manager\n",
      "Successfully installed python-dotenv-0.21.0 webdriver-manager-3.8.4\n"
     ]
    }
   ],
   "source": [
    "# !pip install selenium\n",
    "# !pip install webdriver-manager"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9e5a5271",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[WDM] - Downloading: 100%|████████████████████████████████████████████████████████| 6.29M/6.29M [00:00<00:00, 29.3MB/s]\n",
      "C:\\Users\\minji\\AppData\\Local\\Temp\\ipykernel_10368\\2194676639.py:4: DeprecationWarning: executable_path has been deprecated, please pass in a Service object\n",
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
    "URL = 'https://www.google.co.kr/imghp'\n",
    "driver.get(url=URL)\n",
    "\n",
    "driver.implicitly_wait(time_to_wait = 10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "3468566a",
   "metadata": {},
   "outputs": [],
   "source": [
    "from selenium.webdriver.common.by import By\n",
    "from selenium.webdriver.common.keys import Keys"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "312ec8c2",
   "metadata": {},
   "outputs": [],
   "source": [
    "elem = driver.find_element(By.CSS_SELECTOR, 'body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input')\n",
    "elem.send_keys('동서가구 침대')\n",
    "elem.send_keys(Keys.RETURN)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "14dfabb3",
   "metadata": {},
   "outputs": [],
   "source": [
    "import time\n",
    "elem = driver.find_element(By.TAG_NAME, 'body')\n",
    "for i in range(60):\n",
    "    elem.send_keys(Keys.PAGE_DOWN)\n",
    "    time.sleep(0.1)\n",
    "try:\n",
    "    driver.find_element(By.CSS_SELECTOR, '#islmp > div > div > div.tmS4cc.blLOvc.snjnxc > div.gBPM8 > div.qvfT1 > div.YstHxe > input').click()\n",
    "    for i in range(60):\n",
    "        elem.send_keys(Keys.PAGE_DOWN)\n",
    "        time.sleep(0.1)\n",
    "except:\n",
    "    pass"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "7cca9bdd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "찾은 이미지 개수: 535\n"
     ]
    }
   ],
   "source": [
    "links = []\n",
    "images = driver.find_elements(By.CSS_SELECTOR, '#islrg > div.islrc > div > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img')\n",
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
   "execution_count": 103,
   "id": "b01a3747",
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "ename": "URLError",
     "evalue": "<urlopen error [WinError 10060] 연결된 구성원으로부터 응답이 없어 연결하지 못했거나, 호스트로부터 응답이 없어 연결이 끊어졌습니다>",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTimeoutError\u001b[0m                              Traceback (most recent call last)",
      "File \u001b[1;32m~\\anaconda3\\lib\\urllib\\request.py:1346\u001b[0m, in \u001b[0;36mAbstractHTTPHandler.do_open\u001b[1;34m(self, http_class, req, **http_conn_args)\u001b[0m\n\u001b[0;32m   1345\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[1;32m-> 1346\u001b[0m     \u001b[43mh\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mrequest\u001b[49m\u001b[43m(\u001b[49m\u001b[43mreq\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mget_method\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mreq\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mselector\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mreq\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mdata\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mheaders\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   1347\u001b[0m \u001b[43m              \u001b[49m\u001b[43mencode_chunked\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mreq\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mhas_header\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mTransfer-encoding\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m)\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m   1348\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mOSError\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m err: \u001b[38;5;66;03m# timeout error\u001b[39;00m\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\http\\client.py:1285\u001b[0m, in \u001b[0;36mHTTPConnection.request\u001b[1;34m(self, method, url, body, headers, encode_chunked)\u001b[0m\n\u001b[0;32m   1284\u001b[0m \u001b[38;5;124;03m\"\"\"Send a complete request to the server.\"\"\"\u001b[39;00m\n\u001b[1;32m-> 1285\u001b[0m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_send_request\u001b[49m\u001b[43m(\u001b[49m\u001b[43mmethod\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43murl\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mbody\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mheaders\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mencode_chunked\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\http\\client.py:1331\u001b[0m, in \u001b[0;36mHTTPConnection._send_request\u001b[1;34m(self, method, url, body, headers, encode_chunked)\u001b[0m\n\u001b[0;32m   1330\u001b[0m     body \u001b[38;5;241m=\u001b[39m _encode(body, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mbody\u001b[39m\u001b[38;5;124m'\u001b[39m)\n\u001b[1;32m-> 1331\u001b[0m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mendheaders\u001b[49m\u001b[43m(\u001b[49m\u001b[43mbody\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mencode_chunked\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mencode_chunked\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\http\\client.py:1280\u001b[0m, in \u001b[0;36mHTTPConnection.endheaders\u001b[1;34m(self, message_body, encode_chunked)\u001b[0m\n\u001b[0;32m   1279\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m CannotSendHeader()\n\u001b[1;32m-> 1280\u001b[0m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_send_output\u001b[49m\u001b[43m(\u001b[49m\u001b[43mmessage_body\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mencode_chunked\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mencode_chunked\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\http\\client.py:1040\u001b[0m, in \u001b[0;36mHTTPConnection._send_output\u001b[1;34m(self, message_body, encode_chunked)\u001b[0m\n\u001b[0;32m   1039\u001b[0m \u001b[38;5;28;01mdel\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_buffer[:]\n\u001b[1;32m-> 1040\u001b[0m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43msend\u001b[49m\u001b[43m(\u001b[49m\u001b[43mmsg\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m   1042\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m message_body \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[0;32m   1043\u001b[0m \n\u001b[0;32m   1044\u001b[0m     \u001b[38;5;66;03m# create a consistent interface to message_body\u001b[39;00m\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\http\\client.py:980\u001b[0m, in \u001b[0;36mHTTPConnection.send\u001b[1;34m(self, data)\u001b[0m\n\u001b[0;32m    979\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mauto_open:\n\u001b[1;32m--> 980\u001b[0m     \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mconnect\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    981\u001b[0m \u001b[38;5;28;01melse\u001b[39;00m:\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\http\\client.py:1447\u001b[0m, in \u001b[0;36mHTTPSConnection.connect\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m   1445\u001b[0m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mConnect to a host on a given (SSL) port.\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[1;32m-> 1447\u001b[0m \u001b[38;5;28;43msuper\u001b[39;49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mconnect\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m   1449\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_tunnel_host:\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\http\\client.py:946\u001b[0m, in \u001b[0;36mHTTPConnection.connect\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    945\u001b[0m \u001b[38;5;124;03m\"\"\"Connect to the host and port specified in __init__.\"\"\"\u001b[39;00m\n\u001b[1;32m--> 946\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39msock \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_create_connection\u001b[49m\u001b[43m(\u001b[49m\n\u001b[0;32m    947\u001b[0m \u001b[43m    \u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mhost\u001b[49m\u001b[43m,\u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mport\u001b[49m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mtimeout\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43msource_address\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    948\u001b[0m \u001b[38;5;66;03m# Might fail in OSs that don't implement TCP_NODELAY\u001b[39;00m\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\socket.py:844\u001b[0m, in \u001b[0;36mcreate_connection\u001b[1;34m(address, timeout, source_address)\u001b[0m\n\u001b[0;32m    843\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[1;32m--> 844\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m err\n\u001b[0;32m    845\u001b[0m \u001b[38;5;28;01mfinally\u001b[39;00m:\n\u001b[0;32m    846\u001b[0m     \u001b[38;5;66;03m# Break explicitly a reference cycle\u001b[39;00m\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\socket.py:832\u001b[0m, in \u001b[0;36mcreate_connection\u001b[1;34m(address, timeout, source_address)\u001b[0m\n\u001b[0;32m    831\u001b[0m     sock\u001b[38;5;241m.\u001b[39mbind(source_address)\n\u001b[1;32m--> 832\u001b[0m \u001b[43msock\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mconnect\u001b[49m\u001b[43m(\u001b[49m\u001b[43msa\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    833\u001b[0m \u001b[38;5;66;03m# Break explicitly a reference cycle\u001b[39;00m\n",
      "\u001b[1;31mTimeoutError\u001b[0m: [WinError 10060] 연결된 구성원으로부터 응답이 없어 연결하지 못했거나, 호스트로부터 응답이 없어 연결이 끊어졌습니다",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[1;31mURLError\u001b[0m                                  Traceback (most recent call last)",
      "Input \u001b[1;32mIn [103]\u001b[0m, in \u001b[0;36m<cell line: 3>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m k, i \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;28menumerate\u001b[39m(links):\n\u001b[0;32m      4\u001b[0m     url \u001b[38;5;241m=\u001b[39m i\n\u001b[1;32m----> 5\u001b[0m     \u001b[43murllib\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mrequest\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43murlretrieve\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mD:\u001b[39;49m\u001b[38;5;130;43;01m\\\\\u001b[39;49;00m\u001b[38;5;124;43m가구\u001b[39;49m\u001b[38;5;130;43;01m\\\\\u001b[39;49;00m\u001b[38;5;124;43m4\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;241;43m+\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43m-\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;241;43m+\u001b[39;49m\u001b[38;5;28;43mstr\u001b[39;49m\u001b[43m(\u001b[49m\u001b[43mk\u001b[49m\u001b[43m)\u001b[49m\u001b[38;5;241;43m+\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43m.jpg\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m)\u001b[49m\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\urllib\\request.py:239\u001b[0m, in \u001b[0;36murlretrieve\u001b[1;34m(url, filename, reporthook, data)\u001b[0m\n\u001b[0;32m    222\u001b[0m \u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[0;32m    223\u001b[0m \u001b[38;5;124;03mRetrieve a URL into a temporary location on disk.\u001b[39;00m\n\u001b[0;32m    224\u001b[0m \n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m    235\u001b[0m \u001b[38;5;124;03mdata file as well as the resulting HTTPMessage object.\u001b[39;00m\n\u001b[0;32m    236\u001b[0m \u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[0;32m    237\u001b[0m url_type, path \u001b[38;5;241m=\u001b[39m _splittype(url)\n\u001b[1;32m--> 239\u001b[0m \u001b[38;5;28;01mwith\u001b[39;00m contextlib\u001b[38;5;241m.\u001b[39mclosing(\u001b[43murlopen\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mdata\u001b[49m\u001b[43m)\u001b[49m) \u001b[38;5;28;01mas\u001b[39;00m fp:\n\u001b[0;32m    240\u001b[0m     headers \u001b[38;5;241m=\u001b[39m fp\u001b[38;5;241m.\u001b[39minfo()\n\u001b[0;32m    242\u001b[0m     \u001b[38;5;66;03m# Just return the local path and the \"headers\" for file://\u001b[39;00m\n\u001b[0;32m    243\u001b[0m     \u001b[38;5;66;03m# URLs. No sense in performing a copy unless requested.\u001b[39;00m\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\urllib\\request.py:214\u001b[0m, in \u001b[0;36murlopen\u001b[1;34m(url, data, timeout, cafile, capath, cadefault, context)\u001b[0m\n\u001b[0;32m    212\u001b[0m \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[0;32m    213\u001b[0m     opener \u001b[38;5;241m=\u001b[39m _opener\n\u001b[1;32m--> 214\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mopener\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mopen\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mdata\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mtimeout\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\urllib\\request.py:517\u001b[0m, in \u001b[0;36mOpenerDirector.open\u001b[1;34m(self, fullurl, data, timeout)\u001b[0m\n\u001b[0;32m    514\u001b[0m     req \u001b[38;5;241m=\u001b[39m meth(req)\n\u001b[0;32m    516\u001b[0m sys\u001b[38;5;241m.\u001b[39maudit(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124murllib.Request\u001b[39m\u001b[38;5;124m'\u001b[39m, req\u001b[38;5;241m.\u001b[39mfull_url, req\u001b[38;5;241m.\u001b[39mdata, req\u001b[38;5;241m.\u001b[39mheaders, req\u001b[38;5;241m.\u001b[39mget_method())\n\u001b[1;32m--> 517\u001b[0m response \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_open\u001b[49m\u001b[43m(\u001b[49m\u001b[43mreq\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mdata\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    519\u001b[0m \u001b[38;5;66;03m# post-process response\u001b[39;00m\n\u001b[0;32m    520\u001b[0m meth_name \u001b[38;5;241m=\u001b[39m protocol\u001b[38;5;241m+\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m_response\u001b[39m\u001b[38;5;124m\"\u001b[39m\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\urllib\\request.py:534\u001b[0m, in \u001b[0;36mOpenerDirector._open\u001b[1;34m(self, req, data)\u001b[0m\n\u001b[0;32m    531\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m result\n\u001b[0;32m    533\u001b[0m protocol \u001b[38;5;241m=\u001b[39m req\u001b[38;5;241m.\u001b[39mtype\n\u001b[1;32m--> 534\u001b[0m result \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_call_chain\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mhandle_open\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mprotocol\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mprotocol\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m+\u001b[39;49m\n\u001b[0;32m    535\u001b[0m \u001b[43m                          \u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43m_open\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mreq\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    536\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m result:\n\u001b[0;32m    537\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m result\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\urllib\\request.py:494\u001b[0m, in \u001b[0;36mOpenerDirector._call_chain\u001b[1;34m(self, chain, kind, meth_name, *args)\u001b[0m\n\u001b[0;32m    492\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m handler \u001b[38;5;129;01min\u001b[39;00m handlers:\n\u001b[0;32m    493\u001b[0m     func \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mgetattr\u001b[39m(handler, meth_name)\n\u001b[1;32m--> 494\u001b[0m     result \u001b[38;5;241m=\u001b[39m \u001b[43mfunc\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43margs\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    495\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m result \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[0;32m    496\u001b[0m         \u001b[38;5;28;01mreturn\u001b[39;00m result\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\urllib\\request.py:1389\u001b[0m, in \u001b[0;36mHTTPSHandler.https_open\u001b[1;34m(self, req)\u001b[0m\n\u001b[0;32m   1388\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mhttps_open\u001b[39m(\u001b[38;5;28mself\u001b[39m, req):\n\u001b[1;32m-> 1389\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mdo_open\u001b[49m\u001b[43m(\u001b[49m\u001b[43mhttp\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mclient\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mHTTPSConnection\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mreq\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   1390\u001b[0m \u001b[43m        \u001b[49m\u001b[43mcontext\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_context\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mcheck_hostname\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_check_hostname\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\urllib\\request.py:1349\u001b[0m, in \u001b[0;36mAbstractHTTPHandler.do_open\u001b[1;34m(self, http_class, req, **http_conn_args)\u001b[0m\n\u001b[0;32m   1346\u001b[0m         h\u001b[38;5;241m.\u001b[39mrequest(req\u001b[38;5;241m.\u001b[39mget_method(), req\u001b[38;5;241m.\u001b[39mselector, req\u001b[38;5;241m.\u001b[39mdata, headers,\n\u001b[0;32m   1347\u001b[0m                   encode_chunked\u001b[38;5;241m=\u001b[39mreq\u001b[38;5;241m.\u001b[39mhas_header(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mTransfer-encoding\u001b[39m\u001b[38;5;124m'\u001b[39m))\n\u001b[0;32m   1348\u001b[0m     \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mOSError\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m err: \u001b[38;5;66;03m# timeout error\u001b[39;00m\n\u001b[1;32m-> 1349\u001b[0m         \u001b[38;5;28;01mraise\u001b[39;00m URLError(err)\n\u001b[0;32m   1350\u001b[0m     r \u001b[38;5;241m=\u001b[39m h\u001b[38;5;241m.\u001b[39mgetresponse()\n\u001b[0;32m   1351\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m:\n",
      "\u001b[1;31mURLError\u001b[0m: <urlopen error [WinError 10060] 연결된 구성원으로부터 응답이 없어 연결하지 못했거나, 호스트로부터 응답이 없어 연결이 끊어졌습니다>"
     ]
    }
   ],
   "source": [
    "from urllib import request\n",
    "\n",
    "for k, i in enumerate(links):\n",
    "    url = i\n",
    "    urllib.request.urlretrieve(url, \"D:\\\\가구\\\\4\"+'-'+str(k)+'.jpg') # 설치 경로 변경"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "d4ce12e3",
   "metadata": {},
   "outputs": [],
   "source": [
    "1 책상\n",
    "2 의자\n",
    "3 침대\n",
    "4 서랍/수납장"
   ]
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
