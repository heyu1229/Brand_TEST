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
#---------------elfbar  配对登录用户 并发测试 ----------------------

class Test_Connectmaster_Login():

    def __init__(self):
        self.Url ="http://test2.elfbar.com/connectmaster/login"
        self.time =str(int(time.time()))
        print(self.time)

    def test_001(self):
        headers = {"Access-Control-Expose-Headers": "Authorization",
                   "Content-Language": "en", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
        payload = {"email": "lisa"+self.time+"@qq.com","from":"default"}
        result = requests.post(self.Url, data=payload,headers=headers)#或者直接json=payload
        result = result.json()
        print(result)

def Connectmaster_Login():
    deliver = Test_Connectmaster_Login()
    return deliver.test_001()

try:
    i = 0
    # 开启线程数目
    tasks_number = 100
    print('测试启动')
    time1 = time.perf_counter()
    while i < tasks_number:
        t1 = threading.Thread(target=Connectmaster_Login)
        t1.start()
        i +=1
    time2 = time.perf_counter()
    times = time2 - time1
    print(times/tasks_number)
except Exception as e:
    print(e)

