#!usr/bin/env python
# -*- coding:utf-8 _*-

# @author :   DQ
# @file   :   test.py
# @time   :   2021/03/29


import requests

cookies = {
    'wwwcookie': '18205800',
    '__jsluid_h': 'a7ab2989e04879aad8df0bf7c03b1b7f',
    'UM_distinctid': '178a73df0116c2-0785edad9f769a-c3f3568-240000-178a73df012a35',
    'CNZZDATA1276383350': '1401340496-1617710696-https^%^253A^%^252F^%^252Fwww.baidu.com^%^252F^%^7C1617710696',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'DNT': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'If-None-Match': 'W/^\\^24bb7-5bf4c1936e140^\\^',
    'If-Modified-Since': 'Tue, 06 Apr 2021 11:27:25 GMT',
}

response = requests.get('http://www.samr.gov.cn/', headers=headers, cookies=cookies, verify=False)
print(response.text)
print(response)
