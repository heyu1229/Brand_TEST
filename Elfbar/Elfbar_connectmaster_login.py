'''
@create : lisa
@file :Elfbar
@Date :2022/9/22
@desc :

'''

# -*- coding:UTF-8 -*-
import random

import allure
import pytest,json
import requests
import time,gc
import hashlib
from urllib.parse import urlencode
#---------------elfbar周年庆配对消除游戏 ----------------------
#返回的字段prize_id大于0代表抽中

@allure.feature("")
class Test_Connectmaster_login:

    def setup(self):
        self.Url ="http://test2.elfbar.com/connectmaster/login"
        with allure.step(f"接口地址：{self.Url}"):
             print(self.Url)


    @allure.title("")
    def test_001(self):
        headers = {"Access-Control-Expose-Headers": "Authorization",
                   "Content-Language": "en", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
        for i in range(100):
            # self.time = str(int(time.time()))
            A = str(random.randint(1, 100))
            payload = {
                "email": "lisa" + A + "@qq.com", "from": "default"
            }
            result = requests.post( self.Url, data=payload,headers=headers)#或者直接json=payload
            result = result.json()
            print(result)


if __name__ == '__main__':
    pytest.main(['-s','Elfbar_connectmaster_login.py'])

