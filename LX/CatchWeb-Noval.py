import urllib
from bs4 import BeautifulSoup
import requests
import re
import time

def getHTMLText(url):
    maxTryNum = 20
    for tries in range(maxTryNum):
        try:
            kv = {"user-agent": "Mizilla/5.0"}
            response = requests.get(url, headers=kv, timeout=60)
            return response.text
        except:
            if tries < (maxTryNum - 1):
                continue
            else:
                print("Has tried %d times to access url %s, all failed!" % (maxTryNum, url))
                break

#自笔趣阁网站下载
# url="http://www.biquger.com/biquge/20242/"
url="https://www.smjb.net/xiaoshuo/68890.html"    #修真聊天群 更新到320，后从321开始
# url="http://www.biqudu.tv/0_698/"    #修真聊天群 更新到320，后从321开始
# url="http://www.biquger.com/biquge/16583/"   #极品全能学生 更新到1512，后从1513开始
tx_useragent={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3073.0 Safari/537.36'}
kv = {'applicable-device': 'pc'}      # 是一个标准的浏览器的身份标识的字段
try:
    r = requests.get(url,headers=tx_useragent)
    # r.raise_for_status()
    r.encoding = r.apparent_encoding
    # fout=open('boss.html','wt',encoding="utf-8")
    # ret=fout.write(r.text)
    # fout.close()
    # print("r text is:",r.text)
except:
    print("爬取失败")

soup=BeautifulSoup(r.text,'lxml')
soup.encode("utf-8")

# print(soup.find_all(id="list")[0])
print("标题是",soup.find_all(id="info")[0].select("h1")[0].text)
print("-------------------------------------------------------------------------------")
# print("章节数量共",len(soup.find_all(id="list")[1].select("dd")))  #标签查找
# print("章节数量共",soup)  #标签查找
print("-------------------------------------------------------------------------------")
# print("span:",soup.find_all(id="list")[1].select("dd")[3])
# print("-------------------------------------------------------------------------------")
# print("span3:",soup.find_all(id="list")[1].select("dd")[3].text)
# print("span3 len:",len(soup.find_all(id="list")[1].select("dd")))

# for a in soup.find_all(id="list")[1].select("dd")[3]:
#     link_text = a['href']
#     print("link is ",link_text,a.text)


# print("span3 href:",soup.find_all(id="list")[1].select("dd")[3])

titleName=soup.find_all(id="info")[0].select("h1")[0].text
# f="星际强兵.txt"     #TXT 文档名称
f=titleName+".txt"
with open(f,"a",encoding='utf-8') as file:
    for i in range(len(soup.find_all(id="list")[0].select("dd")))[9:]:            #soup是列表页，“list” 为列表div 的id，dd标签为每个章节
    # for i in range(len(soup.find_all(id="list")[1].select("dd")))[859:]:    #len(soup...)是章节数量; “[293,]”是自第293+1个章节开始循环
        # print("ggewg",i)
        # for a in soup.find_all(id="list")[1].select("dd")[i]:                 # a 为每个章节的标签内容
        for a in soup.find_all(id="list")[0].select("dd")[i]:  # a 为每个章节的标签内容
            # link_text = a['href']
            link_text = "https://www.smjb.net"+a['href']
            # print("tetewt", link_text)
            # r1 = requests.get(link_text, headers=tx_useragent, verify=False, proxies=None, timeout=3)
            # r1 = requests.get(link_text,headers=tx_useragent,  proxies=None, timeout=6)     # 超时6秒
            r1=getHTMLText(link_text)
            # r1 = response.text
            # r1.encoding = r.apparent_encoding
            # print("tetewt2", r1)
            soup2 = BeautifulSoup(r1, 'lxml')
            soup2.encode("utf-8")
            file.write( a.text + "" + "\n")
            print(i,a.text,time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))
            tem = soup2.find_all(id="content")[0].text
            # tem = str(soup2.find_all(id="booktext")[0]).replace('<br/>', "")
            # tem = tem.replace("""<div class="content" id="booktext">""", "")
            # tem=tem.split("<center>",1)[0].replace("\n", "")
            # tem = tem.replace("<div class="content" id="booktext">", "")
            # file.write(tem.split("<center>",1)[0]+"\n")
            file.write(tem + "\n")
