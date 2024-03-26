'''
@create : lisa
@file :EBclub
@Date :2023/9/7
@desc :

'''

# -*- coding:UTF-8 -*-
import pytest,json,threading
import requests
import time,gc
import hashlib
from urllib.parse import urlencode
#---------------EBclub  同一个用户 并发测试 ----------------------

class Test_Home_concurrency():

    def __init__(self):
        self.Url ="https://api-club.elfbar.com/api/global"
        # self.Url = "https://api-club.elfbar.com/api/login"

    def test_001(self):
        #设置代理IP
        # proxy_ip = "119.3.213.221:8080"
        #设置代理信息
        # proxies ={"https":proxy_ip}

        headers = {"Accept-Encoding":"gzip, deflate, br","Accept-Language":"zh-CN,zh;q=0.9","Connection":"keep-alive",
                   "Access-Control-Expose-Headers":"Authorization",
                   "Jwt-Admin-Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvdGVzdC1hcGktY2x1Yi5lbGZiYXIuY29tXC9hcGlcL2F1dGhcL2xvZ2luIiwiaWF0IjoxNjk0MDUxNjE1LCJleHAiOjE2OTY2NDM2MTUsIm5iZiI6MTY5NDA1MTYxNSwianRpIjoibFpJaDRPNHVGek1GcXVaVSIsInN1YiI6OTksInBydiI6Ijg2NjVhZTk3NzVjZjI2ZjZiOGU0OTZmODZmYTUzNmQ2OGRkNzE4MTgiLCJpZCI6OTl9.paH7jcn9Vdv_SBgEjfieKZnPo3TX52Qm72j0LaxGFAQ",
                   "Content-Language":"en","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
                   "Set-Cookie":"token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvdGVzdC1hcGktY2x1Yi5lbGZiYXIuY29tXC9hcGlcL2F1dGhcL2xvZ2luIiwiaWF0IjoxNjk0MDUxODg2LCJleHAiOjE2OTY2NDM4ODYsIm5iZiI6MTY5NDA1MTg4NiwianRpIjoiaXE1TExlQlFQa1lvNTFRMSIsInN1YiI6OTksInBydiI6Ijg2NjVhZTk3NzVjZjI2ZjZiOGU0OTZmODZmYTUzNmQ2OGRkNzE4MTgiLCJpZCI6OTl9.wn8yFqW-"}


        payload = {
                   "email": "dev.testmail@heavengifts.com", "password": "Aa123456!", "login_type": "2"
        }
        payload = {

        }
        # result = requests.post(self.Url, data=payload,headers=headers,proxies=proxies)#或者直接json=payload
        result = requests.get(self.Url, data=payload, headers=headers, )
        result = result.json()
        print(result)

def ClubHome():
    deliver = Test_Home_concurrency()
    return deliver.test_001()

try:
    i = 0
    # 开启线程数目
    tasks_number = 50
    print('测试启动')
    time1 = time.perf_counter()
    while i < tasks_number:
        t1 = threading.Thread(target=ClubHome)
        t1.start()
        i +=1
    time2 = time.perf_counter()
    times = time2 - time1
    print(times/tasks_number)
except Exception as e:
    print(e)

