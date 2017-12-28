import json

import requests
import pymysql

conn = pymysql.connect(host='rm-uf682rl8k87978w84o.mysql.rds.aliyuncs.com',user='root', passwd='Qwer1234', db='bdm252107406_db', use_unicode=True,charset="utf8")

def get_playlist_subscribers():
    url = 'http://api.pingstart.com/ip'
    s = requests.session()
    read_ress = readsqp_address('all')
    f = open("代理IP.txt")
    for line in f.readlines():
        line = line.strip('\n')
        if tuple([line]) in read_ress:
            continue
        proxies = {"http": line}
        try:
            req = s.get(url,timeout=6,proxies=proxies)
            retcont = req.content.decode(encoding='utf-8')
            restime = req.elapsed.microseconds
            str_cont = json.dumps(retcont)
            all_list = str_cont.split('\\n')
            self_ip_list = all_list[1].split(',')
            prox_ip = self_ip_list[0].split('=')
            self_ip_list[0] = line
            write_address(self_ip_list,restime,0)
        except Exception as e:
            print(e)

def write_address(self_ip_list,res_time,status):
    print('[INFO] Start database interactions')
    # warnings.filterwarnings("ignore")
    cursor = conn.cursor()
    if self_ip_list[1] =='Beijing':
        return
    sql = 'insert into proxy_address  (address,status,amount,res_time,country,area,city) values (\'%s\',%d,0,%d,\'%s\',\'%s\',\'%s\');' % (self_ip_list[0],status,res_time,self_ip_list[1],self_ip_list[2],self_ip_list[3],)
    try:
        cursor.execute(sql)
    except Exception as e:
        print(e, sql)
        pass
    conn.commit()

def readsqp_address(status):
    cursor = conn.cursor()
    if status == 'post':
        sql2 = ('SELECT  DISTINCT address FROM proxy_address WHERE status=0')
    elif status == 'get':
        sql2 = ('SELECT  DISTINCT address FROM proxy_address WHERE status=1')
    else:
        sql2 = ('SELECT  DISTINCT address FROM proxy_address ')
    try:
        cursor.execute(sql2)
        qw1 = cursor.fetchall()
    except Exception as e:
        print(e, sql2)
        pass
    conn.commit()
    #print(qw1)
    return qw1

get_playlist_subscribers()