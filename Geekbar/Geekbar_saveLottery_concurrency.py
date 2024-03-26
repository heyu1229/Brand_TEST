'''
@create : lisa
@file :Elfbar
@Date :2022/11/16
@desc :

'''

# -*- coding:UTF-8 -*-
import base64

import pytest,json,threading
import requests
import time,gc
#---------------Geekbar菲律兵大转盘抽奖  单个用户并发测试 ----------------------

class Test_saveLottery_concurrency():

    def __init__(self):
        self.Url ="http://test.geekbar.com/community/saveLottery"
        self.code = "7UZ78UCA5NRC"

    def test_001(self):
        headers = {"cookie":"acceptcookies=yes; _ga=GA1.2.736104669.1662529965; confirmAge=yes; PHPSESSID=i89r09nphkdtv8agb1sjtvdpca; T_ADMIN_ADMINID=11; T_ADMIN_TOKEN=58136d8720eeddd9a8a7789e694c7f8de836bc35f5075b1564db994c0e080f21; T_ADMIN_LOGINTIME=1668493373; _gid=GA1.2.2009224362.1668576049; _gat_gtag_UA_48674434_13=1"}
        geekbar = self.code + "Df6000&True!"
        token = base64.b64encode(geekbar.encode('utf-8'))
        payload = {"code":self.code,
            "type":"lottery",
            "token":token
        }
        result = requests.post(self.Url, data=payload,headers=headers)#或者直接json=payload
        result = result.json()
        print(result)

def VerifyLottery():
    deliver = Test_saveLottery_concurrency()
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

