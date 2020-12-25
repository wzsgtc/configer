# !/usr/bin/python3
# -*-coding:utf-8-*-
# Author: Levi
# Github: todo please input your github link
# CreatDate: 2020/9/10 11:35
# Description: 
# {PROJECT_NAME} todo please input your project from where
"""
    :param
    :param
    :return
"""

from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED


def thread(func_name, iter_info, max_worker):
    with ThreadPoolExecutor(max_workers=max_worker) as executor:
        future_list = [executor.submit(func_name, i) for i in iter_info]
        wait(future_list, return_when=FIRST_COMPLETED)
