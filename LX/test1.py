# import re
# inputStr = """<center>
# 高速文字手打 <a href="http://www.biquger.com">笔趣阁</a> 凡人修仙之仙界篇章节列表<a href="/biquge/77182/"> http://www.biquger.com/biquge/77182/</a></center>
# <div class="bdlikebutton" style="margin-top:5px;"><script>qijixs_bottom()</script></div>
# </div>"""
# # replacedStr = re.sub(r"hello (\w+), nihao \1", "linxinfa", inputStr)
# # replacedStr = re.sub(r"<cen(\w+)", "", inputStr)
# replacedStr =inputStr.split("<cen",1)
# print("replacedStr = ", replacedStr[1])
#
# re_comment = re.compile('<center*</a>')
# print("re_comment",re_comment)
# inputStr = re_comment.sub('', inputStr)
# print("inputStr",inputStr)
#
# #输出结果为: replacedStr = linxinfa

######--------------------------------------------------------------读取EXcel表格
# import pandas as pd
# import numpy as np
# from datetime import datetime
#
# chinabank=pd.read_excel('chinabank.xls')
# print(chinabank)
# ######--------------------------------------------------------------



import requests
import re
import xlwt
import time

# def get_all_page():
#     global all_page
#     url = "http://kaijiang.zhcw.com/zhcw/html/ssq/list_1.html"
#     reponse = requests.get(url=url)
#     reponse.encoding='utf-8'
#     html = reponse.text
#     all_page = int(re.findall(r"class=\"pg\".*?<strong>(.*?)</strong>",html)[0])
#     return all_page

def get_num():
    k = -1
    f = xlwt.Workbook(encoding='utf-8')
    sheet01 = f.add_sheet(u'Sheet1', cell_overwrite_ok=True)

    # for page_num in range(1,all_page):
    #     url = "http://kaijiang.zhcw.com/zhcw/html/ssq/list_"+str(page_num)+".html"
    #     reponse = requests.get(url=url)
    #     time.sleep(5)
    #     reponse.encoding = 'utf-8'
    #     html = reponse.text
    #     rule = r"<tr>.*?<td align=\"center\">(.*?)</td>.*?<td align=\"center\">(.*?)</td>.*?<td align=\"center\" style=\"padding-left:10px;\">.*?<em class=\"rr\">(.*?)</em>.*?<em class=\"rr\">(.*?)</em>.*?<em class=\"rr\">(.*?)</em>.*?<em class=\"rr\">(.*?)</em>.*?<em class=\"rr\">(.*?)</em>.*?<em class=\"rr\">(.*?)</em>.*?<em>(.*?)</em></td>"
    #     num = re.findall(rule, html, re.S | re.M)
    #     # f = xlwt.Workbook(encoding='utf-8')
    #     # sheet01 = f.add_sheet(u'sheel1', cell_overwrite_ok=True)
    sheet01.write(0, 0, "日期")
    sheet01.write(0, 1, "期数")



    f.save("20201028.xls")
    print("数据保存完毕！")

if __name__ == '__main__':
    # get_all_page()
    get_num()
