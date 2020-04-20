from nsetools import Nse
import pandas as pd


nse = Nse()

df = pd.read_csv ('/home/sagarwal9698/stock_market_app/stock_list.csv')

# all_stock_codes = nse.get_stock_codes()
# print(all_stock_codes)

# q =  nse.get_quote('ASHOKLEY')
# from pprint import pprint
# print(q)

list = df['Symbol']
print (list)

from pprint import pprint

q =[]


for i in list:
    q.append (nse.get_quote(i))
    
pprint(q)

fields =['pricebandupper', 'symbol', 'applicableMargin', 'bcEndDate', 'totalSellQuantity', 'adhocMargin', 'companyName', 'marketType', 'exDate', 'bcStartDate', 'css_status_desc', 'dayHigh', 'basePrice', 'securityVar', 'pricebandlower', 'sellQuantity5', 'sellQuantity4', 'sellQuantity3', 'cm_adj_high_dt', 'sellQuantity2', 'dayLow', 'sellQuantity1', 'quantityTraded', 'pChange', 'totalTradedValue', 'deliveryToTradedQuantity', 'totalBuyQuantity', 'averagePrice', 'indexVar', 'cm_ffm', 'purpose', 'buyPrice2', 'secDate', 'buyPrice1', 'high52', 'previousClose', 'ndEndDate', 'low52', 'buyPrice4', 'buyPrice3', 'recordDate', 'deliveryQuantity', 'buyPrice5', 'priceBand', 'extremeLossMargin', 'cm_adj_low_dt', 'varMargin', 'sellPrice1', 'sellPrice2', 'totalTradedVolume', 'sellPrice3', 'sellPrice4', 'sellPrice5', 'change', 'surv_indicator', 'ndStartDate', 'buyQuantity4', 'isExDateFlag', 'buyQuantity3', 'buyQuantity2''buyQuantity1', 'series', 'faceValue', 'buyQuantity5', 'closePrice', 'open', 'isinCode', 'lastPrice']
print(fields)
data = pd.DataFrame(data=q)
data.to_csv("data.csv")

data_read = pd.read_csv("data.csv")
data_read.drop(columns=['symbol', 'bcEndDate'])
data_read1 = data_read
data_read1.to_csv("final.csv")
data_read.head()
