from PyQt6 import QtWidgets
from ui.login import Ui_WindowLogin
from check_db import CheckThread
import WindowsViborRazdela

class WindowLogin(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_WindowLogin()
        self.ui.setupUi(self)
        self.check_db = CheckThread()
        self.check_db.mysignal.connect(self.signal_handler)
        self.ui.label_login_password.setFocus()  # Фокус по умолчанию на тексте
        self.base_line_edit = [self.ui.line_login, self.ui.line_password]
        self.ui.btn_login.clicked.connect(self.login)

    # Проверка пустоты логина и пароля(декоратор)
    def check_input(funct):
        def wrapper(self):
            for line_edit in self.base_line_edit:
                if len(line_edit.text()) == 0:
                    self.ui.label_login_password.setStyleSheet("color: rgba(228, 107, 134, 1)");
                    self.ui.label_login_password.setText('Поле логин или пароль пустое!')
                    return
            funct(self)

        return wrapper

    # Передаем данные в обработчик сигналов
    @check_input
    def login(self):
        login_text = self.ui.line_login.text()
        password_text = self.ui.line_password.text()
        self.check_db.thr_login(login_text, password_text)


    # Обработчик сигналов
    def signal_handler(self, value):
        if value == 'Успешная авторизация':
            self.close()
            global WindowViborRazdela
            WindowViborRazdela = WindowsViborRazdela.WindowViborRazdela()
            WindowViborRazdela.show()
        else:
            self.ui.label_login_password.setStyleSheet("color: rgba(228, 107, 134, 1)");
            self.ui.label_login_password.setText('Неверный логин или пароль!')