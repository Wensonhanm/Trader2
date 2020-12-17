import xlrd
import xlwt
# import xlsxwriter
from xlutils.copy import copy
import time
import pandas as pd

# wb = xlrd.open_workbook('双色球统计结果.xls')
# sh1=wb.sheet_by_name(u'sheel1')
# print(sh1.row_values(0))

df=pd.read_excel('双色球统计结果1.xls',sheet_name='sheet1')
data=df.head()#默认读取前5行的数据
# print("获取到所有的值:\n{0}".format(df))                       #格式化输出
print("输出数据表抬头",df.columns)
print("输出数据表特定列的全部数据：\n",df['日期'])                   #某个列的标签用中括号
print("按标签（抬头）输出：\n",df.loc[:,'日期':'期数'])              #输出选择项为抬头名称
print("df的数据行数(不含抬头)是",len(df),"df的数据列数是",df.columns.size)              #输出选择项为抬头名称
print("df的第4行（不含抬头）第2列数据是",df.iloc[3,1])              #输出特定单元格的数据

nred=1
nblue=34

wb= xlrd.open_workbook('双色球统计结果1.xls')
ws1=wb.sheet_by_name("Sheet1")
# ws1=wb.sheet_by_name("sheel1")
wb2=copy(wb)
ws2=wb2.get_sheet(2)

font0 = xlwt.Font()
font0.name = 'Times New Roman'
font0.colour_index = 2
font0.bold = True

font1 = xlwt.Font()
font1.name = 'Times New Roman'
font1.bold = True # 黑体
font1.underline = True # 下划线
font1.italic = True # 斜体字

style0 = xlwt.XFStyle()
style0.font = font0

style1 = xlwt.XFStyle()
style1.num_format_str = 'D-MMM-YY'

borders = xlwt.Borders()  # 创建边框对象Create Borders
borders.left = xlwt.Borders.THIN  #对边框对象进行操作，指定边框上下左右的边框类型为虚线
# DASHED虚线
# NO_LINE没有
# THIN实线
# May be: NO_LINE, THIN, MEDIUM, DASHED, DOTTED, THICK, DOUBLE, HAIR, MEDIUM_DASHED, THIN_DASH_DOTTED, MEDIUM_DASH_DOTTED, THIN_DASH_DOT_DOTTED, MEDIUM_DASH_DOT_DOTTED, SLANTED_MEDIUM_DASH_DOTTED, or 0x00 through 0x0D.
borders.right = xlwt.Borders.THIN
borders.top = xlwt.Borders.THIN
borders.bottom = xlwt.Borders.THIN
borders.left_colour = 0x40      #指定上下左右的边框颜色为0x40
borders.right_colour = 0x40
borders.top_colour = 0x40
borders.bottom_colour = 0x40
style = xlwt.XFStyle()  # Create Style   #创建样式对象
style.borders = borders  # 将设置好的边框对象borders 加到样式对象style中。Add Borders to Style
style.font=font1
style0.borders = borders  # 将设置好的边框对象borders 加到样式对象style中。Add Borders to Style

# ws2=wb.sheet_by_name("分析")
# print("aa,ge",ws2.name)
# print("成都市滚滚滚",ws1.cell(2,2).value,type(ws1.cell(2,2).value),"aaa",ws1.cell(2,2).value.isdigit())

# if ws1.cell(0,2).value.isdigit():
#     print("这个是滚滚滚")

for i in range(ws1.nrows):
    # print("成都市",i,"bb",ws1.cell(i,2).value,type(ws1.cell(i,2).value),"aaa",ws1.cell(i,2).value.isdigit(),type(i))
    if ws1.cell(i,2).value.isdigit():
        # ws2.write(i,0,i+1,style0)
        ws2.write(i,0,ws1.cell(i,0).value,style0)
        ws2.write(i,1,ws1.cell(i,1).value,style0)
        ws2.write(i,nred+int(ws1.cell(i,2).value),1,style)
        ws2.write(i,nred+int(ws1.cell(i,3).value),1,style)
        ws2.write(i,nred+int(ws1.cell(i,4).value),1,style)
        ws2.write(i,nred+int(ws1.cell(i,5).value),1,style)
        ws2.write(i,nred+int(ws1.cell(i,6).value),1,style)
        ws2.write(i,nred+int(ws1.cell(i,7).value),1,style)
        ws2.write(i,nblue+int(ws1.cell(i,8).value),1,style)
    else:
        print("aaa",i+1)
    # ws2.write(i+1,0,i+1)
    # ws2.write(i+1,0,ws1.cell(i,0))
    # ws2.write(i+1,1,ws1.cell(i,1))
    # ws2.write(i+1,nred+ws1.cell(i,2),1)
    # ws2.write(i+1,nred+ws1.cell(i,3),1)
    # ws2.write(i+1,nred+ws1.cell(i,4),1)
    # ws2.write(i+1,nred+ws1.cell(i,5),1)
    # ws2.write(i+1,nred+ws1.cell(i,6),1)
    # ws2.write(i+1,nred+ws1.cell(i,7),1)
    # ws2.write(i+1,nred+ws1.cell(i,8),1)
for j in range(51):
    if j==0:
        ws2.col(j).width = 3000
    elif j==1:
        ws2.col(j).width = 2700
    else:
        ws2.col(j).width = 900
    # ws2.write(i+1, j, xlwt.Formula('SUM(A2,a,'i')')) # Should output "7" (A1[5] + A2[2])  第二行第二列，输出第一行数字之和
# wb2.save("双色球统计结果.xls")
wb2.save('双色球统计结果.xls')
# def charOrint(va):
#     if type(va)