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

def update_Layout(kod_text, tovar_text, layout):
    con = sqlite3.connect('db/malina_orders.db')
    cur = con.cursor()
    cur.execute(f"INSERT INTO directory_bakery (KOD, NAME, LAYOUT) VALUES ('{kod_text}', '{tovar_text}', '{layout}');")
    con.commit()
    cur.close()
    con.close()

def poiskPeriodaInDB(period, signal):
    con = sqlite3.connect('db/malina_orders.db')
    cur = con.cursor()
    cur.execute(f"SELECT * FROM prognoz_bakery WHERE PERIOD='''{period}''';")
    value = cur.fetchall()
    if value == []:
        signal.emit('Пусто')
    else:
        if value[0][2] == None and value[0][3] == None and value[0][4] == None and value [0][5] == None:
            signal.emit('Пусто')
        if value[0][3] != None:
            signal.emit('За этот период есть сформированный прогноз')
        elif value[0][5] != None:
            signal.emit('За этот период есть сформированные коэффициенты по дням недели')
        elif value[0][3] != None and value[0][5] != None:
            signal.emit('Есть и то и то')
    cur.close()
    con.close()

def addPeriodInDB(period):
    con = sqlite3.connect('db/malina_orders.db')
    cur = con.cursor()
    cur.execute(f"INSERT INTO prognoz_bakery (PERIOD) VALUES ('''{period}''');")
    con.commit()
    cur.close()
    con.close()

def deletePeriodInDB(period):
    con = sqlite3.connect('db/malina_orders.db')
    cur = con.cursor()
    cur.execute(f"DELETE FROM prognoz_bakery where PERIOD = '''{period}'''")
    con.commit()
    cur.close()
    con.close()

def addInPrognoz(savePeriod, saveHeaders, saveDB, saveNull):
    con = sqlite3.connect('db/malina_orders.db')
    cur = con.cursor()
    cur.execute(f"INSERT INTO prognoz_bakery (PERIOD, HEADERS, DATA, SAVENULL) VALUES ('''{savePeriod}''', '''{saveHeaders}''', '''{saveDB}''', '''{saveNull}''');")
    con.commit()
    cur.close()
    con.close()

def updatePrognoz(savePeriod, saveHeaders, saveDB, saveNull):
    con = sqlite3.connect('db/malina_orders.db')
    cur = con.cursor()
    cur.execute(f"UPDATE prognoz_bakery set HEADERS = '''{saveHeaders}''', DATA = '''{saveDB}''', SAVENULL = '''{saveNull}''' where PERIOD = '''{savePeriod}'''")
    con.commit()
    cur.close()
    con.close()

def poiskDataPerioda(period, prognoz):
    con = sqlite3.connect('db/malina_orders.db')
    cur = con.cursor()
    cur.execute(f"SELECT * FROM prognoz_bakery WHERE PERIOD='''{period}''';")
    value = cur.fetchall()
    prognoz.emit(value)
    cur.close()
    con.close()