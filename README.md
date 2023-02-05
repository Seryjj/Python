<!-- # Python



Долполнительные материалы с занятий

Ольга Авдонина: n = int(input())
for i in range (n-1):
print((-3) ** i, end = ',')
print((-3) ** (i+1))


Ольга Авдонина: slov = {}
n = int(input())
for i in range (1,n + 1):
slov[i] = 3 * i + 1
print(slov)


Ольга Авдонина: str1 = input()
str2 = input()
count1 = str1.count(str2)
print(count1)

Vladislav Isaev: a = input()
b = input()
count = 0
for i in range(len(a)):
if a[i:i+len(b)] == b:
count += 1
print(count)
print(a.count(b))


Vladislav Isaev: a = input()
b = input()
count = 0
for i in range(len(a)):
if a[i:i+len(b)] == b:
count += 1
print(count)
print(a.count(b))


Vladislav Isaev: with open('file.txt','r') as f:
a = f.read().split('\n')
print(a)


Vladislav Isaev: mass = ['ssss', 'sngujn556', 44]
types = [str(type(i)) for i in mass]
if "<class 'int'>" in types or "<class 'float'>" in types:
print('Yes')
else:
print('No')



Vladislav Isaev: mass = ["123", "234", "123", "567"]
a = "123"

try:
mass.remove(a)
print((mass.index(a))+1)
except ValueError:
print(-1)


if mass.count(a) < 2:
print(-1)
else:
mass.remove(a)
print((mass.index(a))+1)


Vladislav Isaev: def dividers(a: int, uniq: bool = False) -> list[int]:
""""Возвращает список простых делителей числа.
uniq = True вернет список уникальных делителей"""
i = 2
dividers = []
while a != 1:
while a % i == 0:
dividers.append(i)
a //= i
i += 1
if uniq:
return list(set(dividers))
else:
return dividers


Vladislav Isaev: from math import pi


def format_by_mask(num: float, accuracy: float) -> float:
""""форматирует число по заданной маске"""
accuracy = str(accuracy)
accuracy = len(accuracy[accuracy.find('.')+1::])
return float(f'{pi:0.{accuracy}f}') # f'a:0.3f'

Vladislav Isaev: import random
candys = 117


def input_candy():
global candys
while True:
move = int(input('Введите конфеты '))
if move > 0 and move < 29 and move <= candys:
candys -= move
break
else:
print('Столько взять нельзя')


def bot_take():
global candys
move = random.randint(1, 28)
print(f'Бот взял {move}')
candys -= move


print(f'На столе лежит {candys} конфет')
players = ['Пользователь', "Компьютер"]
move = random.choice(players)
print(f'Первым ходит - {move}')
while True:
if move == 'Пользователь':
input_candy()
print(f'Осталось {candys}')
move = "Компьютер"
else:
bot_take()
print(f'Осталось {candys}')
move = 'Пользователь'
if candys < 29:
print(f'Победил {move}')
break



Vladislav Isaev: def is_victory(field):
vin = False
combs = [[0, 1, 2],
[3, 4, 5],
[6, 7, 8],
[0, 3, 6],
[1, 4, 7],
[2, 5, 8],
[0, 4, 8],
[2, 4, 6]]
for pos in combs:
if field[pos[0]] == field[pos[1]] == field[pos[2]]:
vin = True
break
return vin


def spare(field):
count = 0
for i in field:
if type(i) == str:
count += 1
if count == 9:
return True
else:
return False


field = [1, 2, 3, 4, 5, 6, 7, 8, 9]

players = ['Пользователь', "Компьютер"]
move = choice(players)
print(f'Первым ходит - {move}')
print('-'*10)
show_field()
print('-'*10)
Vladislav Isaev: while True:
if move == 'Пользователь':
print('-'*10)
input_pos()
show_field()
print('-'*10)
move = "Компьютер"
if is_victory(field):
print('Пользователь победил')
break
else:
bot_move()
print('Бот сделал ход')
show_field()
print('-'*10)
move = 'Пользователь'
if is_victory(field):
print('Робот победил')
break
if spare(field):
print('Ничья')
break

Олег Бульденков: c = 'house=дом car=машина men=человек tree=дерево'
ListC = c.split(' ')
# ListC = list(c.items(' '.join(i for i in c.split(' '))))
a = {'house': 'дом', 'car': 'машина', 'men': 'человек', 'tree': 'дерево'}
b = list(a.items())
print(b)
print(ListC)
d = tuple(map(lambda x: tuple(x.split('=')), ListC))
# ListD = list(d.items(' '.join(i for i in d.split(' '))))
print(d)
Сергей М: Олег, в чат запиши, пожалуйста.
Vladislav Isaev: # citys = 'Москва,Уфа,Вологда,Тула,Владивосток,Хабаровск'
# a = list(map((lambda x: x if len(x) > 5 else '-'), citys.split(',')))
# print(','.join(a))




Vladislav Isaev: import telebot
import req

bot = telebot.TeleBot("5371200500:AAFDNMnE3UtL-TBKwY5vjdayGTn3FI89mGA")


@bot.message_handler(commands=['help'])
def send_info(message):
bot.send_message(message.chat.id, "Бот для получения информации курса валют")
info = 'Доступные команды \n \
/valute all - получить коды всех валют \n \
/valute all_v - получить курс всех валют \n \
/valute <код валюты> - получить конкретную валюту'
bot.send_message(message.chat.id, info)


@bot.message_handler(commands=['valute'])
def send_currency(message):
mode = message.text.split()[1]
if mode == 'all':
bot.send_message(message.chat.id, req.available_valute())
elif mode == 'all_v':
bot.send_message(message.chat.id, req.available_valute(True))
else:
bot.send_message(message.chat.id, req.valute(mode))


bot.infinity_polling()
Vladislav Isaev: import requests


def available_valute(curr=False):
res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
valute_keys = list(res['Valute'].keys())
valute_info = 'Cписок доступных валют: \n'
if curr:
for i in valute_keys:
valute_info += f'{i} - {res["Valute"][i]["Name"]} - {res["Valute"][i]["Value"]}' + '\n'
return valute_info
else:
for i in valute_keys:
valute_info += f'{i} - {res["Valute"][i]["Name"]}' + '\n'
return valute_info


def valute(code):
res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
valute_keys = list(res['Valute'].keys())
if code in valute_keys:
return f'{res["Valute"][code]["Name"]} - {res["Valute"][code]["Value"]}'
else:
return 'Неправильный код валюты' -->