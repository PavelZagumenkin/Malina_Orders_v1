import sys

from PyQt6 import QtCore, QtGui, QtWidgets
# from check_db import CheckThread

from WindowsLogin import WindowLogin
# from WindowsViborRazdela import WindowViborRazdela
# import Windows


class Main():
    def __init__(self):
        super().__init__()
        # self.check_db = CheckThread()
        # self.check_db.layout.connect(self.signal_layout)
        # self.check_db.period.connect(self.signal_period)

    # # Проверка пустоты логина и пароля(декоратор)
    # def check_input(funct):
    #     def wrapper(self):
    #         for line_edit in self.base_line_edit:
    #             if len(line_edit.text()) == 0:
    #                 self.ui.label_login_password.setStyleSheet("color: rgba(228, 107, 134, 1)");
    #                 self.ui.label_login_password.setText('Поле логин или пароль пустое!')
    #                 return
    #         funct(self)
    #
    #     return wrapper

    # Обработчик сигналов
    # def signal_handler(self, value):
    #     if value == 'Успешная авторизация':
    #         self.close()
    #         global WindowViborRazdela
    #         WindowViborRazdela = WindowViborRazdela()
    #         WindowViborRazdela.show()
    #     else:
    #         self.ui.label_login_password.setStyleSheet("color: rgba(228, 107, 134, 1)");
    #         self.ui.label_login_password.setText('Неверный логин или пароль!')

    # # Передаем данные в обработчик сигналов
    # @check_input
    # def login(self):
    #     login_text = self.ui.line_login.text()
    #     password_text = self.ui.line_password.text()
    #     self.check_db.thr_login(login_text, password_text)

    # def signal_layout(self, value):
    #     global layout
    #     if value != 'Код отсутствует в БД':
    #         layout = value
    #     else:
    #         layout = 0
    #
    # # Поиск кода в базе данных
    # def poisk_kod(self, kod):
    #     kod_text = kod
    #     # self.check_db.thr_kod(kod_text)
    #     return int(layout)

    def insertInDB(self, savePeriod, saveHeaders, saveDB):
        # self.check_db.thr_savePrognoz(savePeriod, saveHeaders, saveDB)
        pass

    # # Обработка логаута
    # def logout(self):
    #     WindowViborRazdela.close()
    #     global WindowLogin
    #     WindowLogin = WindowLogin()
    #     WindowLogin.show()
    #     WindowLogin.ui.label_login_password.setFocus()  # Фокус по умолчанию на тексте
    #     WindowLogin.ui.label_login_password.setStyleSheet("color: rgb(0, 0, 0)")
    #     WindowLogin.ui.label_login_password.setText('Введите логин и пароль')
    #     WindowLogin.ui.line_login.clear()
    #     WindowLogin.ui.line_password.clear()
    #
    # # Закрываем выбор раздела, открываем выпечку
    # def bakeryOpen(self):
    #     self.close()
    #     global WindowBakery
    #     WindowBakery = Windows.WindowBakery()
    #     WindowBakery.show()

    # # Закрываем окно настроек, открываем выбор раздела
    # def viborRazdelaOpen(self):
    #     self.close()
    #     # WindowViborRazdela.show()

    # def signal_period(self, value):
    #     global otvetPeriod
    #     if value == 'Пусто':
    #         otvetPeriod = 0
    #     elif value == 'За этот период есть прогноз':
    #         otvetPeriod = 1
    #
    # def proverkaPerioda(self, period):
    #     # self.check_db.thr_proverkaPerioda(period)
    #     return otvetPeriod

    # Закрываем выпечку, открываем таблицу для работы
    def bakeryTablesOpen(self, pathOLAP_P, pathOLAP_dayWeek_bakery, periodDay):
        self.hide()
        global WindowBakeryTables
        # WindowBakeryTables = Windows.WindowBakeryTables(pathOLAP_P, pathOLAP_dayWeek_bakery, periodDay)
        WindowBakeryTables.showMaximized()

    # Закрываем таблицу выпечки и возвращаемся к настройкам
    def closeWindowBakeryTables(self):
        self.close()
        # WindowBakery.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    WindowLogin = WindowLogin()
    WindowLogin.show()
    sys.exit(app.exec())