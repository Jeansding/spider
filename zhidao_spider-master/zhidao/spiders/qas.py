#coding:utf-8
from __future__ import print_function
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from zhidao.items import ZhidaoItem  
import re,random,json
from scrapy.selector import Selector
import urlparse


def generate_ajax(teamId,pn,rn):
    team_url = 'https://zhidao.baidu.com/uteam/ajax/answer?teamId=' + teamId + '&pn='+str(pn)+'&rn='+str(rn)+'&type=2&_='
    return team_url+str(random.random())[2:15]

def str_process(item):

    return item.strip().replace("'",'"')

class QasSpider(scrapy.Spider):
    name = 'qas'
    allowed_domains = ["zhidao.baidu.com"]
    start_urls = [
        #"https://zhidao.baidu.com/question/460509474240067645.html",
        #"https://zhidao.baidu.com/uteam/contribute?teamId=91293",
        "https://zhidao.baidu.com/uteam/rankdetail?cid=101"
    ]  #待抓取的列表


    rules = (# 提取匹配 'category.php' (但不匹配 'subsection.php') 的链接并跟进链接(没有callback意味着follow默认为True)
        Rule(LinkExtractor(allow=('rankdetail',)),callback='parse_first'),
        # 提取匹配 'item.php' 的链接并使用spider的parse_item方法进行分析
        Rule(LinkExtractor(allow=('contribute',)), callback='parse_sec'),)
 
    def parse(self, response):
        # 得到队伍的id
        fields = response.xpath('//a[@target="_blank" and contains(@href,"teamId")]/@href')
        for item in fields:
            teamId = item.extract()[19:]
            team_url = generate_ajax(teamId, 0, 50)
            yield scrapy.Request(url=team_url, callback=self.parse_sec, method='GET', meta={'pn': 0, 'rn': 50, \
                                                                                            'teamId': teamId, 'NoPhantomJS': True})

    def parse_sec(self, response):
        data = json.loads(response.body_as_unicode())['data']['monthlyAnswerList']
        if len(data) == 50:
            pn = response.meta['pn'] + 50
            team_url = generate_ajax(response.meta['teamId'], pn, 50)
            yield scrapy.Request(url=team_url, callback=self.parse_sec, method='GET', \
                                 meta={'teamId': response.meta['teamId'], 'pn': pn, 'rn': 50,'NoPhantomJS': True})
        else:
            print(response.url)
            if len(data) == 0:
                yield scrapy.Request(url=response.url, callback=self.parse_sec, method='GET', \
                                     meta={'teamId': response.meta['teamId'], 'pn': response.meta['pn'], 'rn': 50, 'NoPhantomJS': True})
            else:
                print (len(data))
                print('end:',response.meta['pn'])

        for item in data:
            zhidao_base_url = 'https://zhidao.baidu.com/question/'
            yield scrapy.Request(url=zhidao_base_url+item['qid']+'.html+?sort=9&rn=5&pn=0', callback=self.parse_third,\
                                 method='GET',meta={'teamId':response.meta['teamId'],'NoPhantomJS': True})



    def parse_third(self,response):
        item = ZhidaoItem()
        item['best_answer'] = str_process(response.xpath('//*[contains(@id,"best-content")]').xpath('string(.)').extract()[0])
        item['answers'] = map(str_process,response.xpath('//div[@class="answer-text line"]/span').xpath('string(.)').extract())
        item['question_title'] = str_process(response.xpath('//*[@id="wgt-ask"]/h1/span').xpath('string(.)').extract()[0])
        item['question_content'] = response.xpath('//pre[contains(@id,"best-content")]').xpath('string(.)').extract()
        if len(item['question_content']) == 1:
            item['question_content'] = str_process(item['question_content'][0])
        else:
            #print 'question_content_error:'
            #print '\n'.join(item['question_content'])
            item['question_content'] = ""
        item['question_id'] = str(re.findall(r"\/(\d+)\.html",response.url)[0])
        item['team_id'] = response.meta['teamId']
        next_page = response.xpath('//a[@class="pager-next"]/@href').extract()
        if len(next_page) > 0:
            new_url = 'https://zhidao.baidu.com'+next_page[0]
            yield scrapy.Request(url=new_url, callback=self.more_parse, method='GET',
                                 meta={'item': item, 'NoPhantomJS': True})
        else:
            yield item

    def more_parse(self,response):
        item = response.meta['item']
        item['answers'] += map(str_process,
                              response.xpath('//div[@class="answer-text line"]/span').xpath('string(.)').extract())

        next_page = response.xpath('//a[@class="pager-next"]/@href').extract()
        if len(next_page) > 0:
            new_url = 'https://zhidao.baidu.com' + next_page[0]
            yield scrapy.Request(url=new_url, callback=self.more_parse, method='GET',
                                 meta={'item': item, 'NoPhantomJS': True})
        else:
            yield item




        # print response.url
        # point = response.xpath('//*[@id="answer-title"]/li[2]').
        # #print response.body
        # question_base = 'https://zhidao.baidu.com/question/'
        # data_qid = response.xpath('//li[@data-qid]/@data-qid')
        # for item in data_qid:
        #     question_url = question_base+item.extract()
        #     yield scrapy.Request(url=question_url, callback=self.parse_thrid, method='GET')
        #     return


        # item= ZhidaoItem()
        # #authors = hxs.select('//a[@class="titlelnk"]')
        # print(response.request.headers)
        # print(response.request.meta)
        #
        # item['bst_answer']  = response.xpath('//*[contains(@id,"best-content")]/text()').extract()
        # item['answers'] =  response.xpath('//div[@class="answer-text line"]/span/text()').extract()
        # item['question'] = response.xpath('//*[@id="wgt-ask"]/h1/span/text()').extract()
        # item['q_content'] = response.xpath('//div[@accuse="qContent"]/span/text()').extract()
        # item['q_id']=str(re.findall(r"\/(\d+)\.html",response.url))
        # yield item
        #
        #
        # next_page = response.xpath('//*[@class="pager-next"]/@href').extract()
        # print next_page
        # if next_page:
        #     nexturl = response.urljoin(next_page[0])
        #     print nexturl
        #         yield scrapy.Request(nexturl,self.parse)

