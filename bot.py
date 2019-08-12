from telebot import util
import utils
import config
import Keyboards
import telebot
from telebot import types
import sqlite3
from Tables import Hero

bot = telebot.TeleBot(config.token)

stack = utils.Stack()
curpos = utils.massive[0]
@bot.message_handler(commands=['game'])
def game(message):
    conn = sqlite3.connect("1.db")
    cursor = conn.cursor()
    sql = "SELECT * FROM Players WHERE id=?"
    cursor.execute(sql, [(message.chat.id)])
    if len(cursor.fetchall()) == 0:
        cursor.execute("""INSERT INTO Players
                              VALUES ('%s','%s1','1','0','white','20','5','0','0','0','0','0')""" % (
            message.chat.id, message.chat.username))
        conn.commit()
        cursor.close()
        conn.close()
    bot.send_message(message.chat.id, message.chat.id, reply_markup=Keyboards.markup)

    @bot.message_handler(content_types=["text"])
    def handle_message(message):
        global curpos
        for i in curpos.connections:
            if i == message.text:
                for j in utils.massive:
                    if j.name == i:
                        curpos.color = 'black'
                        curpos = j
                        bot.send_message(message.chat.id, message.chat.username, reply_markup=curpos.markup)

@bot.message_handler(regexp="⬅️ Назад")
def handle_message(message):
    global curpos
    for i in curpos.connections:
        for j in utils.massive:
            if j.name == i and j.color == 'black':
                j.color = 'white'
                curpos = j
                bot.send_message(message.chat.id, message.chat.username, reply_markup=curpos.markup)

@bot.message_handler(regexp="Отмена")
def handle_message(message):
    global curpos
    for i in curpos.connections:
        for j in utils.massive:
            if j.name == i and j.color == 'black':
                j.color = 'white'
                curpos = j
                bot.send_message(message.chat.id, message.chat.username, reply_markup=curpos.markup)




if __name__ == '__main__':
    bot.polling(none_stop=True)
