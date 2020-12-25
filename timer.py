# !/usr/bin/python3
# -*-coding:utf-8-*-
# Author: Levi
# Github: todo please input your github link
# CreatDate: 2020/9/7 11:29
# Description: 
# {PROJECT_NAME} todo please input your project from where
"""
    对于python的时间处理一些整合
"""

import datetime
import time


def unix_millisecond():
    return round(time.time() * 1000)


def unix_second():
    return round(time.time())


def current_date(separator="-"):
    return datetime.datetime.now().strftime(f"%Y{separator}%m{separator}%d")


def current_month(separator="-"):
    return datetime.datetime.now().strftime(f"%Y{separator}%m")


def current_time(separator="-"):
    return datetime.datetime.now().strftime(f"%Y{separator}%m{separator}%d %H{separator}%M{separator}%S")


def timer_paraphrase(unix_dur):
    """只转换以秒为单位的时间戳，毫秒请 / 1000"""
    return datetime.datetime.fromtimestamp(unix_dur)
