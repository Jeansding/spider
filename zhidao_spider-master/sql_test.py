#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3
@author: ‘aprilkuo‘
@license: Apache Licence 
@contact: aprilvkuo@gmail.com
@site: 
@software: PyCharm Community Edition
@file: sql_test.py
@time: 2017/11/23 下午10:10
"""

import MySQLdb,random
import MySQLdb.cursors
from twisted.enterprise import adbapi

class SqlPipeline(object):
    def __init__(self):
        dbargs = dict(host='local', db='zhidao', user='root',  # replace with you user name
            passwd='1994',  # replace with you password
            charset='utf8', cursorclass=MySQLdb.cursors.DictCursor, use_unicode=True, )
        self.dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)

    def process_item(self, item, spider):
        res = self.dbpool.runInteraction(self.insert_into_table, item)
        return item


    def insert_into_table(self, conn, item):

        conn.execute('insert into zreading(q_id,question,bst_answer,answers,tags,q_content/'
                      ',team_id) values(%s,%s,%s,%s,%s,%s,%s)', (item['q_id'],item['question'],
                      item['bst_answer'],item['answers'],item['q_content'],item['team_id']))


conn = MySQLdb.connect(host='localhost', db='zhidao', user='root',  # replace with you user name
            passwd='1994',  # replace with you password
            charset='utf8', use_unicode=True, )

cur = conn.cursor()

item = dict(q_id='1', question ='test_q',bst_answer = 'bst_an',answers = 'ans',q_content ='q_test',team_Id='1')
query ='insert into zhidao (q_id,question,bst_answer,answers,q_content' \
       ',teamId) values (%s,"%s","%s","%s","%s",%s)' %(item['q_id'],item['question'],
        item['bst_answer'],item['answers'],item['q_content'],item['team_Id'])

print query

query = 'use zhidao;'

test = '我们'
item

cur.execute(query)
query = "insert into Answers (question_id, answer_id, answer_content ) values (1495176553938770179, 4,'"+test+"')"

query = "insert into Answers (question_id, answer_id, answer_content) values (567303657,0,'\
打免费的咨询电话查不到你的申请信息时可再次申请，工作牌复印件等等。如果个人名下有房产，汽车就比较容易申请了，工作证明，收入证明。多准备资料，我也被拒绝过。首先不要网上申请，信用卡风险增大银行审核要求严了，多去几个银行申请看看，现在金融危机。不要在一棵树上吊死，因为资料极易伪造，所以网上申请很难通过。银行不会相信你的财务状况会有什么变化。一般最好过三个月。其次申请失败不要连续申请，连续申请没成功的可能第一次申请信用卡不明白一些流程和要求是正常的\
')"
print query

#query = 'create database if not exists scrapy;'


# 创建数据库
cur.execute(query)
data = cur.fetchall()
print data
cur.close()
conn.commit()
conn.close()