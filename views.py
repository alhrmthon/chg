import os
import requests
import asyncio
import telebot
from pyrogram import Client,filters,enums

api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
token = os.environ.get("TOKEN")
app = Client("views", bot_token=token, api_id = api_id, api_hash = api_hash)

@app.message_handler(commands=['start'])
def start(message):
    Name = message.chat.first_name
    User = message.from_user.username 
    ID = message.chat.id
    bot.send_message(message.chat.id,f"""<strong>
Hi {Name}
- - - - - - - - -
Send Your Channel Username to increase Views! 
Your Username : @{User}                       
Your ID : {ID} 
- - - - - - - - - 
Developer : @VR_LA
</strong>""" ,parse_mode='html')
@app.message_handler(func=lambda m: True)
def Get(message):
    msg = message.text 
    class GI():
    	def __init__(self):
        	self.r = requests.session()
        	self.username = msg
        	self.token = ""
        	if self.username[0] == "@":
        		self.username = self.username.replace("@", "")
        	self.count = 0
        	self.main()

    	def main(self):
        	self.get_cookies()
        	bot.send_message(message.chat.id,f"""<strong>
[+] Sending request ..
</strong>""" ,parse_mode='html')
        	self.send_request()

    	def get_cookies(self):
        	headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:78.0) Gecko/20100101 Firefox/78.0"
        }
        	r2 = self.r.get("https://telegram.software",headers=headers)

        	self.XSRF_TOKEN = r2.cookies["XSRF-TOKEN"]
        	self.telegramsoftware_session = r2.cookies["telegramsoftware_session"]

        	"Scrap For Token"

        	r = self.r.get("https://telegram.software/", headers=headers)
        	try:
        	   	i = str(r.text)
        	   	token = i.split('<input type="hidden" name="_token" value="')[1]
        	   	token2 = token.split('">')[0]
        	   	self.token = token2
        	except:
        		bot.send_message(message.chat.id,f"""<strong>
[X] Error to get token
</strong>""" ,parse_mode='html')

    	def send_request(self):
        	url = "https://telegram.software/make_views_order"
        	headers = {
            "Host": "telegram.software",
            "User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:78.0) Gecko/20100101 Firefox/78.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Content-Type": "application/x-www-form-urlencoded",
            "Content-Length": "155",
            "Origin": "https://telegram.software",
            "Connection": "close",
            "Referer": "https://telegram.software/",
            "Cookie": f"XSRF-TOKEN={self.XSRF_TOKEN}; telegramsoftware_session={self.telegramsoftware_session}; _ga_LDCYE0PVMB=GS1.1.1640463457.3.0.1640463459.58; _ga=GA1.2.1949754996.1640447487; _gid=GA1.2.760731106.1640447487; _ym_uid=1640440888262602307; _ym_d=1640447487; _ym_isad=2",
            "Upgrade-Insecure-Requests": "1"
        }
        	data = f"_token={self.token}&test_mode=on&number-days=1&slct-day=-&slct-moth=-&slct-year=-&link-channel={self.username}&speed-hour=1800&views=1000"
        	r = self.r.post(url,headers=headers,data=data)
        	if r.text.find('You already used demo')>=0:
        		bot.send_message(message.chat.id,f"""<strong>
[!] Change Your channel username to skip block and use VPN
</strong>""" ,parse_mode='html')
        	else:
        	  bot.send_message(message.chat.id,f"""<strong>
[+] Done Send 1000 Views To Your Channel
</strong>""" ,parse_mode='html')
    GI()
pass
bot.polling(True)