from PyQt6 import QtCore
from handler.db_handler import *

class CheckThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)
    layout = QtCore.pyqtSignal(str)
    zames = QtCore.pyqtSignal(str)
    period = QtCore.pyqtSignal(str)
    prognoz = QtCore.pyqtSignal(list)
    kfBakery = QtCore.pyqtSignal(str)
    kfSklada = QtCore.pyqtSignal(str)
    normativ = QtCore.pyqtSignal(str)
    normativdata = QtCore.pyqtSignal(list)

    # Форма авторизации(поиск по БД в таблице users)
    def thr_login(self, login_text, password_text):
        login(login_text, password_text, self.mysignal)


    # Работа с Выпечкой

    # Расстановка выкладки(поиск в БД в таблице layout)
    def thr_kod(self, kod_text):
        seach_kod(kod_text, self.layout)

    # Добавляем пустой период
    def thr_addPeriod(self, period):
        addPeriodPrognozInDB(period)

    # Проверка наличия созданной даты
    def thr_proverkaPerioda(self, period):
        poiskPeriodaPrognozaInDB(period, self.period)

    # Удаляем пустой период
    def thr_delPeriod(self, period):
        deletePeriodPrognozInDB(period)

    # Добавление выкладки в БД
    def thr_updateLayout(self, kod_text, tovar_text, layout):
        update_Layout(kod_text, tovar_text, layout)

    # Обновление прогноза после редактирования
    def thr_updatePrognoz(self, savePeriod, saveHeaders, saveDB, saveNull):
        updatePrognozInDB(savePeriod, saveHeaders, saveDB, saveNull)

    # Поиск прогноза по периоду
    def thr_poiskPrognoza(self, period):
        poiskDataPeriodaPrognoz(period, self.prognoz)

    # Удаление прогноза из БД
    def thr_deletePrognoz(self, period):
        deletePrognozInDB(period)

    def thr_addPeriodKDayWeek(self, period):
        addPeriodKDayWeekInDB(period)

    def thr_poiskDataPeriodaKdayWeek(self, period):
        poiskDataPeriodaKDayWeek(period, self.prognoz)

    # Поиск коэффициентов по дням недели по периоду
    def thr_updateDayWeek(self, savePeriod, saveHeaders, saveDB, saveNull):
        updateDayWeekInDB(savePeriod, saveHeaders, saveDB, saveNull)

    def thr_proverkaPeriodaKDayWeek(self, period):
        poiskPeriodaKDayWeekInDB(period, self.period)

    def thr_delPeriodKDayWeek(self, period):
        deletePeriodKDayWeekInDB(period)

    def thr_deleteKDayWeek(self, period):
        deleteKDayWeekInDB(period)

    def thr_saveLayoutInDB(self, kod, name, layout):
        saveLayout(kod, name, layout)

    def thr_saveKfBakeryInDB(self, kod, name, layout):
        saveKfBakery(kod, name, layout)

    def thr_poisk_kfBakery(self, kod):
        poiskKfBakery(kod, self.kfBakery)

    # Добавление кф пекарни в БД
    def thr_updateKfBakery(self, kod_text, kbakery):
        update_KfBakery(kod_text, kbakery)

    def thr_poisk_sklada(self, sklad):
        poisk_sklada(sklad, self.kfSklada)

    def thr_proverkaNormativa(self, period):
        proverkaNormativa(period, self.normativ)

    def thr_addPeriodInNormativ(self, period):
        addPeriodNormativInDB(period)

    def thr_deleteNormativ(self, period):
        deleteNormativInDB(period)

    def thr_updateNormativ(self, savePeriod, saveHeaders, saveDB, saveNull):
        updateNormativ(savePeriod, saveHeaders, saveDB, saveNull)

    def thr_saveKfSkladaInDB(self, sklad, kf):
        updateKfSklada(sklad, kf)

    # Поиск прогноза по периоду
    def thr_poiskNormativa(self, period):
        poiskDataPeriodaNormativ(period, self.normativdata)

    def thr_savecookieData(self, year, month, day):
        saveCookieData(year, month, day)

    def thr_proverkaData(self):
        return proverkaData()

    def thr_deleteCookieData(self):
        delCookieData()


    # Работа с Пирожными
    # Проверка наличия созданной даты
    def thr_proverkaPeriodaPie(self, period):
        poiskPeriodaPrognozaPieInDB(period, self.period)


    def thr_proverkaPeriodaKDayWeekPie(self, period):
        poiskPeriodaKDayWeekPieInDB(period, self.period)

    # Поиск прогноза по периоду
    def thr_poiskPrognozaPie(self, period):
        poiskDataPeriodaPrognozPie(period, self.prognoz)

    def thr_poiskDataPeriodaKdayWeekPie(self, period):
        poiskDataPeriodaKDayWeekPie(period, self.prognoz)

    # Удаление прогноза из БД
    def thr_deletePrognozPie(self, period):
        deletePrognozPieInDB(period)

    def thr_deleteKDayWeekPie(self, period):
        deleteKDayWeekPieInDB(period)

    # Обновление прогноза после редактирования
    def thr_updatePrognozPie(self, savePeriod, saveHeaders, saveDB, saveNull):
        updatePrognozPieInDB(savePeriod, saveHeaders, saveDB, saveNull)

    # Удаляем пустой период
    def thr_delPeriodPie(self, period):
        deletePeriodPrognozPieInDB(period)

    # Добавляем пустой период
    def thr_addPeriodPie(self, period):
        addPeriodPrognozPieInDB(period)

    def thr_zames(self, kod_text):
        seach_zames(kod_text, self.zames)

    def thr_updateZames(self, kod_text, zames):
        update_zames(kod_text, zames)

    def thr_saveLayoutZamesInDB(self, kod, name, layout, zames):
        saveLayoutZames(kod, name, layout, zames)

    def thr_addPeriodKDayWeekPie(self, period):
        addPeriodKDayWeekPieInDB(period)

    def thr_delPeriodKDayWeekPie(self, period):
        deletePeriodKDayWeekPieInDB(period)

    def thr_updateDayWeekPie(self, savePeriod, saveHeaders, saveDB, saveNull):
        updateDayWeekPieInDB(savePeriod, saveHeaders, saveDB, saveNull)



