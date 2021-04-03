#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author :   DQ
@file   :   two_main.py
@time   :   2021/03/27
"""

import requests
import execjs
import time


two_url = "http://match.yuanrenxue.com/match/2"

def calculate_m_value():

    with open(r'D:\Code\JSReverse\Two\broke_js.js', encoding='utf-8', mode='r') as f:
        JsData = f.read()

    psd = execjs.compile(JsData).call('get_m_value')
    print(psd)

    return psd

def get_page(page_num,paramets):
    url = f"http://match.yuanrenxue.com/api/match/2?page={page_num}"
    # print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
        "Cookie":paramets
    }

    res = requests.get(url,headers = headers)
    return res.json()


if __name__ == '__main__':

    for i in range(1,6):
        m_value = calculate_m_value()
        ret = get_page(i,m_value)
        data = [__['value'] for __ in ret["data"]]
        print(data)

