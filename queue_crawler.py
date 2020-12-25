# !/usr/bin/python3
# -*-coding:utf-8-*-
# Author: Levi
# Github: todo please input your github link
# CreatDate: 2020/9/7 16:33
# Description: 
# {PROJECT_NAME} todo please input your project from where
"""
    redis 实现队列、无队列一直等待
"""
from redis_connect import RedisConnect


class RedisQueue(object):
    """redis 队列"""
    def __init__(self, name, namespace="queue"):
        self.redis = RedisConnect(db=12)
        self.key = "%s:%s" % (namespace, name)

    def qsize(self):
        """返回队列内list的元素的数量"""
        return self.redis.l_len(key=self.key)

    def put(self, item):
        """添加新元素到队列的最右边"""
        self.redis.put(key=self.key, value=item)

    def get_wait(self, timeout=None):
        """返回队列第一个元素，如果为空则等待至有元素被加入队列（超时时间阈值为timeout，如果为None则一直等待）"""
        item = self.redis.get_wait(key=self.key, timeout=timeout)
        return item

    def get_nowait(self):
        """直接返回队列第一个元素，如果队列为空返回的是None"""
        item = self.redis.get_nowait(key=self.key)
        return item







