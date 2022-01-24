from binance.client import Client
from binance.enums import *


api_key = ##enter your credential
secret_key = ##enter your credential
client = Client(api_key,secret_key)

#Get alert from file
f = open('Alert','r')
lines = f.readlines()
line = lines[-1]
direction = line.split()[0]
# print(direction)

#Get data from Market data endpoint
avg_price = client.get_avg_price(symbol='BNBUSDT')
print('Current Price'+avg_price["price"][0:6])

#Get data from Account endpoint
BNB_Balance = client.get_asset_balance(asset='BNB')
print(BNB_Balance['free'][0:5])
USDT_Balance = client.get_asset_balance(asset='USDT')
print(USDT_Balance['free'][0:6])
BNB_Aomount = str(float(USDT_Balance['free'])/float(avg_price["price"]))
print(BNB_Aomount[0:5])

#Order placing
if direction == 'buy':
    print('buy')
    order = client.create_order(
    symbol='BNBUSDT',
    side=SIDE_BUY,
    type=ORDER_TYPE_LIMIT,
    timeInForce=TIME_IN_FORCE_GTC,
    quantity=BNB_Aomount[0:5],
    price='%s'%(avg_price["price"][0:6]))
if direction == 'sell':
    print("sell")
    order = client.create_order(
    symbol='BNBUSDT',
    side=SIDE_SELL,
    type=ORDER_TYPE_LIMIT,
    timeInForce=TIME_IN_FORCE_GTC,
    quantity=BNB_Balance['free'][0:5],
    price='%s'%(avg_price["price"][0:6]))





# if alert:
#     file=open('data','w+')
#     file.close()

#Creating Log
print("Order created")
f = open('Log','r+')
lines = f.readlines()
f.write('Order created at price %s\n'%(avg_price))
f.close()

print("Sending Email")
f = open('Log','r+')
lines = f.readlines()
f.write('Sending Email\n')
f.close()

fi = open('Full_Log','r+')
fi_lines = fi.readlines()
fi.write('Order created at price %s\n'%(avg_price))
fi.write('Sending Email\n')
fi.close()

exec(open('SendEmail.py').read())
