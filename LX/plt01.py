import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as plf
import matplotlib

# matplotlib.use('qt4agg')
from matplotlib.font_manager import *

myfont = FontProperties(fname=r"C:\Users\贵州场外\AppData\Roaming\Python\Python37\site-packages\matplotlib\mpl-data\fonts\ttf\SimHei.ttf")
chinabank=pd.read_csv('chinabank.csv',encoding = "utf-8",index_col=0)
# chinabank=pd.read_csv('chinabank.csv')
# chinabank=chinabank.ioc[:,:1]
chinabank.head()
print('gegweg',chinabank.head())
# chinabank.index=pd.to_datetime(\chinabank)
# chinabank.close()
print("open is ",chinabank.open)
close=chinabank.close
print("close is ",close)
fig = plt.figure(1)
# rcParams 是绘图参考字典，axes.unicode_minus默认为TRUE，对部分字体不兼容，导致符号显示异常，因此，置为FALSE
plt.rcParams['axes.unicode_minus']=False
# plt.xlim(-2，10)           # 设置x轴的最小值，最大值
# plt.ylim(-1,10)   # 设置y轴的最小值，最大值
plt.plot(close,c='b',ls='solid',lw=1,marker='*')            #plot关键字参数color(或c)用来设置线的颜色. 颜色名称或简写b: blue；g: green；；r: red；c: cyan；m: magenta；y: yellow;k: black;w: white
plt.plot(chinabank.open,c='r',ls='--',lw=1.5,marker='o')    #plot plot方法的关键字参数linestyle(或ls)用来设置线的样式。可取值为：-, solid     --, dashed     -., dashdot   :, dotted      '', ' ', None
plt.plot(chinabank.high,c='y',ls='-.',lw=2,marker='.')      # plot方法的关键字参数linewidth(或lw)可以改变线的粗细，其值为浮点数
plt.plot(chinabank.low,c='k',ls='dotted',lw=2.5,marker='h') #plot关键字参数可以用来设置marker的样式.   '.': point marker    ',': pixel marker      'o': circle marker      'v': triangle_down marker      '^': triangle_up marker
plt.annotate('emphasize point',xy=(4,2.7),xytext=(15,-15),textcoords='offset pixels',arrowprops=dict(arrowstyle='<|-', connectionstyle="arc3,rad=.2"))  # 离散点标注，x表示横坐标的单位数量
plt.text(2, 2.8, 'This is some text',fontdict={'size': 16, 'color': 'r'})  # 标注文字 (2,2.8)这个点是文字左上角的坐标
plt.legend(loc='upper left')                                # 设置图例,需在画完图后设置，否则之后画的图的图例无法显示
# legend方法可接受一个loc关键字参数来设定图例的位置，可取值为数字或字符串：
#      0: ‘best'
#      1: ‘upper right'
#      2: ‘upper left'
#      3: ‘lower left'
#      4: ‘lower right'
#      5: ‘right'
#      6: ‘center left'
#      7: ‘center right'
#      8: ‘lower center'
#      9: ‘upper center'
#      10: ‘center'

plt.xticks(rotation=60)             # rotation 设置x标签文字的旋转角度
plt.title("中国银行股票历史行情报价",loc='right',fontproperties=myfont)
# plt.show()

mpf.candlestick_ohlc(ax,quotes,width=0.7,colorup='r',colordown='green')