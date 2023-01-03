import telebot
from random import randint
from random import choice
from cfg import TOKEN
import time

import req





bot = telebot.TeleBot(TOKEN)
candys = dict()
enable_game = dict()
turn = dict()

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Выбери /game для игры или /currency для актуального курса валют с сайта ЦБ РФ")


@bot.message_handler(commands=['currency'])
def send_welcome(message):
	bot.reply_to(message, "/USD - доллары, /EUR - евро, /CNY - юани, /ALL - все валюты")

@bot.message_handler(commands=['USD'])
def send_welcome(message):
	bot.send_message(message.chat.id, req.valut('USD'))  

@bot.message_handler(commands=['EUR'])
def send_welcome(message):
	bot.send_message(message.chat.id, req.valut('EUR'))  

@bot.message_handler(commands=['CNY'])
def send_welcome(message):
	bot.send_message(message.chat.id, req.valut('CNY'))     


@bot.message_handler(commands=['ALL'])
def send_welcome(message):
	 
    bot.send_message(message.chat.id, req.valut('EUR'))  
    bot.send_message(message.chat.id, req.valut('USD'))
    bot.send_message(message.chat.id, req.valut('CNY'))  
    bot.send_message(message.chat.id, req.valut('AUD'))
    bot.send_message(message.chat.id, req.valut('AZN'))  
    bot.send_message(message.chat.id, req.valut('GBP'))
    bot.send_message(message.chat.id, req.valut('AMD'))  
    bot.send_message(message.chat.id, req.valut('BYN'))
    bot.send_message(message.chat.id, req.valut('BGN'))  
    bot.send_message(message.chat.id, req.valut('BRL'))
    bot.send_message(message.chat.id, req.valut('HUF'))  
    bot.send_message(message.chat.id, req.valut('HKD'))
    bot.send_message(message.chat.id, req.valut('DKK'))  
    bot.send_message(message.chat.id, req.valut('INR'))
    bot.send_message(message.chat.id, req.valut('KZT'))  
    bot.send_message(message.chat.id, req.valut('CAD'))
    bot.send_message(message.chat.id, req.valut('KGS'))  
    bot.send_message(message.chat.id, req.valut('MDL'))
    bot.send_message(message.chat.id, req.valut('HUF'))  
    bot.send_message(message.chat.id, req.valut('NOK'))
    bot.send_message(message.chat.id, req.valut('PLN'))  
    bot.send_message(message.chat.id, req.valut('RON'))
    bot.send_message(message.chat.id, req.valut('XDR'))  
    bot.send_message(message.chat.id, req.valut('TJS'))
    bot.send_message(message.chat.id, req.valut('TRY'))  
    bot.send_message(message.chat.id, req.valut('TMT'))
    bot.send_message(message.chat.id, req.valut('UZS'))  
    bot.send_message(message.chat.id, req.valut('UAH'))    
    bot.send_message(message.chat.id, req.valut('CZK'))  
    bot.send_message(message.chat.id, req.valut('SEK'))
    bot.send_message(message.chat.id, req.valut('CHF'))  
    bot.send_message(message.chat.id, req.valut('ZAR'))
    bot.send_message(message.chat.id, req.valut('KRW'))  
    bot.send_message(message.chat.id, req.valut('JPY'))


def handle_game_proc(message):
    global enable_game
    try:
        if enable_game[message.chat.id] and 1 <= int(message.text) <= 28:
            return True
        else:
            return False
    except KeyError:
        enable_game[message.chat.id] = False
        if enable_game[message.chat.id] and 1 <= int(message.text) <= 28:
            return True
        else:
            return False


@bot.message_handler(commands=['game'])
def send_welcome(message):
    global turn, candys, enable_game
    bot.reply_to(message, "Поехали!")
    time.sleep(1)
    bot.send_message(message.chat.id,  'Правила игры: на столе лежит 117 конфет. Играют два игрока делая ход друг после друга. Первый ход определяется броском монеты. За один ход можно забрать не более чем 28 конфет. Побеждает игрок, сделавший последний ход.')

    candys[message.chat.id] = 117
    turn[message.chat.id] = choice(['Бот', message.chat.first_name])
    bot.send_message(message.chat.id, f'Бросок монетки определил, что первый ход делает {turn[message.chat.id]}')
    enable_game[message.chat.id] = True
    
    if turn[message.chat.id] == 'Бот':
        take = randint(1, candys[message.chat.id] % 29)
        candys[message.chat.id] -= take
        bot.send_message(message.chat.id, f'Бот взял {take}')
        bot.send_message(message.chat.id,
                         f'Осталось {candys[message.chat.id]}')
        turn[message.chat.id] = message.chat.first_name
    bot.send_message(message.chat.id,  "Какое количество конфет возьмёшь ты?")

@bot.message_handler(func=handle_game_proc)
def game_process(message):

    global candys, turn, enable_game

    if turn[message.chat.id] == message.chat.first_name:

        if candys[message.chat.id] > 28:
            candys[message.chat.id] -= int(message.text)

            bot.send_message(message.chat.id,
                             f'Осталось {candys[message.chat.id]}')

            if candys[message.chat.id] > 28:
                take = randint(1, 28)
                candys[message.chat.id] -= take
                bot.send_message(message.chat.id,
                                 f'Бот взял {take}')
                bot.send_message(message.chat.id,
                                 f'Осталось {candys[message.chat.id]}')
                bot.send_message(message.chat.id,  "Ход бота закончен. Твой ход")
                if candys[message.chat.id] <= 28:
                    bot.send_message(message.chat.id, f'{message.chat.first_name} Win')
                    enable_game[message.chat.id] = False
            else:
                bot.send_message(message.chat.id, 'Бот Win')
                enable_game[message.chat.id] = False
        else:
            bot.send_message(message.chat.id, 'Бот Win')
            enable_game[message.chat.id] = False


bot.infinity_polling()


