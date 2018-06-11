# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @Time    : 2018/5/14 20:39
# # @Author  : qiaoyu
# from selenium import webdriver
# import time
# import json
# from utils import logger
# import re
#
#
# class Base:
#     def login(self):
#         """登录QQ空间"""
#
#         logger.info("开始登录QQ空间")
#
#         driver = webdriver.PhantomJS()
#         driver.maximize_window()
#         url = "https://qzone.qq.com/"
#         driver.get(url)
#         driver.implicitly_wait(3)
#
#         with open("config/user.json", "r", encoding="utf-8") as usr:
#             infos = json.load(usr)
#             account = infos['account']
#             password = infos['password']
#         try:
#             # 登录部分
#             driver.switch_to.frame("login_frame")
#             driver.find_element_by_id('switcher_plogin').click()
#             driver.find_element_by_id('u').clear()
#             driver.find_element_by_id('u').send_keys(account)
#             driver.find_element_by_id('p').click()
#             driver.find_element_by_id('p').send_keys(password)
#             driver.find_element_by_id('login_button').click()
#             time.sleep(3)
#             driver.implicitly_wait(20)
#
#             text = driver.page_source
#             result = re.findall("http://(.*).qzone.qq.com\]</title>", text, re.S)
#
#             if result == []:
#                 result =  "null"
#             else:
#                 result=result[0]
#             if result == account:
#                 logger.info("QQ空间登录成功")
#                 driver.get('https://user.qzone.qq.com/2528510434')
#                 self.get_cookie(driver)
#             else:
#                 logger.info("QQ空间登录失败")
#
#                 file_name = str(time.strftime("%Y%m%d%H%M%S", time.localtime(time.time())))
#                 path = 'log/images/' + file_name+'.png'
#                 driver.get_screenshot_as_file(path)
#
#                 logger.info("将出现错误位置保存图片\t"+path)
#             driver.get_screenshot_as_file("base/images/test.png")
#
#         except:
#             logger.info("QQ空间登录模块获取失败")
#
#     def get_cookie(self, driver):
#         logger.info("正在读取QQ空间 cookie")
#
#         cookies = {}
#
#         url_cookies = driver.get_cookies()
#
#         try:
#             for url_cookie in url_cookies:
#                 cookies[url_cookie['name']] = url_cookie['value']
#         except:
#             pass
#         try:
#             with open("config/cookies.json", 'w', encoding="utf-8") as jcookie:
#                 json.dump(cookies, jcookie, indent=4, ensure_ascii=False)
#             logger.info("QQ空间 cookie 写入文件成功")
#         except:
#             logger.info("QQ空间 cookie 写入文件失败")
#
#     # def login_by_cookie(self):
#     #     """使用cookie登录QQ空间"""
#     #
#     #     with open("config/user.json", "r", encoding="utf-8") as usr:
#     #         infos = json.load(usr)
#     #         account = infos['account']
#     #
#     #     # url = 'https://user.qzone.qq.com/'+account
#     #     url = 'https://user.qzone.qq.com/proxy/domain/r.qzone.qq.com/cgi-bin/tfriend/friend_ship_manager.cgi?uin=2528510434&do=1&rd=0.5167004458657134&fupdate=1&clean=1&g_tk=193340148&qzonetoken=c4016a7e28e9de8ddb3e5212e928b90f3058f863df70c180df5cf9f9834c7c487932963af8d8563f&g_tk=193340148'
#     #     header = {
#     #         'accept': '*/*',
#     #         'accept-encoding': 'gzip, deflate, br',
#     #         'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
#     #         'cache-control': 'no-cache',
#     #         'referer': 'https://user.qzone.qq.com/'+account,
#     #         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.33'
#     #                       '86.1 Safari/537.36'
#     #     }
#     #
#     #     try:
#     #         with open("config/cookies.json", 'r', encoding="utf-8") as jcookie:
#     #             cookie = json.load(jcookie)
#     #         logger.info("cookie json 读取成功")
#     #     except:
#     #         logger.info("cookie json 读取失败")
#     #         cookie = 'null'
#     #
#     #     if cookie != 'null':
#     #         logger.info("使用 cookie 登录")
#     #         response = requests.get(url=url, headers=header, cookies=cookie)
#     #         print(response)
#     #         print(response.text,'dd')
