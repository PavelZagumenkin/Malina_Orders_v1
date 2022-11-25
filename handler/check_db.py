from PyQt6 import QtCore
from handler.db_handler import *

class CheckThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)
    layout = QtCore.pyqtSignal(str)
    period = QtCore.pyqtSignal(str)
    prognoz = QtCore.pyqtSignal(list)


    def thr_login(self, login_text, password_text):
        login(login_text, password_text, self.mysignal)

    def thr_kod(self, kod_text):
        seach_kod(kod_text, self.layout)

    def thr_savePrognoz(self, savePeriod, saveHeaders, saveDB, saveNull):
        addInPrognoz(savePeriod, saveHeaders, saveDB, saveNull)

    def thr_updatePrognoz(self, savePeriod, saveHeaders, saveDB, saveNull):
        updatePrognoz(savePeriod, saveHeaders, saveDB, saveNull)

    def thr_proverkaPerioda(self, period):
        poiskPeriodaInDB(period, self.period)

    def thr_poiskPrognoza(self, period):
        poiskDataPerioda(period, self.prognoz)