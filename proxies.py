# !/usr/bin/python3
# -*-coding:utf-8-*-
# Author: Levi
# Github: todo please input your github link
# CreatDate: 2020/9/10 10:07
# Description: 
# {PROJECT_NAME} todo please input your project from where
"""
    :param
    :param
    :return
"""
from redis_connect import RedisConnect
from log import load_my_logging_cfg
from re import findall
import requests
import random
import time


class Proxies(object):
    """代理"""
    def __init__(self):
        self.proxy_name = "proxies"
        self.redis = RedisConnect(db=1)
        self.proxy_pool_number = 10
        self.proxy_number = 1
        self.link = "http://http.tiqu.qingjuhe.cn/getip?num={}&type=1&pack=27357&port=1&lb=1&pb=4&regions="
        self.logfile_name = "proxies.log"
        self.local_logfile_dir = r"E:\worker\configer\log"
        self.logger = load_my_logging_cfg(logfile_name=self.logfile_name, local_logfile_dir=self.local_logfile_dir)

    def proxy_pool_generate(self):
        link = self.link.format(self.proxy_pool_number)
        resp = requests.get(url=link)
        data = findall(r'(.*?:.*?)\r\n', resp.content.decode())
        key = "%s:%s" % (self.proxy_name, "proxies")
        if not len(data):
            self.logger.error("当前代理失效、请检查代理IP")
        if isinstance(data, list):
            for value in data:
                self.redis.put(key=key, value=value)
        proxies = self.redis.l_len(key)
        if proxies:
            self.redis.l_del(key, start=1, end=10)

    def proxy(self):
        link = self.link.format(self.proxy_number)
        resp = requests.get(url=link)
        data = findall(r'(.*?:.*?)\r\n', resp.content.decode())
        if not len(data):
            self.logger.error("当前代理失效、请检查代理IP")
        data = data[0]
        return {
            "http": "http://{}".format(data),
            "https": "https://{}".format(data),
        }

    def proxy_pool(self):
        key = "%s:%s" % (self.proxy_name, "proxies")
        proxies = self.redis.l_all(key=key)
        return {
            "http": "http://{}".format(random.choice(proxies).decode()),
            "https": "https://{}".format(random.choice(proxies).decode()),
        }

    def proxyPool(self):
        return self.redis.l_all(key="proxies")


if __name__ == '__main__':
    p = Proxies()
    while 1:
        p.proxy_pool_generate()
        time.sleep(150)
