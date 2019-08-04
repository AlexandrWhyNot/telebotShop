import telebot
import const
from telebot import types
import sqlite3
import range
import time
import subprocess
import os
import re
import string
import threading
from threading import Thread
import requests


bot = telebot.TeleBot(const.token_bot)
city = dict()
tovar_d = dict()
ves_d = dict()
solo = dict()
ban = dict()
ph = dict()
streat = list()
my_streat = dict()


@bot.message_handler(commands=['start'])
def start_message(message):
        city.clear()
        tovar_d.clear()
        ves_d.clear()
        solo.clear()
        ph.clear()
        del streat[:]
        my_streat.clear()
        print(ban)
        if(message.from_user.first_name in ban) and (ban[message.from_user.first_name] == 3):
                baaaan("sad")
        else:                
                name = message.from_user.first_name
                markup = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton(text="Львов", callback_data="Львов")
                button2 = types.InlineKeyboardButton(text="Киев", callback_data="Киев")
                button3 = types.InlineKeyboardButton(text="Одесса", callback_data="Одесса")
                markup.add(button1, button2, button3)
                bot.send_message(message.chat.id, text = "Привет, " + str(name) + ", Добро пожаловать в наш Добро🆂🅷🅾️🅿️. Есть все что тебе нужно, осталось только подумать чего желаешь! Выберите город, и действия далие.", reply_markup=markup)
        
        

       
@bot.callback_query_handler(func=lambda c: (c.data == "Львов" or c.data == "Киев") or (c.data == "Одесса" or c.data == "mainmanu"))
def inline(c):
        cid = c.message.chat.id
        mid = c.message.message_id
        if c.data == "Львов":
                city[c.from_user.first_name] = "lvov"
        elif c.data == "Киев":
                city[c.from_user.first_name] = "kyiv"
        elif c.data == "Одесса":
                city[c.from_user.first_name] = "odessa"
        elif c.data == "mainmanu":
                keyboardmenu = types.InlineKeyboardMarkup(row_width=2)
                first_butt = types.InlineKeyboardButton(text="Правила", url="https://telegra.ph/Pravila-07-22-3")
                sec_butt = types.InlineKeyboardButton(text="Помощь", url='t.me/alex_kotenko')
                th_butt = types.InlineKeyboardButton(text="Оператор", url='t.me/Underbhoomi')
                f_buttom = types.InlineKeyboardButton(text="Список позиций", callback_data="positions")
                keyboardmenu.add(first_butt, sec_butt, th_butt, f_buttom)
                bot.edit_message_text(chat_id=cid, message_id=mid, text="Список позиций даст доступ к магазину. Не забудь прочитать Правила!",reply_markup=keyboardmenu)
        markup2 = types.InlineKeyboardMarkup()
        url_link = types.InlineKeyboardButton(text="Правила", url="https://telegra.ph/Pravila-07-22-3")
        switch_b1 = types.InlineKeyboardButton(text="Помощь", url='t.me/alex_kotenko')
        switch_b2 = types.InlineKeyboardButton(text="Оператор", url='t.me/Underbhoomi')
        po = types.InlineKeyboardButton(text="Список позиций", callback_data="positions")
        markup2.add(url_link, switch_b1, switch_b2, po)
        bot.edit_message_text(chat_id=cid, message_id=mid, text="Список позиций даст доступ к магазину. Не забудь прочитать Правила!",reply_markup=markup2)

@bot.callback_query_handler(func=lambda call: call.data == "positions" or call.data == "back2")
def positions(call):
        cid = call.message.chat.id
        mid = call.message.message_id

        if call.data == "back2":
                keyboardmenu2 = types.InlineKeyboardMarkup(row_width=2)
                b11 = types.InlineKeyboardButton(text="Фелормония", callback_data="Фелормония")
                b22 = types.InlineKeyboardButton(text="Шелх", callback_data="Шелх")
                b33 = types.InlineKeyboardButton(text="Кортошка", callback_data="Кортошка")
                back1 = types.InlineKeyboardButton(text="Назад", callback_data="mainmanu")
                keyboardmenu2.add(b11, b22, b33, back1)
                bot.edit_message_text(chat_id=cid, message_id=mid, text="Какой товар вам необходим?", reply_markup=keyboardmenu2)
        
        markup3 = types.InlineKeyboardMarkup()
        b1 = types.InlineKeyboardButton(text="Фелормония", callback_data="Фелормония")
        b2 = types.InlineKeyboardButton(text="Шелх", callback_data="Шелх")
        b3 = types.InlineKeyboardButton(text="Кортошка", callback_data="Кортошка")
        back = types.InlineKeyboardButton(text="Назад", callback_data="mainmanu")
        markup3.add(b1, b2, b3, back)
        bot.edit_message_text(chat_id=cid, message_id=mid, text="Какой товар вам необходим?", reply_markup=markup3)

@bot.callback_query_handler(func=lambda tovar: tovar.data == "Фелормония" or tovar.data == "Шелх"  or tovar.data == "Кортошка" or tovar.data == "back4")
def tovar_end(tovar):
        cid = tovar.message.chat.id
        mid = tovar.message.message_id
        markup = types.InlineKeyboardMarkup()
        if tovar.data == "Фелормония" or tovar.data == "1":
                tovar_d[tovar.from_user.first_name] = "Фелормония"
        elif tovar.data == "Шелх" or tovar.data =="3":
                tovar_d[tovar.from_user.first_name] = "Шелх"
        elif tovar.data == "Кортошка" or tovar.data == "3":
                tovar_d[tovar.from_user.first_name] = "Кортошка"
        elif tovar.data == "back4":
                keyboardmenu3 = types.InlineKeyboardMarkup()
                q1 = types.InlineKeyboardButton(text="1г", callback_data="1")
                q2 = types.InlineKeyboardButton(text="3г", callback_data="3")
                q3 = types.InlineKeyboardButton(text="5г", callback_data="5")
                back3 = types.InlineKeyboardButton(text="Назад", callback_data="back2")
                switch_v1 = types.InlineKeyboardButton(text="Оператор", url='t.me/Underbhoomi')
                keyboardmenu3.add(q1, q2, q3, switch_v1, back3)
                bot.edit_message_text(chat_id=cid, message_id=mid, text="Какой вес нужен? Если нужно больше, напишите нашему оператору!", reply_markup=keyboardmenu3)

        
        v1 = types.InlineKeyboardButton(text="1г", callback_data="1")
        v2 = types.InlineKeyboardButton(text="3г", callback_data="3")
        v3 = types.InlineKeyboardButton(text="5г", callback_data="5")
        back3 = types.InlineKeyboardButton(text="Назад", callback_data="back2")
        switch_v = types.InlineKeyboardButton(text="Оператор", url='t.me/Underbhoomi')
        markup.add(v1, v2, v3, back3, switch_v)
        try:
                bot.edit_message_text(chat_id=cid, message_id=mid, text="Какой вес нужен? Если нужно больше, напишите нашему оператору!", reply_markup=markup)
        except:
                v1 = types.InlineKeyboardButton(text="1г", callback_data="1")
                v2 = types.InlineKeyboardButton(text="3г", callback_data="3")
                v3 = types.InlineKeyboardButton(text="5г", callback_data="5")
                back3 = types.InlineKeyboardButton(text="Назад", callback_data="back2")
                switch_v = types.InlineKeyboardButton(text="Оператор", url='t.me/Underbhoomi')
                markup.add(v1, v2, v3, back3, switch_v)

@bot.callback_query_handler(func=lambda ves: (ves.data == "1" or ves.data == "3") or ves.data == "5")
def ves_end(ves):
        try:
                cid = ves.message.chat.id
                mid = ves.message.message_id        
                country = list()
                region = list()
                if ves.data == "1":
                        ves_d[ves.from_user.first_name] = "1"
                elif ves.data == "3":
                        ves_d[ves.from_user.first_name] = "3"
                elif ves.data == "5":
                        ves_d[ves.from_user.first_name] = "5"
                country.append(city[ves.from_user.first_name])
                t = tovar_d[ves.from_user.first_name]
        except KeyError:
                pass
        cid = ves.message.chat.id
        mid = ves.message.message_id 
        region.append(ves.data) 
        ve =  ves_d[ves.from_user.first_name]
        con = sqlite3.connect("DataBase.db")
        cur = con.cursor()
        cur.execute("SELECT DISTINCT streat FROM stock WHERE city = (?) AND name_stock = (?) AND much = (?)",[country[0], t, int(ve)])
        datadb = list(cur)
        markup = types.InlineKeyboardMarkup()  
        for row in datadb:
                a = types.InlineKeyboardButton(text=row[const.const], callback_data=row[const.const]) 
                str(row[const.const])
                streat.append(str(row[const.const]))
                markup.add(a) 
        back4 = types.InlineKeyboardButton(text="Назад", callback_data="back4")
        markup.add(back4)
        con.commit() 
        cur.close()
        con.close()   
        bot.edit_message_text(chat_id=cid, message_id=mid, text="Возможные районы по твоему запросу. Выбери нужный для того, что бы узнать цену.", reply_markup=markup)


@bot.callback_query_handler(func=lambda all_req: all_req.data in streat)
def funct(all_req):
        my_streat[all_req.from_user.first_name] = all_req.data
        cid = all_req.message.chat.id
        mid = all_req.message.message_id
        countrys = city[all_req.from_user.first_name] 
        ts = tovar_d[all_req.from_user.first_name]
        ves =  ves_d[all_req.from_user.first_name]
        st = all_req.data
        con1 = sqlite3.connect("DataBase.db")
        cur = con1.cursor()
        cur.execute("SELECT DISTINCT price FROM stock WHERE city = (?) AND name_stock = (?) AND much = (?) AND streat = (?)",[countrys, ts, int(ves), st])
        datadb = list(cur)
        for row in datadb:
                solo[all_req.from_user.first_name] = row[const.const]
        markup = types.InlineKeyboardMarkup()
        back = types.InlineKeyboardButton(text="Отмена", callback_data="mainmanu")
        buy = types.InlineKeyboardButton(text="Оплатить", callback_data="price")
        markup.add(back, buy)
        con1.commit()
        cur.close()
        con1.close()
        bot.edit_message_text(chat_id=cid, message_id=mid, text="Отлично, что мы имеем? Ты выбрал город - {} на районе {} и по весу  {} будет {}грамм . Тебе нужно заплатить {}грн. Готов повеселится?".format(countrys, st, ts, ves, solo[all_req.from_user.first_name]), reply_markup=markup)


@bot.callback_query_handler(func=lambda yets: yets.data == "price")
def somfunk(yets):
        cid = yets.message.chat.id
        mid = yets.message.message_id
        markup = types.InlineKeyboardMarkup() 
        bby = types.InlineKeyboardButton(text="Отправить на проверку", callback_data="check")
        oo = types.InlineKeyboardButton(text="EasyPay - 95436138", url="https://easypay.ua/ua/catalog/e-money/easypay/easypay-money-deposit?account=95436138")
        markup.add(oo)
        markup.add(bby)
        bot.edit_message_text(chat_id=cid, message_id=mid,text="После перехода на сайт для оплаты, не забудте нажать кнопку 'Отправить на проверку!'На все у тебя есть 35 минут. если ты не успеешь или введешь не не правильно - получишь бан. 3 бана - ЧС.", reply_markup=markup)



server_data = "22.04.2019 13:18 "
server_sum = "100"
serv_d = server_data + server_sum
@bot.callback_query_handler(func=lambda okbuy: okbuy.data == "check")
def ff(okbuy):
        cid = okbuy.message.chat.id
        mid = okbuy.message.message_id
        bot.edit_message_text(chat_id=cid, message_id=mid, text="Введи день, месяц и год отплаты. Пробел часы минуты! Потом через пробел сумму которую заплатил. Пример XX.XX.XX XX:XX xxx")
        time.sleep(2)     


@bot.message_handler(content_types=['text'])
def price_streat(price):
        cid = price.chat.id
        countrys = city[price.from_user.first_name] 
        ts = tovar_d[price.from_user.first_name]
        ves =  ves_d[price.from_user.first_name]
        st = my_streat[price.from_user.first_name]
        so = solo[price.from_user.first_name]
        con1 = sqlite3.connect("DataBase.db")
        cur = con1.cursor()
        cur.execute("SELECT DISTINCT photo FROM stock WHERE city = (?) AND name_stock = (?) AND much = (?) AND streat = (?) AND price = (?)",[countrys, ts, int(ves), st, so])
        datadb = list(cur)
        for row in datadb:
                ph[price.from_user.first_name] = row[const.const]
        con1.commit()
        cur.close()
        con1.close()
        print(ph[price.from_user.first_name])
        if(serv_d == price.text):
                bot.send_message(chat_id=cid, text="Хорошо, скидую ссылку на фото месторасположения!")
                bot.send_message(chat_id=cid, text="Ссылка отправлена. Не забудте ее сохранить!" + ph[price.from_user.first_name])
                conn33 = sqlite3.connect("DataBase.db")
                delliting = ph[price.from_user.first_name]
                cursor = conn33.cursor()
                cursor.execute("DELETE FROM stock WHERE photo = (?)",[delliting])
                conn33.commit()
                cursor.close()
                conn33.close()
        else:   
                if price.from_user.first_name not in ban: 
                        bot.send_message(chat_id=cid, text="Кто то пытается наебать, получай замечание! У тебя 1 замечание. 3 замечания - БАН")
                        ban[price.from_user.first_name] = 1
                        print(ban)
                elif ban[price.from_user.first_name] == 1:
                        bot.send_message(chat_id=cid, text="Кто то пытается наебать, получай замечание! У тебя 2 замечание. 3 замечания - БАН")
                        ban[price.from_user.first_name] = 2
                elif ban[price.from_user.first_name] == 2:
                        ban[price.from_user.first_name] = 3
                        notok = "sad"
                        baaaan(notok)
                elif ban[price.from_user.first_name] == 3:
                        notok = "sad"
                        baaaan(notok)

                
def baaaan(m):
        if m == "end":
                pass
        if m == "sad":
                bot.edit_message_text(m.from_user.first_name, "Ты получил БАН. Давай ДО свидания!")
                

                



  
if __name__ == "__main__":
        bot.polling(none_stop=True, interval=0)
                
        
