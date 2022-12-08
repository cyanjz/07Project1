import numpy as np
from requests import request, Session
from PCH import ScrapUtility
from bs4 import BeautifulSoup
import pandas as pd
import re

headers = ScrapUtility.build_header('''Accept: text/html, */*; q=0.01
Accept-Encoding: gzip, deflate, br
Accept-Language: ko-KR,ko;q=0.9
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Cookie: PCID=dc960711-4697-7c00-cd6f-c174a44135c0-1669164813094; SCOUTER=x361c2kg6anmj7; RB_PCID=1669164813729287420; _fbp=fb.1.1669164813756.43892844; EG_GUID=23c4d663-fad4-492c-9ba9-5add196fccdb; _gcl_au=1.1.1498591150.1669164814; emf.1074.euuid.v5=efa659d8-ma80-4bfa-s3d0-2282f2107c87; _ga=GA1.2.1981804943.1669164814; _gid=GA1.2.1949734383.1669164814; _gat_gtag_UA_134613041_2=1; _dc_gtm_UA-134613041-5=1; _gat_UA-134613041-6=1; _wp_uid=1-e29f6b06f780cc80540ab1c476a61885-s1669164813.967151|windows_10|chrome-llwv3e; _qg_fts=1669164814; QGUserId=2853703625347704; _qg_pushrequest=true; _qg_cm=2; RB_SSID=iAEs09JroC; _gat_UA-134613041-4=1; JSESSIONID=1E398C116D4E68BBE2FF1ED2A414BB9C
Host: www.hanssem.com
Origin: https://www.hanssem.com
Referer: https://www.hanssem.com/category/midCtgList.do?ctgNo=13808&categoryall=Y
sec-ch-ua: "Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36
X-Requested-With: XMLHttpRequest''')

c = '''
AEC	AakniGO2BWABj_4sC9CtPKxBwrXHCRHadY4G85NBzurjlPxhQbnneqIz2mk	.google.com	/	2023-05-22T00:53:30.934Z	62	✓	✓	Lax			Medium	
JSESSIONID	1E398C116D4E68BBE2FF1ED2A414BB9C	www.hanssem.com	/	Session	42						Medium	
RB_SSID	iAEs09JroC	.hanssem.com	/	2022-11-23T01:23:37.000Z	17						Medium	
1P_JAR	2022-11-23-0	.google.com	/	2022-12-23T00:55:23.000Z	18						Medium	
_qg_pushrequest	true	.hanssem.com	/	2022-11-23T01:53:34.000Z	19						Medium	
_qg_cm	2	.hanssem.com	/	2022-12-07T00:53:34.000Z	7						Medium	
_qg_fts	1669164814	.hanssem.com	/	2023-11-23T00:53:37.000Z	17						Medium	
emf.1074.euuid.v5	efa659d8-ma80-4bfa-s3d0-2282f2107c87	.hanssem.com	/	2023-02-21T00:53:34.000Z	53						Medium	
_gcl_au	1.1.1498591150.1669164814	.hanssem.com	/	2023-02-21T00:53:33.000Z	32						Medium	
RB_PCID	1669164813729287420	.hanssem.com	/	2023-12-28T00:53:33.730Z	26						Medium	
_ga	GA1.2.1981804943.1669164814	.hanssem.com	/	2023-12-28T00:53:39.102Z	30						Medium	
SCOUTER	x361c2kg6anmj7	www.hanssem.com	/	2023-12-28T00:53:33.484Z	21						Medium	
_gid	GA1.2.1949734383.1669164814	.hanssem.com	/	2022-11-24T00:53:39.000Z	31						Medium	
EG_GUID	23c4d663-fad4-492c-9ba9-5add196fccdb	.hanssem.com	/	2023-12-28T00:53:33.780Z	43						Medium	
NID	511=IEZA1wrQc8GI_2PMe7mBUbNIdRzwYyMafLox9QZa6Bni18ZwkkAdECjGh-YdhK_MM6fIdy07jr3fEpraHL5v_iKgMEPPRed6q9UKrG4vpCQEvyW701TjfmYfubWK3ytGO1Br66IIBxDHn-XtKzQE0SvXocfHNXmJfbVQNTweifs	.google.com	/	2023-05-25T00:55:23.601Z	178	✓	✓	None			Medium	
_fbp	fb.1.1669164813756.43892844	.hanssem.com	/	2023-02-21T00:53:38.000Z	31			Lax			Medium	
QGUserId	2853703625347704	.hanssem.com	/	2023-11-23T00:53:37.000Z	24						Medium	
_wp_uid	1-e29f6b06f780cc80540ab1c476a61885-s1669164813.967151|windows_10|chrome-llwv3e	.hanssem.com	/	2023-11-23T00:53:34.000Z	85						Medium	
DV	A-83UVf5II8e0J-HU_sc0edyjbcfShg	www.google.com	/	2022-11-23T01:05:23.000Z	33						Medium	
PCID	dc960711-4697-7c00-cd6f-c174a44135c0-1669164813094	www.hanssem.com	/	2023-12-28T00:53:33.094Z	54						Medium	'''

session = Session()
session = ScrapUtility.set_cookies(session, c)
session.header = headers
resp = session.post('https://www.hanssem.com/category/goodsListWebAjax.do')

print(resp.status_code)