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
    cur.execute(f'SELECT * FROM catalog_food WHERE KOD="{kod}";')
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
    cur.execute(f"INSERT INTO catalog_food (KOD, NAME, LAYOUT) VALUES ('{kod_text}', '{tovar_text}', '{layout}');")
    con.commit()
    cur.close()
    con.close()

def poiskPeriodaPrognozaInDB(period, signal):
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
            signal.emit('За этот период есть сформированный прогноз')
    cur.close()
    con.close()

def addPeriodPrognozInDB(period):
    con = sqlite3.connect('db/malina_orders.db')
    cur = con.cursor()
    cur.execute(f"INSERT INTO prognoz_bakery (PERIOD) VALUES ('''{period}''');")
    con.commit()
    cur.close()
    con.close()

def deletePeriodPrognozInDB(period):
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

def updatePrognozInDB(savePeriod, saveHeaders, saveDB, saveNull):
    con = sqlite3.connect('db/malina_orders.db')
    cur = con.cursor()
    cur.execute(f"UPDATE prognoz_bakery set HEADERSPROGNOZ = '''{saveHeaders}''', DATAPROGNOZ = '''{saveDB}''', SAVENULLPROGNOZ = '''{saveNull}''' where PERIOD = '''{savePeriod}'''")
    con.commit()
    cur.close()
    con.close()

def poiskDataPeriodaPrognoz(period, prognoz):
    con = sqlite3.connect('db/malina_orders.db')
    cur = con.cursor()
    cur.execute(f"SELECT * FROM prognoz_bakery WHERE PERIOD='''{period}''';")
    value = cur.fetchall()
    prognoz.emit(value)
    cur.close()
    con.close()

def poiskPeriodaKDayWeekInDB(period, signal):
    con = sqlite3.connect('db/malina_orders.db')
    cur = con.cursor()
    cur.execute(f"SELECT * FROM kdayweek_bakery WHERE PERIOD='''{period}''';")
    value = cur.fetchall()
    if value == []:
        signal.emit('Пусто')
    else:
        if value[0][2] == None:
            signal.emit('Пусто')
        if value[0][3] != None:
            signal.emit('За этот период есть сформированные коэффициенты долей продаж')
    cur.close()
    con.close()

def poiskDataPeriodaKDayWeek(period, prognoz):
    con = sqlite3.connect('db/malina_orders.db')
    cur = con.cursor()
    cur.execute(f"SELECT * FROM kdayweek_bakery WHERE PERIOD='''{period}''';")
    value = cur.fetchall()
    prognoz.emit(value)
    cur.close()
    con.close()

def addPeriodKDayWeekInDB(period):
    con = sqlite3.connect('db/malina_orders.db')
    cur = con.cursor()
    cur.execute(f"INSERT INTO kdayweek_bakery (PERIOD) VALUES ('''{period}''');")
    con.commit()
    cur.close()
    con.close()

def deletePeriodKDayWeekInDB(period):
    con = sqlite3.connect('db/malina_orders.db')
    cur = con.cursor()
    cur.execute(f"DELETE FROM kdayweek_bakery where PERIOD = '''{period}'''")
    con.commit()
    cur.close()
    con.close()

def updateDayWeekInDB(savePeriod, saveHeaders, saveDB, saveNull):
    con = sqlite3.connect('db/malina_orders.db')
    cur = con.cursor()
    cur.execute(f"UPDATE kdayweek_bakery set HEADERSKDAYWEEK = '''{saveHeaders}''', DATAKDAYWEEK = '''{saveDB}''', SAVENULLKDAYWEEK = '''{saveNull}''' where PERIOD = '''{savePeriod}'''")
    con.commit()
    cur.close()
    con.close()

def deleteKDayWeekInDB(period):
    con = sqlite3.connect('db/malina_orders.db')
    cur = con.cursor()
    cur.execute(f"DELETE FROM kdayweek_bakery where PERIOD = '''{period}'''")
    con.commit()
    cur.close()
    con.close()

def saveLayout(kod, name, layuot):
    con = sqlite3.connect('db/malina_orders.db')
    cur = con.cursor()
    cur.execute(f'SELECT * FROM catalog_food WHERE KOD="{kod}";')
    value = cur.fetchall()
    if value != []:
        cur.execute(f"UPDATE catalog_food set NAME = '{name}', LAYOUT = '{layuot}' where KOD = '{kod}'")
    else:
        cur.execute(f"INSERT INTO catalog_food (KOD, NAME, LAYOUT) VALUES ('{kod}', '{name}', '{layuot}');")
    con.commit()
    cur.close()
    con.close()

def poiskKfBakery(kod, kfbakeryotvet):
    con = sqlite3.connect('db/malina_orders.db')
    cur = con.cursor()
    # Проверяем, есть ли такой код
    cur.execute(f'SELECT * FROM catalog_food WHERE KOD="{kod}";')
    value = cur.fetchall()
    if value[0][4] != None:
        kfbakeryotvet.emit(str(value[0][4]))
    else:
        kfbakeryotvet.emit('КФ отсутствует в БД')
    cur.close()
    con.close()

def update_KfBakery(kod_text, kbakery):
    con = sqlite3.connect('db/malina_orders.db')
    cur = con.cursor()
    cur.execute(f"UPDATE catalog_food set KBAKERY = '{kbakery}' where KOD = '{kod_text}'")
    con.commit()
    cur.close()
    con.close()

def poisk_sklada (sklad, kfSkladaotvet):
    con = sqlite3.connect('db/malina_orders.db')
    cur = con.cursor()
    # Проверяем, есть ли такой код
    cur.execute(f'SELECT * FROM catalog_konditerskie WHERE KONDITERSKAY="{sklad}";')
    value = cur.fetchall()
    if value != []:
        kfSkladaotvet.emit(str(value[0][2]))
    else:
        kfSkladaotvet.emit('Склад отсутствует в БД')
    cur.close()
    con.close()

def saveKfBakery(kod, name, layuot):
    con = sqlite3.connect('db/malina_orders.db')
    cur = con.cursor()
    cur.execute(f"UPDATE catalog_food set NAME = '{name}', KBAKERY = '{layuot}' where KOD = '{kod}'")
    con.commit()
    cur.close()
    con.close()

def proverkaNormativa(period, signal):
    con = sqlite3.connect('db/malina_orders.db')
    cur = con.cursor()
    cur.execute(f"SELECT * FROM normativ_bakery WHERE PERIOD='''{period}''';")
    value = cur.fetchall()
    if value == []:
        signal.emit('Пусто')
    else:
        if value[0][2] == None:
            signal.emit('Пусто')
        if value[0][3] != None:
            signal.emit('За этот период есть сформированный норматив')
    cur.close()
    con.close()

def addPeriodNormativInDB(period):
    con = sqlite3.connect('db/malina_orders.db')
    cur = con.cursor()
    cur.execute(f"INSERT INTO normativ_bakery (PERIOD) VALUES ('''{period}''');")
    con.commit()
    cur.close()
    con.close()

def deleteNormativInDB(period):
    con = sqlite3.connect('db/malina_orders.db')
    cur = con.cursor()
    cur.execute(f"DELETE FROM normativ_bakery where PERIOD = '''{period}'''")
    con.commit()
    cur.close()
    con.close()

def updateNormativ(savePeriod, saveHeaders, saveDB, saveNull):
    con = sqlite3.connect('db/malina_orders.db')
    cur = con.cursor()
    cur.execute(
        f"UPDATE normativ_bakery set HEADERSNORMATIV = '''{saveHeaders}''', DATANORMATIV = '''{saveDB}''', SAVENULLNORMATIV = '''{saveNull}''' where PERIOD = '''{savePeriod}'''")
    con.commit()
    cur.close()
    con.close()

def updateKfSklada(sklad, kf):
    con = sqlite3.connect('db/malina_orders.db')
    cur = con.cursor()
    cur.execute(f"UPDATE catalog_konditerskie set KOEFFBAKERY = '{kf}' where KONDITERSKAY = '{sklad}'")
    con.commit()
    cur.close()
    con.close()

def poiskDataPeriodaNormativ(period, signal):
    con = sqlite3.connect('db/malina_orders.db')
    cur = con.cursor()
    cur.execute(f"SELECT * FROM normativ_bakery WHERE PERIOD='''{period}''';")
    value = cur.fetchall()
    signal.emit(value)
    cur.close()
    con.close()

def saveCookieData(year, month, day):
    con = sqlite3.connect('db/malina_orders.db')
    cur = con.cursor()
    cur.execute(f"UPDATE cookie_data set YEAR = '{year}', MONTH = '{month}', DAY = '{day}' where ID = 1")
    con.commit()
    cur.close()
    con.close()

def proverkaData():
    con = sqlite3.connect('db/malina_orders.db')
    cur = con.cursor()
    cur.execute(f"SELECT * FROM cookie_data WHERE ID = 1;")
    value = cur.fetchall()
    if value == [] or value[0][1] == 0:
        value = 0
    cur.close()
    con.close()
    return value

def delCookieData():
    con = sqlite3.connect('db/malina_orders.db')
    cur = con.cursor()
    cur.execute(f"UPDATE cookie_data set YEAR = 0, MONTH = 0, DAY = 0 where ID = 1")
    con.commit()
    cur.close()
    con.close()


# Работаем с пирожными

def poiskPeriodaPrognozaPieInDB(period, signal):
    con = sqlite3.connect('db/malina_orders.db')
    cur = con.cursor()
    cur.execute(f"SELECT * FROM prognoz_pie WHERE PERIOD='''{period}''';")
    value = cur.fetchall()
    if value == []:
        signal.emit('Пусто')
    else:
        if value[0][2] == None:
            signal.emit('Пусто')
        if value[0][3] != None:
            signal.emit('За этот период есть сформированный прогноз')
    cur.close()
    con.close()


def poiskPeriodaKDayWeekPieInDB(period, signal):
    con = sqlite3.connect('db/malina_orders.db')
    cur = con.cursor()
    cur.execute(f"SELECT * FROM kdayweek_pie WHERE PERIOD='''{period}''';")
    value = cur.fetchall()
    if value == []:
        signal.emit('Пусто')
    else:
        if value[0][2] == None:
            signal.emit('Пусто')
        if value[0][3] != None:
            signal.emit('За этот период есть сформированные коэффициенты долей продаж')
    cur.close()
    con.close()

def poiskDataPeriodaPrognozPie(period, prognoz):
    con = sqlite3.connect('db/malina_orders.db')
    cur = con.cursor()
    cur.execute(f"SELECT * FROM prognoz_pie WHERE PERIOD='''{period}''';")
    value = cur.fetchall()
    prognoz.emit(value)
    cur.close()
    con.close()

def poiskDataPeriodaKDayWeekPie(period, prognoz):
    con = sqlite3.connect('db/malina_orders.db')
    cur = con.cursor()
    cur.execute(f"SELECT * FROM kdayweek_pie WHERE PERIOD='''{period}''';")
    value = cur.fetchall()
    prognoz.emit(value)
    cur.close()
    con.close()

def deletePrognozPieInDB(period):
    con = sqlite3.connect('db/malina_orders.db')
    cur = con.cursor()
    cur.execute(f"DELETE FROM prognoz_pie where PERIOD = '''{period}'''")
    con.commit()
    cur.close()
    con.close()

def deleteKDayWeekPieInDB(period):
    con = sqlite3.connect('db/malina_orders.db')
    cur = con.cursor()
    cur.execute(f"DELETE FROM kdayweek_pie where PERIOD = '''{period}'''")
    con.commit()
    cur.close()
    con.close()

def updatePrognozPieInDB(savePeriod, saveHeaders, saveDB, saveNull):
    con = sqlite3.connect('db/malina_orders.db')
    cur = con.cursor()
    cur.execute(f"UPDATE prognoz_pie set HEADERSPROGNOZ = '''{saveHeaders}''', DATAPROGNOZ = '''{saveDB}''', SAVENULLPROGNOZ = '''{saveNull}''' where PERIOD = '''{savePeriod}'''")
    con.commit()
    cur.close()
    con.close()

def deletePeriodPrognozPieInDB(period):
    con = sqlite3.connect('db/malina_orders.db')
    cur = con.cursor()
    cur.execute(f"DELETE FROM prognoz_pie where PERIOD = '''{period}'''")
    con.commit()
    cur.close()
    con.close()

def addPeriodPrognozPieInDB(period):
    con = sqlite3.connect('db/malina_orders.db')
    cur = con.cursor()
    cur.execute(f"INSERT INTO prognoz_pie (PERIOD) VALUES ('''{period}''');")
    con.commit()
    cur.close()
    con.close()

