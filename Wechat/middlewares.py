# -*- coding: utf-8 -*-
# Author:   BinBin
# Email:    289594665@qq.com
# Time :    2017/07/27

import random

import time
from scrapy import signals
from scrapy.http import HtmlResponse, Response
from selenium import webdriver
from PIL import Image
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from rk import RClient


class WechatSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    def __init__(self, agents):
        self.agents = agents

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        print "from_crawler"
        s = cls(crawler.settings.getlist('USER_AGENTS'))
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        print "process_spider_input"
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        print "process_spider_output"
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        print "process_spider_exception"

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        print "process_start_requests"
        for r in start_requests:
            #随机获取UserAgent
            #r.headers.setdefault('User-Agent', random.choice(self.agents))
            r.headers.setdefault('User-Agent', 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 5_0 like Mac OS X; en-us) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3')
            yield r

    def spider_opened(self, spider):
        print "spider_opened"
        spider.logger.info('Spider opened: %s' % spider.name)

class WechatDownloaderMiddleware:

    @classmethod
    def process_request(cls, request, spider):
        #利用PhantomJS加载网页中的javascript动态内容
        print("WechatDownloaderMiddleware")

        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] = (
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 QQBrowser/6.9.11079.201"
        )
        driver = webdriver.PhantomJS(desired_capabilities=dcap)
        driver.set_window_size(1280, 800)
        driver.set_page_load_timeout(20)
        driver.get(request.url)

        ct = time.time()
        local_time = time.localtime(ct)
        data_head = time.strftime("%Y%m%d%H%M%S", local_time)
        data_secs = (ct - long(ct)) * 1000
        timestamp = "%s%05d" % (data_head, data_secs)

        try:
            seccode_image = driver.find_element_by_id('seccodeImage')
            if None != seccode_image:
                print u"Middleware 搜狗分析填入验证码!"
                # 截图
                driver.get_screenshot_as_file('E:/pyworkspace/Wechat/screenshot{0}.png'.format(timestamp))
                # 获取验证码图片位置
                element = driver.find_element_by_id('seccodeImage')
                left = int(element.location['x'])
                top = int(element.location['y'])
                right = int(element.location['x'] + element.size['width'])
                bottom = int(element.location['y'] + element.size['height'])

                # 通过Image处理图像
                im = Image.open('E:/pyworkspace/Wechat/screenshot{0}.png'.format(timestamp))
                im = im.crop((left, top, right, bottom))
                # 保存验证码图片
                im.save('E:/pyworkspace/Wechat/code{0}.png'.format(timestamp))

                rc = RClient('289594665', 'huangwen3895170', '86899', 'da005218780a43269aa9260fa26ec25d')
                im = open('E:/pyworkspace/Wechat/code{0}.png'.format(timestamp), 'rb').read()

                # 若快平台识别验证码
                rk_ret = rc.rk_create(im, 3060)
                code = str(rk_ret["Result"])
                print "code{0}:".format(timestamp) + code
                # 模拟输入验证码，并提交
                elem = driver.find_element_by_id("seccodeInput")
                elem.clear()
                elem.send_keys(code)
                driver.find_element_by_id("submit").click()
                #延时5秒，等待完成页面跳转
                time.sleep(5)

        except NoSuchElementException as e:
            print e

        try:
            verify_img = driver.find_element_by_id('verify_img')
            if None != verify_img:
                print u"Middleware 微信分析填入验证码!"
                # 截图
                driver.get_screenshot_as_file('E:/pyworkspace/Wechat/wescreenshot{0}.png'.format(timestamp))
                # 获取指定元素位置
                element = driver.find_element_by_id('verify_img')
                left = int(element.location['x'])
                top = int(element.location['y'])
                right = int(element.location['x'] + element.size['width'])
                bottom = int(element.location['y'] + element.size['height'])

                # 通过Image处理图像
                im = Image.open('E:/pyworkspace/Wechat/wescreenshot{0}.png'.format(timestamp))
                im = im.crop((left, top, right, bottom))
                # 保存验证码图片
                im.save('E:/pyworkspace/Wechat/wecode{0}.png'.format(timestamp))
                # 若快平台识别验证码
                rc = RClient('289594665', 'huangwen3895170', '86899', 'da005218780a43269aa9260fa26ec25d')
                im = open('E:/pyworkspace/Wechat/wecode{0}.png'.format(timestamp), 'rb').read()

                rk_ret = rc.rk_create(im, 3040)
                wecode = str(rk_ret["Result"])
                print "wecode{0}:".format(timestamp) + wecode
                # 模拟输入验证码，并提交
                elem = driver.find_element_by_id("input")
                elem.clear()
                elem.send_keys(wecode)
                driver.find_element_by_id("bt").click()
                #延时5秒，等待完成页面跳转
                time.sleep(5)

        except NoSuchElementException as e:
            print e

        time.sleep(5)
        content = driver.page_source.encode('utf-8')
        #print "content:" + content.__str__()
        driver.quit()
        return HtmlResponse(request.url, encoding='utf-8', body=content, request=request)