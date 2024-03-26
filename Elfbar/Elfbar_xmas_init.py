'''
@create : lisa
@file :Elfbar
@Date :2022/11/24
@desc :

'''

# -*- coding:UTF-8 -*-
import pytest,json
import requests,allure
import time,gc
import hashlib
from urllib.parse import urlencode
#---------------elfbar圣诞节抓娃娃---游戏初始化接口----------------------

@allure.feature("")
class Test_Xmas_init:

    def setup(self):
        self.Url ="http://test.elfbar.com/xmas/init"
        with allure.step(f"接口地址：{self.Url}"):
             print(self.Url)

    @allure.title("")
    def test_001(self):
        headers = {"Access-Control-Expose-Headers":"Authorization","Authorization":"Bearer none",
                   "Content-Language":"en","Content-Type":"application/json"}
        payload = {
        }
        result = requests.post( self.Url, data=payload,headers=headers)#或者直接json=payload
        result = result.json()
        print(result)


if __name__ == '__main__':
    pytest.main(['-s','Elfbar_xmas_init.py'])

