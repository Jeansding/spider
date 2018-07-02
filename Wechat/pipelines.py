# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import urllib
import time

from DBHelper import db

class WechatPipeline(object):

    def process_item(self, item, spider):
        print ("process_item title:" +  item["article_title"])

        if item["article_title"].strip() == "" or item["article_icon"].strip() == "":
            return

        if None != item["article_icon"] and "" != item["article_icon"].strip:
            timestamp = self.get_time_stamp()
            postfix = ".png"
            if item["article_icon"].find("wx_fmt=") > 0:
                postfix = "." + item["article_icon"][item["article_icon"].find("wx_fmt=") + 7:]

            abs_path = u'/Uploads/Spider/Wechat/Icon/' + timestamp + "." + postfix
            save_path = u'D:/UserUploadFiles勿删' + abs_path
            urllib.urlretrieve(item["article_icon"].strip().encode('utf-8'), save_path)
            item["article_icon"] = abs_path

        item["article_content"] = item["article_content"].replace(u'\'', '&apos;')

        item["article_content"] = item["article_content"].replace(u'\'', '&apos;')
        # item["article_content"] = item["article_content"].replace(u'"', '&quot;')
        print ("item[\"article_url\"]:" + item["article_url"])

        selectSql = u'''select * from T_News where Title=\'{Title}\' and convert(varchar(50), dt, 120) like \'%{dt}%\''''\
            .format(Title=item["article_title"], dt=item["article_time"][0:10])
        row = db.queryAll(selectSql.encode('GBK', 'ignore'))
        if len(row) <= 0:
            sql = u"""insert into T_News(Title, Author, Src,
                                      MobileWeChatURL, NewsTypeID, Content, OrderID,
                                      Destrible, MobileSmallPic, MobileLargePic, PcSmallPic, SharePic, dt)
                              values ('{article_title}','{article_author}','{article_src}',
                                    '{article_url}','{article_type}','{article_content}',1,
                                    '{article_summary}','{MobileSmallPic}','{MobileLargePic}','{PcSmallPic}',
                                    '{SharePic}','{article_time}')""" \
                .format(
                article_title=item["article_title"],
                article_author=item["article_author"],
                article_src=item["article_src"],
                article_url=item["article_url"],
                article_type=item["article_type"],
                article_content=item["article_content"],
                article_summary=item["article_summary"],
                MobileSmallPic=item["article_icon"],
                MobileLargePic=item["article_icon"],
                PcSmallPic=item["article_icon"],
                SharePic=item["article_icon"],
                article_time=item["article_time"]
            )

            # 这里要特殊处理这个\xa0，是空格，GBK无法转化这个编码
            # print "sql:" + sql
            sql = sql.replace(u'\xa0', u' ')
            row = db.execute(sql.encode('GBK', 'ignore'))
            print ("insert new row")

        return item

    def get_time_stamp(self):
        ct = time.time()
        local_time = time.localtime(ct)
        data_head = time.strftime("%Y%m%d%H%M%S", local_time)
        data_secs = (ct - long(ct)) * 1000
        time_stamp = "%s%03d" % (data_head, data_secs)
        return time_stamp