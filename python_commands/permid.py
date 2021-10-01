# importing all required libraries
import telebot
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events

# get your api_id, api_hash, token
# from telegram as described above
api_id = 20700
api_hash = '4f979ebf06573ee562c4d9949c443d94'
token = '2011412066:AAGMkWoYRWZEFb7URPxaCWAyiIRGh-oGy00'
message = "Working..."

# your phone number
phone = '+989100072052'

# creating a telegram session and assigning
# it to a variable client
client = TelegramClient('mobile', api_id, api_hash)

# connecting and building the session
client.connect()

# in case of script ran first time it will
# ask either to input token or otp sent to
# number or sent or your telegram id
if not client.is_user_authorized():
    client.send_code_request(phone)

    # signing in the client
    client.sign_in(phone, input('Enter the code: '))
import time
try:
    count = 1 
    while True:
    # receiver user_id and access_hash, use
    # my user_id and access_hash for reference
    # sending message using telegram client
        client.send_message("shiiiit776679", message, parse_mode='html')   
        time.sleep(10)

except Exception as e:

    # there may be many error coming in while like peer
    # error, wrong access_hash, flood_error, etc
    print(e);

# disconnecting the telegram session
client.disconnect()


