import pymysql
class ZhaopinzhilianPipeline(object):
    def process_item(self, item, spider):
        conn = pymysql.connect(host="localhost", user="root", passwd="149879", db="test", charset="utf8")
        cursor = conn.cursor()
        for i in range(0, len(item["name"])):
            name = item["name"][i]
            company = item["company"][i]
            salary = item["salary"][i]
            loc = item["loc"][i]
            info = item["info"][i]
            xueli = item["xueli"][i]
            time = item["time"][i]
            jy = item["jy"][i]
            sql = "insert into job(name,company,salary,xueli,time,jy,loc,info) values(%s,%s,%s,%s,%s,%s,%s,%s);"
            params = (name,company,salary,xueli,time,jy,loc,info)
            cursor.execute(sql,params)
            conn.commit()
        cursor.close()
        conn.close()
        return item