import scrapy
from scrapy.http import Request
from lxml import etree
from zl.items import ZhaopinzhilianItem

#key=str(input("要爬取的内容："))
class RecuritSpider(scrapy.Spider):
    name = 'job52'
    allowed_domains = ['51job.com']
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}

    def start_requests(self):
        return [Request(
            #"https://search.51job.com/list/020000%252C010000%252C030200%252C040000,000000,0000,00,9,99,"+key+",2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=",
            "https://search.51job.com/list/020000,000000,0000,32,9,99,%2B,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=",
            callback=self.parse,headers=self.header,dont_filter=True)]


    def parse(self, response):
        try:
            item = ZhaopinzhilianItem()
            data = response.text
            res = etree.HTML(data)
            table_list = res.xpath('/html/body/div[@class="dw_wp"]/div[@class="dw_table"]/div[@class="el"]')
            #response.xpath('//div[@class="el"]/p[@class="t1 "]/span/a/@href')
            # response.xpath('//p[@class="t1 "]/span/a/@href')
            for table in table_list:
                item["link"]= table.xpath('./p[@class="t1 "]/span/a/@href')
                for j in range(0, len(item["link"])):

                    surl=item["link"][j]
                    print(surl)

                    yield Request(surl,callback=self.next)
            for i in range(2, 2000):
                #url = "https://search.51job.com/list/020000%252C010000%252C030200%252C040000,000000,0000,00,9,99,"+key+",2,"+str(i)+".html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
                url = "https://search.51job.com/list/020000,000000,0000,32,9,99,%2B,2,"+str(i)+".html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
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
            item["name"]=response.xpath("/html/body/div[3]//h1/text()").extract()     # 职位
            item["company"] = response.xpath('//p[@class="cname"]/a/text()').extract()    # 公司
            res = etree.HTML(response.text)
            zwyx = res.xpath('//div[@class="cn"]/strong/text()') #/html/body/div[@class="jtag inbox"]//p/span/text()
            item["salary"] = [zwyx[0].replace(u'万/月\xa0', u' ')]     # 薪水
            item["loc"] = res.xpath('//div[@class="cn"]/span/text()')  # 地点/html/body/div/div[@class="bmsg inbox"]/p/text()
            if len(res.xpath('//div[@class="bmsg job_msg inbox"]/p/text()'))==0:
                info = res.xpath('//div[@class="bmsg job_msg inbox"]/text()')  # .replace('<br/>','')   /html/body/div//div//div[@class="bmsg job_msg inbox"]/p/text()
                x = ''
                for j in info:
                    d = j.strip().replace('<br>', '')
                    x += d
                item["info"] = [x]  # 简介
            else :
                info = res.xpath('//div[@class="bmsg job_msg inbox"]/p/text()')  # .replace('<br/>','')   /html/body/div//div//div[@class="bmsg job_msg inbox"]/p/text()
                x = ''
                for j in info:
                    d = j.strip().replace('<br/>', '')
                    x += d
                item["info"] = [x]  # 简介
            #item["info"] = res.xpath('//div[@class="bmsg job_msg inbox"]/p/text()')
            item["xueli"] = res.xpath('//div[@class="t1"]/span[2]/text()')  # 学历
            item["time"] = res.xpath('//div[@class="t1"]/span[4]/text()')
            item["jy"] = res.xpath('//div[@class="t1"]/span[1]/text()')


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
            # item = ZhaopinzhilianItem()
            # item["xueli"] = ['']
            # item["time"] = ['']
            # item["jy"] = ['']