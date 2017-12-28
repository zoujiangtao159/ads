import requests

header = {
'Host':'clinkadtracking.com',
'Pragma':'no-cache',
'Cache-Control':'no-cache',
'User-Agent':'Mozilla/5.0 (Linux; Android 7.0; Moto G (5) Plus Build/NPN25.137-33; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.111 Mobile Safari/537.36',
'Upgrade-Insecure-Requests':'1',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,en-US;q=0.9',
'X-Requested-With':'com.pingstart.sample',
}

def get_final_url(jump_url):
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
            if r.headers['location'].find('referrer=') >= 0 >= 0:
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
        if jump_url.find('referrer=') >= 0:
            print(jump_url)
            return
    #jump_url = "market://details?id=com.a.one.ssgl&referrer=af_tranid%3DVr1lwDqnFYxCQUZRITt04Q%26af_prt%3DPMAD%26pid%3Dpm_int%26af_click_lookback%3D7d%26clickid%3D1513664870-2226-1847521587%26advertising_id%3De610a2b0-8028-431e-a7c3-5ca689550b7b%26c%3Dpm_com.a.one.ssgl_2_US_2226_ae3e6f3_57874_8348_SUBID12"
    #print(jump_url,str(int(round(time.time() * 1000))))
    wwww = jump_url.split('?')[-1]
    keo = {}
    for key_value in wwww.split('&'):
        keo[key_value.split('=')[0]] = key_value.split('=')[1]
    return keo


get_final_url('http://c.snnd.co/api/v4/click?campaign_id=9625727&publisher_id=1139&rt=171222020355&_po=3b547673d06d9668ef43b703c745e3d5&_mw=p&_c=50&_cw=p&_ad=1540&publisher_slot=&sub_1=&pub_gaid=302f2641-2c2e-41bc-867f-e1b14556d844&pub_idfa=&pub_aid=72db996fd65bbe82')