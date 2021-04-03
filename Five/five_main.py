#!usr/bin/env python
# -*- coding:utf-8 _*-

# @author :   DQ
# @file   :   five_main.py
# @time   :   2021/03/29

import requests
import execjs

def get_page(page_num, paramets):
    url = f"http://match.yuanrenxue.com/api/match/5?page={page_num}&m={paramets}"
    # print(url)
    res = requests.get(url)
    return res.json()
def calculate_m_value():

    with open(r'D:\Code\JSReverse\Five\js_broke.js', encoding='utf-8', mode='r') as f:
        JsData = f.read()

    psd = execjs.compile(JsData).call("get_is_value")
    print(psd)
    m_value = ""
    return m_value

if __name__ == '__main__':
    calculate_m_value()
    # for i in range(1,6):
    #     m_value = calculate_m_value()
    #     ret = get_page(i,m_value)
    #     data = [__['value'] for __ in ret["data"]]
    #     print(data)

