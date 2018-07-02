import scrapy
from First.items import FirstItem

class Lagou(scrapy.Spider):
    name = "three"
    start_urls = [
        "https://www.lagou.com/"
    ]
    
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
        for item in response.xpath('//div[@class="menu_box"]/div/dl/dd/a'):
            jobClass = item.xpath('text()').extract()
            jobUrl = item.xpath("@href").extract_first()

            oneItem = FirstItem()
            oneItem["jobClass"] = jobClass
            oneItem["jobUrl"] = jobUrl
            # print(jobUrl)
            # yield oneItem

            # jobUrl https://www.lagou.com/zhaopin/Java/2/?filterOption=3
            # https://www.lagou.com/zhaopin/Java/
            # print(jobUrl)
            for i in range(30):
                
                jobUrl2 = jobUrl + str(i+1)
                # print(jobUrl2)
                try:
                    yield scrapy.Request(url = jobUrl2  ,cookies=self.cookie , meta = {"jobClass":jobClass} , callback=self.parse_url)
                except:
                    pass
                    
    # def parse_url(self , response):
    #     jobClass = response.meta["jobClass"]
    #     for sel2 in response.xpath('//ul[@class="item_con_list"]/li'):
    #         jobName = sel2.xpath('div/div/div/a/h3/text()').extract()
    #         Item = FirstItem()
    #         Item["jobName"] = jobName
    #         print(jobName)
    #         # yield Item
            
    def parse_url(self , response):
        jobClass = response.meta["jobClass"]


        for sel2 in response.css('.list_item_top div div a h3'):
            jobName = sel2.xpath('text()').extract()

            print(jobName)