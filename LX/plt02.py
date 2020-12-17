import os

import requests
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

# %matplotlib inline

# 获取微软(MSFT)的日图历史K线
data = requests.get('https://api.trochil.cn/v1/usstock/history',
# data = requests.get('https://api.trochil.cn/v1/cnstock/markets',
                    params={
                        'symbol': 'MSFT',
                        'start_date': '2018-01-01',
                        'end_date': '2020-11-17',
                        # 'apikey': os.getenv("4b79f90b6de3898cc5f5beae6273948f")  # 使用您的API密钥
                        'apikey':"4b79f90b6de3898cc5f5beae6273948f"
                    })
# print('11，is',data.text)
df = pd.DataFrame.from_records(data.json()["data"])
print('11，is',df.to_excel)
df["datetime"] = pd.to_datetime(df["datetime"])
df.set_index("datetime", inplace=True)
df.head()

df2 = df["2020-11"]

# chinabank=pd.read_csv('chinabank.csv',encoding = "utf-8",index_col=0)
chinabank=pd.read_csv('chinabank.csv',encoding = "utf-8")
chinabank.head()
df3=chinabank

print('21，is',df3[0:3])
# print('220，is',df3['datetime'])
# # print('221，is',df3.iloc[2,1])
# # print('222，is',df3.iloc[2,2])
# # print('223，is',df3.iloc[2,3])
# # print('224，is',df3.iloc[2,4])
# print('31，is',type(df3[0:3]))
df3["datetime"] = pd.to_datetime(df3["datetime"])

df3.set_index("datetime", inplace=True)

mpf.plot(df3, type="candle", title="Candlestick for MSFT", ylabel="price($)")