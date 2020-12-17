# 在python中，对excel表格读，写，追加数据，用以下三个模块：
# 1、xlrd 读取excel表中的数据
# 2、xlwt 创建一个全新的excel文件,然后对这个文件进行写入内容以及保存。
# 3、xlutils 读入一个excel文件，然后进行修改或追加，不能操作xlsx，只能操作xls。
# 4、openpyxl：主要针对xlsx格式的excel进行读取和编辑。

# 一、读excel表
# 读excel要用到xlrd模块
# 1、导入模块  import xlrd
# 2、打开excel文件
# table = data.sheets()[0] #通过索引顺序获取
# table = data.sheet_by_index(0) #通过索引顺序获取
# table = data.sheet_by_name(u'Sheet1')#通过名称获取

# -------------------------------------------------------------------------------------------------------------------
# 代码如下：
# import xlrd
# data = xlrd.open_workbook(r"C:\Users\907968\Desktop\test.xlsx")
# table1 = data.sheets()[0]
# table2 = data.sheet_by_index(0)
# table3=data.sheet_by_name(u'Sheet1')
# print(table1)
# print(table2)
# print(table3)

# 返回：---------------------------------------------------------
#
# <xlrd.sheet.Sheet object at 0x0000000002F7F208>
# <xlrd.sheet.Sheet object at 0x0000000002F7F208>
# <xlrd.sheet.Sheet object at 0x0000000002F7F208>

# 3、获取行数和列数
# import xlrd
# data = xlrd.open_workbook(r"C:\Users\907968\Desktop\test.xlsx")
# table = data.sheets()[0]
# nrows = table.nrows
# ncols = table.ncols
# print("行数:%d\n列数:%d"%(nrows,ncols))

# 返回：----------------------------------
# 行数:13
# 列数:3

# 4、获取整行和整列的值，以列表形式返回
# rows = table.row_values(0)
# cols = table.col_values(0)
# print("rows:%s\ncols:%s"%(rows,cols))
#
# 返回：-------------------------------
# rows:['A1', 'B1', 'C1']
# cols:['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 'A13']
#
# 5、获取单元格数据
# cell_A1 = table.cell_value(0,0)
# cell_C4 = table.cell_value(3,2)
# print("A1:%s\nC4:%s"%(cell_A1,cell_C4))
#
# 返回：
#
# A1:A1
# C4:C4
#
# 还可以使用行列索引来获取单元格数据
#
# cell_A1 = table.row(0)[0].value
# cell_C4 = table.col(2)[3].value
# print("A1:%s\nC4:%s"%(cell_A1,cell_C4))
#
# 返回：
#
# A1:A1
# C4:C4

# 三、写excel操作
# 1、导入：
# import xlwt
#
# 2、创建workbook
# workbook = xlwt.Workbook(encoding='utf-8', style_compression=0)
# encoding:设置字符编码，一般要这样设置：w = Workbook(encoding=’utf-8’)，就可以在excel中输出中文了。默认是ascii
# style_compression:表示是否压缩，不常用。

# 3、创建一个sheet对象，一个sheet对象对应Excel文件中的一张表格
# sheet = workbook.add_sheet('test', cell_overwrite_ok=True)
# 其中的test是这张表的名字,cell_overwrite_ok，表示是否可以覆盖单元格，其实是Worksheet实例化的一个参数，默认值是False

# 4、向表中添加数据
# sheet.write(0, 0, 'EnglishName') # 其中的'0-行, 0-列'指定表中的单元，'EnglishName'是向该单元写入的内容
# sheet.write(1, 0, 'Marcovaldo')
# txt1 = '中文名字'
# sheet.write(0, 1, txt1)
# txt2 = '马可瓦多'
# sheet.write(1, 1, txt2)
#
# 5、保存
# workbook.save(r'e:\test1.xls')
#
# 6、单元格格式变更
# workbook = xlwt.Workbook()
# style = xlwt.XFStyle() # 初始化样式
# font = xlwt.Font() # 为样式创建字体
# font.name = 'Times New Roman'
# font.bold = True # 黑体
# font.underline = True # 下划线
# font.italic = True # 斜体字
# style.font = font # 设定样式
# worksheet.col(0).width = 3333  # 设置单元格宽度
#
# import datetime
# style.num_format_str = 'M/D/YY' # 输入一个日期到单元格 Other options: D-MMM-YY, D-MMM, MMM-YY, h:mm, h:mm:ss, h:mm, h:mm:ss, M/D/YY h:mm, mm:ss, [h]:mm:ss, mm:ss.0
# worksheet.write(0, 0, datetime.datetime.now(), style)
# 单元格添加一个公式
# worksheet.write(1, 0, xlwt.Formula('A1*B1')) # Should output "10" (A1[5] * A2[2])  第二行第一列，输出第一行数字乘积
# worksheet.write(1, 1, xlwt.Formula('SUM(A1,B1)')) # Should output "7" (A1[5] + A2[2])  第二行第二列，输出第一行数字之和
# 向单元格添加一个超链接
# worksheet.write(0, 0, xlwt.Formula('HYPERLINK("https://www.baidu.com";"百度")')) # 输出文本百度，为超链接第一行第一列
# 合并列和行
# worksheet.write_merge(0, 1, 0, 3, '合并从第一行到第二行，第一列到第四列') # Merges row 0's columns 0 through 3.
# worksheet.write_merge(2,3, 0, 3, '合并从第三行到第四行，第一列到第四列', style) # Merges row 1 through 2's columns 0 through 3.
设置单元格内容的对其方式:
#Alignment n. 结盟; 队列，排成直线; 校直，调整; [工] 准线;
#HORZ 水平的；地平式;
#GENERAL 普遍的; 大致的; 综合的; 总的，全体的;
#FILLED 满的; 填满的; 充气的; 加载的;
#JUSTIFIED adj.	有正当理由的，合理的; 事出有因的;
#DISTRIBUTED 分布式的;
#VERT n.	森林中的草木，绿色; 倾侧; 倾转;
# alignment = xlwt.Alignment() # 创建对其格式的对象 Create Alignment
# alignment.horz = xlwt.Alignment.HORZ_CENTER #我猜是左右的对其，水平居中 May be: HORZ_GENERAL, HORZ_LEFT, HORZ_CENTER, HORZ_RIGHT, HORZ_FILLED, HORZ_JUSTIFIED, HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED
# alignment.vert = xlwt.Alignment.VERT_CENTER #我猜是上下的对其 May be: VERT_TOP, VERT_CENTER, VERT_BOTTOM, VERT_JUSTIFIED, VERT_DISTRIBUTED
# style = xlwt.XFStyle() #创建样式对象 Create Style
# style.alignment = alignment # 将格式Alignment对象加入到样式对象Add Alignment to Style
# worksheet.write(0, 0, '单元居中', style)  #写入的时候调用样式style
# 10、为单元格议添加边框:

# import xlwt
# workbook = xlwt.Workbook()
# worksheet = workbook.add_sheet('小马过河')
# borders = xlwt.Borders()  # 创建边框对象Create Borders
# borders.left = xlwt.Borders.DASHED  #对边框对象进行操作，指定边框上下左右的边框类型为虚线
# # DASHED虚线
# # NO_LINE没有
# # THIN实线
# # May be: NO_LINE, THIN, MEDIUM, DASHED, DOTTED, THICK, DOUBLE, HAIR, MEDIUM_DASHED, THIN_DASH_DOTTED, MEDIUM_DASH_DOTTED, THIN_DASH_DOT_DOTTED, MEDIUM_DASH_DOT_DOTTED, SLANTED_MEDIUM_DASH_DOTTED, or 0x00 through 0x0D.
# borders.right = xlwt.Borders.DASHED
# borders.top = xlwt.Borders.DASHED
# borders.bottom = xlwt.Borders.DASHED
# borders.left_colour = 0x40      #指定上下左右的边框颜色为0x40
# borders.right_colour = 0x40
# borders.top_colour = 0x40
# borders.bottom_colour = 0x40
# style = xlwt.XFStyle()  # Create Style   #创建样式对象
# style.borders = borders  # 将设置好的边框对象borders 加到样式对象style中。Add Borders to Style
# worksheet.write(0, 0, '单元格内容', style)   #向单元格第一行第一列写入“单元格内容”，并使用创建好的样式对象style
# workbook.save('添加边框.xls')
# #创建边框对象，对边框对象进行操作，指定边框上下左右的边框类型为虚线等等，指定上下左右的边框颜色为0x40。指定上下左右的边框颜色为0x40，将设置好的边框对象borders 加到样式对象style中。Add Borders to Style，#向单元格第一行第一列写入“单元格内容”，并使用创建好的样式对象style
# 复制代码
# 回到顶部
# 11、为单元格设置背景色:
# #SOLID 固体; 立体图形; 立方体;

# import xlwt
# workbook = xlwt.Workbook()
# worksheet = workbook.add_sheet('小马过河')
# pattern = xlwt.Pattern() # 创建模式对象Create the Pattern
# pattern.pattern = xlwt.Pattern.SOLID_PATTERN # May be: NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
# pattern.pattern_fore_colour = 5 #设置模式颜色 May be: 8 through 63. 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta, 7 = Cyan, 16 = Maroon, 17 = Dark Green, 18 = Dark Blue, 19 = Dark Yellow , almost brown), 20 = Dark Magenta, 21 = Teal, 22 = Light Gray, 23 = Dark Gray, the list goes on...
# style = xlwt.XFStyle() # 创建样式对象Create the Pattern
# style.pattern = pattern # 将模式加入到样式对象Add Pattern to Style
# worksheet.write(0, 0, '单元格内容', style)#向单元格写入内容时使用样式对象style
# workbook.save('设置背景颜色.xls')


#
# 四、追加数据
# import xlrd
# import xlutils.copy
# data = xlrd.open_workbook(r'C:\Users\907968\Desktop\test222.xls')
# ws = xlutils.copy.copy(data)
# table=ws.get_sheet(0)
# table.write(0,3,'D1')
# ws.save(r'C:\Users\907968\Desktop\test222.xls')
#
# 追加前：
# A1 B1 C1
# 追加后：
# A1 B1 C1 D1

# 四、openpyxl对Excel的操作
# 创建一个工作薄：wb = openpyxl.Workbook()
# 新增一个sheet表单：wb.create_sheet('test_case')
# 保存case.xlsx文件：wb.save('cases.xlsx')
# 打开工作簿：wb = openpyxl.load_workbook('cases.xlsx')
# 选取表单：sh = wb['Sheet1']
# 读取第一行、第一列的数据：ce = sh.cell(row=1, column=1)
# 按行读取数据：row_data = list(sh.rows)
# 关闭工作薄：wb.close()
# 按列读取数据：columns_data = list(sh.columns)
# 写入数据之前，该文件一定要处于关闭状态
# 写入第一行、第四列的数据
# value = 'result'：sh.cell(row=1, column=4, value='result')
# 获取最大行总数、最大列总数：sh.max_row、sh.max_column
# del 删除表单的用法：del wb['sheet_name']
# remove
# 删除表单的用法：sh = wb['sheet_name']

# wb.remove(sh)
#-----------------------------------------------------------------------------------------
# 复制代码
# import openpyxl
# 创建一个工作簿
# wb = openpyxl.Workbook()
# 创建一个test_case的sheet表单
# wb.create_sheet('test_case')
# 保存为一个xlsx格式的文件
# wb.save('cases.xlsx')

# 8  # 读取excel中的数据
# 9  # 第一步：打开工作簿
# wb = openpyxl.load_workbook('cases.xlsx')
# 11  # 第二步：选取表单
# sh = wb['Sheet1']
# 13  # 第三步：读取数据
# 14  # 参数 row:行  column：列
# ce = sh.cell(row=1, column=1)  # 读取第一行，第一列的数据
# print(ce.value)

# 17  # 按行读取数据 list(sh.rows)
# print(list(sh.rows)[1:])  # 按行读取数据，去掉第一行的表头信息数据
# for cases in list(sh.rows)[1:]:
# case_id = cases[0].value
# case_excepted = cases[1].value
# case_data = cases[2].value
# print(case_excepted, case_data)

# 24  # 关闭工作薄
# wb.close()




# -------------------------------------------------------------------------------------------------------------------
# Pandas 库操作
# #方法一：默认读取第一个表单
# df=pd.read_excel('lemon.xlsx')#这个会直接默认读取到这个Excel的第一个表单
# data=df.head()#默认读取前5行的数据
# print("获取到所有的值:\n{0}".format(data))#格式化输出
#
# #方法二：通过指定表单名的方式来读取
# df=pd.read_excel('lemon.xlsx',sheet_name='student')#可以通过sheet_name来指定读取的表单
# data=df.head()#默认读取前5行的数据
# print("获取到所有的值:\n{0}".format(data))#格式化输出

# #方法三：通过表单索引来指定要访问的表单，0表示第一个表单
# #也可以采用表单名和索引的双重方式来定位表单
# #也可以同时定位多个表单，方式都罗列如下所示
# df=pd.read_excel('lemon.xlsx',sheet_name=['python','student'])#可以通过表单名同时指定多个
# # df=pd.read_excel('lemon.xlsx',sheet_name=0)#可以通过表单索引来指定读取的表单
# # df=pd.read_excel('lemon.xlsx',sheet_name=['python',1])#可以混合的方式来指定
# # df=pd.read_excel('lemon.xlsx',sheet_name=[1,2])#可以通过索引 同时指定多个
# data=df.values#获取所有的数据，注意这里不能用head()方法哦~
# print("获取到所有的值:\n{0}".format(data))#格式化输出

# ------------------------------------------------------------------------------------
# pandas操作Excel的行列
# 1：读取指定的单行，数据会存在列表里面

# #1：读取指定行
# df=pd.read_excel('lemon.xlsx')#这个会直接默认读取到这个Excel的第一个表单
# data=df.ix[0].values#0表示第一行 这里读取数据并不包含表头，要注意哦！
# print("读取指定行的数据：\n{0}".format(data))
# 得到的结果如下所示:

# 2：读取指定的多行，数据会存在嵌套的列表里面：
# df=pd.read_excel('lemon.xlsx')
# data=df.ix[[1,2]].values#读取指定多行的话，就要在ix[]里面嵌套列表指定行数
# print("读取指定行的数据：\n{0}".format(data))

# 3：读取指定的行列：
# df=pd.read_excel('lemon.xlsx')
# data=df.ix[1,2]#读取第一行第二列的值，这里不需要嵌套列表
# print("读取指定行的数据：\n{0}".format(data))

# 4：读取指定的多行多列值：
# df=pd.read_excel('lemon.xlsx')
# data=df.ix[[1,2],['title','data']].values#读取第一行第二行的title以及data列的值，这里需要嵌套列表
# print("读取指定行的数据：\n{0}".format(data))

# 5：获取所有行的指定列
# df=pd.read_excel('lemon.xlsx')
# data=df.ix[:,['title','data']].values#读所有行的title以及data列的值，这里需要嵌套列表
# print("读取指定行的数据：\n{0}".format(data))

# 6：获取行号并打印输出
# df=pd.read_excel('lemon.xlsx')
# print("输出行号列表",df.index.values)

# 输出结果是：
# 输出行号列表 [0 1 2 3]

# 7：获取列名并打印输出
# df=pd.read_excel('lemon.xlsx')
# print("输出列标题",df.columns.values)

# 运行结果如下所示：
# 输出列标题 ['case_id' 'title' 'data']

# 8：获取指定行数的值：
# 复制代码
# df=pd.read_excel('lemon.xlsx')
# print("输出值",df.sample(3).values)#这个方法类似于head()方法以及df.values方法
#
# 输出值
#  [[2 '输入错误的密码' '{"mobilephone":"18688773467","pwd":"12345678"}']
#  [3 '正常充值' '{"mobilephone":"18688773467","amount":"1000"}']
#  [1 '正常登录' '{"mobilephone":"18688773467","pwd":"123456"}']]
# 复制代码

# 9：获取指定列的值：
# df=pd.read_excel('lemon.xlsx')
# print("输出值\n",df['data'].values)

#-----------------------------------------------------------------------------------------------------------
# pandas处理Excel数据成为字典
# 实现的代码如下所示：

# df=pd.read_excel('lemon.xlsx')
# test_data=[]
# for i in df.index.values:#获取行号的索引，并对其进行遍历：
#     #根据i来获取每一行指定的数据 并利用to_dict转成字典
#     row_data=df.ix[i,['case_id','module','title','http_method','url','data','expected']].to_dict()
#     test_data.append(row_data)
# print("最终获取到的数据是：{0}".format(test_data))

# 最终获取到的数据是：
# [{'title': '正常登录', 'case_id': 1, 'data': '{"mobilephone":"18688773467","pwd":"123456"}'},
# {'title': '输入错误的密码', 'case_id': 2, 'data': '{"mobilephone":"18688773467","pwd":"12345678"}'},
# {'title': '正常充值', 'case_id': 3, 'data': '{"mobilephone":"18688773467","amount":"1000"}'},
# {'title': '充值输入负数', 'case_id': 4, 'data': '{"mobilephone":"18688773467","amount":"-100"}'}]