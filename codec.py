# !/usr/bin/python3
# -*-coding:utf-8-*-
# Author: Levi
# Github: todo please input your github link
# CreatDate: 2020/9/7 14:29
# Description: 
# {PROJECT_NAME} todo please input your project from where
"""
    :param
    :param
    :return
"""
from Cryptodome.Util.Padding import unpad, pad
from urllib.parse import unquote, quote
from Cryptodome.Cipher import DES3
import hashlib
import execjs
import base64
import time
import os


def parse_bytes(data):
    if isinstance(data, list) or isinstance(data, set):
        data = [i.decode() for i in data]
    elif isinstance(data, bytes):
        return data.decode()
    else:
        raise Exception(f"parse_bytes did't have parse {type(data)}")
    return data


def md5(info):
    m = hashlib.md5()
    m.update(bytes(info, 'utf-8'))
    return m.hexdigest()


def b64_decode(info):
    return base64.b64decode(info).decode()


def b64_encode(info):
    return base64.b64encode(info).decode()


def url_decode(info):
    return unquote(info)


def url_encode(info):
    return quote(info)


def des_decode(info, key, date=time.strftime("%Y%m%d")):
    des = DES3.new(key=key.encode(), mode=DES3.MODE_CBC, iv=date.encode())
    decrypted_data = des.decrypt(base64.b64decode(info))
    plain_text = unpad(decrypted_data, DES3.block_size).decode()
    return plain_text

def node_parse(data, func, *args):
    os.environ["NODE_PATH"] = os.getcwd() + "/node_modules"
    print(execjs.get().name)
    ctx = execjs.compile(data)
    len_args = len(args)
    if len_args:
        if len_args == 1:
            return ctx.call(f'{func}', args[0])
        elif len_args == 2:
            return ctx.call(f'{func}', args[0], args[1])
        elif len_args == 3:
            return ctx.call(f'{func}', args[0], args[1], args[2])
        elif len_args == 4:
            return ctx.call(f'{func}', args[0], args[1], args[2], args[3])
    else:
        return ctx.call(f'{func}')

