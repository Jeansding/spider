# frame to mysql
import pymysql
import jieba
import pandas as pd
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
from sqlalchemy import create_engine
# df = pd.read_csv(r'C:\Users\Mengcao.Quan\Desktop\lagou2.csv',encoding='gbk')
# connect = create_engine('mysql+pymysql://root:hunteron@192.168.50.90:3306/test?charset=utf8',echo=True)
# pd.io.sql.to_sql(df,'lagou',connect,if_exists='replace')
#

def sql_frame(sql):
    con = pymysql.connect(host='192.168.50.90', port=3306, user='root', passwd='hunteron', db='test', charset='utf8')
    cur = con.cursor(cursor=pymysql.cursors.DictCursor)
    def read_table(cur, sql):
        try:
            cur.execute(sql)
            data = cur.fetchall()
            frame = pd.DataFrame(list(data))
        except:  # , e:
            frame = pd.DataFrame()
        return frame
    return read_table(cur, sql)
    con.commit()
    cur.close()
    con.close()

data = sql_frame("SELECT distinct `职位描述及要求` FROM `lagou`;")
for i in data:
    for w in data[i]:
        cut = jieba.cut(w)
        print(' '.join(cut))
print(len(data))