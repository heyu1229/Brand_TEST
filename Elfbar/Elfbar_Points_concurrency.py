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
        self.Url ="https://test.elfbar.com/lottery/exchange"

    def test_001(self):

        headers = {"Authorization":"Bearer 5d2aBfPDofJrsgzg_wXR5Gg54lIdGRameboiKB02xvLdW4HM3l_qIiOAH0BDSCxYSa-FY-C-0fItLLDFh3LkLbCdi-p8-7xJPbtBwpWERDCa7aLgzlTCSOT_xyZcLOp9_xdCA5StJooLqm81by_N6K3AU8MtoeazYnU_rbWrgdX_bucslP3iw5FvCOX27cCDSRFxsPBfa8SKqsQuYj_SwJL3lYhtRHF7Kdx195lbzEQnkFMgCeHeVuiss0tpkZZnZKfM"}
        payload = {"ids[]":"1","totalPoint":"1.11",
                   "name": "lisa",
                   "phone": "18888052595",
                   "street": "22",
                   "city": "22",
                   "province": "223",
                   "postcode": "22",
                   "shopId": "1",
                   "from": "default",
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
    tasks_number = 3
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

