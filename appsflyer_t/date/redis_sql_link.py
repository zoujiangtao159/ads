import redis

class Redis111:

    def __init__(self, host='r-2ze953dbb80a7ea4.redis.rds.aliyuncs.com', port=6379, db=1, password='Qwer1234'):
        self.__conn = redis.Redis(connection_pool=redis.BlockingConnectionPool(max_connections=15,host=host, port=port, db=db, password=password))

    def __getattr__(self, command):
        def _(*args):
            return getattr(self.__conn, command)(*args) # 重新组装方法调用
        return _
class Redis2:

    def __init__(self, host='r-2ze953dbb80a7ea4.redis.rds.aliyuncs.com', port=6379, db=2, password='Qwer1234'):
        self.__conn = redis.Redis(connection_pool=redis.BlockingConnectionPool(max_connections=15,host=host, port=port, db=db, password=password))

    def __getattr__(self, command):
        def _(*args):
            return getattr(self.__conn, command)(*args) # 重新组装方法调用
        return _

class Redis3:

    def __init__(self, host='r-2ze953dbb80a7ea4.redis.rds.aliyuncs.com', port=6379, db=3, password='Qwer1234'):
        self.__conn = redis.Redis(connection_pool=redis.BlockingConnectionPool(max_connections=15,host=host, port=port, db=db, password=password))

    def __getattr__(self, command):
        def _(*args):
            return getattr(self.__conn, command)(*args) # 重新组装方法调用
        return _
    
class Redis4:

    def __init__(self, host='r-2ze953dbb80a7ea4.redis.rds.aliyuncs.com', port=6379, db=4, password='Qwer1234'):
        self.__conn = redis.Redis(connection_pool=redis.BlockingConnectionPool(max_connections=15,host=host, port=port, db=db, password=password))

    def __getattr__(self, command):
        def _(*args):
            return getattr(self.__conn, command)(*args) # 重新组装方法调用
        return _

class Redis5:

    def __init__(self, host='r-2ze953dbb80a7ea4.redis.rds.aliyuncs.com', port=6379, db=5, password='Qwer1234'):
        self.__conn = redis.Redis(connection_pool=redis.BlockingConnectionPool(max_connections=15,host=host, port=port, db=db, password=password))

    def __getattr__(self, command):
        def _(*args):
            return getattr(self.__conn, command)(*args) # 重新组装方法调用
        return _

class Redis6:

    def __init__(self, host='r-2ze953dbb80a7ea4.redis.rds.aliyuncs.com', port=6379, db=6, password='Qwer1234'):
        self.__conn = redis.Redis(connection_pool=redis.BlockingConnectionPool(max_connections=15,host=host, port=port, db=db, password=password))

    def __getattr__(self, command):
        def _(*args):
            return getattr(self.__conn, command)(*args) # 重新组装方法调用
        return _
#存发送appsflyer的data
class Redis7:

    def __init__(self, host='r-2ze953dbb80a7ea4.redis.rds.aliyuncs.com', port=6379, db=7, password='Qwer1234'):
        self.__conn = redis.Redis(connection_pool=redis.BlockingConnectionPool(max_connections=15,host=host, port=port, db=db, password=password))

    def __getattr__(self, command):
        def _(*args):
            return getattr(self.__conn, command)(*args) # 重新组装方法调用
        return _

class Redis8:

    def __init__(self, host='r-2ze953dbb80a7ea4.redis.rds.aliyuncs.com', port=6379, db=8, password='Qwer1234'):
        self.__conn = redis.Redis(connection_pool=redis.BlockingConnectionPool(max_connections=15,host=host, port=port, db=db, password=password))

    def __getattr__(self, command):
        def _(*args):
            return getattr(self.__conn, command)(*args) # 重新组装方法调用
        return _
'''
if __name__ == "__main__":
    #samesongresult = fanhuijieguo('296189201')
    conn_redis = Redis111()
    qq = conn_redis.get('user_info' + '296189201')
    print(qq)
    conn_redis = Redis111()
    qq = conn_redis.get('user_info' + '131755101')
    print(qq)
    conn_redis = Redis111()
    qq = conn_redis.get('user_info' + '303797357')
    print(qq)
'''