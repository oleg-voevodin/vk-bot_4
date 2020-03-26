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


vk_session = vk_api.VkApi(token='')
longpoll = VkBotLongPoll(vk_session, '166545677')
vk = vk_session.get_api()


for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat:
        print('')
    elif event.type == VkBotEventType.MESSAGE_NEW and event.from_user:
        print("")
