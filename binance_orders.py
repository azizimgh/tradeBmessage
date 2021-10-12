from binance.client import Client
from config import *

class binance_handler:
    def __init__(self):
        self.cl = Client(api_key ,api_secret)
    def buy_market(self,coin,amount):
        print("buy")
        try :
            self.cl.order_market_buy( symbol=coin.upper() +"USDT", quantity=amount)
            return False
        except Exception as e: return str(e)
    def sell_market(self,coin,amount):
        try:
            self.cl.order_market_sell(symbol=coin.upper() + "USDT", quantity=amount)
            return False
        except Exception as e:
            return str(e)
    def buy_limit(self,coin,amount,price):
        try:
            self.cl.order_limit_buy(symbol=coin.upper() + "USDT", quantity=amount,price=price)
            return False
        except Exception as e:
            return str(e)
    def sell_limit(self,coin,amount,price):
        try:
            self.cl.order_limit_sell(symbol=coin.upper() + "USDT", quantity=amount, price=price)
            return False
        except Exception as e:
            return str(e)