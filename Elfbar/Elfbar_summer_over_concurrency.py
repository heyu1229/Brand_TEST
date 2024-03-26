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
#---------------elfbarSummer  同一个用户 并发测试 ----------------------

class Test_Summer_concurrency():

    def __init__(self):
        self.Url ="http://test2.elfbar.com/summer/over"

    def test_001(self):

        headers = {"Access-Control-Expose-Headers":"Authorization",
                   "Authorization":"Bearer 70345JtGWn_-cf0z_S5cT8Zo9DbcBuAJoenMprVAf438xbywcFvGEJnl47ED27UhiXTE8QeM01TadNWw6hcHjh6AVem06oeRXM8UtyeJ9RBF_r6bb-d7GNS3TCaZ_a1TotZ108_KQ72GmUn0E5WPh6gSDOCL3vxSyPdTvw8aPvgprgGLP_073WiCcLLkB2vrZSf4YO1pDz7MkQgINGX59i6COExT20MjnT-E6A_1CEBOmai9G8MRKNcGm7mmOQB-aXoh-5FRCMOdgTQoIe8_hpm-o1siFcKdANIE4jU08LfH1aVPJB_ZDQXeGGLlBdAdZtQV4BgBxlt1NUX4EiVvk_znqQrk07Q14Z1F07qZRMcl-ly3AoNnYy0r955Hu4XQYZpMU-2rNaf8NlzEJaEJgPxfHCF9WYM",
                   "Content-Language":"en","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
                   "Cookie":"__atuvc=1%7C16; __atuvs=643f98b177463cb5000; _ga_8G02ZXM69R=GS1.1.1681889460.1.1.1681889460.0.0.0; _ga=GA1.2.31196203.1681889460; _gid=GA1.2.1042506293.1681889461; _gat_gtag_UA_48674434_15=1"}


        payload = {
                   "gm_keys":"6dac_eWrDtG6NddlxqGm_foIGuCyYkJ6VpJMo_QDJAVMNC7BAWsKFl6BfnK8VkbyiDXNpoZLKlodDHdnhPSwnOEa0xd4wc6PJkpulLeOHSyTMDS-zDzxRpI-_HsTYulsFznhU45RpRtpU9KlcQIVqCIo0LdgBZu_k6mJEEfIR0PkYlGmsPd6p4XgCIGVBp6MLbNJGXwMlMR4sdexJIjTW_f6wT17jXED5y6fBRM57CCyBjPlCw",
                    "gm_grade":"2",
                    "cards_id":"3"

        }
        result = requests.post(self.Url, data=payload,headers=headers)#或者直接json=payload
        result = result.json()
        print(result)

def Summer():
    deliver = Test_Summer_concurrency()
    return deliver.test_001()

try:
    i = 0
    # 开启线程数目
    tasks_number = 10
    print('测试启动')
    time1 = time.perf_counter()
    while i < tasks_number:
        t1 = threading.Thread(target=Summer)
        t1.start()
        i +=1
    time2 = time.perf_counter()
    times = time2 - time1
    print(times/tasks_number)
except Exception as e:
    print(e)

