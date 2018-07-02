# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tutorial.items import ManhuaItem
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor

#scrapy crawl hz -o 327.csv

class HzSpider(CrawlSpider):
    name = 'hz'
    allowed_domains = ['51job.com']
    start_urls = ['http://search.51job.com/list/080200,000000,0000,00,9,99,python,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=1&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=']

    rules = (
        Rule(LinkExtractor(allow=(r's=\d+&t=\d+')), callback='parse_item'),
        Rule(LxmlLinkExtractor(allow=(r'lang=c&stype'),restrict_xpaths=(r"/html/body/div[2]/div[4]/div[54]/div/div/div/ul/li")))
        ,
    )

    def parse_item(self, response):

         item = ManhuaItem()
         item["name"] = response.xpath("//div//h1/text()").extract()[0]
         item["time"] = ",".join(response.xpath('//div[@class="t1"]//span/text()').extract())
         item["sallary"] = ",".join(response.xpath('//div[@class="jtag inbox"]//p/span/text()').extract())
         item["duty"] = "".join(response.xpath('//div//div//div[@class="bmsg job_msg inbox"]/p/text()').extract()).strip()#.replace("&nbsp",'')#.replace(u"\n",'')
         item["location"] = " ".join(response.xpath('//div/div[@class="bmsg inbox"]/p/text()').extract()).replace(u"\t",'').replace(u"\n",'')
         # item['duty'] = div.xpath("./p/span/a/text()")[0].extract().strip()
         # item['time'] = div.xpath("./span[4]/text()").extract()
         # item['name'] = div.xpath("./span[1]/a/text()").extract()
         # item['location'] = div.xpath("./span[2]/text()").extract()
         # item['sallary'] = div.xpath("./span[3]/text()").extract()
         yield  item