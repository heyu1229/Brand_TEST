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
#---------------elfbar周年庆大转盘抽奖（请求的邮箱要在库里已存在的）  并发测试 ----------------------
#返回的字段prize_id大于0代表抽中

class Test_VerifyLottery_concurrency():

    def __init__(self):
        self.Url ="https://test.elfbar.com/lottery/startLottery"

    def test_001(self):

        headers = {"Authorization":"Bearer 5ac9zW4_WMpqkkKL_iSfFyD-BvxynTy9EOjtov4Phh4H2i2nrqfUBbwqdTTRnWZbSrSZcKeYsI3ZBljOYwfA7Y59YwaAIIQGFrhPjidDAhdbDD76srAUgdC7l5wzgpVN6HJDYLznooCiH1gJdpZcb55C1QflK-m7G6SbJyEhKwhLt6EDPbfi3uBM3cd-Sf2ub5w9atMdiu45PpIDCGNKLm3TgirSBIypfNEs7NnoXEBCusNB5Nlh_B2ieBOShlroVT9Q"}
        payload = {"shopId":"1",
        }
        result = requests.post(self.Url, data=payload,headers=headers)#或者直接json=payload
        result = result.json()
        print(result)

def VerifyLottery():
    deliver = Test_VerifyLottery_concurrency()
    return deliver.test_001()

try:
    i = 0
    # 开启线程数目
    tasks_number = 10
    print('测试启动')
    time1 = time.perf_counter()
    while i < tasks_number:
        t1 = threading.Thread(target=VerifyLottery)
        t1.start()
        i +=1
    time2 = time.perf_counter()
    times = time2 - time1
    print(times/tasks_number)
except Exception as e:
    print(e)

