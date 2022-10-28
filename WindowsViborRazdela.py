from PyQt6 import QtWidgets
from ui.viborRazdela import Ui_WindowViborRazdela
import WindowsLogin
import WindowsBakery

class WindowViborRazdela(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_WindowViborRazdela()
        self.ui.setupUi(self)
        self.ui.btn_exit.clicked.connect(self.logout)
        self.ui.btn_bakery.clicked.connect(self.bakeryOpen)

    # Обработка логаута
    def logout(self):
        self.close()
        global WindowLogin
        WindowLogin = WindowsLogin.WindowLogin()
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
        WindowBakery = WindowsBakery.WindowBakery()
        WindowBakery.show()