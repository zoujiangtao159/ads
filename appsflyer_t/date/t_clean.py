import json
import time
from date.redis_sql_link import Redis111,Redis2,Redis3,Redis4,Redis5,Redis6


def t_clean_json(data,headers,app_info):
    conn_redis = Redis111()
    conn_redis_2 = Redis2()
    conn_redis_3 = Redis3()
    conn_redis_4 = Redis4()
    conn_redis_5 = Redis5()
    conn_redis_6 = Redis6()
    try:
      conn_redis.set(data['advertiserId'], data)
      conn_redis_4.set(data['advertiserId'], headers)
      conn_redis_5.set(app_info['app_id'], app_info)
      conn_redis_6.set(app_info['app_id'], data)
    except:
      try:
        conn_redis_2.set(data['android_id'], data)
        conn_redis_4.set(data['android_id'], headers)
        conn_redis_5.set(app_info['app_id'], app_info)
        conn_redis_6.set(app_info['app_id'], data)
      except:
        conn_redis_3.set(str(int(time.time())),data)
        conn_redis_4.set(str(int(time.time())), headers)
        conn_redis_5.set(app_info['app_id'], app_info)
        conn_redis_6.set(app_info['app_id'], data)
            
'''
key_list = Redis4().keys()
value = Redis4().get(key_list[0])
print(value[])
'''

def shengchengua():
    key_list = Redis2().keys()
    value = Redis2().get(key_list[0])
    value_res = value.decode(encoding='utf-8')
    redis_value = json.dumps(value_res)

    print(redis_value)


#shengchengua()
