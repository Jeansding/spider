import requests
import re

import pymysql

conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='5801200zxg',
    db='mynovel',
    charset='utf8'
)
cursor = conn.cursor()

def getClassList():
    response = requests.get('http://www.quanshuwang.com/')
    response.encoding = 'gbk'
    result = response.text
    reg = '<li><a href="(.*?)">(.*?)</a></li>'
    classList = re.findall(reg , result)
    classList = classList[:11]
    return classList

def getPage(url):
    response = requests.get(url)
    response.encoding = 'gbk'
    result = response.text
    reg = '<em id="pagestats">1/(.*?)</em>'
    page = re.findall(reg , result)
    return page

def getNovelList(url):
    response = requests.get(url)
    response.encoding = 'gbk'
    result = response.text
    reg = '<a target="_blank" title="(.*?)" href="(.*?)" class="clearfix stitle">'
    novelList = re.findall(reg , result)
    return novelList

def getNovelPage(url):
    response = requests.get(url)
    response.encoding = 'gbk'
    result = response.text
    imgUrl = ""
    sort = ""
    author = ""
    status = "" 
    chapterUrl = ""
    description = ""
    try:
        reg = r'<meta property="og:description" content="(.*?)"/>'
        description = re.findall(reg,result,re.S)[0]
        reg = r'<meta property="og:image" content="(.*?)"/>'
        imgUrl = re.findall(reg,result)[0]
        reg = r'<meta property="og:novel:category" content="(.*?)"/>'
        sort = re.findall(reg,result)[0]
        reg = r'<meta property="og:novel:author" content="(.*?)"/>'
        author = re.findall(reg,result)[0]
        reg = r'<meta property="og:novel:status" content="(.*?)"/>'
        status = re.findall(reg,result)[0]
        reg = r'<a href="(.*?)" class="reader"'
        chapterUrl = re.findall(reg,result)[0]
    except:
        pass
    return imgUrl , sort , author , status , chapterUrl , description

def getNovelChapter(url): #获取章节列表
    response = requests.get(url)
    response.encoding = 'gbk'
    result = response.text
    reg = r'<li><a href="(.*?)" title=".*?">(.*?)</a></li>'
    chapterListUrl = re.findall(reg , result)
    return chapterListUrl #每个章节的列表和名称

def getChapterContent(url):
    response = requests.get(url)
    response.encoding = 'gbk'
    result = response.text
    reg = r'style5\(\);</script>(.*?)<script type="text/javascript">style6'
    chapterContent = ""
    if re.findall(reg , result , re.S):
        chapterContent = re.findall(reg , result , re.S)[0] #re.S python中可以匹配多行
    else:
        pass
    return chapterContent

for classUrl , className in getClassList():
    page = 1
    if getPage(classUrl):
        page = getPage(classUrl)[0]
    else:
        pass
    print(page)
    for i in range(int(page)):
        # print(classUrl[:classUrl.index('_')] + '_' + str(i + 1) + '.html')
        classUrl = classUrl[:classUrl.index('_')] + '_' + str(i + 1) + '.html' 
        for novelName , novelUrl in getNovelList(classUrl):
            imgUrl , sort , author , status , chapterUrl , description = getNovelPage(novelUrl)
            cursor.execute("insert into novel (sortname , name , imgurl , description , status , author) values ('{}' , '{}' , '{}' , '{}' , '{}' , '{}')" .format (sort , novelName , imgUrl , description , status , author))
            conn.commit()
            lastrowid = cursor.lastrowid #插入数据的ID值
            for chapterUrl , chapterName in getNovelChapter(chapterUrl):
                content = getChapterContent(chapterUrl)
                cursor.execute("insert into chapter(novelid , title , content) values({} , '{}' , '{}')".format(lastrowid , chapterName , content))
                conn.commit()

conn.close()