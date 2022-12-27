from PyQt6 import QtCore
from handler.db_handler import *

class CheckThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)
    layout = QtCore.pyqtSignal(str)
    period = QtCore.pyqtSignal(str)
    prognoz = QtCore.pyqtSignal(list)

    # Форма авторизации(поиск по БД в таблице users)
    def thr_login(self, login_text, password_text):
        login(login_text, password_text, self.mysignal)

    # Расстановка выкладки(поиск в БД в таблице layout)
    def thr_kod(self, kod_text):
        seach_kod(kod_text, self.layout)

    # Добавляем пустой период
    def thr_addPeriod(self, period):
        addPeriodInDB(period)

    # Проверка наличия созданной даты
    def thr_proverkaPerioda(self, period):
        poiskPeriodaInDB(period, self.period)

    # Удаляем пустой период
    def thr_delPeriod(self, period):
        deletePeriodInDB(period)

    # Добавление выкладки в БД
    def thr_updateLayout(self, kod_text, tovar_text, layout):
        update_Layout(kod_text, tovar_text, layout)

    # Сохранение прогноза в БД
    def thr_savePrognoz(self, savePeriod, saveHeaders, saveDB, saveNull):
        addPrognozInDB(savePeriod, saveHeaders, saveDB, saveNull)

    # Обновление прогноза после редактирования
    def thr_updatePrognoz(self, savePeriod, saveHeaders, saveDB, saveNull):
        updatePrognoz(savePeriod, saveHeaders, saveDB, saveNull)

    # Поиск прогноза по периоду
    def thr_poiskPrognoza(self, period):
        poiskDataPerioda(period, self.prognoz)

    # Удаление прогноза из БД
    def thr_deletePrognoz(self, period):
        deletePrognozInDB(period)

    # Поиск коэффициентов по дням недели по периоду
    def thr_saveDayWeek(self, savePeriod, saveHeaders, saveDB, saveNull):
        addDayWeekInDB(savePeriod, saveHeaders, saveDB, saveNull)