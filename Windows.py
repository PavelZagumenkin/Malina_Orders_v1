from PyQt6 import QtCore, QtGui, QtWidgets
import win32com.client
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtWidgets import QTableView
from main import Main
from ui.login import Ui_WindowLogin
from ui.viborRazdela import Ui_WindowViborRazdela
from ui.bakery import Ui_WindowBakery
from ui.bakeryTables import Ui_WindowBakeryTables


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
        self.ui.btn_exit_bakery.clicked.connect(self.viborRazdelaOpen)
        self.ui.btn_path_OLAP_P.clicked.connect(self.olap_p)
        self.ui.btn_path_dayWeek_bakery.clicked.connect(self.olap_dayWeek_bakery)
        self.ui.btn_koeff_bakery.clicked.connect(self.koeff_bakery_start)
        self.base_fileOLAP_bakery = [self.ui.lineEdit_OLAP_P, self.ui.lineEdit_OLAP_dayWeek_bakery]

    def olap_p(self):
        fileName = QFileDialog.getOpenFileName(self, 'Выберите файл OLAP по продажам', 'Отчеты', 'Excel файл (*.xlsx)')
        self.ui.lineEdit_OLAP_P.setText(fileName[0])
        self.ui.lineEdit_OLAP_P.setStyleSheet("padding-left: 5px; color: rgb(0, 0, 0)")

    def olap_dayWeek_bakery(self):
        fileName = QFileDialog.getOpenFileName(self, 'Выберите файл OLAP по дням недели для пекарни', 'Отчеты',
                                               'Excel файл (*.xlsx)')
        self.ui.lineEdit_OLAP_dayWeek_bakery.setText(fileName[0])
        self.ui.lineEdit_OLAP_dayWeek_bakery.setStyleSheet("padding-left: 5px; color: rgb(0, 0, 0)")

    # Проверяем на пустоту полей для отчетов
    def check_bakeryOLAP(funct_bakery):
        def wrapper(self):
            for line_edit in self.base_fileOLAP_bakery:
                if len(line_edit.text()) == 0 or line_edit.text() == 'Файл отчета неверный, укажите OLAP по продажам за 7 дней' or line_edit.text() == 'Файл отчета неверный, укажите OLAP по продажам по дня недели для Выпечки пекарни' or line_edit.text() == 'Вы выбрали одинаковые файлы отчета. Хватит издеваться над программой!':
                    line_edit.setStyleSheet("padding-left: 5px; color: rgba(228, 107, 134, 1)")
                    line_edit.setText('Не выбран файл отчета!')
                    return
                elif line_edit.text() == 'Не выбран файл отчета!':
                    return
            funct_bakery(self)

        return wrapper

    # Обрабытываем кнопку "Выпечка"
    @check_bakeryOLAP
    def koeff_bakery_start(self):
        pathOLAP_P = self.ui.lineEdit_OLAP_P.text()
        pathOLAP_dayWeek_bakery = self.ui.lineEdit_OLAP_dayWeek_bakery.text()
        if pathOLAP_P != pathOLAP_dayWeek_bakery:
            self.bakeryTable(pathOLAP_P, pathOLAP_dayWeek_bakery)
        else:
            self.ui.lineEdit_OLAP_P.setStyleSheet("padding-left: 5px; color: rgba(228, 107, 134, 1)")
            self.ui.lineEdit_OLAP_P.setText('Вы выбрали одинаковые файлы отчета. Хватит издеваться над программой!')
            self.ui.lineEdit_OLAP_dayWeek_bakery.setStyleSheet("padding-left: 5px; color: rgba(228, 107, 134, 1)")
            self.ui.lineEdit_OLAP_dayWeek_bakery.setText(
                'Вы выбрали одинаковые файлы отчета. Хватит издеваться над программой!')

    def bakeryTable(self, pathOLAP_P, pathOLAP_dayWeek_bakery):
        Excel = win32com.client.Dispatch("Excel.Application")
        wb_OLAP_P = Excel.Workbooks.Open(pathOLAP_P)
        wb_OLAP_dayWeek_bakery = Excel.Workbooks.Open(pathOLAP_dayWeek_bakery)
        sheet_OLAP_P = wb_OLAP_P.ActiveSheet
        sheet_OLAP_dayWeek_bakery = wb_OLAP_dayWeek_bakery.ActiveSheet

        if sheet_OLAP_P.Name != "OLAP по продажам ОБЩИЙ":
            wb_OLAP_P.Close()
            wb_OLAP_dayWeek_bakery.Close()
            Excel.Quit()
            self.ui.lineEdit_OLAP_P.setStyleSheet("padding-left: 5px; color: rgba(228, 107, 134, 1)")
            self.ui.lineEdit_OLAP_P.setText('Файл отчета неверный, укажите OLAP по продажам за 7 дней')
        elif sheet_OLAP_dayWeek_bakery.Name != "OLAP по дням недели для Пекарни":
            wb_OLAP_P.Close()
            wb_OLAP_dayWeek_bakery.Close()
            Excel.Quit()
            self.ui.lineEdit_OLAP_dayWeek_bakery.setStyleSheet("padding-left: 5px; color: rgba(228, 107, 134, 1)")
            self.ui.lineEdit_OLAP_dayWeek_bakery.setText(
                'Файл отчета неверный, укажите OLAP по продажам по дня недели для Выпечки пекарни')
        else:
            wb_OLAP_P.Close()
            wb_OLAP_dayWeek_bakery.Close()
            Excel.Quit()
            self.bakeryTablesOpen(pathOLAP_P, pathOLAP_dayWeek_bakery)


class WindowBakeryTables(QtWidgets.QMainWindow, Main):
    def __init__(self, pathOLAP_P, pathOLAP_dayWeek_bakery):
        super().__init__()
        self.ui = Ui_WindowBakeryTables()
        self.ui.setupUi(self)
        Excel = win32com.client.Dispatch("Excel.Application")
        wb_OLAP_P = Excel.Workbooks.Open(pathOLAP_P)
        wb_OLAP_dayWeek_bakery = Excel.Workbooks.Open(pathOLAP_dayWeek_bakery)
        sheet_OLAP_P = wb_OLAP_P.ActiveSheet
        sheet_OLAP_dayWeek_bakery = wb_OLAP_dayWeek_bakery.ActiveSheet



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
            self.closeWindowBakeryTables()
            event.accept()
        else:
            event.ignore()
