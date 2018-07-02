import scrapy
from scrapy.http import Request

from lxml import etree
from zl.items import ZhaopinzhilianItem
key=input("要爬取的内容：")
#key='深度学习'
class RecuritSpider(scrapy.Spider):
    name = 'zl'
    allowed_domains = ['zhaopin.com']
    #start_urls = ['http://www.zhaopin.com/']
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}

    def start_requests(self):
        return [Request(
            "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=上海%2b北京&kw="+key+"&isadv=0&sg=68b030ac696c4c4a9dffcd3a64403fd0&p=1",
            callback=self.parse,headers=self.header,dont_filter=True)]


    def parse(self, response):
        try:
            item = ZhaopinzhilianItem()
            data = response.text
            res = etree.HTML(data)
            table_list = res.xpath('//table[@class="newlist"]')
            for table in table_list:
                item["link"]= table.xpath('.//td[@class="zwmc"]//a[1]//@href')
                for j in range(0, len(item["link"])):

                    surl=item["link"][j]
                    print(surl)

                    yield Request(surl,callback=self.next)
            for i in range(2, 91):
                url = "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=上海%2b北京&kw="+key+"&isadv=0&sg=68b030ac696c4c4a9dffcd3a64403fd0&p=" + str(
                    i)

                yield Request(url, callback=self.parse)


        except Exception as e:
            print(e)
    def next(self,response):
        try:
            '''
            conn = pymysql.connect(host="127.0.0.1", user="root", passwd="149879", db="test", charset="utf8")
            cursor = conn.cursor()
            '''
            item = ZhaopinzhilianItem()
            item["zwmc"]=response.xpath("//div[@class='inner-left fl']/h1/text()").extract()

            item["gsmc"] = response.xpath("//div[@class='inner-left fl']/h2/a[@target='_blank']/text()").extract()

            res = etree.HTML(response.text)
            item["gsgm"]= res.xpath("/html/body/div[6]/div[2]/div[1]/ul/li[1]/strong/text()")


            zwyx = res.xpath("/html/body/div[6]/div[1]/ul/li[1]/strong/text()")
            item["zwyx"] = [zwyx[0].replace(u'元/月\xa0', u' ')]
            #print(item["zwyx"])
            item["gzdd"] = res.xpath("/html/body/div[6]/div[1]/ul/li[2]/strong/a/text()")

            # zprs= res.xpath("/html/body/div[6]/div[1]/ul/li[7]/strong/text()")
            # item["zprs"]=[zprs[0].replace(u'人',u' ')]
            #zprs=res.xpath("/html/body/div[6]/div[1]/div[@class='terminalpage-main clearfix']/div[1]/div[1]/p[1]/text()")
            zprs = res.xpath("/html/body/div[6]/div[1]/div[1]/div[1]/div[1]/p/text()")#.replace('<br/>','')
            x=''
            for j in zprs:
                d=j.strip().replace('<br/>','')
                x+=d
            item["zprs"] = [x]
            item["minxueli"] = res.xpath("/html/body/div[6]/div[1]/ul/li[6]/strong/text()")
            '''
            sql = "insert into zhaopin(zwmc,gsmc,zwyx,zprs,gzdd,gsgm,minxueli) values(%s,%s,%s,%s,%s,%s,%s);"
            params = (item["zwmc"][0], item["gsmc"][0], item["zwyx"][0],item["zprs"][0],item["gzdd"][0],item["gsgm"][0],item["minxueli"][0])
            cursor.execute(sql, params)
            conn.commit()
            cursor.close()
            conn.close()
            '''
            yield item
        except Exception as e:
            print(e)