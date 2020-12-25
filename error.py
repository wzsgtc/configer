# !/usr/bin/python3
# -*-coding:utf-8-*-
# Author: Levi
# Github: todo please input your github link
# CreatDate: 2020/9/10 11:43
# Description: 
# {PROJECT_NAME} todo please input your project from where
"""
    :param
    :param
    :return
"""
from dingtalkchatbot.chatbot import DingtalkChatbot
headers = {"Content-Type": "application/json"}
dd_webhook = "https://oapi.dingtalk.com/robot/send?access_token=b2700203a0838eaef76d9db1acedeb368ba8af1929d5ede29950668809bde7c4"


def send(info):
    if not isinstance(info, str):
        info = str(info)
    # 消息类型和数据格式参照钉钉开发文档
    xd = DingtalkChatbot(webhook=dd_webhook)
    xd.send_text(msg=info)


