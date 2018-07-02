# -*- coding: utf-8 -*-
import scrapy
from company.items import CompanyItem
import re

class YellowSpider(scrapy.Spider):
    name = 'yellow'  
    sum = 0
    # start_urls = ['http://b2b.huangye88.com/qiye/ruanjian1720/']
    start_urls = ['http://b2b.huangye88.com/']
    cookie = {
        'user_trace_token':'20170823200708-9624d434-87fb-11e7-8e7c-5254005c3644',
        'LGUID':'20170823200708-9624dbfd-87fb-11e7-8e7c-5254005c3644 ',
        'index_location_city':'%E5%85%A8%E5%9B%BD',
        'JSESSIONID':'ABAAABAAAIAACBIB27A20589F52DDD944E69CC53E778FA9',
        'TG-TRACK-CODE':'index_code',
        'X_HTTP_TOKEN':'5c26ebb801b5138a9e3541efa53d578f',
        'SEARCH_ID':'739dffd93b144c799698d2940c53b6c1',
        '_gat':'1',
        'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6':'1511162236,1511162245,1511162248,1511166955',
        'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6':'1511166955',
        '_gid':'GA1.2.697960479.1511162230',
        '_ga':'GA1.2.845768630.1503490030',
        'LGSID':'20171120163554-d2b13687-cdcd-11e7-996a-5254005c3644',
        'PRE_UTM':'' ,
        'PRE_HOST':'www.baidu.com',
        'PRE_SITE':'https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D7awz0WxWjKxQwJ9xplXysE6LwOiAde1dreMKkGLhWzS%26wd%3D%26eqid%3D806a75ed0001a451000000035a128181',
        'PRE_LAND':'https%3A%2F%2Fwww.lagou.com%2F',
        'LGRID':'20171120163554-d2b13811-cdcd-11e7-996a-5254005c3644'
    }

    def parse(self , response):
        result = response.text
        for i in response.xpath('//ul[@class="qiyecont"]'):
            urls = i.xpath("li/a/@href").extract()
            for url in urls:
                yield scrapy.Request(url=url , cookies=self.cookie ,  callback=self.parseP)

    def parseP(self, response):
        #第一次解析 获取省份名字 和 省份Url
        for i in response.xpath('//div[@class="main"]/div[1]/div[@class="ad_list"]/a'):
            firstName = i.xpath("text()").extract()
            firstUrl = i.xpath("@href").extract()
            oneItem = CompanyItem()
            oneItem["firstName"] = firstName
            oneItem["firstUrl"] = firstUrl

            for url in oneItem["firstUrl"]:
                yield scrapy.Request(url=url , cookies=self.cookie , meta = {"firstUrl" : firstUrl} , callback=self.get_page)
    
    def get_page(self , response):
        #第二次解析 获取公司链接 ，进入下一层
        firstUrl = response.meta["firstUrl"]
        
        #首先计算这个页面有多少页
        page = response.css('.box .tit2 span em::text').extract()
        # print(page)
        #测试类型转换
        # print(type(int(page[0])))
        page = int(page[0])//20 + 1
        
        # print(firstUrl , page) #获得url 和 page

        for p in range(page):
            #获取所有页数的url
            newUrl = firstUrl[0] + "pn" + str(p+1)  
            # print(newUrl)
            yield scrapy.Request(url=newUrl , cookies=self.cookie , callback=self.parse_url)

        


    def parse_url(self , response):
        #找到公司链接
        for i in response.css('#jubao dl dt h4 a'):
            # companyName = i.xpath('text()').extract()
            companyUrl = i.xpath('@href').extract()           
            yield scrapy.Request(url=companyUrl[0] , cookies=self.cookie , callback=self.parse_url2)

    def parse_url2(self , response):
        #第三次解析 获得公司简介，联系方式url

        jianjieUrl = response.xpath('//ul[@class="meun"]/a/@href').extract()
        # print(jianjieUrl[-1:])
        # print(type(jianjieUrl[-1:])) --> list
        url2 = jianjieUrl[-1:][0]
        yield scrapy.Request(url=url2 , cookies=self.cookie , callback=self.parse_url3)

    def parse_url3(self , response):
        
        #第四次解析 获取公司简介
        # print("4444444444444444444444")
        # data = response.css('.con-txt li a::text').extract()
        # print(data)
        oneItem = CompanyItem()

        for i in response.css('.con-txt'):
            lianxiren = i.xpath('li[1]/a/text()').extract()
            # print("联系人: " , lianxiren[0])

            telephone = i.xpath('li[2]/text()').extract()
            # print("手机号： ", telephone)

            companyName = i.xpath('li[3]/text()').extract()
            # print("公司名称： " , companyName)
            
            # youbian = i.xpath('li[4]/text()').extract()
            zhuye = i.xpath('li[5]/a/@href').extract()
            # print("公司主页： " , zhuye)

            oneItem["lianxiren"] = lianxiren
            oneItem["telephone"] = telephone
            # oneItem["companyName"] = companyName
            # oneItem["youbian"] = youbian
            # oneItem["zhuye"] = zhuye


        # for x in response.xpath('//ul[@class="l-txt"][2]'):
            
        #     #  ul + p 选取ul后面的第一个p元素
        #     companyType = x.css('.company-rz + li::text').extract()
        #     # print(companyType)

        #     companyProduct = x.xpath('li[@class="contro-num"]/text()').extract()
        #     # print(companyProduct)

        #     oneItem["companyType"] = companyType
        #     oneItem["companyProduct"] = companyProduct

        #     # companyLocal = x.css('.contro-num + li')

        #     companyLocal = ""

        #     for local in x.css('.contro-num + li'):
        #         local1 = local.xpath('a[1]/text()').extract()
        #         local2 = local.xpath('a[2]/text()').extract()

        #         companyLocal = local1 + local2
            
        #     # print(companyLocal)
        #     oneItem["companyLocal"] = companyLocal

        yield oneItem