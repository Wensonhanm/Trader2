# -*- coding: utf-8 -*-
# '''
#    zw_tur.py
#    tur海龟策略
#
# '''
import sys;
sys.path.append("zwQuant/source/")

import numpy as np
import pandas as pd

#zwQuant
import zwSys as zw
import zwTools as zwt
import zwQTBox as zwx
import zwQTDraw as zwdr
import zwBacktest as zwbt
import zwStrategy as zwsta
import zw_talib as zwta

#=======================    
  
#zwQuant/source/zwStrategy.py

     
    
def macdx(qx):
    # '''
    #  MACD策略01
    #  MACD称为指数平滑异同平均线
    # 当 macd>0，买入；
    # 当 macd<0，卖出
    # 默认参数示例：
    # qx.staVars=[12,26,'2014-01-01','']
    #
    # '''
    stknum=0;
    xtim,xcod=qx.xtim,qx.stkCode
    dprice=qx.xbarWrk['dprice'][0];
    dcash=qx.qxUsr['cash'];
    dnum0=zwx.xusrStkNum(qx,xcod)
    #
    xk=qx.xbarWrk['macd'][0];
    #xk=qx.xbarWrk['msign'][0];
    #xk=qx.xbarWrk['mdiff'][0];
    
    
    if xk>0:
        if dnum0==0:
            stknum = int(dcash*qx.stkKCash /dprice);#dsum=stknum*kprice
            #stknum = 500
            #print(xtim,stknum,dnum,'++b,%.2f,%.2f,%.2f,$,%.2f,%.2f' %(dprice,dlow,dup,kprice,dsum))    
            #print(xtim,stknum,'++xd',xcod,dprice,x9,x1)    
    elif (xk<0):
            #stknum = -500
            stknum = -1
            #stknum = -1;dsum=dnum*kprice
            
    if stknum!=0:
        #print(xtim,stknum,'xd',xcod,dprice,x9,x1)    
        pass;
        
    return stknum    
          

def macdx_dataPre(qx,xnam0,ksgn0):
    # '''
    # MACD策略, 数据预处理函数
    #
    # Args:
    #     qx (zwQuantX): zwQuantX数据包
    #     xnam0 (str)：函数标签
    #     ksgn0 (str): 价格列名称，一般是'adj close'
    #     '''

    zwx.sta_dataPre0xtim(qx,xnam0);
    #----对各只股票数据，进行预处理，提高后期运算速度
    ksgn,qx.priceCalc,qx.priceBuy=ksgn0,ksgn0,ksgn0  #'adj close';
    for xcod in zw.stkLibCode:
        d20=zw.stkLib[xcod];
        
        #  计算交易价格kprice和策略分析采用的价格dprice,kprice一般采用次日的开盘价
        #d20['dprice']=d20['open']*d20[ksgn]/d20['close']
        #d20['kprice']=d20['dprice'].shift(-1)
        d20['dprice']=d20['close']
        d20['kprice']=d20['dprice']
        #
        d=qx.staVars[0];d2=qx.staVars[1];
        d20=zwta.MACD(d20,d,d2,'close');
        #d20['macd1n']=d20['macd'].shift(1)
        #d20['msign1n']=d20['msign'].shift(1)
        #
        zw.stkLib[xcod]=d20;
        if qx.debugMod>0:
            print(d20.tail())    
            #---
            fss='tmp\\'+qx.prjName+'_'+xcod+'.csv'
            d20.to_csv(fss)   
    #
    #print(d20.tail())    
    #xxx
    
#-------------------
   
def bt_endRets(qx):            
    #---ok ，测试完毕
    # 保存测试数据，qxlib，每日收益等数据；xtrdLib，交易清单数据
    #qx.qxLib=qx.qxLib.round(4)
    qx.qxLib.to_csv(qx.fn_qxLib,index=False,encoding='utf-8')
    qx.xtrdLib.to_csv(qx.fn_xtrdLib,index=False,encoding='utf-8')
    qx.prQLib()
    #
    #-------计算交易回报数据
    zwx.zwRetTradeCalc(qx)
    zwx.zwRetPr(qx)
    
    #-------绘制相关图表，可采用不同的模板
    # 初始化绘图模板：dr_quant3x
    zwdr.dr_quant3x_init(qx,12,8);
    #  设置相关参数
    xcod=zw.stkLibCode[0];ksgn=qx.priceBuy;
    #xcod='glng';ksgn=qx.priceBuy;
    #kmid8=[['aeti',ksgn],['egan',ksgn],['glng',ksgn,'ma_5','ma_30'],['simo',ksgn,'ma_5','ma_30']]   
    #kmid8=[[xcod,ksgn,'xhigh','xlow']]   
    #kmid8=[[xcod,ksgn,'macd','msign']]   
    mstr1,mstr2,mstr3='macd','msign','mdiff'
    kmid8=[[xcod,ksgn,mstr1,mstr2,mstr3]]   
    #
    #kmid8=[[xcod,ksgn]]   
    # 绘图
    zwdr.dr_quant3x(qx,xcod,'val',kmid8,'')
    # 可设置，中间图形窗口的标识
    #qx.pltMid.legend([]);
    #
    print('')
    print('每日交易推荐')
    print('::xtrdLib',qx.fn_xtrdLib)
    print(qx.xtrdLib.tail())
    #print(qx.xtrdLib)


#==================main
#--------init，设置参数
#rss='\\zwdat\\cn\\day\\'
rss='dat\\'
xlst=['600401']   #600401,*ST海润,*SThr 
qx=zwbt.bt_init(xlst,rss,'macd',10000);

#
#---设置策略参数


#qx.staVars=[35,15,'2014-01-01','']  #  30,15,=14339.67,43.40 %
qx.staVars=[12,26,'2015-01-01','']  #  30,15,=14339.67,43.40 %
qx.debugMod=1
#qx.staFun=tur10; #---绑定策略函数&运行回溯主函数
#qx.staFun=zwsta.tur10; #---绑定策略函数&运行回溯主函数
qx.staFun=macdx; #---绑定策略函数&运行回溯主函数
#---根据当前策略，对数据进行预处理
#zwsta.tur10_dataPre(qx,'sta00','close')
#zwsta.tur10_dataPre(qx,'tur10','close')
macdx_dataPre(qx,'macd','close')
#----运行回溯主程序

zwbt.zwBackTest(qx)
#----输出回溯结果
bt_endRets(qx)
# '''
# ,最终资产价值 ,回报率
#
# 30,10,=9325.77, -6.74 %
# 20,10,=$12407.49, 24.07 %
# 10,10,=$12544.90,25.45 %
# 5,10,=$15057.73, 50.58 %
# 5,5,=$19511.12，95.11 %
# '''