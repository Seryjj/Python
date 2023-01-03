from telegram import Update
from cfg import TOKEN

from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello  {update.effective_user.first_name}')


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()



import telebot
from SEM9_BOT.cfg import TOKEN


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()	



# import telebot
# import cnfg
# import model
# bot = telebot.TeleBot(cnfg.TOKEN)

# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
# bot.reply_to(message, "Howdy, how are you doing?")


# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
# bot.reply_to(message, model.abc_delete(message.text))

# print('server run')
# bot.infinity_polling()


# def abc_delete(message):
# find_txt = 'абв'
# lst = [i for i in message.split() if find_txt not in i]
# return "".join(lst)




# import telebot


# def del_abv(text):
# text = text.split(' ')
# return ' '.join([i for i in text if 'абв' not in i])


# bot = telebot.TeleBot("5371200500:AAFDNMnE3UtL-TBKwY5vjdayGTn3FI89mGA")



# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
# bot.send_message(message.chat.id, del_abv(message.text))
# bot.send_message(message.chat.id, f'из исходной строки {message.text} \
# удалены все слова с "абв"')


# bot.infinity_polling()