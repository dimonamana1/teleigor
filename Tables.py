import sqlite3


class Hero:

    def OutStat(id):
        Table = sqlite3.connect("1.db");
        cursor = Table.cursor()
        cursor.execute("SELECT username FROM Players WHERE id LIKE " + id + ";")
        Name = str(cursor.fetchone()[0])
        cursor.execute("SELECT level FROM Players WHERE id LIKE " + id + ";")
        Lvl = str(cursor.fetchone()[0])
        cursor.execute("SELECT exp FROM Players WHERE id LIKE " + id + ";")
        Exp = str(cursor.fetchone()[0])
        cursor.execute("SELECT fraction FROM Players WHERE id LIKE " + id + ";")
        Fraction = str(cursor.fetchone()[0])
        cursor.execute("SELECT gold FROM Players WHERE id LIKE " + id + ";")
        Gold = str(cursor.fetchone()[0])
        cursor.execute("SELECT donat FROM Players WHERE id LIKE " + id + ";")
        Dimonds = str(cursor.fetchone()[0])
        cursor.execute("SELECT big_name FROM Players WHERE id LIKE " + id + ";")
        Status = str(cursor.fetchone()[0])
        cursor.execute("SELECT rate FROM Players WHERE id LIKE " + id + ";")
        Rating = str(cursor.fetchone()[0])
        cursor.execute("SELECT win FROM Players WHERE id LIKE " + id + ";")
        Win = str(cursor.fetchone()[0])
        cursor.execute("SELECT lose FROM Players WHERE id LIKE " + id + ";")
        Loose = str(cursor.fetchone()[0])
        cursor.execute("SELECT draws FROM Players WHERE id LIKE " + id + ";")
        Draw = str(cursor.fetchone()[0])

        a = Name + "\n" + "🎖 Уровень:" + Lvl + "\n" + "🌟 Опыт:" + Exp + "\n" + "💟 Фракция: " + Fraction + "\n" + "💰 Золото:" + Gold + "\n" + "💎 Алмазы:" + Dimonds + "\n" + "🏆 Звание" + Status + "\n";
        a = a + "💯 Рейтинг:" + Rating + "\n" + "🏆 Побед:" + Win + "\n" + "🤕 Поражений:" + Loose + "\n" + "🤝 Ничьих:" + Draw + "\n";
        return (a);

    def Arena(id):
        Table = sqlite3.connect("2.db");
        cursor = Table.cursor()
        cursor.execute("SELECT AllHp FROM Skills WHERE id LIKE " + id + ";")
        AllHp = str(cursor.fetchone())
        cursor.execute("SELECT Hp FROM Skills WHERE id LIKE " + id + ";")
        Hp = str(cursor.fetchone())
        Table = sqlite3.connect("1.db");
        cursor = Table.cursor()
        cursor.execute("SELECT username FROM Players WHERE id LIKE " + id + ";")
        Name = str(cursor.fetchone()[0])
        cursor.execute("SELECT level FROM Players WHERE id LIKE " + id + ";")
        Lvl = str(cursor.fetchone()[0])
        answer ="  "+ Name + "🎖" + Lvl + " 🖤 (" + Hp + "/" + AllHp + ") \n \n  Добро пожаловать на Арену Лакедемон! \n \n  Тут ты можешь принять участие в одиночных, групповых, хаотических и тренировочных боях, повысить рейтинг и опыт, а также заработать золото."
        return (answer);

    def shop(id):
        Table = sqlite3.connect("1.db");
        cursor = Table.cursor()
        cursor.execute("SELECT gold FROM Players WHERE id LIKE " + id + ";")
        Gold = str(cursor.fetchone()[0])
        cursor.execute("SELECT donat FROM Players WHERE id LIKE " + id + ";")
        Dimonds = str(cursor.fetchone()[0])
        a = "У тебя есть: 💰Золото ‒ " + Gold + ", 💎Алмазы ‒ "+ Dimonds + "\n \n Что тебя интересует?"
        return (a);

