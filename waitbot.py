import requests
import vk_api
from random import randint as random
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import datetime
from time import sleep
#Отправка сообщения
def msgsend(msg1,msg2):
    if event.from_user: #Если написали в ЛС
        vk.messages.send(user_id=event.user_id,message=msg1 ,random_id = random(10000,100000))
                
    elif event.from_chat: #Если написали в Беседе
        vk.messages.send(chat_id=event.chat_id,message=msg2 ,random_id = random(10000,100000))

def log():
    today = datetime.datetime.today()
    file = open("my.log",'a')
    file.write(today.strftime("%d.%m.%Y %H:%M:%S") + ', Text from: '+str(event.user_id)+ ', Text: '+str(event.text))
    file.write("\n")
    file.close()
    print(today.strftime("%d.%m.%Y %H:%M:%S") + ' Text from: '+str(event.user_id)+ ' Text: '+str(event.text))

vk_session = vk_api.VkApi(token='')
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()



today = datetime.datetime.today()


for event in longpoll.listen():
    
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        log()
        
        strr = today.strftime("%d.%m.%Y %H:%M:%S") + ', Text from: '+str(event.user_id)+ ', Text: '+str(event.text) + " Status: Completed"
        #Слушаем longpoll, если пришло сообщение то:			        
        if event.text != "":
            msgsend("Бот находится на обслуживании, подождите немного)","Бот находится на обслуживании, подождите немного)")
            vk.messages.send(user_id=550760548,message= strr ,random_id = random(10000,100000))
