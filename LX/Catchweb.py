# 引用外部库
import pandas as pd
import urllib
from bs4 import BeautifulSoup
import requests
import re


# #引用页地址
# # url = 'https://www.zhipin.com/c101010100/?query=%E6%95%B0%E6%8D%AE%E8%BF%90%E8%90%A5&page=2&ka=page-2'
# url = "https://datainfo.fx168.com/calendar.shtml"
# tx_useragent={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3073.0 Safari/537.36'}
# kv = {'applicable-device': 'pc'}      # 是一个标准的浏览器的身份标识的字段
# try:
#     r = requests.get(url,headers=tx_useragent)
#     # r.raise_for_status()
#     # r.encoding = r.apparent_encoding
#     fout=open('boss.html','wt',encoding="utf-8")
#     ret=fout.write(r.text)
#     fout.close()
#     print(r.text)
# except:
#     print("爬取失败")


from selenium import webdriver
from time import sleep
import xlwt

# chrome_path = "C:\Users\贵州场外\AppData\Local\Programs\Python\Python37\chromedriver.exe"
# driver = webdriver.chrome(executable_path=chrome_path)
driver=webdriver.Chrome(executable_path=r"C:\Users\贵州场外\AppData\Local\Programs\Python\Python37\chromedriver.exe")
driver.get("https://datainfo.fx168.com/calendar.shtml")

print('Before search================')

# 打印当前页面title
title = driver.title
# print(title)
# sleep(3)
# r=driver.find_element_by_id("datetime_box_time")
# r1=driver.find_element_by_xpath("//li[@date='2020-10-01']").click()           # 模拟点击click
soup=BeautifulSoup(driver.page_source,'lxml')                # 将模拟页获得的页代码赋给soup
soup.encode("utf-8")
soup1=soup.find_all("dd")            #soup 自soup 中获得数据窗代码
# soup2=soup1.find_all("dd")                                   #截取每行数据
# soup3=soup2.find_all("span")

f = xlwt.Workbook()
sheet1 = f.add_sheet('财经数据', cell_overwrite_ok=True)
# row0 = ["北京时间", "重要性", "指标内容", "前值", "前值修正", "预测值", "公布值", "注释"]
colume_name= ["北京时间", "重要性", "指标内容", "前值", "前值修正", "预测值", "公布值", "注释"]  #抬头数据项

for item in range(len(colume_name)):                # 写入抬头
    sheet1.write(0,item,colume_name[item])

irow=1
for item in range(len(soup1)):
    print("item,irow len(soup1))is ",item,irow,len(soup1))
    # print("that is ", soup.select('dd')[0].select('.span1')[0].text)
    sheet1.write(irow, 0, soup.select('dd')[irow-1].select('.span1')[0].text)
    sheet1.write(irow, 1, soup.select('dd')[irow - 1].select('.span2')[0].text)
    sheet1.write(irow, 2, soup.select('dd')[irow - 1].select('.span3')[0].text)
    sheet1.write(irow, 3, soup.select('dd')[irow - 1].select('.span4')[0].text)
    sheet1.write(irow, 4, soup.select('dd')[irow - 1].select('.span12')[0].text)
    sheet1.write(irow, 5, soup.select('dd')[irow - 1].select('.span5')[0].text)
    sheet1.write(irow, 6, soup.select('dd')[irow - 1].select('.span6')[0].text)
    sheet1.write(irow, 7, soup.select('dd')[irow - 1].select('.span7')[0].text)
    irow+=1
    f.save('财经日历.xls')



# driver.quit()



