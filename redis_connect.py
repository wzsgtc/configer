# !/usr/bin/python3
# -*-coding:utf-8-*-
# Author: Levi
# Github: todo please input your github link
# CreatDate: 2020/9/7 14:44
# Description: 
# {PROJECT_NAME} todo please input your project from where
"""
    :param
    :param
    :return
"""
import time
import redis
import requests


class RedisConnect:
    __pool = None

    def __init__(self, db):
        self.redis_host = "127.0.0.1"
        self.redis_port = 6379
        self.redis_password = "liwei123"
        self.db = db
        self.connect = self.redis_connect()
        self.proxies_db = 1

    def redis_connect(self):
        if RedisConnect.__pool is None:
            __pool = redis.ConnectionPool(host=self.redis_host, port=self.redis_port, password=self.redis_password,
                                          db=self.db, max_connections=10)
        return redis.Redis(connection_pool=__pool)

    def l_len(self, key):
        return self.connect.llen(key)

    def put(self, key, value):
        self.connect.rpush(key, value)

    def get_wait(self, key, timeout):
        return self.connect.blpop(key, timeout=timeout)

    def get_nowait(self, key):
        return self.connect.lpop(name=key)

    def l_del(self, key, start, end):
        self.connect.ltrim(name=key, start=start, end=end)

    def l_push(self, key, value):
        self.connect.lpush(key, value)

    def l_all(self, key):
        return self.connect.lrange(name=key, start=0, end=-1)

    def d_set(self, name, key, value):
        self.connect.hset(name, key, value)

    def s_set(self, key, value):
        return self.connect.sadd(key, value)

    def s_all(self, key):
        return self.connect.smembers(key)

    def p_one(self):
        while 1:
            url = "http://http.tiqu.qingjuhe.cn/getip?num=1&type=1&pack=27357&port=1&lb=1&pb=4&regions="
            resp = requests.get(url)
            if "code" in resp.content.decode():
                print(resp.content.decode())
                time.sleep(2)
                continue
            else:
                break
        return resp.content.decode()


if __name__ == '__main__':
    r = RedisConnect(db=1)
    r.p_one()
