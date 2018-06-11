#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/14 20:33
# @Author  : qiaoyu
from qq01.opr_like import Like
from utils.log import log


class QQzone:
    def like(self):
        log.run().debug("执行 QQzone.like()")  # 打印日志
        li = Like()
        li.like()

    def main(self):
        log.info().info("程序开始运行")   # 打印日志
        self.like()

        log.info().info("程序运行结束")  # 打印日志


if __name__ == '__main__':
    qq = QQzone()
    qq.main()
