#coding:utf8
#
#NGP app爬取 从360上面爬取 10.1.8.57  /mnt/
#
import requests
from lxml import etree
import urllib
import math
import os
from filechunkio import FileChunkIO
import threading
import Queue
import datetime
import traceback
from collections import namedtuple
import boto.s3.connection
import MySQLdb
import multiprocessing
import time
import signal
import errno
# AWS S3
AWS = {
    'ACCESS_KEY_ID': 'AKIAJRRTI7UMYVNY56DQ',
    'ACCESS_KEY': 'S7xuo6xzgYwMema7ThL+P46a8wwB9bt5Q81a59r+',
    'REGION': 'us-east-1',
    'BUCKET': 'adplatformstatis',
    'BUCKET_UPLOAD': 'sdkvideo',
    #'BUCKET_UPLOAD': 'd3ahdvlqntqhyj.cloudfront.net',
}

DATABASES = {
    'default': {
        'NAME': 'pspm',
        'USER': 'pspm',
        'PASSWORD': 'k592JB6XsiIqV4LTigVU',
        #'HOST': '10.1.7.12',
        'HOST': 'aurora-pspm-master-cluster.cluster-cuqhddmsuo71.us-west-2.rds.amazonaws.com',
        # 'HOST': '192.168.3.224',
        # 'PASSWORD': '123',
        # 'USER': 'root',
        'PORT': '3306'
    },
}

DATABASES13 = {
    'default': {
        'NAME': 'pspm',
        'USER': 'pspm',
        'PASSWORD': 'k592JB6XsiIqV4LTigVU',
        #'HOST': '10.1.7.13',
        'HOST': 'aurora-pspm-slave-03.cuqhddmsuo71.us-west-2.rds.amazonaws.com',
        # 'HOST': '192.168.3.224',
        # 'PASSWORD': '123',
        # 'USER': 'root',
        'PORT': '3306'
    },
}

class StorageS3(object):


    def __init__(self):
        self.conn = boto.connect_s3(
            aws_access_key_id=AWS['ACCESS_KEY_ID'],
            aws_secret_access_key=AWS['ACCESS_KEY'],
            is_secure=False,
        )
        self.bucket_name = AWS['BUCKET_UPLOAD']

    def get_bucket(self):
        self.bucket = self.conn.get_bucket(self.bucket_name)
        self.bucket.set_acl('public-read')
        return self.bucket


class UploadS3(StorageS3):

    def __init__(self,  file_path, key_name):
        super(UploadS3, self).__init__()
        self.Chunk = namedtuple('Chunk', ['num', 'offset', 'length'])

        self.file_path = file_path
        self.key_name = key_name
        self.thread_count = 10
        self.chunk_size = 8 << 20

    def queue_init(self, file_size):
        chunk_count = int(math.ceil(file_size*1.0/self.chunk_size))
        _queue = Queue.Queue(maxsize=chunk_count)
        for i in range(0, chunk_count):
            offset = self.chunk_size * i
            length = min(self.chunk_size, file_size-offset)
            chunk = self.Chunk(i+1, offset, length)
            _queue.put(chunk)
        return _queue

    def upload_chunk(self, bucket_mp, _queue, headers, _type):
        ''' upload file chunk '''
        while not _queue.empty():
            chunk = _queue.get()
            fp = FileChunkIO(self.file_path, 'r', offset=chunk.offset,
                             bytes=chunk.length)
            if _type == 'big':
                bucket_mp.upload_part_from_file(fp, part_num=chunk.num,
                                                headers=headers)
            else:
                bucket_mp.set_contents_from_file(fp, headers=headers,
                                                 policy='public-read')
            fp.close()
            _queue.task_done()

    def upload_file(self, _queue, headers, _type):
        ''' upload file '''
        if _type == 'big':
            bucket_mp = self.get_bucket().initiate_multipart_upload(
                self.key_name, policy='public-read')
        else:
            bucket_mp = self.get_bucket().new_key(self.key_name)

        if _queue.qsize() < self.thread_count:
            self.thread_count = _queue.qsize()

        for i in range(0, self.thread_count):
            t = threading.Thread(target=self.upload_chunk,
                                 args=(bucket_mp, _queue, headers, _type))
            t.setDaemon(True)
            t.start()
        _queue.join()
        if _type == 'big':
            bucket_mp.complete_upload()
        return bucket_mp

    # @app.task
    def upload_start(self, content_type='application/octet-stream'):
        file_size = os.stat(self.file_path).st_size
        _queue = self.queue_init(file_size)
        headers = {
            "Content-Type": content_type
        }
        _type = 'big' if file_size >= 5242880 else 'small'
        res =self.upload_file(_queue, headers, _type)
        return res


class Update_appinfo():
    def __init__(self):
        self.android_pid = []
        self.get_android_packageIds()

    def get_android_packageIds(self):
        conn1 = MySQLdb.connect(db=DATABASES13["default"]["NAME"], user=DATABASES13["default"]["USER"],
                                passwd=DATABASES13["default"]["PASSWORD"],
                                host=DATABASES13["default"]["HOST"], charset="utf8mb4")

        cur1 = conn1.cursor()
        cur1.execute(
            "select package_name from campaign where   platform=1 and is_api = 1 and campaign_status =1 and create_time > '%s' group by package_name"%str(datetime.datetime.today()-datetime.timedelta(minutes=1440))[:19])
        self.android_pid = cur1.fetchall()
        conn1.close()
        #self.android_pid = [('com.android.chrome',),('org.mozilla.firefox',)]
        print(len(self.android_pid), ": get_android_packageIds:", datetime.datetime.now())

    def Schedule(self,a,b,c):
        '''
        a:已经下载的数据块
        b:数据块的大小
        c:远程文件的大小
        '''
        per = 100.0*a*b/c
        if per > 100:
            per = 100
        if per//10 == 0:
            print('%2.f%%' % per)

    def worker(self,package_list):
        name = multiprocessing.current_process().name
        for apkcom in package_list:
            print(name,'--start--',apkcom[0],datetime.datetime.now())
            try:
                url = 'http://zhushou.360.cn/search/index/?kw='+str(apkcom[0])
                url_ht = 'http://zhushou.360.cn/'
                a = requests.get(url)
                #print a.status_code
                selector = etree.HTML(a.text)
                content = selector.xpath('//li//dt//a//@href')
                content1 = selector.xpath('//div[@class="download comdown"]//a//@href')
                #packagename  appname  appsize appurl  time
                for i in range(len(content1)):
                    j = content1[i]
                    if str(apkcom[0]) in  j.split('/')[-1].split('_'):
                        #print i,j
                        app_name = j.split('/')[-1]
                        #download
                        #urllib.urlretrieve(j,app_name,Schedule)

                        url_1 = url_ht+content[i]
                        #print url_1
                        app_info = requests.get(url_1)
                        app_size =  etree.HTML(app_info.text).xpath('//div//span[@class="s-3"]//text()')[-1]
                        app_version =   etree.HTML(app_info.text).xpath('//tbody//tr//td//text()')[5]

                        print (name, '--download--')
                        urllib.urlretrieve(j, app_name)

                        filepath = app_name
                        cname = 'sdkvideo/appNoGP/%s'%app_name
                        print(name, '--uploads3--')
                        u = UploadS3(filepath, cname)
                        res = u.upload_start()
                        print(name, 'resend', res)
                        app_downloadurl = 'https://d3ahdvlqntqhyj.cloudfront.net/%s'%cname
                        print(name, 'end insql--', str(apkcom[0]), app_name, app_size, app_downloadurl)

                        conn = MySQLdb.connect(db=DATABASES["default"]["NAME"], user=DATABASES["default"]["USER"],
                                                passwd=DATABASES["default"]["PASSWORD"],
                                                host=DATABASES["default"]["HOST"], charset="utf8mb4")
                        cur = conn.cursor()
                        sql = 'replace into app_nogp(package_name,app_name,app_size,app_url,version) values (%s,%s,%s,%s,%s)'
                        cur.execute(sql,(str(apkcom[0]), app_name, app_size,app_downloadurl,app_version))
                        conn.commit()
                        conn.close()
                        os.popen('rm %s'%app_name)
                        print(name, 'end rm app')

            except:
                traceback.print_exc()
            print(name, '--end--', datetime.datetime.now())
        os._exit(3)

    def wait_child(signum, frame):
        try:
            while True:
                # -1 表示任意子进程
                # os.WNOHANG 表示如果没有可用的需要 wait 退出状态的子进程，立即返回不阻塞
                cpid, status = os.waitpid(-1, os.WNOHANG)
                if cpid == 0:
                    break
        except OSError as e:
            if e.errno == errno.ECHILD:
                pass
            else:
                raise

    signal.signal(signal.SIGCHLD, wait_child)

    def update_start(self):

        if len(self.android_pid) < 50:
            worker_0 = multiprocessing.Process(name='worker_android_1', target=self.worker, args=(self.android_pid,))
            worker_0.start()
        else:
            all_pid_nums = 6
            num = len(self.android_pid) / all_pid_nums
            for i in range(all_pid_nums):
                start_num = i * num
                end_num = (i + 1) * num if i + 1 < all_pid_nums else (i + 2) * num
                worker = multiprocessing.Process(name='%s' % ('worker_android_' + str(i)), target=self.worker,
                                                 args=(self.android_pid[start_num:end_num],))
                worker.start()

'''
if __name__ == '__main__':
    print ("upate package begin:", datetime.datetime.now())
    start = time.clock()
    up = Update_appinfo()
    up.update_start()
    elapsed = (time.clock() - start)
    print 'Date:{}, Time used:{}'.format(datetime.datetime.now().strftime(
        "%Y-%m-%D %H:%M:%S"), elapsed)
'''

if __name__ == '__main__':

