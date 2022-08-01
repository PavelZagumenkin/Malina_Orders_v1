import sys
import win32com.client
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtWidgets import QFileDialog
from check_db import *
# from ui.order import Ui_WindowMain
# from ui.bakeryOrders import Ui_WindowBakery


class WindowBakery(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_WindowBakery()
        self.ui.setupUi(self)

    def closeEvent(self, event):
        reply = QMessageBox()
        reply.setWindowTitle("Завершение работы с таблицой")
        reply.setWindowIcon(QtGui.QIcon("image/icon.png"))
        reply.setText("Вы хотите завершить работу с таблицей?")
        reply.setIcon(QMessageBox.Icon.Question)
        reply.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        reply.setDefaultButton(QMessageBox.StandardButton.Cancel)
        otvet = reply.exec()

        if otvet == QMessageBox.StandardButton.Yes:
            WindowMain.closeWindowBakery()
            WindowMain.show()
            event.accept()
        else:
            event.ignore()


class WindowMain(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_WindowMain()
        self.ui.setupUi(self)
        self.WindowBakery = None
        self.ui.label_login_password.setFocus()  # Фокус по умолчанию на тексте
        self.check_db = CheckThread()
        self.check_db.mysignal.connect(self.signal_handler)
        self.ui.btn_login.clicked.connect(self.login)
        self.ui.btn_path_OLAP_P.clicked.connect(self.olap_p)
        self.ui.btn_path_dayWeek_bakery.clicked.connect(self.olap_dayWeek_bakery)
        self.ui.btn_path_dayWeek_pie.clicked.connect(self.olap_dayWeek_pie)
        self.ui.btn_path_dayWeek_cakes.clicked.connect(self.olap_dayWeek_cakes)
        self.ui.btn_path_ost_cakes.clicked.connect(self.olap_ost_cakes)
        self.ui.btn_path_ost_filling.clicked.connect(self.olap_ost_filling)
        self.ui.btn_bakery.clicked.connect(self.bakery_start)
        # self.ui.btn_pie.clicked.connect(self.pie)
        # self.ui.btn_cakes.clicked.connect(self.cakes)
        # self.ui.btn_filling.clicked.connect(self.filling)
        # self.ui.btn_others.clicked.connect(self.others)
        self.ui.btn_exit.clicked.connect(self.exit)

        self.base_line_edit = [self.ui.line_login, self.ui.line_password]
        self.base_fileOLAP_bakery = [self.ui.lineEdit_OLAP_P, self.ui.lineEdit_OLAP_dayWeek_bakery]
        # self.base_fileOLAP_pie = [self.ui.lineEdit_OLAP_P, self.ui.lineEdit_OLAP_dayWeek_pie]
        # self.base_fileOLAP_cakes = [self.ui.lineEdit_OLAP_P, self.ui.lineEdit_OLAP_dayWeek_cakes, self.ui.lineEdit_ost_cakes]

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
            self.ui.p_home.setEnabled(False)
            self.ui.p_settings.setEnabled(True)
            self.ui.stackedWidget.setCurrentIndex(1)
        else:
            self.ui.label_login_password.setStyleSheet("color: rgba(228, 107, 134, 1)");
            self.ui.label_login_password.setText('Неверный логин или пароль!')

    # Передаем данные в обработчик сигналов
    @check_input
    def login(self):
        login_text = self.ui.line_login.text()
        password_text = self.ui.line_password.text()
        self.check_db.thr_login(login_text, password_text)

    # Обрабатываем кнопку выхода
    def exit(self):
        self.ui.p_home.setEnabled(True)
        self.ui.p_settings.setEnabled(False)
        self.ui.label_login_password.setStyleSheet("color: rgb(0, 0, 0)");
        self.ui.label_login_password.setText('Введите логин и пароль')
        self.ui.line_login.clear()
        self.ui.line_password.clear()
        self.ui.stackedWidget.setCurrentIndex(0)

    # Прописываем выбранные пути в поля
    def olap_p(self):
        fileName = QFileDialog.getOpenFileName(self, 'Выберите файл OLAP по продажам', 'Отчеты', 'Excel файл (*.xlsx)')
        self.ui.lineEdit_OLAP_P.setText(fileName[0])
        self.ui.lineEdit_OLAP_P.setStyleSheet("padding-left: 5px; color: rgb(0, 0, 0)")

    def olap_dayWeek_bakery(self):
        fileName = QFileDialog.getOpenFileName(self, 'Выберите файл OLAP по дням недели для пекарни', 'Отчеты',
                                               'Excel файл (*.xlsx)')
        self.ui.lineEdit_OLAP_dayWeek_bakery.setText(fileName[0])
        self.ui.lineEdit_OLAP_dayWeek_bakery.setStyleSheet("padding-left: 5px; color: rgb(0, 0, 0)")

    def olap_dayWeek_pie(self):
        fileName = QFileDialog.getOpenFileName(self, 'Выберите файл OLAP по дням недели для пирожных', 'Отчеты',
                                               'Excel файл (*.xlsx)')
        self.ui.lineEdit_OLAP_dayWeek_pie.setText(fileName[0])
        self.ui.lineEdit_OLAP_dayWeek_pie.setStyleSheet("padding-left: 5px; color: rgb(0, 0, 0)")

    def olap_dayWeek_cakes(self):
        fileName = QFileDialog.getOpenFileName(self, 'Выберите файл OLAP по дням недели для тортов', 'Отчеты',
                                               'Excel файл (*.xlsx)')
        self.ui.lineEdit_OLAP_dayWeek_cakes.setText(fileName[0])
        self.ui.lineEdit_OLAP_dayWeek_cakes.setStyleSheet("padding-left: 5px; color: rgb(0, 0, 0)")

    def olap_ost_cakes(self):
        fileName = QFileDialog.getOpenFileName(self, 'Выберите файл OLAP остатков тортов', 'Отчеты',
                                               'Excel файл (*.xlsx)')
        self.ui.lineEdit_ost_cakes.setText(fileName[0])
        self.ui.lineEdit_ost_cakes.setStyleSheet("padding-left: 5px; color: rgb(0, 0, 0)")

    def olap_ost_filling(self):
        fileName = QFileDialog.getOpenFileName(self, 'Выберите файл OLAP остатков начинки', 'Отчеты',
                                               'Excel файл (*.xlsx)')
        self.ui.lineEdit_ost_filling.setText(fileName[0])
        self.ui.lineEdit_ost_filling.setStyleSheet("padding-left: 5px; color: rgb(0, 0, 0)")

    # Проверяем на пустоту полей для отчетов
    def check_bakeryOLAP(funct_bakery):
        def wrapper(self):
            for line_edit in self.base_fileOLAP_bakery:
                if len(line_edit.text()) == 0:
                    line_edit.setStyleSheet("padding-left: 5px; color: rgba(228, 107, 134, 1)")
                    line_edit.setText('Не выбран файл отчета!')
                    return
                elif line_edit.text() == 'Не выбран файл отчета!':
                    return
            funct_bakery(self)

        return wrapper

    # Обрабытываем кнопку "Выпечка"
    @check_bakeryOLAP
    def bakery_start(self):
        pathOLAP_P = self.ui.lineEdit_OLAP_P.text()
        pathOLAP_dayWeek_bakery = self.ui.lineEdit_OLAP_dayWeek_bakery.text()
        self.bakeryTable(pathOLAP_P, pathOLAP_dayWeek_bakery)

    def bakeryTable(self, pathOLAP_P, pathOLAP_dayWeek_bakery):
        global Excel  # Непонятно работает, или нет
        Excel = win32com.client.Dispatch("Excel.Application")
        global wb_OLAP_P  # Непонятно работает, или нет
        wb_OLAP_P = Excel.Workbooks.Open(pathOLAP_P)
        global wb_OLAP_dayWeek_bakery  # Непонятно работает, или нет
        wb_OLAP_dayWeek_bakery = Excel.Workbooks.Open(pathOLAP_dayWeek_bakery)
        sheet_OLAP_P = wb_OLAP_P.ActiveSheet
        sheet_OLAP_dayWeek_bakery = wb_OLAP_dayWeek_bakery.ActiveSheet
        if sheet_OLAP_P.Name != "OLAP по продажам ОБЩИЙ":
            wb_OLAP_P.Close()
            Excel.Quit()
            self.ui.lineEdit_OLAP_P.setStyleSheet("padding-left: 5px; color: rgba(228, 107, 134, 1)")
            self.ui.lineEdit_OLAP_P.setText('Файл отчета неверный, укажите OLAP по продажам за 7 дней')
        elif sheet_OLAP_dayWeek_bakery.Name != "OLAP по дням недели для Пекарни":
            wb_OLAP_dayWeek_bakery.Close()
            Excel.Quit()
            self.ui.lineEdit_OLAP_dayWeek_bakery.setStyleSheet("padding-left: 5px; color: rgba(228, 107, 134, 1)")
            self.ui.lineEdit_OLAP_dayWeek_bakery.setText(
                'Файл отчета неверный, укажите OLAP по продажам по дня недели для Выпечки пекарни')
        else:
            if self.WindowBakery is None:
                self.WindowBakery = WindowBakery()
                self.WindowBakery.showMaximized()
                WindowMain.hide()

    def closeWindowBakery(self):
        self.WindowBakery = None
        wb_OLAP_P.Close()  # Непонятно работает, или нет
        wb_OLAP_dayWeek_bakery.Close()  # Непонятно работает, или нет
        Excel.Quit()  # Непонятно работает, или нет


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    WindowMain = WindowMain()
    WindowMain.show()
    sys.exit(app.exec())
