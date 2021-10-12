from flask import Flask, request
import json
from send_blue_handler import send_handler
from binance_orders import *

sender = send_handler()
buyer = binance_handler()
app = Flask(__name__)

def respond_back(state_of_order,number):
    print(state_of_order)
    if not state_of_order: sender.send_message("Order placed successfully", number)
    else: sender.send_message("Order not placed for this reason" + str(state_of_order), number)

def execute_message(message,number):
    print(message)
    splitted = message.split(" ")
    print(splitted)
    #checking for market orders
    if len(splitted) == 3 and splitted[0].strip().lower() == "buy":
        respond_back(buyer.buy_market(splitted[1].strip().upper(),float(splitted[2].strip().lower())),number)
    if len(splitted) == 3 and splitted[0].strip().lower() == "sell":
        respond_back(buyer.buy_market(splitted[1].strip().upper(),float(splitted[2].strip().lower())),number)
    # checking for limit orders
    if len(splitted) == 4 and splitted[0].strip().lower() == "buy":
        respond_back(buyer.buy_limit(splitted[1].strip().upper(), float(splitted[2].strip().lower()),float(splitted[3].strip().lower())),number)
    if len(splitted) == 4 and splitted[0].strip().lower() == "sell":
        respond_back(buyer.sell_limit(splitted[1].strip().upper(), float(splitted[2].strip().lower()),float(splitted[3].strip().lower())),number)

@app.route('/', methods=['GET'])
def index():  return ('<h1>Trade by message is up and running</h1>', 200, None)

@app.route('/order', methods=['POST'])
def catch_webhook():
    try:
        content, from_number = json.loads(request.data)['content'], json.loads(request.data)['from_number']
        execute_message(content,from_number)
        return { "code" : "succes" }
    except Exception as e: return  { "code": str(e)}

if __name__ == '__main__':
    app.run(host ='0.0.0.0')
