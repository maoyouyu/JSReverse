#!usr/bin/env python
# -*- coding:utf-8 _*-
# @author :   DQ
# @file   :   three_main.py
# @time   :   2021/03/28


import requests


def calculate_m_value():
    # ret = requests.get("http://match.yuanrenxue.com/match/3")
    # print(ret)
    # print(ret.headers)
    sess = requests.session()
    headers = {
        "Host": "match.yuanrenxue.com",
        "Connection": "keep-alive",
        "Content-Length": "0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
        "DNT": "1",
        "Accept": "*/*",
        "Origin": "http://match.yuanrenxue.com",
        "Referer": "http://match.yuanrenxue.com/match/3",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
    }
    sess.headers = headers
    res = sess.get("http://match.yuanrenxue.com/logo",headers=headers)
    ret = requests.get("http://match.yuanrenxue.com/logo",headers=headers)
    print(res.cookies)
    print(ret.cookies)


def get_page(page_num, paramets):
    url = f"http://match.yuanrenxue.com/api/match/3?page={page_num}"
    # print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
        "Cookie": paramets
    }

    res = requests.get(url, headers=headers)
    return res.json()


if __name__ == '__main__':
    calculate_m_value()
    # for i in range(1,6):
    #     m_value = calculate_m_value()
    #     ret = get_page(i,m_value)
    #     data = [__['value'] for __ in ret["data"]]
    #     print(data)
