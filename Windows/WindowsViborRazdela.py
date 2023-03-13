from PyQt6 import QtWidgets, QtGui
from ui.viborRazdela import Ui_WindowViborRazdela
import Windows.WindowsBakery, Windows.WindowsLogin, Windows.WindowsPie


class WindowViborRazdela(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_WindowViborRazdela()
        self.ui.setupUi(self)
        self.ui.btn_exit.clicked.connect(self.logout)
        self.ui.btn_bakery.clicked.connect(self.bakeryOpen)
        self.ui.btn_pie.clicked.connect(self.pieOpen)

        # Устанавливаем иконку
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.setWindowIcon(icon)

    # Обработка логаута
    def logout(self):
        self.close()
        global WindowLogin
        WindowLogin = Windows.WindowsLogin.WindowLogin()
        WindowLogin.show()
        WindowLogin.ui.label_login_password.setFocus()  # Фокус по умолчанию на тексте
        WindowLogin.ui.label_login_password.setStyleSheet("color: rgb(0, 0, 0)")
        WindowLogin.ui.label_login_password.setText('Введите логин и пароль')
        WindowLogin.ui.line_login.clear()
        WindowLogin.ui.line_password.clear()

    # Закрываем выбор раздела, открываем выпечку
    def bakeryOpen(self):
        self.close()
        global WindowBakery
        WindowBakery = Windows.WindowsBakery.WindowBakery()
        WindowBakery.show()

    # Закрываем выбор раздела, открываем пирожные
    def pieOpen(self):
        self.close()
        global WindowPie
        WindowPie = Windows.WindowsPie.WindowPie()
        WindowPie.show()