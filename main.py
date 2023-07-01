import requests

from time import sleep
TOKEN = '6031625012:AAFdxBk9YBo_m2U4llpFUk854ZoLXTPWSZ0'

def get_updates(TOKEN):
    URL = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
    response = requests.get(URL)
    updates=response.json()['result']
    return updates
def sendMessage(chat_id:str, text:str):
    URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    kb1={
        'text':"DOG"
    }
    
    keyboard=[[kb1]]
    keyboard={
        'keyboard':keyboard,
        'resize_keyboard':True
    }
    parametrs={
        'chat_id':chat_id,
        'text':text,
        "reply_markup":keyboard
    }
    response=requests.post(URL,json=parametrs)
    return response.json()
print(sendMessage(get_updates(TOKEN)[-1]["message"]["chat"]['id'],'non'))
def sendPhoto(chat_id:str,photo:str):
    URL = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
    paramters = {
        'chat_id':chat_id,
        'photo':photo
        }
    response = requests.get(URL, params=paramters)
    return response.json()

# last_id = -1

# while True:
#     update = get_updates(TOKEN)
#     message_keys=update[-1]["message"].keys()
#     if "text" in message_keys:
#         print(1)
#         last_update = update[-1]
#         update_id = last_update["update_id"]
#         URL2="https://random.dog/woof.json"
#         response=requests.get(URL2)
#         a=response.json()
#         x=update
#         text = x[-1]['message']['text']
#         if last_id != update_id:
#             print(text)
#             if text=="DOG":
#                 photo = a["url"]
#                 chat_id = x[-1]["message"]["chat"]['id']
#                 sendPhoto(chat_id=chat_id, photo=photo)
#                 print("photo")

#         last_id =update_id
m=0
while True:
    update=get_updates(TOKEN)
    URL2="https://random.dog/woof.json"
    response=requests.get(URL2)
    a=response.json()
    x=update
    text = x[-1]['message']['text']
    if len(x)!=m:
        if text=="DOG":
            photo = a["url"]
            chat_id = x[-1]["message"]["chat"]['id']
            sendPhoto(chat_id=chat_id, photo=photo)
            print("photo")
    m=len(x)
# x=get_updates(TOKEN)
# print(len(x))
# while True:
#     x=get_updates(TOKEN)
#     if len(x)!=m:
#         text = get_updates(TOKEN)[-1]['message']['text']
#         chat_id = get_updates(TOKEN)[-1]["message"]["chat"]['id']
#         sendMessage(chat_id=chat_id, text=text)
#         print(text)
#         m=len(x)