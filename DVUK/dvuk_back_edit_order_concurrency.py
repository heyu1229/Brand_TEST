'''
@create : lisa
@file :dvuv_edit_order.py
@Date :2022/6/2
@desc :

'''

import unittest
import requests,threading,time,datetime


#---------------DVUK编辑订单 ：不同的登录系统用户创建不同的订单，客户相同且货品编码相同，分别编辑该两个不同的订单抢最后的库存   并发----------------------
class Edit_order():

    def __init__(self):
        self.base_url = 'https://beta-backend.deepvaping.co.uk/backend/order-detail/editOrder'
    #用户已登录
    def Edit_order1(self):
        payload = {"remove_promotion_products":" ","product[31251_normal_0][sample_type]":" ",
                   "product[31251_normal_0][deal_price]":"10.19","product[31251_normal_0][quantity]":"350",
                   "product[31251_normal_0][id]":"31251",
                   "product[31251_normal_0][type]": "normal", "products[31251_normal_0][promotion_id]": "0",
                   "order[shipping_id]": "4",
                   "order[pay_method_id]": "1", "order[real_shipping_fee]": "160", "order[po_no]": " ",
                   "ship[ship_name]": "just test", "ship[ship_address]": "Unit 16, The Gateway Estate, Birmingham Cargo Airport,",
                   "ship[ship_city]": "Birmingham",
                   "ship[ship_zip]": "B26 3QD", "ship[ship_region_id]": "3285", "ship[ship_province]": "Birmingham",
                   "ship[ship_phone]": "+44 7943 868422","order[tax_id]": " ",
                   "order[company_name]": " ","order_id": "20221104020982"
                   }

        headers = {"Accept-Language": "zh-CN,zh;q=0.9", "Cache-Control":"no-cache", "Connection": "keep-alive", "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
                   "Cookie":"PHPSESSID=srn29e4024j2igetrhf7f9k1s4","Origin":"https://beta-backend.deepvaping.co.uk",
                   "Pragma":"no-cache",
                   "Referer":"https://beta-backend.deepvaping.co.uk/backend/order-detail/index?id=20221104020982&tab=edit",
                   "Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin",
                   "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1",
                   }
        r = requests.post(self.base_url, data=payload, headers=headers)
        result = r.json()
        print(result)

    def Edit_order2(self):
        payload = {"remove_promotion_products":" ","product[31251_normal_0][sample_type]":" ",
                   "product[31251_normal_0][deal_price]":"10.19","product[31251_normal_0][quantity]":"340",
                   "product[31251_normal_0][id]":"31251",
                   "product[31251_normal_0][type]": "normal", "products[31251_normal_0][promotion_id]": "0",
                   "order[shipping_id]": "4",
                   "order[pay_method_id]": "1", "order[real_shipping_fee]": "160", "order[po_no]": " ",
                   "ship[ship_name]": "just test", "ship[ship_address]": "Unit 16, The Gateway Estate, Birmingham Cargo Airport,",
                   "ship[ship_city]": "Birmingham",
                   "ship[ship_zip]": "B26 3QD", "ship[ship_region_id]": "3285", "ship[ship_province]": "Birmingham",
                   "ship[ship_phone]": "+44 7943 868422","order[tax_id]": " ",
                   "order[company_name]": " ","order_id": "20221104056022"
                   }

        headers = {"Accept-Language": "zh-CN,zh;q=0.9", "Cache-Control":"no-cache", "Connection": "keep-alive", "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
                   "Cookie":"PHPSESSID=i9flb6k8i92s691u0qi5cudrpm","Origin":"https://beta-backend.deepvaping.co.uk",
                   "Pragma":"no-cache",
                   "Referer":"https://beta-backend.deepvaping.co.uk/backend/order-detail/index?id=20221104056022&tab=edit",
                   "Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin",
                   "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1",
                   }
        r = requests.post(self.base_url, data=payload, headers=headers)
        result = r.json()
        print(result)



def edit_order1():
    edit_order = Edit_order()
    return edit_order.Edit_order1()

def edit_order2():
    edit_order = Edit_order()
    return edit_order.Edit_order2()

try:
    i = 0
    # 开启线程数目
    tasks_number = 1
    print('测试启动')
    time1 = time.perf_counter()
    while i < tasks_number:
        t1 = threading.Thread(target=edit_order1)
        t1.start()
        t2 = threading.Thread(target=edit_order2)
        t2.start()
        i +=1
    time2 = time.perf_counter()
    times = time2 - time1
    print(times/tasks_number)
except Exception as e:
    print(e)