'''
@create : lisa
@file :dvuv_edit_order.py
@Date :2022/6/2
@desc :

'''

import unittest
import requests,threading,time,datetime


#---------------DVUK编辑订单 ：不同的登录系统用户创建不同的订单，客户相同且货品编码相同，分别编辑该两个不同的订单抢最后的库存   并发----------------------
class SummerOver():

    def __init__(self):
        self.url = 'http://test2.elfbar.com/summer/over'
    #用户已登录
    def test1_001(self):
        headers = {"Access-Control-Expose-Headers":"Authorization",
                   "Authorization":"Bearer e46674DN6P7VDAu-9KaOJ738LCuKSs0Ft6rb-eYC5sQ5hNdq41Z75ElL0XT5-dqraGy79yl15HqmKvuDQ0HIp2-Qo5zAaiv12Umj4XUfShc-N3ms1PAIa0RhowZjZuy42YQC3ulKW0Q_N7xwWOQI170Dy0f1nlcfORQhQjwcNAmhb4maklfK95-oNxY85gCJPJfnhZbeg6ZHz7ic1A8hMQY82EpyJ0dyK9Pu0VO_KxtkJmhSm506LQ7owhOr9xsWv1RD_ANwaelyRAHDlt8hPoV1CaFBkw8HNPvaqVJlIVG305iNmBhaPvMZrZP3r4374fMOS4BV6x4-TT4qwjGkXUwTFEZQR5pH_AvmwBhiHI4TjLcHwiJm05F91LgVPIpZVyn5f1W5UXvY4RZM7A",
                   "Content-Language":"en","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
                   "Cookie":"__atuvc=1%7C16; __atuvs=643f9d70fd805666000; _ga_8G02ZXM69R=GS1.1.1681890674.1.1.1681890674.0.0.0; _ga=GA1.2.631828140.1681890674; _gid=GA1.2.1764731860.1681890676; token=Bearer+e46674DN6P7VDAu-9KaOJ738LCuKSs0Ft6rb-eYC5sQ5hNdq41Z75ElL0XT5-dqraGy79yl15HqmKvuDQ0HIp2-Qo5zAaiv12Umj4XUfShc-N3ms1PAIa0RhowZjZuy42YQC3ulKW0Q_N7xwWOQI170Dy0f1nlcfORQhQjwcNAmhb4maklfK95-oNxY85gCJPJfnhZbeg6ZHz7ic1A8hMQY82EpyJ0dyK9Pu0VO_KxtkJmhSm506LQ7owhOr9xsWv1RD_ANwaelyRAHDlt8hPoV1CaFBkw8HNPvaqVJlIVG305iNmBhaPvMZrZP3r4374fMOS4BV6x4-TT4qwjGkXUwTFEZQR5pH_AvmwBhiHI4TjLcHwiJm05F91LgVPIpZVyn5f1W5UXvY4RZM7A"}


        payload = {
                   "gm_keys":"1254P8W6ngxe2KWxBy2PIBojyDpomb31IfsLQu0btXLGdDTaYVlTSFc-_XVFEhmlwXMdT8S-VyTvxHzHsrtpGXo0EtmGaHzcmBJQCR8GgJ7j0ycP8v26z_sAcLrdug3ihDwBY2wo8xWWO2_mqXMCeKSD6tfEtvZffL-i8ef7wRy7KlqBugVMSeTao3x2wKjoho_C62LRx8CNGIOF74gTimc0mo-FlaJ2Ih1J",
                    "gm_grade":"2",
                    "cards_id":"3"
#1  5
        }
        result = requests.post( self.url, data=payload,headers=headers)#或者直接json=payload
        result = result.json()
        print(result)


    def test2_002(self):
        headers = {"Access-Control-Expose-Headers":"Authorization",
                   "Authorization":"Bearer f148sxbSj5ofsipgK7xQojYvaTeGHu6d90XqTGEdH3mTDTRcoZYAulBd_jdyBMMcotwh_yQOoWjtLOZCu-XLr51Gy-fuC_SJodQkY8vKyhUE-bNphnVIkQQxoFwlBfpjq5is3rFM-aCaz-TpKmJfVT3gqltJVA60hhXdkLgFUrWTPZDEg4fYMLpnV1gRvISX0dBQ2ELERIKAgpRGCIzNqZ38zPccLxdTwRFH1b3zJJpB-UHtiCeNFm_vdeYHcjDtW-3MhDm4RLd1BAeOoBe9c3vGpXfF5plFnQVRcf3LADST5ck2bfV5WrdL7OMyUaXMBtBeDTsZAS7oC3MWXTSMuashz74r92YMSbqtCNdK7Axp5LOGt-Wcino7p3K7PPS87GiMP544-VMHk5K3N3Q",
                   "Content-Language":"en","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
                   "Cookie":"__atuvc=1%7C16; __atuvs=643f9e19a61d1ca1000; _ga_8G02ZXM69R=GS1.1.1681890843.1.1.1681890843.0.0.0; _ga=GA1.2.824207372.1681890844; _gid=GA1.2.582863350.1681890844; _gat_gtag_UA_48674434_15=1; token=Bearer+f148sxbSj5ofsipgK7xQojYvaTeGHu6d90XqTGEdH3mTDTRcoZYAulBd_jdyBMMcotwh_yQOoWjtLOZCu-XLr51Gy-fuC_SJodQkY8vKyhUE-bNphnVIkQQxoFwlBfpjq5is3rFM-aCaz-TpKmJfVT3gqltJVA60hhXdkLgFUrWTPZDEg4fYMLpnV1gRvISX0dBQ2ELERIKAgpRGCIzNqZ38zPccLxdTwRFH1b3zJJpB-UHtiCeNFm_vdeYHcjDtW-3MhDm4RLd1BAeOoBe9c3vGpXfF5plFnQVRcf3LADST5ck2bfV5WrdL7OMyUaXMBtBeDTsZAS7oC3MWXTSMuashz74r92YMSbqtCNdK7Axp5LOGt-Wcino7p3K7PPS87GiMP544-VMHk5K3N3Q"}


        payload = {
                   "gm_keys":"4298J-uzD1-ywE49QRkRVBDJJzdehXqUYs6PXv0a9bDq32Uqj47dH8qH3sEAtDsBJO7y6zeWnz-ts91X2QXZ6UYfMnRxWbSpLX60I1zb0a_TnIDfXN5iNOk4DwkPV4DbTZjeSsAAnb-6E0iGFDt4a3FUvMcyMk01Kn7ntzpUtiFt4CjfF4jjVvkRRRFkHC7_0qu9so76ksng6qalbNtvZ_dN8OIMNWvT8Ta4hQ",
                    "gm_grade":"2",
                    "cards_id":"3"

        }
        result = requests.post( self.url, data=payload,headers=headers)#或者直接json=payload
        result = result.json()
        print(result)




def test_001():
    summer_over = SummerOver()
    return summer_over.test1_001()

def test_002():
    summer_over = SummerOver()
    return summer_over.test2_002()

try:
    i = 0
    # 开启线程数目
    tasks_number = 1
    print('测试启动')
    time1 = time.perf_counter()
    while i < tasks_number:
        t1 = threading.Thread(target=test_001)
        t1.start()
        t2 = threading.Thread(target=test_002)
        t2.start()
        i +=1
    time2 = time.perf_counter()
    times = time2 - time1
    print(times/tasks_number)
except Exception as e:
    print(e)