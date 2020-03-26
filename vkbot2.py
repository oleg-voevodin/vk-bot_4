import requests
import vk_api
from random import randint as random
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import datetime
from time import sleep
import json

#Отправка сообщения
def msgsend(msg1,msg2):
    if event.from_user: #Если написали в ЛС
        vk.messages.send(user_id=event.user_id,message=msg1 ,random_id = random(10000,100000),keyboard = keyboard.get_keyboard())
    elif event.from_chat: #Если написали в Беседе
        vk.messages.send(chat_id=event.chat_id,message=msg2 ,random_id = random(10000,100000))

def log():
    today = datetime.datetime.today()
    file = open("my.log",'a')
    file.write(today.strftime("%d.%m.%Y %H:%M:%S") + ', Text from: '+str(event.user_id)+ ', Text: '+str(event.text))
    file.write("\n")
    file.close()
    print(today.strftime("%d.%m.%Y %H:%M:%S") + ' Text from: '+str(event.user_id)+ ' Text: '+str(event.text))

def upd(str):
    ls = json.load(open("bd.json", "r", encoding="utf-8"))
    ls.update(str)
    with open('bd.json', 'w', encoding="utf-8") as f:
        json.dump(ls, f, indent=4, ensure_ascii = False)
        f.close()

vk_session = vk_api.VkApi(token='')
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

keyboard = VkKeyboard(one_time=False)
keyboard.add_button('Пак', color=VkKeyboardColor.POSITIVE)


today = datetime.datetime.today()


for event in longpoll.listen():
    ls = json.load(open("bd.json", "r", encoding="utf-8"))
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        log()
        strr = today.strftime("%d.%m.%Y %H:%M:%S") + ', Text from: '+str(event.user_id)+ ', Text: '+str(event.text) + " Status: Completed"
        #Слушаем longpoll, если пришло сообщение то:			        
        if event.text == 'Пак' or event.text == 'пак':
            msgsend("https://yadi.sk/d/LIIC7R4_3ZrwDh  Вот ваш пак, хозяин","...") 
            vk.messages.send(user_id=550760548,message = strr ,random_id = random(10000,100000))
            ls = json.load(open("bd.json", "r", encoding="utf-8"))
            if (str(event.user_id) in ls) == False:
                ids = {str(event.user_id):{}}
                upd(ids)        
                    
        elif event.text == 'Начать':
            msgsend("Привет, я стремный бот, написанный ручками владельца и отрубающийся без причины)0))))0))0. Меня зовут Юки и все что я могу - это дать вам пак с лолями. Напишите пак и получите ссылочку","...")
            ls = json.load(open("bd.json", "r", encoding="utf-8"))
            if (str(event.user_id) in ls) == False :
                ids = {str(event.user_id):{}}
                upd(ids)
            
        else:
            msgsend("Напишите Пак, чтобы получить ваш пак с лольками","...")

                