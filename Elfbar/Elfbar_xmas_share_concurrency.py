'''
@create : lisa
@file :Elfbar
@Date :2022/9/22
@desc :

'''

# -*- coding:UTF-8 -*-
import pytest,json,threading
import requests
import time,gc
import hashlib
from urllib.parse import urlencode
#---------------elfbar  抓娃娃分享  并发测试 ----------------------

class Test_Xmas_share_concurrency():

    def __init__(self):
        self.Url ="http://test.elfbar.com/xmas/share"

    def test_001(self):
        headers = {"Access-Control-Expose-Headers": "Authorization", "Authorization": "Bearer 173bfBvpXYEaLFRVZBoAoLuGJxVlguXg2Xri1m9_A6XmrYk2s6dVNuWhRVVgDbR20inXUEnTFrBiR3kbfa72ysXk-B2r729Ky7yxX5ozUutSRRKsdQ",
                   "Content-Language": "en", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                   "Cookie": "token=Bearer%20173bfBvpXYEaLFRVZBoAoLuGJxVlguXg2Xri1m9_A6XmrYk2s6dVNuWhRVVgDbR20inXUEnTFrBiR3kbfa72ysXk-B2r729Ky7yxX5ozUutSRRKsdQ; _ga_8G02ZXM69R=GS1.1.1669970086.6.1.1669971536.0.0.0; _ga=GA1.2.623142646.1669863104; _gid=GA1.2.1714427324.1669863104; __atuvc=50%7C48; __atuvs=6389b8a6f0e2fb7200f; T_XMAS_CLAW_AUTH=173bfBvpXYEaLFRVZBoAoLuGJxVlguXg2Xri1m9_A6XmrYk2s6dVNuWhRVVgDbR20inXUEnTFrBiR3kbfa72ysXk-B2r729Ky7yxX5ozUutSRRKsdQ; PHPSESSID=bemtjbo7pvnejnjpg5geq2eilh"}
        payload = {"share_from": "facebook"}
        result = requests.post(self.Url, data=payload,headers=headers)#或者直接json=payload
        result = result.json()
        print(result)

def XmasShare():
    deliver = Test_Xmas_share_concurrency()
    return deliver.test_001()

try:
    i = 0
    # 开启线程数目
    tasks_number = 20
    print('测试启动')
    time1 = time.perf_counter()
    while i < tasks_number:
        t1 = threading.Thread(target=XmasShare)
        t1.start()
        i +=1
    time2 = time.perf_counter()
    times = time2 - time1
    print(times/tasks_number)
except Exception as e:
    print(e)

