import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from random import randint as random
import datetime
from time import sleep
import json
import re
from PIL import Image,ImageFont,ImageDraw
import requests

#Обновление базы данных
def upd(str):
    ls = json.load(open("/root/vkbot-env/bd.json", "r", encoding="utf-8"))
    ls.update(str)
    with open('/root/vkbot-env/bd.json', 'w', encoding="utf-8") as f:
        json.dump(ls, f, indent=4, ensure_ascii = False)
        f.close()

#И так ясно 
def loli_license(name,id0): #Процедура обработки фотографии
    num = random(0,37) #Рандомный номер исходника. Работает для исходников, сохраненных как 1.пнг, 2.пнг и т.д.
    img = Image.open('/root/vkbot-env/' + str(num) + ".png") #Путь - путь до исходника (сам введешь)
    draw = ImageDraw.Draw(img) #Создаем виртуальную модель для изменения  
    today = datetime.datetime.today() #Сегодняшняя дата 
    time = today.strftime("%d.%m.%Y")#тоже дата
    overtime = datetime.timedelta(60)
    endtime = today + overtime
    endtime = endtime.strftime("%d.%m.%Y")
    if num == 1: #Для каждого исходника свой набор координат (логично)
        font = ImageFont.truetype("/root/vkbot-env/DINNextCYR-BoldItalic.otf", 60) #Загружаем шрифт,тут же регулируем размер
        draw.text((600, 425),name,(0,0,0),font=font) #Пишет имя по координатам со шрифтом 
        draw.text((520, 595),time,(0,0,0),font=font) #Пишет дату по координатам
    if (num == num) and (num!=1): 
        font = ImageFont.truetype("/root/vkbot-env/1.ttf", 36) 
        draw.text((286, 110),name, (255, 255, 255), font=font) 
        draw.text((419, 154),time,(255,255,255),font=font) 
        draw.text((430, 198),endtime,(255,255,255),font=font) 
        font = ImageFont.truetype("/root/vkbot-env/1.otf", 26)
        draw.text((220, 371),id0,(255,255,255),font=font) 
    img.save('/root/vkbot-env/loli.png')
#Логи (поломанные)
def log(event):
    today = datetime.datetime.today()
    file = open("my.log",'w')
    file.write(today.strftime("%d.%m.%Y %H:%M:%S") + ', Text from: '+str(event.obj.from_id)+ ', Text: '+str(event.obj.text))
    file.write("\n")
    file.close()
    #print(today.strftime("%d.%m.%Y %H:%M:%S") + ' Text from: '+str(event.user_id)+ ' Text: '+str(event.text))

#Role play
def nrol(event,ls,n):
    if 'conv' in ls[str(event.obj.from_id)]:
        if str(event.obj.peer_id) in ls[str(event.obj.from_id)]['conv']:
            if 'role' not in ls[str(event.obj.from_id)]['conv'][str(event.obj.peer_id)]:
                ls[str(event.obj.from_id)]['conv'][str(event.obj.peer_id)].update({'role':n})
        else: 
            ls[str(event.obj.from_id)]['conv'].update({str(event.obj.peer_id):{'role':n}})
    else:
        ls[str(event.obj.from_id)].update({'conv':{str(event.obj.peer_id):{'role':n}}})

vk_session = vk_api.VkApi(token='')
longpoll = VkBotLongPoll(vk_session, '166545677')
vk = vk_session.get_api()

keyboard = VkKeyboard(one_time=True)
keyboard.add_button('Пак', color=VkKeyboardColor.POSITIVE)

while True:
    try:
        for event in longpoll.listen():
            log(event)
            if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat: #Conversation
                text = str(event.obj.text)
                today = datetime.datetime.today()
                strr = today.strftime("%d.%m.%Y %H:%M:%S") + ', Text from: '+str(event.obj.from_id)+ ', Text: '+str(event.obj.text) + " Status: Completed"
                #Start
                if event.obj.text == "Начать":
                    strr = "Ок, начинай сосать, дядя))0)0))0"
                    vk.messages.send(chat_id = int(event.chat_id),message = strr ,random_id = random(10000,100000),attachment = "photo-166545677_457248564")
                #help
                if (event.obj.text == "Помощь") or (event.obj.text == 'Помоги') or (event.obj.text == 'ддз помощь'): 
                    vk.messages.send(chat_id = int(event.chat_id),message ="Пишов нахуй",random_id = random(10000,100000), keyboard = keyboard.get_keyboard())
                    vk.messages.send(user_id=550760548,message = strr ,random_id = random(10000,100000))
                    ls = json.load(open("/root/vkbot-env/bd.json", "r", encoding="utf-8"))
                    if (str(event.obj.from_id) in ls) == False:
                        ids = {str(event.obj.from_id):{}}
                        upd(ids)        
                #///
                if event.obj.text == 'Пак' or event.obj.text == 'пак'  or event.obj.text == "[club166545677|Доски для твоего забора] Пак" or event.obj.text == "[club166545677|@lolidro4] Пак": 
          
                    if vk.groups.isMember(group_id = '166545677', user_id = event.obj.from_id) == 1:
                        print(vk.groups.isMember(group_id = '166545677', user_id = event.obj.from_id))
                        vk.messages.send(chat_id = int(event.chat_id),message ="https://yadi.sk/d/LIIC7R4_3ZrwDh  Вот ваш пак, хозяин",random_id = random(10000,100000))
                        vk.messages.send(user_id=550760548,message = strr ,random_id = random(10000,100000))
                        ls = json.load(open("/root/vkbot-env/bd.json", "r", encoding="utf-8"))
                        if (str(event.obj.from_id) in ls) == False:
                            ids = {str(event.obj.from_id):{}}
                            upd(ids)
                    else:
                        vk.messages.send(chat_id = int(event.chat_id),message ="Ты не подписался, но все равно просишь пак? Даю в последний раз...\n https://yadi.sk/d/LIIC7R4_3ZrwDh",random_id = random(10000,100000))
                #Place for triggers
                if "эрик" in text.lower():
                    s = "Эрик, ты чо охуел??!"
                    vk.messages.send(chat_id = int(event.chat_id),message = s ,random_id = random(10000,100000))
                #Licenze
                if text.lower().startswith('лицензия'): #Если текст начинается с 'Лицензия' любыми буковами
                    name = ''
                    id0 = str(event.obj.from_id)
                    try:
                        ls = text.split(' ') #Переводим текст в список, удаляя пробелы
                        for i in range(1,len(ls)):
                            name = name + str(ls[i]) + ' ' #Пользователь вводит два слова. Например Лицензия Няша Кавайяша, вот Няша Кавайняша и попадает в name
                    except:
                        vk.messages.send(user_id = event.obj.from_id,message = 'Чегось?', random_id = random(10000,100000))
                        continue
                    loli_license(name,id0) #Описанная выше процедурка
                    a = vk.photos.getMessagesUploadServer() #Подключаемся к загрузочнуму серверу 
                    b = requests.post(a['upload_url'], files={'photo': open('/root/vkbot-env/loli.png', 'rb')}).json() #Читаем хуйню, полученную после процедуры
                    c = vk.photos.saveMessagesPhoto(photo = b['photo'], server = b['server'], hash = b['hash'])[0]#Сохраняем на серве 
                    d = 'photo{}_{}'.format(c['owner_id'], c['id']) #Даем имя по канонам вк
                    vk.messages.send(chat_id = int(event.chat_id), attachment = d, random_id = random(10000,100000)) #Отправляем фотку хуле
                    ls = json.load(open("/root/vkbot-env/bd.json", "r", encoding="utf-8"))
                    if (str(event.obj.from_id) in ls) == False:
                                   ids = {str(event.obj.from_id):{}}
                                   upd(ids)
                #Up role
                if text.lower().startswith("ддз повысить"):
                    ls = json.load(open("/root/vkbot-env/bd.json", "r", encoding="utf-8"))
                    user_id = re.findall(r'ддз повысить \[id(\d*)\|.*]', text.lower())[0]
                    if (str(event.obj.from_id) in ls) == False:
                        ids = {str(event.obj.from_id):{}}
                        upd(ids)
                    if (str(user_id) in ls) == False:
                        ids = {str(event.obj.from_id):{}}
                        upd(ids)
                    if not('role' in ls[str(event.obj.from_id)]['conv'][str(event.obj.peer_id)]) or not(str(event.obj.peer_id) in ls[str(event.obj.from_id)]['conv']) or not('conv' in ls[str(event.obj.from_id)] ):
                        nrol(event,ls,0)
                    if not('role' in ls[str(user_id)]['conv'][str(event.obj.peer_id)]) or not(str(event.obj.peer_id) in ls[str(user_id)]['conv']) or not('conv' in ls[str(user_id)] ):
                        if 'conv' in ls[str(user_id)]:
                            if str(event.obj.peer_id) in ls[str(user_id)]['conv']:
                                ls[str(user_id)]['conv'][str(event.obj.peer_id)].update({'role':0})
                            else:
                                ls[str(user_id)]['conv'].update({str(event.obj.peer_id):{'role':0}})
                        else:
                            ls[str(user_id)].update({'conv':{str(event.obj.peer_id):{'role':0}}})
                    if ls[str(event.obj.from_id)]['conv'][str(event.obj.peer_id)]['role'] > ls[str(user_id)]['conv'][str(event.obj.peer_id)]['role']:
                        ls[str(user_id)]['conv'][str(event.obj.peer_id)]['role']+=1
                    with open('/root/vkbot-env/bd.json', 'w', encoding="utf-8") as f:
                        json.dump(ls, f, indent=4, ensure_ascii = False)
                        f.close()
                    vk.messages.send(chat_id=event.chat_id, message = "Вроде повысила...",random_id = random(10000,100000))
                            
          #kick
                if (event.obj.text).lower().startswith("ддз кик"): 
                    ls = json.load(open("/root/vkbot-env/bd.json", "r", encoding="utf-8"))
                    try:
                        if ls[str(event.obj.from_id)]['conv'][str(event.obj.peer_id)]['role'] > 0:
                            user_id = re.findall(r'ддз кик \[id(\d*)\|.*]', (event.obj.text).lower())[0]
                            vk.messages.send(chat_id=event.chat_id, message = "Покасики лохб",random_id = random(10000,100000))
                            vk.messages.removeChatUser(user_id=user_id,chat_id=event.chat_id)
                    except:
                        vk.messages.send(chat_id=event.chat_id, message = "Обзаведись сначала ролью, а потом уже людей кикай",random_id = random(10000,100000))
                #Role down           
                if text.lower().startswith("ддз понизить"):
                    ls = json.load(open("/root/vkbot-env/bd.json", "r", encoding="utf-8"))
                    user_id = re.findall(r'ддз понизить \[id(\d*)\|.*]', text.lower())[0]
                    if (str(event.obj.from_id) in ls) == False:
                        ids = {str(event.obj.from_id):{}}
                        upd(ids)
                    if (str(user_id) in ls) == False:
                        ids = {str(event.obj.from_id):{}}
                        upd(ids)
                    if not('role' in ls[str(event.obj.from_id)]['conv'][str(event.obj.peer_id)]) or not(str(event.obj.peer_id) in ls[str(event.obj.from_id)]['conv']) or not('conv' in ls[str(event.obj.from_id)] ):
                        nrol(event,ls,0)
                    if not('role' in ls[str(user_id)]['conv'][str(event.obj.peer_id)]) or not(str(event.obj.peer_id) in ls[str(user_id)]['conv']) or not('conv' in ls[str(user_id)] ):
                        if 'conv' in ls[str(user_id)]:
                            if str(event.obj.peer_id) in ls[str(user_id)]['conv']:
                                ls[str(user_id)]['conv'][str(event.obj.peer_id)].update({'role':0})
                            else:
                                ls[str(user_id)]['conv'].update({str(event.obj.peer_id):{'role':0}})
                        else:
                            ls[str(user_id)].update({'conv':{str(event.obj.peer_id):{'role':0}}})
                    if ls[str(event.obj.from_id)]['conv'][str(event.obj.peer_id)]['role'] > ls[str(user_id)]['conv'][str(event.obj.peer_id)]['role']:
                        ls[str(user_id)]['conv'][str(event.obj.peer_id)]['role']-=1
                    with open('/root/vkbot-env/bd.json', 'w', encoding="utf-8") as f:
                        json.dump(ls, f, indent=4, ensure_ascii = False)
                        f.close()
                    vk.messages.send(chat_id=event.chat_id, message = "ЪеЪ",random_id = random(10000,100000))
                #another trigger
                if ("аниме говно" in text.lower()) or ("аниме сосать" in text.lower()):
                    vk.messages.send(chat_id=event.chat_id, message = "Че сказал? Бан нахуй!",random_id = random(10000,100000))
                    vk.messages.removeChatUser(user_id=int(event.obj.from_id),chat_id=event.chat_id)
                #another trigger......
                if event.obj.from_id == 421020042:
                    vk.messages.send(chat_id=event.chat_id, message = "САДОВНИКОВ, твою мать!!!",random_id = random(10000,100000))
                    404427180
                #another trigger......
                if (event.obj.from_id == 404427180) and (random(1,10) == 5):
                    vk.messages.send(chat_id=event.chat_id, message = "привет не отвлекаю?",random_id = random(10000,100000))

                #admin registration
                if text.lower() == "ддз рег":
         
                    vk.messages.send(chat_id=event.chat_id, message = str(event.chat_id)+" "+str(event.obj.peer_id),random_id = random(10000,100000))
                    cc = dict(vk.messages.getConversationMembers(peer_id = event.obj.peer_id))
                    for i in cc["items"]:
                        if i["member_id"] == event.obj.from_id:
                            admin = i.get('is_admin', False)
                    if admin == True:
                        vk.messages.send(chat_id=event.chat_id, message ='Ну ты и сука',random_id = random(10000,100000))
                        ls = json.load(open("/root/vkbot-env/bd.json", "r", encoding="utf-8"))
                        if (str(event.obj.from_id) in ls) == False:
                            ids = {str(event.obj.from_id):{}}
                            upd(ids)
                        ls = json.load(open("/root/vkbot-env/bd.json", "r", encoding="utf-8"))
                        nrol(event,ls,5)
                        with open('/root/vkbot-env/bd.json', 'w', encoding="utf-8") as f:
                            json.dump(ls, f, indent=4, ensure_ascii = False)
                            f.close()
                #Role   
                if (event.obj.text).lower() == "ддз роль":
                    ls = json.load(open("/root/vkbot-env/bd.json", "r", encoding="utf-8"))
                    if (str(event.obj.from_id) in ls) == False:
                            ids = {str(event.obj.from_id):{}}
                            upd(ids)
                    ls = json.load(open("/root/vkbot-env/bd.json", "r", encoding="utf-8"))
                    if 'conv' in ls[str(event.obj.from_id)]:
                        if str(event.obj.peer_id) in ls[str(event.obj.from_id)]['conv']:
                            if 'role' in ls[str(event.obj.from_id)]['conv'][str(event.obj.peer_id)]:
                                vk.messages.send(chat_id=event.chat_id, message =str(ls[str(event.obj.from_id)]['conv'][str(event.obj.peer_id)]['role']),random_id = random(10000,100000))
                            else:
                                ls[str(event.obj.from_id)]['conv'][str(event.obj.peer_id)].update({'role':0})
                                vk.messages.send(chat_id=event.chat_id, message =str(ls[str(event.obj.from_id)]['conv'][str(event.obj.peer_id)]['role']),random_id = random(10000,100000))
                        else: 
                            ls[str(event.obj.from_id)]['conv'].update({str(event.obj.peer_id):{'role':0}})
                            vk.messages.send(chat_id=event.chat_id, message =str(ls[str(event.obj.from_id)]['conv'][str(event.obj.peer_id)]['role']),random_id = random(10000,100000))
                    else:
                        ls[str(event.obj.from_id)].update({'conv':{str(event.obj.peer_id):{'role':0}}})
                        vk.messages.send(chat_id=event.chat_id, message =str(ls[str(event.obj.from_id)]['conv'][str(event.obj.peer_id)]['role']),random_id = random(10000,100000))
                    with open('/root/vkbot-env/bd.json', 'w', encoding="utf-8") as f:
                        json.dump(ls, f, indent=4, ensure_ascii = False)
                        f.close()                



                print('Новое сообщение:')
                print('Для меня от: ', end='')
                print(str(event.obj.from_id))
                print('Текст:', event.obj.text)
                print()
                

            elif event.type == VkBotEventType.MESSAGE_NEW and event.from_user:
                text = str(event.obj.text)

                if text.lower().startswith("спокойной ночи") and str(event.obj.from_id) == "506520476":
                    vk.messages.send(user_id = int(event.obj.from_id),message = "Сладких снов, дорогой создатель! \n Я люблю тебя))" ,random_id = random(10000,100000))

                if text.lower().startswith('лицензия'): #Если текст начинается с 'Лицензия' любыми буковами
                    id0 = str(event.obj.from_id)
                    name = ''
                    try:
                        ls = text.split(' ') #Переводим текст в список, удаляя пробелы
                        for i in range(1,len(ls)):
                            name = name + str(ls[i]) + ' ' #Пользователь вводит два слова. Например Лицензия Няша Кавайяша, вот Няша Кавайняша и попадает в name
                    except:
                        vk.messages.send(user_id = event.obj.from_id,message = 'Чегось?', random_id = random(10000,100000))
                        continue
                    loli_license(name,id0) #Описанная выше процедурка
                    a = vk.photos.getMessagesUploadServer() #Подключаемся к загрузочнуму серверу 
                    b = requests.post(a['upload_url'], files={'photo': open('/root/vkbot-env/loli.png', 'rb')}).json() #Читаем хуйню, полученную после процедуры
                    c = vk.photos.saveMessagesPhoto(photo = b['photo'], server = b['server'], hash = b['hash'])[0]#Сохраняем на серве 
                    d = 'photo{}_{}'.format(c['owner_id'], c['id']) #Даем имя по канонам вк                    
                    vk.messages.send(user_id = int(event.obj.from_id), attachment = d, random_id = random(10000,100000)) #Отправляем фотку хуле
                    ls = json.load(open("/root/vkbot-env/bd.json", "r", encoding="utf-8"))
                    if (str(event.obj.from_id) in ls) == False:
                                   ids = {str(event.obj.from_id):{}}
                                   upd(ids)

                  

                if event.obj.text == "Начать":
                    nach = "Привет, я бот Юки. Могу подарить тебе скромный подарочек) Напиши мне \"Пак\" и забирай 10к лолек! \n \n Так же у меня есть замечательная функция, я могу выдать тебе именную лицензию! \n Напиши лицензия [Имя] [Фамилия] (В Именительном падеже) \n В квдратные скобки можешь вписать все, что захочешь)"
                    today = datetime.datetime.today()
                    strr = today.strftime("%d.%m.%Y %H:%M:%S") + ', Text from: '+str(event.obj.from_id)+ ', Text: '+str(event.obj.text) + " Status: Completed"
                    vk.messages.send(user_id = int(event.obj.from_id),message = nach ,random_id = random(10000,100000), keyboard = keyboard.get_keyboard())
                    vk.messages.send(user_id=550760548,message = strr ,random_id = random(10000,100000))
                    ls = json.load(open("/root/vkbot-env/bd.json", "r", encoding="utf-8"))
                    if (str(event.obj.from_id) in ls) == False:
                        ids = {str(event.obj.from_id):{}}
                        upd(ids)
                
                if event.obj.text == 'Пак' or event.obj.text == 'пак':
                    if vk.groups.isMember(group_id = '166545677', user_id = event.obj.from_id) == 1:
                        today = datetime.datetime.today()
                        strr = today.strftime("%d.%m.%Y %H:%M:%S") + ', Text from: '+str(event.obj.from_id)+ ', Text: '+str(event.obj.text) + " Status: Completed"
                        vk.messages.send(user_id = int(event.obj.from_id),message ="https://yadi.sk/d/LIIC7R4_3ZrwDh  Вот ваш пак, хозяин",random_id = random(10000,100000))
                        vk.messages.send(user_id=550760548,message = strr ,random_id = random(10000,100000))
                        ls = json.load(open("/root/vkbot-env/bd.json", "r", encoding="utf-8"))
                        if (str(event.obj.from_id) in ls) == False:
                            ids = {str(event.obj.from_id):{}}
                            upd(ids) 
                    else:
                        vk.messages.send(user_id = int(event.obj.from_id),message ="Ты не подписался, но все равно просишь пак? Даю в последний раз...\n https://yadi.sk/d/LIIC7R4_3ZrwDh",random_id = random(10000,100000))
                
                if event.from_group:
                    continue                
                
                else:
                    today = datetime.datetime.today()
                    strr = today.strftime("%d.%m.%Y %H:%M:%S") + ', Text from: '+str(event.obj.from_id)+ ', Text: '+str(event.obj.text) + " Status: Completed"
                    vk.messages.send(user_id = int(event.obj.from_id),message ="Простите, я вас не поняла... Напишите Пак или Начать",random_id = random(10000,100000))


            elif event.type == VkBotEventType.GROUP_JOIN:
                try:
                    ls = json.load(open("/root/vkbot-env/bd.json", "r", encoding="utf-8"))
                    if (str(event.obj.user_id) in ls) == False:
                        ids = {str(event.obj.user_id):{}}
                        upd(ids)
                    vk.messages.send(user_id = int(event.obj.user_id),message ="Добро пожаловать в мою уютную группу, семпай!!! Напиши Начать, чтобы узнать обо мне побольше",random_id = random(10000,100000))
                    
              
                except TypeError:
                    continue

            elif event.type == VkBotEventType.GROUP_LEAVE:
                try:
                    vk.messages.send(user_id = 506520476,message ="ливнул *id{}".format(event.obj.user_id),random_id = random(10000,100000))
                    ls = json.load(open("/root/vkbot-env/bd.json", "r", encoding="utf-8"))
                    if (str(event.obj.user_id) in ls) == False:
                        ids = {str(event.obj.user_id):{}}
                        upd(ids)
                    
                    vk.messages.send(user_id = int(event.obj.user_id),message ="Пожалуйста, не уходи!!! Напиши мне, что я сделала не так и я постараюсь исправиться...",random_id = random(10000,100000))
                    
                      
                except:
                    continue



            elif event.type == VkBotEventType.MESSAGE_REPLY:
                print('Новое сообщение:')
                print('От меня для: ', end='')
                print(event.obj.peer_id)
                print('Текст:', event.obj.text)
                print()
    
            else:
                print(event.type)
                print()
    except:
        continue
