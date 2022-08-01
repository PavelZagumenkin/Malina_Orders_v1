import sys
import win32com.client
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtWidgets import QFileDialog
from check_db import *
from WindowLogin import *
from ui.viborRazdela import Ui_WindowViborRazdela
from ui.bakery import Ui_WindowBakery


class Main():
    def __init__(self):
        super().__init__()
        self.check_db = CheckThread()
        self.check_db.mysignal.connect(self.signal_handler)
        self.WindowsLogin = None

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

    # Обработчик сигналов
    def signal_handler(self, value):
        if value == 'Успешная авторизация':
            WindowLogin.close()
            self.WindowViborRazdela = WindowViborRazdela()
            self.WindowViborRazdela.show()
        else:
            WindowLogin.ui.label_login_password.setStyleSheet("color: rgba(228, 107, 134, 1)");
            WindowLogin.ui.label_login_password.setText('Неверный логин или пароль!')

    # Передаем данные в обработчик сигналов
    @check_input
    def login(self):
        login_text = WindowLogin.ui.line_login.text()
        password_text = WindowLogin.ui.line_password.text()
        self.check_db.thr_login(login_text, password_text)

    def bakeryOpen(self):
        WindowViborRazdela.close(self)
        self.WindowBakery = WindowBakery()
        self.WindowBakery.show()

    def viborRazdelaOpen(self):
        WindowBakery.close(self)
        self.WindowViborRazdela = WindowViborRazdela()
        self.WindowViborRazdela.show()


    def logout(self):
        WindowViborRazdela.close(self)
        WindowLogin.show()
        WindowLogin.ui.label_login_password.setFocus()  # Фокус по умолчанию на тексте
        WindowLogin.ui.label_login_password.setStyleSheet("color: rgb(0, 0, 0)")
        WindowLogin.ui.label_login_password.setText('Введите логин и пароль')
        WindowLogin.ui.line_login.clear()
        WindowLogin.ui.line_password.clear()



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


# class WindowBakeryTables(QtWidgets.QMainWindow, Main):
#     def __init__(self):
#         super().__init__()
#         self.ui = Ui_WindowBakery()
#         self.ui.setupUi(self)

# def closeEvent(self, event):
#     reply = QMessageBox()
#     reply.setWindowTitle("Завершение работы с таблицой")
#     reply.setWindowIcon(QtGui.QIcon("image/icon.png"))
#     reply.setText("Вы хотите завершить работу с таблицей?")
#     reply.setIcon(QMessageBox.Icon.Question)
#     reply.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
#     reply.setDefaultButton(QMessageBox.StandardButton.Cancel)
#     otvet = reply.exec()
#
#     if otvet == QMessageBox.StandardButton.Yes:
#         WindowMain.closeWindowBakery()
#         WindowMain.show()
#         event.accept()
#     else:
#         event.ignore()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    WindowLogin = WindowLogin()
    WindowLogin.show()
    sys.exit(app.exec())
