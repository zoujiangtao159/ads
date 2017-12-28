import hashlib
import json
import random
import traceback
import urllib

import requests
import time
from ads.appsflyer_t.date.redis_sql_link import Redis111,Redis2,Redis3,Redis4,Redis5,Redis6,Redis7


def appfly_request(refer_url):
    data2 = {"device": "potter",
            "firstLaunchDate": "2017-11-06_060910+0000",        #第一次启动时间#
            "referrer": "af_tranid=YsEp2MEbUuQ2X0vrXtIECA&pid=solosystem_int&clickid=e0c1996e-7502-41cb-bd79-88a329c11d87__pspm&af_siteid=143347&af_sub1=47_5079&gaid=3ea4c99c-c509-47ea-88a6-eeb54b42145e&af_channel=143347_47_5079&c=tier1",
            "installDate": "2017-11-06_060847+0000",            #安装时间#
            #"extraReferrers": "{\"af_tranid=YsEp2MEbUuQ2X0vrXtIECA&pid=solosystem_int&clickid=e0c1996e-7502-41cb-bd79-88a329c11d87__pspm&af_siteid=143347&af_sub1=47_5079&gaid=3ea4c99c-c509-47ea-88a6-eeb54b42145e&af_channel=143347_47_5079&c=tier1\":\"[1511840398895,1511840398913,1511840398968,1511840399600,1511840400613]\"}",
            "sdk": "24",                                        #手机安卓版本
            "carrier": "",                                      #运营商
            "batteryLevel": "96.0",                             #电池电量
            #"android_id": "48d3d31bd41ae2f6",
            #"imei": "351856081013831",
            "deviceFingerPrintId": "ffffffff-cb12-69b1-0000-000068358894",      #指纹ID
            "date1": "2017-11-06_060847+0000",                  #等于安装时间firstInstallTime
            "tokenRefreshConfigured": False,                    #token刷新配置
            "af_preinstalled": "false",                         #appsflyer预安装
            "advertiserIdEnabled": "true",                      #广告客户已启用
            "af_sdks": "0000000000",
            "iaecounter": "1",
            "appsflyerKey": "qbKVyawAiwNX3b4D3Frijm",
            "lang_code": "en",                                                 #代码语言
            "registeredUninstall": False,                                     #注册卸载
            #"installer_package": "com.google.android.packageinstaller",  #安装来源
            "app_version_name": "5.0.1",                                    #app版本号
            "lang": "English",                                                  #语言
            "timepassedsincelastlaunch": "-1",                            #应用单次启动时间#
            "advertiserId": "1f0ba7e7-8520-48e1-9c7e-d4775f609ca9",    #广告ID
            "isGaidWithGps": "true",
            "deviceData": {
                "cpu_abi": "armeabi-v7a",
                "cpu_abi2": "armeabi",
                "arch": "",                                                 #开发者模式
                "build_display_id": "NPN25.137-33"
            },
            "af_v2": "7485d5cdfb2ddbb8ca8be5045c24b2ecae52a14e",      #af秘钥#
            "deviceType": "user",                                          #设备类型
            "af_v": "bbc2771fe3f6d10b495e278e521e497e60c48f92",         #af_v#
            "app_version_code": "15",                                   #app版本号
            "af_events_api": "1",                                       #af时间api
            "platformextension": "android_native",                     #平台拓展
            "network": "WIFI",                                          #网络
            "operator": "",                                                #操作者
            "country": "CN",                                            #国家
            "date2": "2017-11-06_060847+0000",                      #等于安装时间 lastUpdateTime
            "brand": "motorola",
            "af_timestamp": "1509948549969",                        #时间戳#
            "uid": "1509948527824-6831593699037592394",             #UID#
            "isFirstCall": "true",                                      #是第一个电话
            "counter": "1",                                                #计数器
            "model": "Moto G (5) Plus",                                 #型号
            "product": "potter"                                         #产品
            }
    #redis取值
    data_code = "{'device': 'G8142', 'firstLaunchDate': '2017-12-14_053631-0500', 'installDate': '2017-12-14_053629-0500', 'sdk': '25', 'carrier': '', 'batteryLevel': '100.0', 'deviceFingerPrintId': 'ffffffff-c4af-3fd9-0000-000023cd71f1', 'date1': '2017-12-14_053629-0500', 'af_preinstalled': 'false', 'advertiserIdEnabled': 'true', 'af_sdks': '0000000000', 'iaecounter': '0', 'appsflyerKey': 'fZvuk792H9hJQKmaTwuXxA', 'lang_code': 'en', 'app_version_name': '1.0', 'lang': 'English', 'timepassedsincelastlaunch': '0', 'android_id': '2dc7057f6a4d17c4', 'advertiserId': '67263353-c03f-4a7f-8103-5bca5d10c204', 'isGaidWithGps': 'true', 'deviceData': {'build_display_id': '45.0.A.7.120', 'arch': '', 'cpu_abi': 'arm64-v8a', 'cpu_abi2': ''}, 'af_v2': 'd5b6baab6c6c3b5d339a9e78c868e7860ba0556c', 'deviceType': 'user', 'af_v': '3fb92b4895288e5af27a0038d5ffe31ca942337f', 'app_version_code': '1', 'af_events_api': '1', 'platformextension': 'android_native', 'network': 'WIFI', 'operator': 'VIETTEL', 'country': 'US', 'date2': '2017-12-14_053629-0500', 'brand': 'Sony', 'af_timestamp': '1513247791195', 'uid': '1513247789245-7492075964336390204', 'isFirstCall': 'true', 'counter': '1', 'model': 'G8142', 'product': 'G8142'}"
    value_res_data = eval(data_code)
    redis_value_data = json.dumps(value_res_data)
    data = json.loads(redis_value_data)

    header = {
        'Content-Length': '1180',
        'Content-Type': 'application/json',
        'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.0; Moto G (5) Plus Build/NPN25.137-33)',
        'Host': 't.appsflyer.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
    }

    #refer_url = 'http://c.snnd.co/api/v4/click?campaign_id=8999118&publisher_id=1139&rt=171222020355&_po=79b16c6956481ef572be24e95a848f9d&_mw=p&_c=50&_cw=p&_ad=1368&publisher_slot=&sub_1=&pub_gaid=302f2641-2c2e-41bc-867f-e1b14556d844&pub_idfa=&pub_aid=72db996fd65bbe82'
    #refer_url = ''
    refer_package =get_final_url(refer_url)
    print('refer_package',refer_package)
    time.sleep(10)
    data2 = json.dumps(data)
    data3 = json.loads(data2)
    #data3['advertiserId'] = "302f2641-2c2e-41bc-867f-e1b14556d844"
    # 发送请求的时间戳
    data3['af_timestamp'] = str(int(round(time.time() * 1000)))
    print(str(int(round(time.time() * 1000))))
    # data3['af_timestamp'] = "1513563247921";

    url = 'https://t.appsflyer.com/api/v4/androidevent?' + 'buildnumber=4.8.5&app_id=' + refer_package['id']

    #refer
    data3['referrer'] = urllib.parse.unquote(refer_package['referrer'])
    print(data3['referrer'])

    #生成应用安装时间戳
    install_rand_time = random.randint(50000, 100000)
    af_installDate = int(data3['af_timestamp']) - install_rand_time
    print(af_installDate)
    # af_installDate = 1513563230131

    #生成uid
    aa = random.randint(100, 999)
    uid = str(af_installDate) +'-'+str(int(random.random() * 10 ** 16)) + str(aa)
    data3['uid'] = uid
    # data3['uid'] = "1513563230131-5575256377220633155"

    # 安装时间戳转化为installDate"installDate": "2017-11-06_060847+0000",
    af_i222stallDate  =time.gmtime(af_installDate/1000)
    af_i222stallDate22 = time.strftime("%Y-%m-%d_%H%M%S"+"+0000", af_i222stallDate)
    data3['installDate'] = af_i222stallDate22

    #启动时间"firstLaunchDate": "2017-11-06_060910+0000"
    lanch_rand_time = random.randint(0, install_rand_time)
    # firstLaunchDate_time_u = af_installDate + lanch_rand_time
    firstLaunchDate_time_u = int(data3['af_timestamp']) - lanch_rand_time
    firstLaunchDate_time = time.gmtime(firstLaunchDate_time_u / 1000)
    firstLaunchDate_time22 = time.strftime("%Y-%m-%d_%H%M%S" + "+0000", firstLaunchDate_time)
    data3['firstLaunchDate'] = firstLaunchDate_time22
    print(firstLaunchDate_time22)

    #启动时长
    lan_time = random.randint(0, 30)
    data3['timepassedsincelastlaunch'] = str(-1)

    #iaecounter
    iaecounter = 1
    data3['iaecounter'] = str(iaecounter)

    #date1
    data3['date1'] = data3['installDate']
    data3['date2'] = data3['installDate']

    # 生成af_v
    sh1 = data3['appsflyerKey'][0:7]+data3['uid'][0:7]+data3['af_timestamp'][6:13]
    afv = hashlib.sha1(sh1.encode()).hexdigest()
    data3['af_v'] = afv

    # 生成af_v2
    tomd5 = str(data3['appsflyerKey'])+str(data3['af_timestamp'])+str(data3['uid'])+str(data3['installDate'])+str(data3['counter'])+str(data3['iaecounter'])
    af_md5 = hashlib.md5(tomd5.encode()).hexdigest()
    af_v2 = hashlib.sha1(af_md5.encode()).hexdigest()
    data3['af_v2'] = af_v2

    #是第一次请求isFirstCall
    data3['isFirstCall'] = "true"

    #第一次counter
    data3["counter"] =str(1)

    #registeredUninstall
    data3['registeredUninstall'] = False



    header['Content-Length'] = str(len(str(data3)))
    print(json.dumps(data3))
    link ='70.169.70.83:80'
    proxies = {
        "http": link,
        "https": link,
    }
    s = requests.session()
    qwq = s.post(url,headers=header,data=json.dumps(data3), verify=False)
    print(qwq.content)
    print(url)
    conn_redis_7 = Redis7()
    print(str(refer_package['id'])+"_"+str(int(round(time.time() * 1000))))
    with open(str(refer_package['id']), "a+") as f:
        json.dump(data3, f)
        print("加载入文件完成...")





def get_final_url(jump_url):
    header = {
        'Host': 'clinkadtracking.com',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; Moto G (5) Plus Build/NPN25.137-33; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.111 Mobile Safari/537.36',
        'Upgrade-Insecure-Requests': '1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,en-US;q=0.9',
        'X-Requested-With': 'com.pingstart.sample',
    }
    line ='70.169.70.83:80'
    proxies = {
        "http": line,
        "https": line,
    }
    for i in range(15):
        header['Host'] = jump_url.split('/')[2]
        r = requests.get(jump_url, allow_redirects=False,verify=False,headers=header)
        try:
            if r.headers['location'].split('/')[0].find('http') >= 0:
                jump_url = r.headers['location']
                print(r.headers['location'])
            if r.headers['location'].find('referrer=') >= 0:
                jump_url = r.headers['location']
        except:
            try:
                jump_url_list = r.headers['Refresh']
                jump_url = jump_url_list.split(';')[1].split('url=')[1]
                print(jump_url)
            except:
                r = requests.get(jump_url,verify=False, headers=header)
                jump_url = r.url
                if jump_url == r.url:
                    continue
        if jump_url.find('referrer=') >= 0 or jump_url.find('play.google.com') >= 0:
            print(jump_url)
            break
    #jump_url = "market://details?id=com.a.one.ssgl&referrer=af_tranid%3DVr1lwDqnFYxCQUZRITt04Q%26af_prt%3DPMAD%26pid%3Dpm_int%26af_click_lookback%3D7d%26clickid%3D1513664870-2226-1847521587%26advertising_id%3De610a2b0-8028-431e-a7c3-5ca689550b7b%26c%3Dpm_com.a.one.ssgl_2_US_2226_ae3e6f3_57874_8348_SUBID12"
    #print(jump_url,str(int(round(time.time() * 1000))))
    wwww = jump_url.split('?')[-1]
    keo = {}
    for key_value in wwww.split('&'):
        keo[key_value.split('=')[0]] = key_value.split('=')[1]
    return keo






if __name__ == '__main__':
    url_123 = ['http://c.snnd.co/api/v4/click?campaign_id=9570818&publisher_id=1139&rt=171227030202&_po=b1e8ac1a27953b241c3444809b255126&_mw=p&_c=50&_cw=p&_ad=1434&publisher_slot=&sub_1=&pub_gaid=785fa536-39ba-4426-83bc-c9cec0d5ebbf&pub_idfa=&pub_aid=04a45210b59814a3', 'http://c.snnd.co/api/v4/click?campaign_id=10206812&publisher_id=1139&rt=171227030202&_po=f3d34532311b9a6c5999a6d7ef2a874a&_mw=p&_c=50&_cw=p&_ad=1368&publisher_slot=&sub_1=&pub_gaid=785fa536-39ba-4426-83bc-c9cec0d5ebbf&pub_idfa=&pub_aid=04a45210b59814a3', 'http://c.snnd.co/api/v4/click?campaign_id=8344353&publisher_id=1139&rt=171227030202&_po=01e87fb5e7aa618543ca25841785830c&_mw=p&_c=50&_cw=p&_ad=1368&publisher_slot=&sub_1=&pub_gaid=785fa536-39ba-4426-83bc-c9cec0d5ebbf&pub_idfa=&pub_aid=04a45210b59814a3', 'http://c.snnd.co/api/v4/click?campaign_id=7720388&publisher_id=1139&rt=171227030202&_po=f26d299d576d2a6004decb112132b78b&_mw=p&_c=50&_cw=p&_ad=1368&publisher_slot=&sub_1=&pub_gaid=785fa536-39ba-4426-83bc-c9cec0d5ebbf&pub_idfa=&pub_aid=04a45210b59814a3', 'http://c.snnd.co/api/v4/click?campaign_id=10168257&publisher_id=1139&rt=171227030202&_po=19f744c4c728685da541e7cc14fed89c&_mw=p&_c=50&_cw=p&_ad=1368&publisher_slot=&sub_1=&pub_gaid=785fa536-39ba-4426-83bc-c9cec0d5ebbf&pub_idfa=&pub_aid=04a45210b59814a3', 'http://c.snnd.co/api/v4/click?campaign_id=8614115&publisher_id=1139&rt=171227030202&_po=934a25adeca15bc691f9ff953aa9ebec&_mw=p&_c=50&_cw=p&_ad=1368&publisher_slot=&sub_1=&pub_gaid=785fa536-39ba-4426-83bc-c9cec0d5ebbf&pub_idfa=&pub_aid=04a45210b59814a3', 'http://c.snnd.co/api/v4/click?campaign_id=10283387&publisher_id=1139&rt=171227030202&_po=1e9321b60f4fed3241b32cc28d26b355&_mw=p&_c=50&_cw=p&_ad=1290&publisher_slot=&sub_1=&pub_gaid=785fa536-39ba-4426-83bc-c9cec0d5ebbf&pub_idfa=&pub_aid=04a45210b59814a3', 'http://c.snnd.co/api/v4/click?campaign_id=10117949&publisher_id=1139&rt=171227030202&_po=00298696d51186957f324811d75df9f3&_mw=p&_c=50&_cw=p&_ad=1368&publisher_slot=&sub_1=&pub_gaid=785fa536-39ba-4426-83bc-c9cec0d5ebbf&pub_idfa=&pub_aid=04a45210b59814a3', 'http://c.snnd.co/api/v4/click?campaign_id=10283301&publisher_id=1139&rt=171227030202&_po=b39d46b071a835e59b95310701984936&_mw=p&_c=50&_cw=p&_ad=1368&publisher_slot=&sub_1=&pub_gaid=785fa536-39ba-4426-83bc-c9cec0d5ebbf&pub_idfa=&pub_aid=04a45210b59814a3', 'http://c.snnd.co/api/v4/click?campaign_id=8998360&publisher_id=1139&rt=171227030202&_po=7e2606cbe8747792ec194afbc340f178&_mw=p&_c=50&_cw=p&_ad=1368&publisher_slot=&sub_1=&pub_gaid=785fa536-39ba-4426-83bc-c9cec0d5ebbf&pub_idfa=&pub_aid=04a45210b59814a3', 'http://c.snnd.co/api/v4/click?campaign_id=8997848&publisher_id=1139&rt=171227030202&_po=a779a0b176ee1e704a9c52f5f83972c4&_mw=p&_c=50&_cw=p&_ad=1368&publisher_slot=&sub_1=&pub_gaid=785fa536-39ba-4426-83bc-c9cec0d5ebbf&pub_idfa=&pub_aid=04a45210b59814a3', 'http://c.snnd.co/api/v4/click?campaign_id=9625727&publisher_id=1139&rt=171227030202&_po=3b547673d06d9668ef43b703c745e3d5&_mw=p&_c=50&_cw=p&_ad=1540&publisher_slot=&sub_1=&pub_gaid=785fa536-39ba-4426-83bc-c9cec0d5ebbf&pub_idfa=&pub_aid=04a45210b59814a3', 'http://c.snnd.co/api/v4/click?campaign_id=10206805&publisher_id=1139&rt=171227030202&_po=dc061e4bf79c1d66b4e93c4de6cba823&_mw=p&_c=50&_cw=p&_ad=1368&publisher_slot=&sub_1=&pub_gaid=785fa536-39ba-4426-83bc-c9cec0d5ebbf&pub_idfa=&pub_aid=04a45210b59814a3', 'http://c.snnd.co/api/v4/click?campaign_id=10281597&publisher_id=1139&rt=171227030202&_po=24091d43095cad66479698d4fb26e87d&_mw=p&_c=50&_cw=p&_ad=1290&publisher_slot=&sub_1=&pub_gaid=785fa536-39ba-4426-83bc-c9cec0d5ebbf&pub_idfa=&pub_aid=04a45210b59814a3', 'http://c.snnd.co/api/v4/click?campaign_id=9684420&publisher_id=1139&rt=171227030202&_po=a779a0b176ee1e704a9c52f5f83972c4&_mw=p&_c=50&_cw=c&_ad=1368&publisher_slot=&sub_1=&pub_gaid=785fa536-39ba-4426-83bc-c9cec0d5ebbf&pub_idfa=&pub_aid=04a45210b59814a3', 'http://c.snnd.co/api/v4/click?campaign_id=5228157&publisher_id=1139&rt=171227030202&_po=cf2742525b01803af284395fb97b75e1&_mw=p&_c=50&_cw=p&_ad=1368&publisher_slot=&sub_1=&pub_gaid=785fa536-39ba-4426-83bc-c9cec0d5ebbf&pub_idfa=&pub_aid=04a45210b59814a3', 'http://c.snnd.co/api/v4/click?campaign_id=9887695&publisher_id=1139&rt=171227030202&_po=a5a852ca88356fbbb6a536b6c1c23f94&_mw=p&_c=50&_cw=p&_ad=1368&publisher_slot=&sub_1=&pub_gaid=785fa536-39ba-4426-83bc-c9cec0d5ebbf&pub_idfa=&pub_aid=04a45210b59814a3', 'http://c.snnd.co/api/v4/click?campaign_id=10000578&publisher_id=1139&rt=171227030202&_po=e8645220012b2827a143e0469dfb9025&_mw=p&_c=50&_cw=p&_ad=1368&publisher_slot=&sub_1=&pub_gaid=785fa536-39ba-4426-83bc-c9cec0d5ebbf&pub_idfa=&pub_aid=04a45210b59814a3', 'http://c.snnd.co/api/v4/click?campaign_id=9887740&publisher_id=1139&rt=171227030202&_po=154c604c776dbd6d4762687c0d0f2a01&_mw=p&_c=50&_cw=p&_ad=1368&publisher_slot=&sub_1=&pub_gaid=785fa536-39ba-4426-83bc-c9cec0d5ebbf&pub_idfa=&pub_aid=04a45210b59814a3']
    for url_tracm in url_123:
        try:
            qqq = appfly_request(url_tracm)
        except:
            traceback.print_exc()




'''
https://play.google.com/store/apps/details?id=com.panda.clean.security&referrer=af_tranid%3DyMDKAEC662qPf7iRqc_NsA%26pid%3Dsolosystem_int%26clickid%3D51ecd365-3e28-41fd-a13c-fc88aaa093c0__pspm%26af_siteid%3D47%26af_sub1%3D47_henry%26gaid%3D1f0ba7e7-8520-48e1-9c7e-d4775f609ca9%26af_channel%3D47_47_henry%26c%3Dtier1
'''
