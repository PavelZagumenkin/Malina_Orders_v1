from PyQt6 import QtCore
from handler.db_handler import *

class CheckThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)
    layout = QtCore.pyqtSignal(str)

    def thr_login(self, login_text, password_text):
        login(login_text, password_text, self.mysignal)

    def thr_kod(self, kod_text):
        seach_kod(kod_text, self.layout)

    def thr_savePrognoz(self, savePeriod, saveHeaders, saveDB):
        pass

