# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
from twisted.enterprise import adbapi
import MySQLdb.cursors
import traceback

class SqlPipeline(object):
    def __init__(self):
        dbargs = dict(host='localhost', db='zhidao', user='root',  # replace with you user name
                      passwd='1994',  # replace with you password
                      charset='utf8', cursorclass=MySQLdb.cursors.DictCursor, use_unicode=True, )
        self.dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)
        print "connected to mysql"

    def process_item(self, item, spider):
        self.dbpool.runInteraction(self.insert_into_table, item)
        return item

    def insert_into_table(self, conn, item):
        if len(item['answers']) != 0:
            for index, ans in enumerate(item['answers']):
                try:
                    conn.execute('insert into Answers (question_id, answer_id, answer_content) values (%s,%s,\'%s\');' % (item['question_id'], str(index), ans))
                except Exception, e:
                    print 'error1:'
                    print 'traceback:\n%s'%traceback.print_exc()
                    print ('insert into Answers (question_id, answer_id, answer_content) values (%s,%s,\'%s\');' % (item['question_id'], str(index), ans))
            try:
                conn.execute('insert into zhidao (question_id, question_title, best_answer,question_content,team_id) values (%s,\'%s\',\'%s\',\'%s\',%s);' % (
                            item['question_id'], item['question_title'], item['best_answer'], item['question_content'],item['team_id']))
            except Exception, e:
                print 'error2:'
                print 'traceback:\n%s'%traceback.print_exc()
                print 'insert into zhidao (question_id, question_title, best_answer,question_content,team_id) values (%s,\'%s\',\'%s\',\'%s\',%s);' % (
                    item['question_id'], item['question_title'], item['best_answer'], item['question_content'],item['team_id'])
