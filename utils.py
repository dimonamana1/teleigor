import Keyboards


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class Menu(object):

    def __init__(self, name, markup, color, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10):
        self.name = name
        self.markup = markup
        self.color = color
        self.connections = (v1, v2, v3, v4, v5, v6, v7, v8, v9, v10)


menu = Menu('Home', Keyboards.markup, 'black', '⚔️Арена', '🏘Город', '🎖 Герой', '🏰 Клан', '🏆 Лиги', '📜 Летопись',
            '❓Помощь', '⚙️ Настройки', 0, 0)
menu1 = Menu('⚔️Арена', Keyboards.markup1, 'white', 'Home', '⚔️ Одиночный', '👥 Командный', ' Хаотический',
             '👊 Тренировочный', 0, 0, 0, 0, 0)
menu11 = Menu('⚔️ Одиночный', Keyboards.markup11, 'white', '⚔️Арена', 0, 0, 0, 0, 0, 0, 0, 0, 0)
menu12 = Menu('👥 Командный', Keyboards.markup12, 'white', '⚔️Арена', 0, 0, 0, 0, 0, 0, 0, 0, 0)
menu13 = Menu('💀 Хаотический', Keyboards.markup13, 'white', '⚔️Арена', 0, 0, 0, 0, 0, 0, 0, 0, 0)
menu14 = Menu('👊 Тренировочный', Keyboards.markup14, 'white', '⚔️Арена', 0, 0, 0, 0, 0, 0, 0, 0, 0)
menu2 = Menu('🏘Город', Keyboards.markup2, 'white', 'Home', '🏠 Торговец', '🎲 Лотерея', '🏛 Академия', '🏫 Ратуша',
             '💒 Храм', '🏚 Таверна', '🐺 Зверинец', '💎 Банк', 0)
menu21 = Menu('🏠 Торговец', Keyboards.markup21, 'white', '🏘Город', 0, 0, 0, 0, 0, 0, 0, 0, 0)
menu22 = Menu('🎲 Лотерея', Keyboards.markup22, 'white', '🏘Город', 0, 0, 0, 0, 0, 0, 0, 0, 0)
menu23 = Menu('🏛 Академия', Keyboards.markup23, 'white', '🏘Город', 0, 0, 0, 0, 0, 0, 0, 0, 0)
menu24 = Menu('🏫 Ратуша', Keyboards.markup24, 'white', '🏘Город', 0, 0, 0, 0, 0, 0, 0, 0, 0)
menu25 = Menu('💒 Храм', Keyboards.markup25, 'white', '🏘Город', 0, 0, 0, 0, 0, 0, 0, 0, 0)
menu26 = Menu('🏚 Таверна', Keyboards.markup26, 'white', '🏘Город', '🤠 Найти задание', 0, 0, 0, 0, 0, 0, 0, 0)
menu261 = Menu('🤠 Найти задание', Keyboards.markup261, 'white', '🤠 Таверна', 0, 0, 0, 0, 0, 0, 0, 0, 0)
menu27 = Menu('🐺 Зверинец', Keyboards.markup27, 'white', '🏘Город', 0, 0, 0, 0, 0, 0, 0, 0, 0)
menu28 = Menu('💎 Банк', Keyboards.markup28, 'white', '🏘Город', '💎 Купить алмазы', '🗄 История платежей', 0, 0, 0, 0, 0,
              0, 0)
menu282 = Menu('💎 Купить алмазы', Keyboards.markup282, 'white', '💎 Банк', 0, 0, 0, 0, 0, 0, 0, 0, 0)
menu283 = Menu('🗄 История платежей', Keyboards.markup283, 'white', '💎 Банк', 0, 0, 0, 0, 0, 0, 0, 0, 0)
menu3 = Menu('🎖 Герой', Keyboards.markup3, 'white', 'Home', 0, 0, 0, 0, 0, 0, 0, 0, 0)
menu4 = Menu('🏰 Клан', Keyboards.markup4, 'white', 'Home', '📩 Приглашения', 0, 0, 0, 0, 0, 0, 0, 0)
menu44 = Menu('📩 Приглашения', Keyboards.markup44, 'white', '🏰 Клан', '🔍 Искать по имени', '🕵️‍♂️ Нанять скаута', 0, 0, 0,
              0, 0, 0, 0)
menu441 = Menu('🔍 Искать по имени', Keyboards.markup441, 'white', '📩 Приглашения', 0, 0, 0, 0, 0, 0, 0, 0, 0)
menu442 = Menu('🕵️‍♂️ Нанять скаута', Keyboards.markup442, 'white', '📩 Приглашения', 0, 0, 0, 0, 0, 0, 0, 0, 0)
menu46 = Menu('❌ Покинуть клан', Keyboards.markup46, 'white', '🏰 Клан', 0, 0, 0, 0, 0, 0, 0, 0, 0)
menu5 = Menu('🏆 Лиги', Keyboards.markup5, 'white', 'Home', 0, 0, 0, 0, 0, 0, 0, 0, 0)
menu51 = Menu('🏆 Лига', Keyboards.markup51, 'white', '🏆 Лиги', 0, 0, 0, 0, 0, 0, 0, 0, 0)

massive = [menu, menu1, menu11, menu12, menu13, menu14, menu2, menu21, menu22, menu23, menu24, menu25, menu26,
           menu261, menu27, menu28, menu282, menu283, menu3, menu4, menu44, menu441, menu442, menu46, menu5, menu51]

mas = {'⚔️Арена' : 23}