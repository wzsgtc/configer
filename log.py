# !/usr/bin/python3
# -*-coding:utf-8-*-
# Author: Levi
# Github: todo please input your github link
# CreatDate: 2020/9/7 14:12
# Description: 
# {PROJECT_NAME} todo please input your project from where
"""
    :param
    :param
    :return
"""


import logging.config
import os


def logger_dic(logfile_name, local_logfile_dir=None, prod_logfile_dir=None):
    # 定义三种日志输出格式 开始
    standard_format = '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                      '[%(levelname)s][%(message)s]'  # 其中name为getlogger指定的名字
    simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'
    id_simple_format = '[%(levelname)s][%(asctime)s] %(message)s'
    # 定义日志输出格式 结束
    # local_logfile_dir = "D:\\roma\\all_crawer\\log"  # log文件的目录
    # prod_logfile_dir = "/var/log/"
    if local_logfile_dir is None:
        pass
    elif prod_logfile_dir is None:
        pass
    else:
        raise OSError("未指定LOG日志目录")
    logfile_dir = local_logfile_dir
    # 如果不存在定义的日志目录就创建一个
    if not os.path.isdir(logfile_dir):
        os.mkdir(logfile_dir)

    # log文件的全路径
    logfile_path = os.path.join(logfile_dir, logfile_name)
    # log配置字典
    LOGGING_DIC = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': standard_format
            },
            'simple': {
                'format': simple_format
            },
        },
        'filters': {},
        'handlers': {
            # 打印到终端的日志
            'console': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',  # 打印到屏幕
                'formatter': 'simple'
            },
            # 打印到文件的日志,收集info及以上的日志
            'default': {
                'level': 'INFO',
                'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
                'formatter': 'standard',
                'filename': logfile_path,  # 日志文件
                'maxBytes': 1024 * 1024 * 5,  # 日志大小 5M
                'backupCount': 5,
                'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
            },
        },
        'loggers': {
            # logging.getLogger(__name__)拿到的logger配置
            '': {
                'handlers': ['default', 'console'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
                'level': 'INFO',
                'propagate': True,  # 向上（更高level的logger）传递
            },
        },
    }
    return LOGGING_DIC


def load_my_logging_cfg(logfile_name, local_logfile_dir):
    LOGGING_DIC = logger_dic(logfile_name, local_logfile_dir)
    logging.config.dictConfig(LOGGING_DIC)  # 导入上面定义的logging配置
    logger = logging.getLogger(__name__)  # 生成一个log实例
    # logger.info('It works!')  # 记录该文件的运行状态
    return logger


# if __name__ == '__main__':
#     logfile_name, local_logfile_dir = "test", r"E:\worker\configer\log"
#     load_my_logging_cfg(logfile_name, local_logfile_dir)
