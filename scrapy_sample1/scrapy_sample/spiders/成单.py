# -*- coding:utf-8 -*-
import pandas as pd
import pymysql
from sqlalchemy import create_engine
# connect = create_engine('mysql+pymysql://root:hunteron@192.168.50.90:3306/test?charset=utf8',echo=True)
# to_sql=pd.io.sql.to_sql(te,'dingjian',connect,if_exists='replace')
def sql_frame(sql):
    con = pymysql.connect(host='localhost', port=3306, user='root', passwd='149879', db='test', charset='utf8')
    cur = con.cursor(cursor=pymysql.cursors.DictCursor)
    def read_table(cur, sql):  # sql_order is a string
        try:
            cur.execute(sql)  # 多少条记录
            data = cur.fetchall()
            frame = pd.DataFrame(list(data))
        except:  # , e:
            frame = pd.DataFrame()
        return frame
    return read_table(cur, sql)
    con.commit()
    cur.close()
    con.close()

pos=sql_frame("SELECT * FROM `dw_rom_autosql_747_t` where `year`>2016;")
print(pos)