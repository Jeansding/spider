import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import pandas as pd
import re
import random
name=[]
city=[]
times=[]
work_time=[]
money=[]
key=[]
attract=[]
company=[]
industry=[]
info=[]

for x in range(1,31):
    ua=UserAgent()
    headers1={'User-Agent': 'ua.random'}#使用随机header，模拟人类
    cookiess = {
        'user_trace_token': '20170823200708-9624d434-87fb-11e7-8e7c-5254005c3644',
        'LGUID': '20170823200708-9624dbfd-87fb-11e7-8e7c-5254005c3644 ',
        'index_location_city': '%E5%85%A8%E5%9B%BD',
        'JSESSIONID': 'ABAAABAAAIAACBIB27A20589F52DDD944E69CC53E778FA9',
        'TG-TRACK-CODE': 'index_code',
        'X_HTTP_TOKEN': '5c26ebb801b5138a9e3541efa53d578f',
        'SEARCH_ID': '739dffd93b144c799698d2940c53b6c1',
        '_gat': '1',
        'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1511162236,1511162245,1511162248,1511166955',
        'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1511166955',
        '_gid': 'GA1.2.697960479.1511162230',
        '_ga': 'GA1.2.845768630.1503490030',
        'LGSID': '20171120163554-d2b13687-cdcd-11e7-996a-5254005c3644',
        'PRE_UTM': '',
        'PRE_HOST': 'www.baidu.com',
        'PRE_SITE': 'https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D7awz0WxWjKxQwJ9xplXysE6LwOiAde1dreMKkGLhWzS%26wd%3D%26eqid%3D806a75ed0001a451000000035a128181',
        'PRE_LAND': 'https%3A%2F%2Fwww.lagou.com%2F',
        'LGRID': '20171120163554-d2b13811-cdcd-11e7-996a-5254005c3644'
    }
    url='https://www.lagou.com/beijing-zhaopin/jiqixuexi/'+str(x)
    r = requests.get(url,headers=headers1).text
    soup = BeautifulSoup(r,'html.parser')
    url_two=re.findall('<a class="position_link" href="(.*?)" target="_blank"',r, re.S) #二级界面的网址
    for i in range(len(url_two)-1):  #爬取二级页面关于职位的描述
        print("第"+str(x)+"页第"+str(i)+"个职位")
        new_proxy=['112.114.76.176:6668','222.172.239.69:6666','112.114.78.54:6673','121.31.103.33:6666','110.73.30.246:6666','113.121.245.32:6667','114.239.253.38:6666','116.28.106.165:6666','220.179.214.77:6666','110.73.32.7:6666','118.80.181.186:6675','60.211.17.10:6675','110.72.20.245:6673','114.139.48.8:6668','111.124.231.101:6668','110.73.33.207:6673','113.122.42.161:6675','122.89.138.20:6675','61.138.104.30:1080','121.31.199.91:6675','218.56.132.156:8080','218.56.132.156:8080','220.249.185.178:9999','60.190.96.190:808','121.31.196.109:8123','121.31.196.109:8123','61.135.217.7:80','61.135.217.7:80','61.155.164.109:3128','61.155.164.109:3128','61.155.164.110:3128','124.89.33.75:9999','124.89.33.75:9999','113.200.214.164:9999','113.200.214.164:9999','119.90.63.3:3128','112.250.65.222:53281','112.250.65.222:53281','222.222.169.60:53281','122.136.212.132:53281','122.136.212.132:53281','58.243.50.184:53281','58.243.50.184:53281','125.66.140.27:53281','125.66.140.27:53281','139.224.24.26:8888','139.224.24.26:8888']
        new_proxy={'http':random.choice(new_proxy)}
        headers2={'User-Agent': 'ua.random'}
        new_url='{}'.format(url_two[i])
        cookiess = {'JSESSIONID': '99021FFD6F8EC6B6CD209754427DEA93','_gat': '1',  'user_trace_token': '20170203041008-9835aec2-e983-11e6-8a36-525400f775ce', 'PRE_UTM': '',  'PRE_HOST': '',  'PRE_SITE': '',  'PRE_LAND': 'https%3A%2F%2Fwww.lagou.com%2Fzhaopin%2F','LGUID': '20170203041008-9835b1c9-e983-11e6-8a36-525400f775ce',  'SEARCH_ID': 'bfed7faa3a0244cc8dc1bb361f0e8e35',  'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1486066203',  'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1486066567',  '_ga': 'GA1.2.2003702965.1486066203',  'LGSID': '20170203041008-9835b03a-e983-11e6-8a36-525400f775ce',  'LGRID': '20170203041612-714b1ea3-e984-11e6-8a36-525400f775ce'}
        r1 = requests.get(new_url,headers=headers2,cookies=cookiess,proxies=new_proxy).text
        soup1 = BeautifulSoup(r1,'html.parser')
        s9=soup1.select('.job_bt p') #关于职位的描述
        c=''
        for j in s9:
            d=j.text.strip().replace(' ','')
            print(d)
            c+=d+''
        info.append(c)
        import time
        ts=random.randrange(1,4)
        print("==========休息"+str(ts)+"秒============")
        time.sleep(ts)
    s= soup.select('.position_link h3')
    for i in s:
        name.append(i.text)
    s1=soup.select('.add em')

    for i in s1:
        city.append(i.text)
        #print(city)
    s2=soup.select('.format-time')
    for i in s2:
        times.append(i.text)
    s3=soup.select('.money')
    for i in s3:
        money.append(i.text)
    s4=soup.select('.p_bot')
    work_key=[]
    for i in s4:
        work_key.append(i.text.replace('\n','').strip())

    for i in work_key:
        index=i.index("经")
        work_time.append(i[index:len(i)])
    s5=soup.select('.company_name a')

    for i in s5:
        company.append(i.text)
    s6=soup.select('.industry')

    for i in s6:
        industry.append(i.text.replace(' ','').strip())

    s7=soup.select('.li_b_l')
    key1=[]
    for i in s7:
        key1.append(i.text.strip().replace(' ','').replace('\n','/'))
    for i in range(len(key1)):
        if i%2!=0:
            key.append(key1[i])

    s8=soup.select('.li_b_r')
    for i in s8:
        attract.append(i.text.replace('“','').replace('”',''))

    print(len(name),len(city),len(times),len(money),len(work_time),len(company),len(industry),len(key),len(attract),len(info))
data1=[]
for i in range(len(name)):
    a=name[i],city[i],times[i],money[i],work_time[i],company[i],industry[i],key[i],attract[i],info[i]
    data1.append(a)
data=pd.DataFrame(data1)
data.columns=['职位名称','城市','发布时间','薪水','工作年限','公司','行业','关键词','职位诱惑','职位描述及要求']
data.to_csv(r"C:\Users\Mengcao.Quan\Desktop\lagou2.csv")  #职位的描述有些乱码，用gbk编码不成功，只能用utf-8