from nsetools import Nse
import pandas as pd

nse = Nse()

df = pd.read_csv ('/home/sagarwal9698/stock_market_app/stock_list.csv')
list = df['Symbol']

q =[]
for i in list:
    q.append (nse.get_quote(i))

# data.drop(columns=['symbol', 'bcEndDate'])
# data.to_csv("data.csv")

# breakpoint()

useful_columns =[ 'symbol', 'companyName', 'lastPrice', 'pChange', 'dayHigh', 'dayLow', 'open', 'previousClose', 'totalSellQuantity', 'deliveryToTradedQuantity', 'high52', 'low52', 'basePrice',	'sellQuantity5', 'sellQuantity4', 'sellQuantity3', 'sellQuantity2', 'sellQuantity1', 'quantityTraded', 'totalTradedValue', 'totalBuyQuantity', 'averagePrice', 'buyPrice2', 'buyPrice1', 'buyPrice4', 'buyPrice3', 'deliveryQuantity', 'buyPrice5', 'sellPrice1', 'sellPrice2', 'totalTradedVolume', 'sellPrice3', 'sellPrice4', 'sellPrice5', 'buyQuantity4', 'buyQuantity3', 'buyQuantity2', 'buyQuantity1', 'buyQuantity5']

data = pd.DataFrame(data=q, columns=useful_columns)

dataToWrite = data[useful_columns]

from datetime import date
date_today = date.today()
file_name = date_today.strftime("data_" + "%d_%m_%Y" + ".csv")

dataToWrite.to_csv(file_name)

# data_read = pd.read_csv("data.csv")
# data_read.drop(columns=['symbol', 'bcEndDate'])
# data_read1 = data_read
# data_read1.to_csv("final.csv")
# data_read.head()
