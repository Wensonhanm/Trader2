# 方法1
# from requests import get
# from bs4 import BeautifulSoup
# from user_agent import generate_user_agent
# import time
#
#
# def request_content(start, end):
#     url_link = 'https://datachart.500.com/ssq/history/newinc/history.php?start={0}&end={1}'.format(start, end)
#     headers = {
#         'User-Agent': generate_user_agent(device_type='desktop', os=('mac', 'linux', 'win', 'android'))
#     }
#     response = get(url_link, headers=headers, timeout=6)
#     page_content = BeautifulSoup(response.content, "html.parser")
#     html_tag = page_content.find_all('tbody', id='tdata')[0]
#     return html_tag.find_all('tr', 't_tr1')
#
#
# class ssqclazz:
#     def __init__(self):
#         self.period = ''  # 期号
#         self.red_1 = ''  # 红球
#         self.red_2 = ''
#         self.red_3 = ''
#         self.red_4 = ''
#         self.red_5 = ''
#         self.red_6 = ''
#         self.blue_1 = ''  # 蓝球
#         self.happy_sunday = ''  # 快乐星期天
#         self.pool_prize = ''  # 奖池奖金(元)
#         self.first_count = ''  # 一等奖 注数
#         self.first_prize = ''  # 一等奖 奖金(元)
#         self.second_count = ''  # 二等奖 注数
#         self.second_prize = ''  # 二等奖 奖金(元)
#         self.total_prize = ''  # 总投注额(元)
#         self.lottery_date = ''  # 开奖日期
#
#     def __str__(self):
#         return '{0}，{1}，{2}，{3}，{4}，{5}，{6}，{7}，{8}，{9}，{10}，{11}，{12}，{13}，{14}，{15}'.format(self.period, self.red_1,
#                                                                                               self.red_2, self.red_3,
#                                                                                               self.red_4, self.red_5,
#                                                                                               self.red_6,
#                                                                                               self.blue_1,
#                                                                                               self.happy_sunday,
#                                                                                               self.pool_prize,
#                                                                                               self.first_count,
#                                                                                               self.first_prize,
#                                                                                               self.second_count,
#                                                                                               self.second_prize,
#                                                                                               self.total_prize,
#                                                                                               self.lottery_date)
#
#     def tr_tag(self, tag):
#         tds = tag.find_all('td')
#         index = 0
#         self.period = tds[index].string
#         index += 1
#         self.red_1 = tds[index].string
#         index += 1
#         self.red_2 = tds[index].string
#         index += 1
#         self.red_3 = tds[index].string
#         index += 1
#         self.red_4 = tds[index].string
#         index += 1
#         self.red_5 = tds[index].string
#         index += 1
#         self.red_6 = tds[index].string
#         index += 1
#         self.blue_1 = tds[index].string
#         index += 1
#         self.happy_sunday = tds[index].string
#         index += 1
#         self.pool_prize = tds[index].string
#         index += 1
#         self.first_count = tds[index].string
#         index += 1
#         self.first_prize = tds[index].string
#         index += 1
#         self.second_count = tds[index].string
#         index += 1
#         self.second_prize = tds[index].string
#         index += 1
#         self.total_prize = tds[index].string
#         index += 1
#         self.lottery_date = tds[index].string
#
#
# if __name__ == '__main__':
#     file = open('ssq.txt', mode='a+', encoding='utf-8')
#     localtime = time.localtime(time.time())
#     lyear = localtime.tm_year
#     ymin = 3  # 双色球03年上线
#     ymax = lyear - 2000
#     print('===抓取数据开始===，200%s-20%s' % (ymin, ymax))
#     for year in range(ymin, ymax + 1):
#         start = '{0}001'.format(year)
#         end = '{0}300'.format(year)
#         trs = request_content(start, end)
#         for tr in trs:
#             ssqobj = ssqclazz()
#             ssqobj.tr_tag(tr)
#             objstr = ssqobj.__str__()
#             file.write(objstr)
#             file.write('\n')
#             print(objstr)
#         file.write('\n')
#         print()
#         time.sleep(3)
#     file.close()
#     print('抓取完毕！！！')



# --------------------------------------------
#  方法2
#!/usr/bin/env python3
#-*-coding:utf-8-*-
# @Author  : 杜文涛
# @Time    : 2018/4/19 16:01
# @File    : cpssq.py
#×××双色球数据

import requests
import re
import xlwt
import time

def get_all_page():
    global all_page
    url = "http://kaijiang.zhcw.com/zhcw/html/ssq/list_1.html"
    reponse = requests.get(url=url)
    reponse.encoding='utf-8'
    html = reponse.text
    all_page = int(re.findall(r"class=\"pg\".*?<strong>(.*?)</strong>",html)[0])
    return all_page

def get_num():
    k = -1
    f = xlwt.Workbook(encoding='utf-8')
    sheet01 = f.add_sheet(u'Sheet1', cell_overwrite_ok=True)

    print("本次抓取共获得",all_page,"页")
    for page_num in range(1,all_page):
    # for page_num in range(1,2):
        url = "http://kaijiang.zhcw.com/zhcw/html/ssq/list_"+str(page_num)+".html"
        reponse = requests.get(url=url)
        time.sleep(5)
        reponse.encoding = 'utf-8'
        html = reponse.text
        rule = r"<tr>.*?<td align=\"center\">(.*?)</td>.*?<td align=\"center\">(.*?)</td>.*?<td align=\"center\" style=\"padding-left:10px;\">.*?<em class=\"rr\">(.*?)</em>.*?<em class=\"rr\">(.*?)</em>.*?<em class=\"rr\">(.*?)</em>.*?<em class=\"rr\">(.*?)</em>.*?<em class=\"rr\">(.*?)</em>.*?<em class=\"rr\">(.*?)</em>.*?<em>(.*?)</em></td>"
        num = re.findall(rule, html, re.S | re.M)
        # f = xlwt.Workbook(encoding='utf-8')
        # sheet01 = f.add_sheet(u'sheel1', cell_overwrite_ok=True)
        sheet01.write(0, 0, "日期")
        sheet01.write(0, 1, "期数")
        sheet01.write(0, 2, "第一个红球")
        sheet01.write(0, 3, "第二个红球")
        sheet01.write(0, 4, "第三个红球")
        sheet01.write(0, 5, "第四个红球")
        sheet01.write(0, 6, "第五个红球")
        sheet01.write(0, 7, "第六个红球")
        sheet01.write(0, 8, "蓝球")
        print("正在写入第%s页" % (page_num))
        for i in range(0,len(num)):
            k += 1
            sheet01.write(k + 1, 0, num[i][0])
            sheet01.write(k + 1, 1, num[i][1])
            sheet01.write(k + 1, 2, num[i][2])
            sheet01.write(k + 1, 3, num[i][3])
            sheet01.write(k + 1, 4, num[i][4])
            sheet01.write(k + 1, 5, num[i][5])
            sheet01.write(k + 1, 6, num[i][6])
            sheet01.write(k + 1, 7, num[i][7])
            sheet01.write(k + 1, 8, num[i][8])
    f.save(r"C:\Users\贵州场外\Documents\Python Project\AmazingQuant-master\LX\双色球20201113.xls")
    print("数据保存完毕！")

if __name__ == '__main__':
    get_all_page()
    get_num()