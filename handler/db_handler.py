import sqlite3


def login(login, password, signal):
    con = sqlite3.connect('db/malina_orders.db')
    cur = con.cursor()

    # Проверяем, есть ли такой пользователь
    cur.execute(f'SELECT * FROM users WHERE LOGIN="{login}";')
    value = cur.fetchall()

    if value != [] and value[0][2] == password:
        signal.emit('Успешная авторизация')
    else:
        signal.emit('Неверный логин или пароль!')

    cur.close()
    con.close()

def seach_kod(kod, signal):
    con = sqlite3.connect('db/malina_orders.db')
    cur = con.cursor()

    # Проверяем, есть ли такой код
    cur.execute(f'SELECT * FROM directory_bakery WHERE KOD="{kod}";')
    value = cur.fetchall()

    if value != []:
        signal.emit(str(value[0][3]))
    else:
        signal.emit('Код отсутствует в БД')

    cur.close()
    con.close()

def addInPrognoz(savePeriod, saveHeaders, saveDB, signal):
    con = sqlite3.connect('db/malina_orders.db')
    cur = con.cursor()

    # Проверяем, есть ли такой код
    cur.execute(f'SELECT * FROM prognoz_bakery WHERE PERIOD="{savePeriod}";')
    value = cur.fetchall()

    if value != []:
        signal.emit('За этот период уже есть прогноз!')
    elif value == []:
        signal.emit('Прогноз сохранен в БД')
        # cur.execute(f"INSERT INTO prognoz_bakery (PERIOD) VALUES ('{savePeriod}')")
        cur.execute(f"INSERT INTO prognoz_bakery (PERIOD, HEADERS, DATA) VALUES ('{savePeriod}', '{saveHeaders}', '{saveDB}')")
        con.commit()

    cur.close()
    con.close()
