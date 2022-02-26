import sqlite3
HW_db = sqlite3.connect('HW_db.db')
cursor = HW_db.cursor()
cursor.execute('''create table if not exists homework(id integer primary key autoincrement, number int)''')
number = int(input('Введите число'))
cursor.execute('''insert into homework(number) values(?)''', (number,))
class new_datebase:
    def __init__(self, *args):
        self.args = args

    @staticmethod  #статический метод обновления id, чтобы id было по порядку после преобразований по функциям.
    def id_update():
        cursor.execute('''select id from homework''')
        arr = cursor.fetchall()
        m = 1
        for i in arr:
            id_star = int(i[0])
            cursor.execute('''update homework set id = ? where id = ?''', (m, id_star))
            HW_db.commit()
            m += 1

    def args_len(self):
        if len(self.args) == 1:
            print('Передан 1 аргумент, в бд добавляется значение 3')
            cursor.execute('''insert into homework(number) values(3)''')
            new_datebase.id_update() #обновляется id
        elif len(self.args) >= 2:
            if str(self.args[1]).isdigit():
                print('Передано 2 и более аргументов, 2-й аргумент является числом, следовательно удаляется  первая запись из БД')
                cursor.execute('''delete from homework where id = 1''')
                HW_db.commit()
                new_datebase.id_update() #обновляется id
            elif not str(self.args[1]).isdigit() and not str(self.args[1]).isalpha() and not str(self.args[0]).isdigit() and not str(self.args[0]).isalpha() and str(self.args[2]).isdigit():
                print('Передано более двух аргументов, первые два - типы не определены. 3 - число. Запись с id 3 Обновляется на 77')
                cursor.execute('''update homework set number = 77 where id = 3''')
                HW_db.commit()
                new_datebase.id_update() #обновляется id

class_new_DB = new_datebase(1)
class_new_DB.args_len()
cursor.execute('''select * from homework''')
k = cursor.fetchall()
for i in k:
    print(' '.join([str(j) for j in i]))





