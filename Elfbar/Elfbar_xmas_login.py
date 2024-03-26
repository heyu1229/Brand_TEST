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
#---------------elfbar圣诞节抓娃娃---游戏注册登录接口----------------------

@allure.feature("")
class Test_Xmas_login:

    def setup(self):
        self.Url ="http://test.elfbar.com/xmas/login"
        with allure.step(f"接口地址：{self.Url}"):
             print(self.Url)

    @allure.title("")
    def test_001(self):
        headers = {"Access-Control-Expose-Headers":"Authorization","Authorization":"Bearer none",
                   "Content-Language":"en","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
                   "Cookie":"T_XMAS_CLAW_AUTH=45b2m_qCjIcLuLcVvj5kfxyW3pALKWkAuyaRXT_s_0QsWJIRd41akwvOt87W2YvMps9n58LBKEtP24vVsmvu1Deut0RlY3LsY2Nm_ZjuULCObH_V248"}
        for i in range(1,20):
            current_time =str(time.time())
            payload = {"email":"132"+current_time+"@qq.com","from":"default"}
            result = requests.post( self.Url, data=payload,headers=headers)#或者直接json=payload
            result = result.json()
            print(result)
            i=i+1


if __name__ == '__main__':
    pytest.main(['-s','Elfbar_xmas_login.py'])

