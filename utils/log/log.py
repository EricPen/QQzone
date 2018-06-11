#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/16 11:25
# @Author  : qiaoyu#!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @Time    : 2018/5/16 12:02
# # @Author  : qiaoyu

import os
import logging.config

# 定义三种日志输出格式 开始

standard_format = '[%(asctime)s] [%(threadName)s:%(thread)d] [task_id:%(name)s] [%(filename)s:%(lineno)d]' \
                  ' [%(levelname)s] [%(message)s]' #其中name为getlogger指定的名字

simple_format = '[%(levelname)s] [%(asctime)s] [%(filename)s:%(lineno)d] %(message)s'
simple_format_02 = '[%(levelname)s] [%(asctime)s] %(message)s'

id_simple_format = '[%(levelname)s][%(asctime)s] %(message)s'

# 定义日志输出格式 结束

logfile_temp = os.path.dirname(os.path.abspath(__file__))+"/temp"  # 临时文件的目录

# 如果不存在临时目录就创建一个
if not os.path.isdir(logfile_temp):
    os.mkdir(logfile_temp)

logfile_dir = os.path.dirname(os.path.abspath(__file__))+"/temp/log"  # log文件的目录

# 如果不存在临时目录就创建一个
if not os.path.isdir(logfile_dir):
    os.mkdir(logfile_dir)

# log文件的全路径
logfile_service = os.path.join(logfile_dir, 'service.log')
logfile_run = os.path.join(logfile_dir, 'run.log')
logfile_debug = os.path.join(logfile_dir, 'debug.log')
logfile_error = os.path.join(logfile_dir, 'error.log')


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
        'simple02': {
            'format': simple_format_02
        },
    },
    'filters': {},
    'handlers': {
        # 打印到终端的日志
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'simple'
        },
        'console_simple': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'simple02'
        },
        # 打印到文件的日志,收集所有的日志
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            'formatter': 'standard',
            'filename': logfile_service,  # 日志文件
            'maxBytes': 1024*1024*5,  # 日志大小 5M
            'backupCount': 5,
            'encoding': 'utf-8',  # 日志文件的编码
        },
        # 打印到文件的日志,收集debug日志
        'debug': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            'formatter': 'simple',
            'filename': logfile_debug,  # 日志文件
            'maxBytes': 1024*1024*5,  # 日志大小 5M
            'backupCount': 5,
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },

        # 打印到文件的日志,收集info及以上的日志
        'running': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            'formatter': 'simple',
            'filename': logfile_run,  # 日志文件
            'maxBytes': 1024*1024*5,  # 日志大小 5M
            'backupCount': 5,
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },

        # 打印到文件的日志,收集错误日志
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            'formatter': 'standard',
            'filename': logfile_error,  # 日志文件
            'maxBytes': 1024*1024*5,  # 日志大小 5M
            'backupCount': 5,
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },

    },
    'loggers': {
        # logging.getLogger(__name__)拿到的logger配置
        '': {
            'handlers': ['default'],    # 只能写入文件不能打印到屏幕
            'level': 'DEBUG',
            'propagate': True,  # 向上（更高level的logger）传递
        },
        'debug': {
            'handlers': ['debug', 'console'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG',
        },
        'info': {
            'handlers': ['running', 'console_simple'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'INFO',
        },
        'error': {
            'handlers': ['error', 'console'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'ERROR',
        },
    },
}


def run():
    """记录运行的日志"""   # 控制台不显示
    logging.config.dictConfig(LOGGING_DIC)
    logger = logging.getLogger(__name__)
    return logger


def debug():
    """调试信息日志"""    # 开启状态下控制台显示

    start_debug = True      # True 为开启调试模式

    if start_debug:
        logging.config.dictConfig(LOGGING_DIC)
        logger = logging.getLogger("debug")
        return logger


def info():
    """记录正常运行的日志"""     # 控制台显示
    logging.config.dictConfig(LOGGING_DIC)
    logger = logging.getLogger("info")
    return logger


def error():
    """记录错误信息"""    # 控制台显示
    logging.config.dictConfig(LOGGING_DIC)
    logger = logging.getLogger("error")
    return logger


def exception():
    """捕捉异常信息"""    # 控制台显示
    logging.config.dictConfig(LOGGING_DIC)
    logger = logging.getLogger("error")
    return logger
