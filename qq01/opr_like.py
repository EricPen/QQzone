#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/15 14:46
# @Author  : qiaoyu
from utils.log import log
from selenium import webdriver
import time
import json
import os


class Like:
    def like(self):
        log.run().debug("执行 Like.like()")   # 打印日志
        driver = self.login()
        if driver != 'error':
            log.info().info("QQ已登录，开始进入点赞系统")
            while driver != 'error':
                driver = self.praise(driver)
        else:
            log.info().info("因登录失败,程序开始停止运行")   # 打印日志

    def login(self):
        """登录QQ空间"""

        log.run().debug("执行Like.login()")   # 打印日志

        author_info = False
        try:
            log.info().info("正在读取用户信息")  # 打印日志

            with open("config/user.json", "r", encoding="utf-8") as usr:
                infos = json.load(usr)
                account = infos['account']
                password = infos['password']

            author_info = True
            log.info().info("用户信息读取成功")   # 打印日志

        except Exception as e:

            log.exception().exception(e)  # 打印日志
            log.error().error("用户信息读取失败")  # 打印日志

        if author_info:
            # 登录部分
            log.info().info("开始登录QQ空间")  # 打印日志
            driver = webdriver.PhantomJS()
            driver.maximize_window()
            url = "https://qzone.qq.com/"
            driver.get(url)
            driver.implicitly_wait(3)

            try:
                driver.switch_to.frame("login_frame")
                try:
                    driver.find_element_by_id('switcher_plogin').click()
                except:
                    log.run().info("默认显示账号密码登录，不需要切换")

                driver.find_element_by_id('u').clear()
                driver.find_element_by_id('u').send_keys(account)
                driver.find_element_by_id('p').click()
                driver.find_element_by_id('p').send_keys(password)

                driver.find_element_by_id('login_button').click()
                time.sleep(3)
                driver.implicitly_wait(20)

                log.debug().debug("即将开始验证QQ登录")

                return self.login_on(driver)  # 判断是否登录

            except Exception as login_01:

                log.exception().exception(login_01)  # 打印日志
                log.error().info("QQ空间登录模块获取失败")  # 打印日志

                return 'error'

        else:
            return 'error'

    def praise(self, driver):
        """点赞部分"""
        log.run().debug("执行Like.praise()")  # 打印日志
        log.info().info("查找未点赞目标")
        driver.refresh()    # 刷新
        driver.implicitly_wait(10)

        if self.login_on(driver) != 'error':  # 检查是否在线

            # 判断自己是否点赞
            try:

                praise_person = driver.find_element_by_xpath('//*[@id="feed_friend_list"]/li[1]/div[@class="f-single-foot"]/div[@class="f-like-list f-like _likeInfo"]/div[@class="user-list"]/a').get_attribute("class")
                if praise_person == 'item _ownerlike q_namecard':
                    result = False
                else:
                    result = True
            except:
                result = True
                log.info().info("找到目标，准备点赞")  # 打印日志
            # 判断是否点赞
            try:
                if result:
                    driver.find_element_by_css_selector("[class='fui-icon icon-op-praise']").click()
                    log.info().info("点赞成功")  # 打印日志
            except Exception as e106:

                log.exception().exception(e106)  # 打印日志
                log.error().error("点赞发生错误")  # 打印日志

            time.sleep(3)
            return driver
        else:
            time.sleep(60)
            log.info().info("正尝试重新登录")  # 打印日志
            driver_now = self.login()  # 重新登录,

            if driver_now != 'error':  # 若成功则继续点赞
                return driver
            else:
                return 'error'

    def login_on(self, driver):
        """验证QQ空间是否登录"""
        log.run().debug("执行Like.login_on()")  # 打印日志
        try:
            driver.find_element_by_id('QZ_Toolbar_Container')
            log.run().debug("QQ已登录")  # 打印日志

            return driver
        except Exception as login_02:
            log.exception().exception(login_02)  # 打印日志
            log.info().info("QQ未登录")  # 打印日志

            self.screenshot(driver)
            return 'error'

    def screenshot(self, driver):
        """截屏"""
        log.run().debug("执行Like.screenshot()")  # 打印日志
        file_name = "login_" + str(time.strftime("%Y%m%d%H%M%S", time.localtime(time.time())))+".png"

        file_temp = os.path.dirname(os.path.abspath(__file__)) + "/temp"  # 临时文件的目录

        # 如果不存在临时目录就创建一个
        if not os.path.isdir(file_temp):
            os.mkdir(file_temp)

        file_dir = os.path.dirname(os.path.abspath(__file__)) + "/temp/screen_shot/"  # 截屏图片的目录

        # 如果不存在该目录就创建一个
        if not os.path.isdir(file_dir):
            os.mkdir(file_dir)

        file_path = file_dir + file_name
        driver.get_screenshot_as_file(file_path)

        log.info().info("已将出现错误位置截屏：/temp/screen_shot/")  # 打印日志

    # def get_content(self, driver):
    #     try:
    #         """获取说说的信息"""
    #         name = driver.find_element_by_css_selector("[class='f-name q_namecard ']").text
    #         current_time = str(driver.find_element_by_xpath(
    #             '//*[@id="fct_2690674795_311_5_1526387808_0_1"]/div[1]/div[4]/div[2]/span').text)
    #         time_now = str(time.strftime("%Y%m%d%H%M%S", time.localtime(time.time())))
    #         try:
    #             content = driver.find_element_by_css_selector("[class='f-info']").text
    #         except:
    #             content = ''
    #
    #         with open('log/record.log','a+', encoding="utf-8") as lrecord:
    #             log_text=time_now+"\t"+name+"\t"+current_time+"\t"+content+"\n"
    #             lrecord.write(log_text)
    #     except:
    #         logger.info("获取空间说说信息出错")

