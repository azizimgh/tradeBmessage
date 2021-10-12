from config import *
import requests

class send_handler:

    def __init__(self) -> None:
        self.key = send_blue_key
        self.sec= send_blue_sec
        self.url = send_url

    def send_message(self,message, number):
        try:
            payload = { "number": "+" + str(number),"content": message, }
            headers = {'sb-api-key-id': self.key,'sb-api-secret-key': self.sec ,  'Content-Type': 'application/json',}
            response = requests.request("POST", self.url, headers=headers, json=payload)
            return True
        except Exception as e:
            return e

