import requests
from telegram import Update


def valut(val):



    res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
# for i in res.values():
#     print(i)

    text=res['Date'][:10],res['Valute'][val]['Name'], res['Valute'][val]['Value']/res['Valute'][val]['Nominal']
    text2=''

    for i in text:
        text2 +=str(i)
        text2 +=' '
    return text2




# print(valut('USD'))