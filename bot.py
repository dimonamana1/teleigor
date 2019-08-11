from telebot import util
import utils
import config
import Keyboards
import telebot
from telebot import types
import sqlite3

bot = telebot.TeleBot(config.token)

stack = utils.Stack()


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

    @bot.message_handler(regexp="⚔️Арена")
    def handle_message(message):
        stack.push(Keyboards.markup)
        bot.send_message(message.chat.id, "1", reply_markup=Keyboards.markup1)

        @bot.message_handler(regexp="⬅️ Назад")
        def handle_message(message):
            bot.send_message(message.chat.id, "1", reply_markup=stack.peek())
            stack.pop()

        @bot.message_handler(regexp="⚔️ Одиночный")
        def handle_message(message):
            stack.push(Keyboards.markup1)
            bot.send_message(message.chat.id, "1", reply_markup=Keyboards.markup11)

            @bot.message_handler(regexp="Отмена")
            def handle_message(message):
                bot.send_message(message.chat.id, "1", reply_markup=stack.peek())
                stack.pop()

        @bot.message_handler(regexp="👥 Командный")
        def handle_message(message):
            stack.push(Keyboards.markup1)
            bot.send_message(message.chat.id, "1", reply_markup=Keyboards.markup12)

            @bot.message_handler(regexp="Отмена")
            def handle_message(message):
                bot.send_message(message.chat.id, "1", reply_markup=stack.peek())
                stack.pop()

            @bot.message_handler(regexp="⚔️ Новый бой")
            def handle_message(message):
                bot.send_message(message.chat.id, "1", reply_markup=stack.peek())
                stack.push(Keyboards.markup12)

                @bot.message_handler(regexp="Отмена")
                def handle_message(message):
                    bot.send_message(message.chat.id, "1", reply_markup=stack.peek())
                    stack.pop()

        @bot.message_handler(regexp="💀 Хаотический")
        def handle_message(message):
            stack.push(Keyboards.markup1)
            bot.send_message(message.chat.id, "1", reply_markup=Keyboards.markup13)

            @bot.message_handler(regexp="⬅️ Назад")
            def handle_message(message):
                bot.send_message(message.chat.id, "1", reply_markup=stack.peek())
                stack.pop()

        @bot.message_handler(regexp="👊 Тренировочный")
        def handle_message(message):
            stack.push(Keyboards.markup1)
            bot.send_message(message.chat.id, "1", reply_markup=Keyboards.markup14)

            @bot.message_handler(regexp="Отмена")
            def handle_message(message):
                bot.send_message(message.chat.id, "1", reply_markup=stack.peek())
                stack.pop()

    @bot.message_handler(regexp="🏘Город")
    def handle_message(message):
        stack.push(Keyboards.markup)
        bot.send_message(message.chat.id, "1", reply_markup=Keyboards.markup2)

        @bot.message_handler(regexp="🏠 Торговец")
        def handle_message(message):
            stack.push(Keyboards.markup2)
            bot.send_message(message.chat.id, "1", reply_markup=Keyboards.markup21)

            @bot.message_handler(regexp="⬅️ Назад")
            def handle_message(message):
                bot.send_message(message.chat.id, "1", reply_markup=stack.peek())
                stack.pop()

        @bot.message_handler(regexp="🎲 Лотерея")
        def handle_message(message):
            stack.push(Keyboards.markup2)
            bot.send_message(message.chat.id, "1", reply_markup=Keyboards.markup22)

            @bot.message_handler(regexp="⬅️ Назад")
            def handle_message(message):
                bot.send_message(message.chat.id, "1", reply_markup=stack.peek())
                stack.pop()

        @bot.message_handler(regexp="🏛 Академия")
        def handle_message(message):
            stack.push(Keyboards.markup2)
            bot.send_message(message.chat.id, "1", reply_markup=Keyboards.markup23)

            @bot.message_handler(regexp="⬅️ Назад")
            def handle_message(message):
                bot.send_message(message.chat.id, "1", reply_markup=stack.peek())
                stack.pop()

        @bot.message_handler(regexp="🏫 Ратуша")
        def handle_message(message):
            stack.push(Keyboards.markup2)
            bot.send_message(message.chat.id, "1", reply_markup=Keyboards.markup24)

            @bot.message_handler(regexp="⬅️ Назад")
            def handle_message(message):
                bot.send_message(message.chat.id, "1", reply_markup=stack.peek())
                stack.pop()

        # @bot.message_handler(regexp="🏚🏚💒 Храм")
        # def handle_message(message):
        #     bot.send_message(message.chat.id, "1", reply_markup=Keyboards.markup25)

        @bot.message_handler(regexp="🏚 Таверна")
        def handle_message(message):
            stack.push(Keyboards.markup2)
            bot.send_message(message.chat.id, "1", reply_markup=Keyboards.markup26)

            @bot.message_handler(regexp="🤠 Найти задание")
            def handle_message(message):
                bot.send_message(message.chat.id, "1", reply_markup=Keyboards.markup261)

                @bot.message_handler(regexp="⬅️ Назад")
                def handle_message(message):
                    bot.send_message(message.chat.id, "1", reply_markup=stack.peek())
                    stack.pop()

            @bot.message_handler(regexp="⬅️ Назад")
            def handle_message(message):
                bot.send_message(message.chat.id, "1", reply_markup=stack.peek())
                stack.pop()

        @bot.message_handler(regexp="🐺 Зверинец")
        def handle_message(message):
            stack.push(Keyboards.markup2)
            bot.send_message(message.chat.id, "1", reply_markup=Keyboards.markup27)

            @bot.message_handler(regexp="⬅️ Назад")
            def handle_message(message):
                bot.send_message(message.chat.id, "1", reply_markup=stack.peek())
                stack.pop()

        @bot.message_handler(regexp="💎 Банк")
        def handle_message(message):
            stack.push(Keyboards.markup2)
            bot.send_message(message.chat.id, "1", reply_markup=Keyboards.markup28)

            @bot.message_handler(regexp="⬅️ Назад")
            def handle_message(message):
                bot.send_message(message.chat.id, "1", reply_markup=stack.peek())
                stack.pop()

        @bot.message_handler(regexp="⬅️ Назад")
        def handle_message(message):
            bot.send_message(message.chat.id, "1", reply_markup=stack.peek())
            stack.pop()

    @bot.message_handler(regexp="🎖 Герой")
    def handle_message(message):
        stack.push(Keyboards.markup)
        bot.send_message(message.chat.id, "1", reply_markup=Keyboards.markup3)

        @bot.message_handler(regexp="⬅️ Назад")
        def handle_message(message):
            bot.send_message(message.chat.id, "1", reply_markup=stack.peek())
            stack.pop()

    @bot.message_handler(regexp="🏰 Клан")
    def handle_message(message):
        stack.push(Keyboards.markup)
        bot.send_message(message.chat.id, "1", reply_markup=Keyboards.markup4)

        @bot.message_handler(regexp="⬅️ Назад")
        def handle_message(message):
            bot.send_message(message.chat.id, "1", reply_markup=stack.peek())
            stack.pop()

    @bot.message_handler(regexp="🏆 Лиги")
    def handle_message(message):
        stack.push(Keyboards.markup)
        bot.send_message(message.chat.id, "1", reply_markup=Keyboards.markup5)

        @bot.message_handler(regexp="⬅️ Назад")
        def handle_message(message):
            bot.send_message(message.chat.id, "1", reply_markup=stack.peek())
            stack.pop()

    # @bot.message_handler(regexp="📜 Летопись")
    # def handle_message(message):
    #     bot.send_message(message.chat.id, "1", reply_markup=Keyboards.markup6)

    # @bot.message_handler(regexp="❓Помощь")
    # def handle_message(message):
    #     bot.send_message(message.chat.id, "1", reply_markup=Keyboards.markup7)

    # @bot.message_handler(regexp="⚙️ Настройки")
    # def handle_message(message):
    #     bot.send_message(message.chat.id, "1", reply_markup=Keyboards.markup8)


if __name__ == '__main__':
    bot.polling(none_stop=True)
