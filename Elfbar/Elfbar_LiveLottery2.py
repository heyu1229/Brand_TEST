'''
@create : lisa
@file :Elfbar
@Date :2022/9/22
@desc :

'''

# -*- coding:UTF-8 -*-
import allure,threading
import pytest,json
import requests
import time,gc
import hashlib
from urllib.parse import urlencode
#---------------elfbar周年庆直播抽奖   并发----------------------
#返回的字段prize_id大于0代表抽中


class Test_LiveLottery():

    def __init__(self):
        self.Url ="http://test.elfbar.com/activity/liveLottery"

    def test_001(self):
        headers = {"cookie":"authed=1"}
        payload = {
        }
        result = requests.post( self.Url, data=payload,headers=headers)#或者直接json=payload
        result = result.json()
        print(result)

def LiveLottery():
    deliver = Test_LiveLottery()
    return deliver.test_001()

try:
    i = 0
    # 开启线程数目
    tasks_number = 100
    print('测试启动')
    time1 = time.perf_counter()
    while i < tasks_number:
        t1 = threading.Thread(target=LiveLottery)
        t1.start()
        i +=1
    time2 = time.perf_counter()
    times = time2 - time1
    print(times/tasks_number)
except Exception as e:
    print(e)

