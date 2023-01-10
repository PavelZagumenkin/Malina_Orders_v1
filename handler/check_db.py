from PyQt6 import QtCore
from handler.db_handler import *

class CheckThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)
    layout = QtCore.pyqtSignal(str)
    period = QtCore.pyqtSignal(str)
    prognoz = QtCore.pyqtSignal(list)
    kfbakery = QtCore.pyqtSignal(str)

    # Форма авторизации(поиск по БД в таблице users)
    def thr_login(self, login_text, password_text):
        login(login_text, password_text, self.mysignal)

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

    def thr_poisk_kfbakery(self, kod):
        poiskKfBakery(kod, self.kfbakery)

    # Добавление кф пекарни в БД
    def thr_updateKfbakery(self, kod_text, kbakery):
        update_Kfbakery(kod_text, kbakery)