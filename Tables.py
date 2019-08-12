import sqlite3
class Hero:

    def OutStat(id):
        Table = sqlite3.connect("1.db");
        cursor = Table.cursor()
        Name = cursor.execute("SELECT username FROM Players WHERE id LIKE " + id + ";")
        Lvl = cursor.execute("SELECT level FROM Players WHERE id LIKE " + id + ";")
        Exp = cursor.execute("SELECT exp FROM Players WHERE id LIKE " + id + ";")
        Fraction = cursor.execute("SELECT fraction FROM Players WHERE id LIKE " + id + ";")
        Gold = cursor.execute("SELECT gold FROM Players WHERE id LIKE " + id + ";")
        Dimonds = cursor.execute("SELECT donat FROM Players WHERE id LIKE " + id + ";")
        Status = cursor.execute("SELECT big_name FROM Players WHERE id LIKE " + id + ";")
        Rating = cursor.execute("SELECT rate FROM Players WHERE id LIKE " + id + ";")
        Win = cursor.execute("SELECT win FROM Players WHERE id LIKE " + id + ";")
        Loose = cursor.execute("SELECT lose FROM Players WHERE id LIKE " + id + ";")
        Draw = cursor.execute("SELECT draws FROM Players WHERE id LIKE " + id + ";")

        print (cursor.fetchall())


        a = Name + "\n" +"🎖 Уровень:" + Lvl+ "\n" + "🌟 Опыт:" + Exp + "\n" + "💟 Фракция: "+ Fraction + "\n"+"💰 Золото:" + Gold + "\n"  +"💎 Алмазы:" + Dimonds + "\n"+ "🏆 Звание" + Status +"\n";
        a = a + "💯 Рейтинг:" + Rating+ "\n" + "🏆 Побед:" + Win + "\n" + "🤕 Поражений:" + Loose+ "\n" + "🤝 Ничьих:" + Draw+ "\n";
        return(a);

    def Arena(id):
        Table = sqlite3.connect("2.db");
        cursor = Table.cursor()
        AllHp = cursor.execute("SELECT AllHp FROM Skills WHERE id LIKE " + id + ";")
        Hp = cursor.execute("SELECT Hp FROM Skills WHERE id LIKE " + id + ";")
        Table = sqlite3.connect("1.db");
        cursor = Table.cursor()
        Name = cursor.execute("SELECT username FROM Players WHERE id LIKE " + id + ";")
        Lvl = cursor.execute("SELECT level FROM Players WHERE id LIKE " + id + ";")
        answer = Name + "🎖"+ Lvl+" 🖤 ("+Hp+"/"+AllHp+ " \n \n + Добро пожаловать на Арену Лакедемон! \n \n Тут ты можешь принять участие в одиночных, групповых, хаотических и тренировочных боях, повысить рейтинг и опыт, а также заработать золото."
        return (answer);