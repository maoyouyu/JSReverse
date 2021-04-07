#!usr/bin/env python
# -*- coding:utf-8 _*-

# @author :   DQ
# @file   :   test.py
# @time   :   2021/03/29


import requests
import execjs
# url = "http://mall.ckcest.cn/mall/listContent.ilf"
# ret = requests.get(url)
# arg1 = ret.text.split("arg1=")[-1].split(";")[0].strip('"').strip("'")
# print(arg1)
# with open(r'D:\Code\JSReverse\zggckjzszx\test.js', encoding='utf-8', mode='r') as f:
#     JsData = f.read()
# psd = execjs.compile(JsData).call('get_arg3_value', arg1)

import requests

cookies = {
    '_Collect_ISNEW': '1617799373226',
    '_Collect_UD': 'b077b785-7842-430c-843e-092f560e4d50',
    '_uab_collina': '161780090977104704735464',
    '_YS_userAccect': '6d8dd931-78c6-4926-83b2-19deb6aa5c19',
    '_Collect_SN': '0',
    'JSESSIONID': '7088752567F0116296839F95DC940900',
    'Hm_lvt_789fd650fa0be6a2a064d019d890b87f': '1617799373',
    'acw_tc': '276aedda16178034084306783e5eb8cf3e66f0c5f9ccccc484d73bb8f45976',
    'Hm_lpvt_789fd650fa0be6a2a064d019d890b87f': '1617803456',
    'ssxmod_itna': 'YqfOGKBKDK0KCDlSD+obkneDvP7Iq+6IfAxXdD/AY+DnqD=GFDK40EYgwtup+p=obrBTX1L7=YcGP5yEnu+Wd+G40aDbqGkzmir4GGjxBYDQxAYDGDDPkDj4ibDY4tBnwxWKDwDlKDgD7QlUqDfDDLnbGAnYeLnmqdV0qiDAuqgAG+nD0tDIqGXYBuPbqDBDanPDYpWKwN/DBQD7kiBn4iDC2mqFSGYA4wfFbqsDYv=S7wY8YhKehgq3UfQf7qI494GXDDAKi4GPD===',
    'ssxmod_itna2': 'YqfOGKBKDK0KCDlSD+obkneDvP7Iq+6IfAxNG9i5xBuwSD7P32BFfBp7NFCZhzRnrYrXC2DSdFqwSBElg2Atk8L8bEHLUhptC5ftPEFpDRE37p5ix7jPjDjKD2FYD===',
    'acw_sc__v2': '606db8c2db355082f0e9d00cdcd615b24bc7cfc9',
}

headers = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'DNT': '1',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'Referer': 'http://mall.ckcest.cn/mall/list.html',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

params = (
    ('dbId', '1000'),
    ('text', ''),
    ('express', ''),
    ('secondSearchExpress', ''),
    ('fieldSearchExpress', ''),
    ('fieldSearchEntity', ''),
    ('order', '1'),
    ('startYear', '1700'),
    ('endYear', '2099'),
    ('page', '1'),
    ('limit', '10'),
    ('model', '1'),
    ('isadvanced', '0'),
    ('picture', ''),
    ('uuid', ''),
)

response = requests.get('http://mall.ckcest.cn/mall/listContent.ilf', headers=headers, params=params, cookies=cookies, verify=False)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('http://mall.ckcest.cn/mall/listContent.ilf?dbId=1000&text=&express=&secondSearchExpress=&fieldSearchExpress=&fieldSearchEntity=&order=1&startYear=1700&endYear=2099&page=1&limit=10&model=1&isadvanced=0&picture=&uuid=', headers=headers, cookies=cookies, verify=False)
print(response.text)
