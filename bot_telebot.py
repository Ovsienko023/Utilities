import telebot
import requests
import json
import random
# from config import token
token = '1205575777:AAF7_nZpA6guaj0N29oRj5f_VHCSjHG4bfE'

bot = telebot.TeleBot(token)

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Go Memas', 'Расскажи анекдот')

hello = ['привет', 'хай', 'салам']
how_are_you = ['как ты?', 'как ты', 'как дела?', 'как дела']
you_bot = ['ты бот', 'бот', 'железка', 'робот']
why = ['почему?', 'почему']


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Вниманиеее, Марш!', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    print(message.json['chat']['last_name'],
            message.json['chat']['first_name'], 
            '\nText message:' , 
            message.json['text'])
    print()

    if message.text.lower() in hello:
        bot.send_message(message.chat.id, 'Привет, Бро')

    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай')

    elif message.text.lower() in how_are_you:
        stik_id = "CAACAgQAAxkBAANaXqnPGjm2fK_JzFp2ZFZx_-ZJMp4AAlMAA4Nq0BBBM4UbNgMorxkE"
        stik_id2 = "CAACAgQAAxkBAAIBqF6sNENCbJyQWGuFdNMB9KmQU08DAAJgAANdK6kBaJoptFkvrzwZBA"
        count = random.randint(0, 100)
        if count % 2 == 0:
            count += 1
            bot.send_sticker(message.chat.id, stik_id)
            
        else:
            count += 1
            bot.send_sticker(message.chat.id, stik_id2)

    elif message.text.lower() in why:
        stik_id = "CAACAgIAAxkBAAIBlV6sMGmZhTIIu6rr7xy9vptLupihAAJEAAMorh4Xx65tFgUyrO8ZBA"
        bot.send_sticker(message.chat.id, stik_id)   

    elif message.text == 'Go Memas':
        mem = requests.get('https://meme-api.herokuapp.com/gimme')
        mem = mem.json()['url']
        bot.send_photo(message.chat.id, mem)

    elif message.text == 'Go funny story':
        mem = requests.get('http://rzhunemogu.ru/RandJSON.aspx?CType=1')
        reg = mem.text.rstrip().split(':')[1:]
        reg = ''.join(reg)[1:-2]
        bot.send_message(message.chat.id, reg)

    elif message.text.lower() in you_bot:
        video_id = 'BAACAgIAAxkBAAIBQ16sH6iKy283jcz9juj_GhBOUebbAALFBQACWIZgSXGkiXDwOrHDGQQ'
        bot.send_video(message.chat.id, video_id)

    else:
        stik_id = "CAACAgIAAxkBAAIBaV6sK0uuvd9uAAGZtiUuHIWSZeUKogACLAADKK4eF-GCrBAafrCoGQQ"
        bot.send_sticker(message.chat.id, stik_id)
        bot.send_message(message.chat.id, 'Ты знаешь кто я?', reply_markup=keyboard1)



# @bot.message_handler(content_types=['sticker'])
# def send_stiker(message):
#     print(message)


# @bot.message_handler(content_types=['photo'])
# def send_stiker(message):
#     print(message)

# @bot.message_handler(content_types=['video'])
# def send_message(message):
#     print(message.chat.video_id)              
        
        
bot.polling()