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
#---------------elfbar周年庆大转盘抽奖 ----------------------
#返回的字段prize_id大于0代表抽中

@allure.feature("")
class Test_VerifyLottery:

    def setup(self):
        self.Url ="http://test.elfbar.com/activity/verifyLottery"
        with allure.step(f"接口地址：{self.Url}"):
             print(self.Url)

    @allure.title("")
    def test_001(self):
        lottery="elfbarAnniversary2022!"
        verify ={"code":"65736432674986016",
                 "verifyResult":bool(1)}
        verify_lottery = lottery + json.dumps(verify,separators=(',',':'))
        m = hashlib.md5()   #生成MD5对象
        m.update(verify_lottery.encode('utf-8'))   #对数据加密
        api_md5 = m.hexdigest() #获取密文

        headers = {"cookie":"code_token="+api_md5}
        payload = {"code":"65736432674986016",
            "email":"1004856404@qq.com"
        }
        result = requests.post( self.Url, data=payload,headers=headers)#或者直接json=payload
        result = result.json()
        print(result)


if __name__ == '__main__':
    pytest.main(['-s','Elfbar_VerifyLottery.py'])

