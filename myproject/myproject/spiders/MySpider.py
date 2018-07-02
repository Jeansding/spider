# -*- coding:utf-8 -*-
import scrapy
import re

from myproject.items import MyItem

#Spider是指定URL，发送请求和接收原始数据，再根据Item进行数据操作
class MySpider(scrapy.Spider):
    name = 'myspider'

    #可传入pageIndex参数合成完整URL
    def __init__(self, pageIndex=None, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
        self.start_urls = ['http://www.qiushibaike.com/hot/page/%s' % pageIndex]

    #根据Item进行数据操作
    def parse(self, response):
        #print response.body.decode('response.encoding') #打印原始数据
        pattern = re.compile('<div class="author clearfix">.*?<h2>(.*?)</h2>' + 
                        '.*?' + 
                        '<div class="content">.*?<span>(.*?)</span>.*?</div>' +
                         '.*?' + 
                        '<div class="main-text">(.*?)<div class="likenum">'
                        ,re.S)
        items = re.findall(pattern,response.body.decode(response.encoding))
        print ("lin len: %d"%(len(items)))
        for item in items:         
            print ("lin User: %s"%(item[0].strip()))
            print ("lin Content: %s"%(item[1].strip()))
            print ("lin God comments: %s"%(item[2].strip()))
            myItems = MyItem(user=item[0], content=item[1], godComment=item[2])
            yield myItems