from PyQt6 import QtWidgets, QtCore
from PyQt6.QtCore import Qt
from ui.login import Ui_WindowLogin
from handler.check_db import CheckThread
import Windows.WindowsViborRazdela
import win32com.client
from PyQt6.QtWidgets import QMessageBox
from PyQt6 import QtGui
import sys

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
        try:
            win32com.client.Dispatch("Excel.Application")
        except:
            self.dialogNOExcel()
            sys.exit()

        # Устанавливаем иконку
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.setWindowIcon(icon)

        # Добавляем картинку
        self.label_logo_721 = QtWidgets.QLabel(parent=self.ui.centralwidget)
        self.label_logo_721.setGeometry(QtCore.QRect(0, 0, 731, 721))
        self.label_logo_721.setText("")
        self.label_logo_721.setPixmap(QtGui.QPixmap("image/logo_721.png"))
        self.label_logo_721.setScaledContents(False)
        self.label_logo_721.setObjectName("label_logo_721")

    def dialogNOExcel(self):
        dialogBox = QMessageBox()
        dialogBox.setText(
            "На вашем компьютере не установлен пакет Microsoft Office EXCEL.\nПрограмма не сможет работать корректно.\nПожалуйста установите пакет Microsoft Office EXCEL 10 или выше и перезапустите программу!")
        dialogBox.setWindowIcon(QtGui.QIcon("image/icon.png"))
        dialogBox.setWindowTitle('Прекращение работы!')
        dialogBox.setIcon(QMessageBox.Icon.Critical)
        dialogBox.setStandardButtons(QMessageBox.StandardButton.Ok)
        dialogBox.exec()

    # Проверка пустоты логина и пароля(декоратор)
    def check_input(funct):
        def wrapper(self):
            for line_edit in self.base_line_edit:
                if len(line_edit.text()) == 0:
                    self.ui.label_login_password.setStyleSheet("color: rgba(228, 107, 134, 1)")
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
            WindowViborRazdela = Windows.WindowsViborRazdela.WindowViborRazdela()
            WindowViborRazdela.show()
        else:
            self.ui.label_login_password.setStyleSheet("color: rgba(228, 107, 134, 1)")
            self.ui.label_login_password.setText('Неверный логин или пароль!')

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Return or event.key() == Qt.Key.Key_Enter:
            self.ui.btn_login.click()  # Имитируем нажатие кнопки btn_login