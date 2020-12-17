import urllib
from bs4 import BeautifulSoup
import requests
import re


url="http://www.biquger.com/biquge/77182/21949353"
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

# print(soup.find_all(id="booktext")[0])
print("-------------------------------------------------------------------------------")
# print(soup.find_all(id="list")[1].select("dd"))  #标签查找
print("-------------------------------------------------------------------------------")

print("span:",str(soup.find_all(id="booktext")[0]).replace('<br/>',"").replace("\n", ""))
tem=str(soup.find_all(id="booktext")[0]).replace('<br/>',"")
print("span tem",type(tem))
print("span2:",tem.split("<center>",1)[0].replace("\n", ""))

print("aaaaa-------------------------------------------------------------------------------")

# print("span3:",re.compile('<div [^>]* id="booktext">',tem.split("<center>",1)[0].replace("\n", "")))
# print("span3:",soup.find_all(id="list")[1].select("dd")[3].text)
# print("span3 len:",len(soup.find_all(id="list")[1].select("dd")))

#
#
# f="凡人.txt"
# with open(f,"a") as file:
#     for i in range(len(soup.find_all(id="list")[1].select("dd"))):
#         # print("ggewg",i)
#         for a in soup.find_all(id="list")[1].select("dd")[i]:
#             link_text = a['href']
#             print("link is ", link_text, a.text)
#             file.write(link_text +""+a.text+""+"\n")
# print(soup.find_all('div',id='datetime_box_time'))  #属性加标签过滤