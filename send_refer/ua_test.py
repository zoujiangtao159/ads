import json

from ads.appsflyer_t.date.redis_sql_link import Redis111,Redis2,Redis3,Redis4

def get_ua(data):
    if int(data['sdk']) >= 21:
        Dalvik_ua = 'Dalvik/2.1.0 (Linux; U; '
    else:
        Dalvik_ua = 'Dalvik/1.6.0 (Linux; U; '
    if int(data['sdk']) == 1:
        android_version = 'Android 1.0'
    elif int(data['sdk']) == 2:
        android_version = 'Android 1.1'
    elif int(data['sdk']) == 3:
        android_version = 'Android 1.5'
    elif int(data['sdk']) == 4:
        android_version = 'Android 1.6'
    elif int(data['sdk']) == 5:
        android_version = 'Android 2.0'
    elif int(data['sdk']) == 6:
        android_version = 'Android 2.0.1'
    elif int(data['sdk']) == 7:
        android_version = 'Android 2.1.3'
    elif int(data['sdk']) == 8:
        android_version = 'Android 2.2.2'
    elif int(data['sdk']) == 9:
        android_version = 'Android 2.3'
    elif int(data['sdk']) == 10:
        android_version = 'Android 2.3.3'
    elif int(data['sdk']) == 11:
        android_version = 'Android 3.0.6'
    elif int(data['sdk']) == 12:
        android_version = 'Android 3.1.6'
    elif int(data['sdk']) == 13:
        android_version = 'Android 3.2'
    elif int(data['sdk']) == 14:
        android_version = 'Android 4.0'
    elif int(data['sdk']) == 15:
        android_version = 'Android 4.0.3'
    elif int(data['sdk']) == 16:
        android_version = 'Android 4.1'
    elif int(data['sdk']) == 17:
        android_version = 'Android 4.2'
    elif int(data['sdk']) == 18:
        android_version = 'Android 4.3'
    elif int(data['sdk']) == 19:
        android_version = 'Android 4.4'
    elif int(data['sdk']) == 20:
        android_version = 'Android 4.4W'
    elif int(data['sdk']) == 21:
        android_version = 'Android 5.0'
    elif int(data['sdk']) == 22:
        android_version = 'Android 5.1'
    elif int(data['sdk']) == 23:
        android_version = 'Android 6.0'
    elif int(data['sdk']) == 24:
        android_version = 'Android 7.0'
    elif int(data['sdk']) == 25:
        android_version = 'Android 7.1'
    elif int(data['sdk']) == 26:
        android_version = 'Android 8.0'
    elif int(data['sdk']) == 27:
        android_version = 'Android 8.1'
    else:
        print('error sdk version cont read',data['sdk'])
    try:
        model_ua = data['model']
    except:
        print('error model_ua cant read')
    try:
        build_ua = data['deviceData']['build_display_id']
    except:
        print('error build_ua cant read')
    ua_result = Dalvik_ua+android_version+'; '+model_ua+' Build/'+build_ua+')'
    return  ua_result

def red_data(key):
    value = Redis2().get(key)
    value_res = eval(value)
    redis_value = json.dumps(value_res)
    redis_value_list = json.loads(redis_value)
    # print(redis_value)
    ua_result_data = get_ua(redis_value_list)
    try:
        ua = Redis4().get(key)
        value_res_ua = eval(ua)
        redis_value_ua = json.dumps(value_res_ua)
        redis_value_list = json.loads(redis_value_ua)
    except:
        print('error read Redis4 ')
    if ua_result_data == redis_value_list['User-Agent']:
        print(key)
    else:
        print('not:', ua_result_data, '\r\n', redis_value_list['User-Agent'], eval(key))





red_data('00489ad7-111a-4bce-8a3b-cbf492cf348a')