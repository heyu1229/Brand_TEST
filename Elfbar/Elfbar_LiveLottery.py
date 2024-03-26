'''
@create : lisa
@file :Elfbar
@Date :2022/9/22
@desc :

'''

# -*- coding:UTF-8 -*-
import allure
import pytest,json
import requests
import time,gc
import hashlib
from urllib.parse import urlencode
#---------------elfbar周年庆直播抽奖 ----------------------
#返回的字段prize_id大于0代表抽中

@allure.feature("")
class Test_LiveLottery:

    def setup(self):
        self.Url ="http://test.elfbar.com/activity/liveLottery"
        with allure.step(f"接口地址：{self.Url}"):
             print(self.Url)

    @allure.title("")
    def test_001(self):
        headers = {"cookie":"authed=1"}
        payload = {
        }
        result = requests.post( self.Url, data=payload,headers=headers)#或者直接json=payload
        result = result.json()
        print(result)


if __name__ == '__main__':
    pytest.main(['-s','Elfbar_LiveLottery.py'])

