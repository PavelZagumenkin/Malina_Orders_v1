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
        if value[0][2] == None:
            signal.emit('Пусто')
        if value[0][3] != None:
            if value[0][6] == None:
                signal.emit('За этот период есть сформированный прогноз')
            else:
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

def deletePrognozInDB(period):
    con = sqlite3.connect('db/malina_orders.db')
    cur = con.cursor()
    cur.execute(f"DELETE FROM prognoz_bakery where PERIOD = '''{period}'''")
    con.commit()
    cur.close()
    con.close()

def addPrognozInDB(savePeriod, saveHeaders, saveDB, saveNull):
    con = sqlite3.connect('db/malina_orders.db')
    cur = con.cursor()
    cur.execute(f"UPDATE prognoz_bakery set HEADERSPROGNOZ = '''{saveHeaders}''', DATAPROGNOZ = '''{saveDB}''', SAVENULLPROGNOZ = '''{saveNull}''' where PERIOD = '''{savePeriod}'''")
    con.commit()
    cur.close()
    con.close()

def updatePrognoz(savePeriod, saveHeaders, saveDB, saveNull):
    con = sqlite3.connect('db/malina_orders.db')
    cur = con.cursor()
    cur.execute(f"UPDATE prognoz_bakery set HEADERSPROGNOZ = '''{saveHeaders}''', DATAPROGNOZ = '''{saveDB}''', SAVENULLPROGNOZ = '''{saveNull}''' where PERIOD = '''{savePeriod}'''")
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

def addDayWeekInDB(savePeriod, saveHeaders, saveDB, saveNull):
    con = sqlite3.connect('db/malina_orders.db')
    cur = con.cursor()
    cur.execute(f"UPDATE prognoz_bakery set HEADERSKDAYWEEK = '''{saveHeaders}''', DATAKDAYWEEK = '''{saveDB}''', SAVENULLKDAYWEEK = '''{saveNull}''' where PERIOD = '''{savePeriod}'''")
    con.commit()
    cur.close()
    con.close()