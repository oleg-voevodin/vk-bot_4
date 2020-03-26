#!/usr/bin/python
# -*- coding: utf-8 -*-
import vk_api
import requests
import time
import re
import time
import datetime as dt
global MESFILE, LOGIN, TOKEN, PASSWORD
RANDOM_NUM = time.time()
file_h = open('ProcessHistory.cfg', 'a')
file_h.write('--------------------------------------------------------------\n')
file_h.write('Start                                 //coded by SaliRr\n')
now = dt.datetime.now()
connect= requests.get('https://vk.com/')
status =connect.status_code
print('Connection to  https://vk.com/ :')
print('%s' % status)
file_h.write('Connection to  https://vk.com/ : {} \n'.format(status))
#открытие необходимых файлов - текст сообщений
try:
    message_r = open('Текст сообщения.txt', 'r')
    file_h.write('message_r opened')
    MESFILE = message_r.read()
    message_r.close()
    file_h.write('message_r closed')
except IOError:
    message_r = open('Текст сообщения.txt', 'w')
    file_h.write('message_r created')
    message_r.write('Тестовое сообщение!')
    message_r.close()
    file_h.write('message_r opened')
#открытие необходимых файлов - настройка аутентификации
try:
    login_r = open('login settings.txt', 'r')
    nums = login_r.read().splitlines()
    LOGIN = nums[0]
    PASSWORD = nums[1]
    TOKEN = nums[2]
    login_r.close()
except IOError:
    login_r = open('login settings.txt', 'w')
    login_r.write('''ЛОГИН/НОМЕР_ТЕЛЕФОНА
ПАРОЛЬ
ТОКЕН_ПРИЛОЖЕНИЯ
''')
    login_r.close()

#аутентификация
if status != 200:
    print('Ethernet connection Failed')
    file_h.write('Ethernet connection Failed\n')
    file_h.write('Check your Ethernet connection\n')
else:
    s = requests.Session()
    vk = vk_api.VkApi(login=LOGIN,
                    password=PASSWORD,
                    token= TOKEN,                                 
                    api_version='5.92',
                    app_id=6121396,
                    scope=215989462,)
    try:
        vk.auth(token_only=True)
        print('Authentication : Success')
        file_h.write('Authentication : Success\n')

    except vk_api.AuthError as error_msg:
        print('Authentication : Error')
        file_h.write('Authentication : Error\n')
        file_h.write('Error name %s' % error_msg)
        input("Press Enter to exit...")

profile_get=vk.method('account.getProfileInfo')
print('User :%s' % profile_get.get('first_name'))
file_h.write('User information: %s \n' % profile_get)
#рассылка лс
def user_post(url, list_ids=[]):                          #list_ids - кортёж id
    for i in list_ids:
        try:
            vk.method('messages.send', values = {
                'user_ids' : i ,
                'random_id':  RANDOM_NUM,
                'message' : MESFILE,                                #filechange
                'attachment' : url,                            #filechange
            },)
            print('Personal method/messages.send ', 'users_id = ', i)
            file_h.write('{}.{}.{}. {}:{}:{} Personal send method/messages.send ids= {} message= {} attachment= {} \n'.format(now.day, now.month, now.year, now.hour, now.minute, now.second, i, MESFILE, url))
        except vk_api.exceptions.ApiError as error_msg_l:
            file_h.write('{}.{}.{}. {}:{}:{} Error:{} \n'.format(now.day, now.month, now.year, now.hour, now.minute, now.second, error_msg_l))
            continue
        time.sleep(3.5)
    return None

#рассылка по беседам с последующим закрепом
def conversation_post(url, start, stop, pin, pause):
    for i in range(start, stop):
        try:
            mes_id = vk.method('messages.send', values = {
                'user_ids' : i ,
                'random_id':  RANDOM_NUM,
                'peer_id' : 2000000000 + i, 
                'message' : MESFILE,                                #filechange
                'attachment' : url,                            #filechange
            },)
            print('Conv method/messages.send ', 'dilog_id =', i, 'message_id =', mes_id)
            file_h.write('{}.{}.{}. {}:{}:{} Conversation_post method/messages.send peer_id= {} message= {} attachment= {} \n'.format(now.day, now.month, now.year, now.hour, now.minute, now.second, 2000000000 + i, MESFILE, url))
            time.sleep(pause)
        except vk_api.exceptions.ApiError as error_msg_l:
            file_h.write('{}.{}.{}. {}:{}:{} Error:{} \n'.format(now.day, now.month, now.year, now.hour, now.minute, now.second, error_msg_l))
        if pin == 'Y':
            try:
                vk.method('messages.pin', values={
                    'peer_id' : 2000000000 + i,
                    'message_id' : mes_id,
                })
                print('Conv_pin method/messages.pin ', 'message_id =', mes_id)
                file_h.write('{}.{}.{}. {}:{}:{} Conversation_post сonv_pin method/messages.pin message_id= {} peer_id= {}\n'.format(now.day, now.month, now.year, now.hour, now.minute, now.second, mes_id, 2000000000 + i))
            except vk_api.exceptions.ApiError as error_msg_l:
                file_h.write('{}.{}.{}. {}:{}:{} Error:{} \n'.format(now.day, now.month, now.year, now.hour, now.minute, now.second, error_msg_l))
        else:
            continue
    return None

#постинг на стены
def wall_post(id_owner, url, num):
    i= 0 
    while i < num:
        try:
            post_id = vk.method('wall.post', values={
                'owner_id': id_owner,
                'message': MESFILE,
                'attachments': url,
            })
            i+=1
            print('Wall_p method/wall.post ', 'post_id =', post_id)
            file_h.write('{}.{}.{}. {}:{}:{} Wall_post Wall_p method/wall.post owner_id= {} message= {} attachment= {} posts number= {}\n'.format(now.day, now.month, now.year, now.hour, now.minute, now.second, id_owner, MESFILE, url, num))
            time.sleep(5) 
        except vk_api.exceptions.ApiError as error_msg_l:
            file_h.write('{}.{}.{}. {}:{}:{} Error:{} \n'.format(now.day, now.month, now.year, now.hour, now.minute, now.second, error_msg_l))
            print("Somethig went wrong")
            break     
    return None

#пост онлайн друзьям
#получаю список друзей онлайн
#ипользую функцию user_post
def post_to_online(your_id, online_url):
    try:
        list_f = vk.method('friends.getOnline', values={
            'user_id': your_id,
            'order': 'random',
        })
        print('Online spam')
        for i in list_f:
            try:
                vk.method('messages.send', values = {
                        'user_ids' : i ,
                        'random_id':  RANDOM_NUM,
                        'message' : MESFILE,                                #filechange
                        'attachment' : online_url,                            #filechange
                    },)
                print('PersonalOnline method/messages.send ', 'users_id =', i)
                file_h.write('{}.{}.{}. {}:{}:{} Post_to_online PersonalOnline method/messages.send owner_id= {} message= {} attachment= {} user_ids= {} \n'.format(now.day, now.month, now.year, now.hour, now.minute, now.second, your_id, MESFILE, online_url, i))
            except vk_api.exceptions.ApiError as error_msg_l:
                file_h.write('{}.{}.{}. {}:{}:{} Error:{} \n'.format(now.day, now.month, now.year, now.hour, now.minute, now.second, error_msg_l))
        time.sleep(3.5)
    except vk_api.exceptions.ApiError as error_msg_l:
        file_h.write('{}.{}.{}. {}:{}:{} Error:{} \n'.format(now.day, now.month, now.year, now.hour, now.minute, now.second, error_msg_l))
        print("Somethig went wrong")
        file_h.write('{}.{}.{}. {}:{}:{} posting_conf: Cancle \n'.format(now.day, now.month, now.year, now.hour, now.minute, now.second))
    return list_f

#спам в беседы от имени сообщества
def group_spam(start, stop, token, url):
    url = 'https://api.vk.com/method/messages.send'
    response = requests.get('https://api.vk.com/method/messages.send')
    status = response.status_code
    for i in range(start, stop):
        requests.post(url, data={
            'message': MESFILE,
            'peer_id': 2000000000 + i,
            'v' : '5.67',
            'access_token': token,
            'attachment': url,
        })
        print('Group method/messages.send ', 'id = ', i)
        file_h.write('{}.{}.{}. {}:{}:{} Group_spam Group method/messages.send v : 5.67 message= {} token_code= {} attachment= {} peer_id= {} \n'.format(now.day, now.month, now.year, now.hour, now.minute, now.second, MESFILE, token, url, 2000000000 + i))
        time.sleep(0.5)
    return status

menu = True
while menu == True:
    '''
    posting_ls=input('Рассылка сообщений в ЛС[Y/N]:')
    if posting_ls == 'Y':
        print('Впишите необходимые данные!\n')
        ls_mes = str(input('Сообщение*:'))
        ls_ur = str(input('Медиавложение:'))
        ls_list_ids =(input('ID-шники пользователей*:'))
        user_post(mes=ls_mes, url=ls_ur, list_ids=ls_list_ids)
        print('Done!')
        file_h.write('{}.{}.{}. {}:{}:{} posting_ls: Done \n'.format(now.day, now.month, now.year, now.hour, now.minute, now.second))
    else:
        continue
        '''
    posting_conf=input('Рассылка сообщений в беседы(от имени пользователя)[Y/N]:')
    if posting_conf == 'Y':
        print('Впишите необходимые данные!\n')
        #conf_mes = str(input('Сообщение*:'))
        cond_url = str(input('Медиавложение:'))
        conf_srart = int(input('От (номер беседы)*:'))
        conf_stop = int(input('До (номер беседы)*:'))
        conf_pin = str(input('С закрепом/Без[Y/N]*:'))
        conf_pause = int(input('Пауза(сек)*:'))
        conversation_post(url=cond_url, start=conf_srart, stop=conf_stop, pin=conf_pin, pause=conf_pause)
        print('Done!')
        file_h.write('{}.{}.{}. {}:{}:{} posting_conf: Done \n'.format(now.day, now.month, now.year, now.hour, now.minute, now.second))
    else:
        file_h.write('{}.{}.{}. {}:{}:{} posting_conf: Cancle \n'.format(now.day, now.month, now.year, now.hour, now.minute, now.second))

    post_to_online_ls=input('Рассылка сообщений в ЛС(всем online друзьям)[Y/N]:')
    if post_to_online_ls == 'Y':
        print('Впишите необходимые данные!\n')
        on_id = int(input('ID страницы*:'))
        #on_mes = str(input('Сообщение*:'))
        on_url = str(input('Медиавложение:'))
        post_to_online(your_id=on_id, online_url=on_url)
        print('Done!')
        file_h.write('{}.{}.{}. {}:{}:{} post_to_online_ls: Done \n'.format(now.day, now.month, now.year, now.hour, now.minute, now.second))
    else:
        file_h.write('{}.{}.{}. {}:{}:{} post_to_online_ls: Cancle \n'.format(now.day, now.month, now.year, now.hour, now.minute, now.second))

    group_spam_м=input('Рассылка сообщений в беседы(от имени сообщества)[Y/N]:')
    if group_spam_м == 'Y':
        print('Впишите необходимые данные!\n')
        g_token = str(input('Токен сообщества*:'))
        #g_mes = str(input('Сообщение*:'))
        g_url = str(input('Медиавложение:'))
        g_srart = int(input('От (номер беседы)*:'))
        g_stop = int(input('До (номер беседы)*:'))
        group_spam(start=g_srart, stop=g_stop, token=g_token, url=g_url)
        print('Done!')
        file_h.write('{}.{}.{}. {}:{}:{} group_spam_м: Done \n'.format(now.day, now.month, now.year, now.hour, now.minute, now.second))
    else:
        file_h.write('{}.{}.{}. {}:{}:{} group_spam_м: Cancle \n'.format(now.day, now.month, now.year, now.hour, now.minute, now.second))

    wall_post_м=input('Размещение записей[Y/N]:')
    if wall_post_м == 'Y':
        print('Впишите необходимые данные!\n')
        w_id_owner = g_mes = int(input('ID страницы:'))
        #w_mes = str(input('Сообщение*:'))
        w_url = str(input('Медиавложение:'))
        w_num = int(input('Кол-во записей*:'))
        wall_post(id_owner=w_id_owner, url=w_url, num=w_num)
        print('Done!')
        file_h.write('{}.{}.{}. {}:{}:{} wall_post_м: Done \n'.format(now.day, now.month, now.year, now.hour, now.minute, now.second))
        repeat = str(input('Начать заново?[Y/N]:'))
        if repeat == 'Y':
            menu = True
        else:
            menu = False  
    else:
        file_h.write('{}.{}.{}. {}:{}:{} wall_post_м: Cancle \n'.format(now.day, now.month, now.year, now.hour, now.minute, now.second))
        repeat = str(input('Начать заново?[Y/N]:'))
        if repeat == 'Y':
            menu = True
        else:
            menu = False  
            print('Handle closed')       
        file_h.write('Handle closed \n')
                

if __name__ == '__main__':
    input("Press Enter to exit...")
else:
    print("import\n status : Success")
    
    