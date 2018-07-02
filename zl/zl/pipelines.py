import pymysql
class ZhaopinzhilianPipeline(object):
    def process_item(self, item, spider):
        conn = pymysql.connect(host="localhost", user="root", passwd="149879", db="test", charset="utf8")
        cursor = conn.cursor()
        for i in range(0, len(item["zwmc"])):

            zwmc = item["zwmc"][i]
            gsmc = item["gsmc"][i]
            zwyx = item["zwyx"][i]
            gzdd = item["gzdd"][i]
            gsgm = item["gsgm"][i]
            minxueli = item["minxueli"][i]
            zprs = item["zprs"][i]
            sql = "insert into zhaopin(zwmc,gsmc,zwyx,zprs,gzdd,gsgm,minxueli) values(%s,%s,%s,%s,%s,%s,%s);"
            params = (zwmc,gsmc,zwyx,zprs,gzdd,gsgm,minxueli)
            cursor.execute(sql,params)
            conn.commit()
        cursor.close()
        conn.close()
        return item