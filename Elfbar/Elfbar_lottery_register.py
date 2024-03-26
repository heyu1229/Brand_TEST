'''
@create : lisa
@file :Elfbar
@Date :2022/11/24
@desc :

'''

# -*- coding:UTF-8 -*-
import pytest,json,base64
import requests,allure
import time,gc
import hashlib
from urllib.parse import urlencode
#---------------elfbar圣诞节抓娃娃---游戏开始接口----------------------

@allure.feature("")
class Test_register:

    def setup(self):
        self.Url ="https://test.elfbar.com/lottery/register"
        with allure.step(f"接口地址：{self.Url}"):
             print(self.Url)

    @allure.title("")
    def test_001(self):
        headers = {}

        payload = {
                   "name":"555",
                    "phone":"18888052590",
                    "email":"555@qq.com",
                    "referrer":" ",
                    "shopId":"1",
                    "from":"default"


        }
        result = requests.post( self.Url, data=payload,headers=headers)#或者直接json=payload
        result = result.json()
        print(result)


if __name__ == '__main__':
    pytest.main(['-s','Elfbar_summer_over.py'])

