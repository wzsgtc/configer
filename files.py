# !/usr/bin/python3
# -*-coding:utf-8-*-
# Author: Levi
# Github: todo please input your github link
# CreatDate: 2020/9/7 13:59
# Description: 
# {PROJECT_NAME} todo please input your project from where
"""
    :param
    :param
    :return
"""
import os


def existence(file_path):
    if os.path.exists(file_path):
        return True
    else:
        return False


def writeable(file_path, file_info, read_and_write):
    if existence(file_path):
        with open(file_path, read_and_write) as f:
            f.write(file_info)
    else:
        raise OSError(f"{file_path} if not find")


def readable(file_path, read_and_write, mode):
    if existence(file_path):
        with open(file_path, read_and_write) as f:
            if mode == "readlines":
                data = f.readlines()
            elif mode == "readline":
                data = f.readline()
            else:
                data = f.read()
        return data
    else:
        raise OSError(f"{file_path} if not find")
