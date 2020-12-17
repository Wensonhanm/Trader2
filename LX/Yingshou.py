# 导入库文件
import xlrd

# 打开Excel文件读取数据
data = xlrd.open_workbook('20190731.xls')
#查看文件中包含sheet的名称
data.sheet_names()
# 得到第一个工作表，或者通过索引顺序 或 工作表名称
table = data.sheets()[0]
table = data.sheet_by_index(0)
table = data.sheet_by_name(u'含中间人费用新表')

# 获取行数和列数
nrows = table.nrows
ncols = table.ncols

# 获取整行和整列的值（数组）
i=10
table.row_values(i)
table.col_values(i)
print("表格行共 ",nrows,"行")
print("表格列共 ", ncols, "列")

# 循环行,得到索引的列表
for rownum in range(table.nrows):
    print(table.row_values(rownum))

# 单元格
cell_A1 = table.cell(2,4).value
cell_C4 = table.cell(2,3).value
print("A1:%s\nC4:%s"%(cell_A1,cell_C4))

#4、获取整行和整列的值，以列表形式返回
rows = table.row_values(0)
cols = table.col_values(0)
print("rows:%s\ncols:%s"%(rows,cols))
# 分别使用行列索引
cell_A1 = table.row(0)[0].value

print("cell_A1 is ",table.row(0)[0].value,"行")