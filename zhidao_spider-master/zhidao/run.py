#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3
@author: ‘aprilkuo‘
@license: Apache Licence 
@contact: aprilvkuo@gmail.com
@site: 
@software: PyCharm Community Edition
@file: run.py
@time: 2017/11/23 上午12:51
"""

from scrapy import cmdline
name = 'qas'
cmd = 'scrapy crawl {0} -o test5.csv -s LOG_FILE=log.log1'.format(name)
print cmd
cmdline.execute(cmd.split())


# from selenium import webdriver
#
# browser = webdriver.PhantomJS()  #浏览器初始化；Win下需要设置phantomjs路径，linux下置空即可
# url = 'http://www.zhidaow.com'  # 设置访问路径
# browser.get(url)  # 打开网页
# print browser.page_source
# title = browser.find_elements_by_xpath('//h2')  # 用xpath获取元素
#
# for t in title:  # 遍历输出
#     print t.text # 输出其中文本
#     print t.get_attribute('class')  # 输出属性值
#
# browser.quit()  # 关闭浏览器。当出现异常时记得在任务浏览器中关闭PhantomJS，因为会有多个PhantomJS在运行状态，影响电脑性能