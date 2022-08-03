from PyQt6 import QtCore, QtGui, QtWidgets
from main import Main
from ui.login import Ui_WindowLogin
from ui.viborRazdela import Ui_WindowViborRazdela
from ui.bakery import Ui_WindowBakery


class WindowLogin(QtWidgets.QMainWindow, Main):
    def __init__(self):
        super().__init__()
        self.ui = Ui_WindowLogin()
        self.ui.setupUi(self)
        self.ui.label_login_password.setFocus()  # Фокус по умолчанию на тексте
        self.base_line_edit = [self.ui.line_login, self.ui.line_password]
        self.ui.btn_login.clicked.connect(self.login)


class WindowViborRazdela(QtWidgets.QMainWindow, Main):
    def __init__(self):
        super().__init__()
        self.ui = Ui_WindowViborRazdela()
        self.ui.setupUi(self)
        self.ui.btn_exit.clicked.connect(self.logout)
        self.ui.btn_bakery.clicked.connect(self.bakeryOpen)


class WindowBakery(QtWidgets.QMainWindow, Main):
    def __init__(self):
        super().__init__()
        self.ui = Ui_WindowBakery()
        self.ui.setupUi(self)
        self.ui.btn_exit.clicked.connect(self.viborRazdelaOpen)

