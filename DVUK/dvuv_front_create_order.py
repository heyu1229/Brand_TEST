'''
@create : lisa
@file :dvuv_edit_order.py
@Date :2022/6/2
@desc :

'''

import unittest
import requests,threading,time,datetime,json

#---------------DVUK前台创建订单并发抢库存  ----------------------
class Create_order():

    def __init__(self):
        self.base_url = 'https://beta.deepvaping.co.uk/checkout/createOrder'
    #用户已登录
    def Create_order1(self):
        payload = {
                   "paymentMethod": "1","shippingMethod": "4","address[province]": "Birmingham",
                   "address[first_name]": "lisa_aaaa", "address[last_name]": "lisa_aaaa",
                   "address[street]": "Unit 16, The Gateway Estate, Birmingham Cargo Airport,",
                   "address[city]":"Birmingham","address[zipcode]":"B26 3QD",
                   "address[phone]": "13355856225","address[province_id]":"0",
                   "address[country]": "3285","address[consignee]": "lisa_aaaa lisa_aaaa",
                   "address[company_name]":"aaaaa", "address[tax_id]": " ","billAddress[province]": "Birmingham",
                   "billAddress[first_name]": "lisa_aaaa", "billAddress[last_name]": "lisa_aaaa",
                   "billAddress[street]": "Unit 16, The Gateway Estate, Birmingham Cargo Airport,",
                   "billAddress[city]": "Birmingham","billAddress[post_code]":"B26 3QD",
                   "billAddress[phone]": "13355856225","billAddress[province_id]":"0","billAddress[country]":"3285",
                   "orderNote": " ","isUseBrandPoint": "false", "isUseNormalPoint": "false",
                   }




        headers = {"Accept-Language": "zh-CN,zh;q=0.9", "Cache-Control":"no-cache, private",
                   "Accept-Encoding": "gzip, deflate, br","Accept": "application/json, text/plain, */*",
                   "Connection": "keep-alive",
                   "Content - Length": "901",
                   "Content - Type": "application / x - www - form - urlencoded",
                   "Cookie":"PHPSESSID=i9flb6k8i92s691u0qi5cudrpm; _ga=GA1.3.1774276444.1667283862; product-viewed=[%221190%22]; XSRF-TOKEN=eyJpdiI6IkNLaGgycEN4eERhZ0VNdERhd2xCZEE9PSIsInZhbHVlIjoiOVpHakNjUmxTendrRVdtcHpXRXZQRnFOaEJKcks5QTZERnlVR3BBMTA2dnhGajkxR0F1dG5PNFR0TFZzNkdDKyIsIm1hYyI6ImMwZTBhYzQ3OTUxZDQyZWI5ZGY4NTI2Njk5OThjMTNjMWMyYWYyMzVjNzJhNmIzZGM0OTE0YjY4OTExMTYwNWEifQ%3D%3D; deepvaping_uk_beta_session=eyJpdiI6IlwvQjNYY2JoMENnWVdtZTJpTEZZU2FnPT0iLCJ2YWx1ZSI6Inl1U2V5QmV3a1NPUmJlam5oUUg5alFHU2J5ZEE1amdqaTFsTjVBenhSZGFjbUdKaituWnBjMFNobTRcL240Um5NIiwibWFjIjoiYjk0NjhjODMwOTIxNzg1Y2M3MGFhMzA2NGVkNjM0OWRlYjBkOWRkYmJlODc2NDZiYTk5NTkzNzFlYmFiMGFhOCJ9",
                   "Host": "beta.deepvaping.co.uk",
                   "Origin":"https://beta.deepvaping.co.uk","Referer": "https://beta.deepvaping.co.uk/checkout",
                   "Pragma":"no-cache","Referer":"https://beta.deepvaping.co.uk/checkout",
                   "Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin",
                   "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
                   "X-CSRF-TOKEN":"Dwq5SqpAEpo4ymjUwowAYiPoq2zwR5xxj2fLhW5h",
                   "X-Requested-With":"XMLHttpRequest",
                   "X - XSRF - TOKEN": "eyJpdiI6Im5yTWdCNG5TcGtRQ0lnOVB2TDZzWnc9PSIsInZhbHVlIjoiSk5kUnJXUEs2cG14alladVRsdTFTaWpNcmdKNnl4MzZnbFRyV1ZQMG9kUDFMdEFmdFh2TW5IdkJVTFEwaHF3ciIsIm1hYyI6ImJiNDhiNDY3ODM2N2JmNDc4MDMyMTEzYTE0NjBmNzQ3OGFjOGE4ZGFhYjU4MTdhOTlkM2UwMjczYmRmMGY3NDkifQ =="
                   }
        result = requests.post(self.base_url, data=payload, headers=headers)
        result = result.json()
        print(result)

def front_create_order():
    create_oder = Create_order().Create_order1()


try:
    i=0
    tasts_number=10
    print("测试启动")
    while i < tasts_number:
        t = threading.Thread(target=front_create_order)
        t.start()
        i+=1
    print(datetime.datetime.now())
except Exception as e:
    print(e)
