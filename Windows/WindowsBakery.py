import datetime
import win32com.client
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QFileDialog
from ui.bakery import Ui_WindowBakery
from handler.check_db import CheckThread
import Windows.WindowsViborRazdela
import Windows.WindowsBakeryTables

class WindowBakery(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_WindowBakery()
        self.ui.setupUi(self)
        self.check_db = CheckThread()
        self.check_db.period.connect(self.signal_period)
        self.base_fileOLAP_bakery = [self.ui.lineEdit_OLAP_P, self.ui.lineEdit_OLAP_dayWeek_bakery]
        TodayDate = datetime.datetime.today()
        EndDay = datetime.datetime.today() + datetime.timedelta(days=6)
        self.ui.dateEdit_startDay.setDate(QtCore.QDate(TodayDate.year, TodayDate.month, TodayDate.day))
        self.ui.dateEdit_EndDay.setDate(QtCore.QDate(EndDay.year, EndDay.month, EndDay.day))
        self.periodDay = [self.ui.dateEdit_startDay.date(), self.ui.dateEdit_EndDay.date()]
        self.ui.dateEdit_startDay.userDateChanged['QDate'].connect(self.setEndDay)
        self.ui.btn_exit_bakery.clicked.connect(self.viborRazdelaOpen)
        self.ui.btn_path_OLAP_P.clicked.connect(self.olap_p)
        self.ui.btn_path_dayWeek_bakery.clicked.connect(self.olap_dayWeek_bakery)
        self.ui.btn_koeff_bakery.clicked.connect(self.koeff_bakery_start)
        if self.proverkaPerioda(self.periodDay) == 0:
            self.ui.label_startDay_and_endDay.setText("Укажите начало периода для формирования данных")
            self.ui.label_startDay_and_endDay.setStyleSheet("color: rgba(0, 0, 0, 1)")
            self.ui.btn_prosmotrPrognoz.setEnabled(False)
        elif self.proverkaPerioda(self.periodDay) == 1:
            self.ui.label_startDay_and_endDay.setText('За данный период уже создан прогноз!')
            self.ui.label_startDay_and_endDay.setStyleSheet("color: rgba(228, 107, 134, 1)")
            self.ui.btn_prosmotrPrognoz.setEnabled(True)

    def setEndDay(self):
        self.ui.dateEdit_EndDay.setDate(self.ui.dateEdit_startDay.date().addDays(6))
        self.periodDay = [self.ui.dateEdit_startDay.date(), self.ui.dateEdit_EndDay.date()]
        if self.proverkaPerioda(self.periodDay) == 0:
            self.ui.label_startDay_and_endDay.setText("Укажите начало периода для формирования данных")
            self.ui.label_startDay_and_endDay.setStyleSheet("color: rgba(0, 0, 0, 1)")
            self.ui.btn_prosmotrPrognoz.setEnabled(False)
        elif self.proverkaPerioda(self.periodDay) == 1:
            self.ui.label_startDay_and_endDay.setText('За данный период уже создан прогноз!')
            self.ui.label_startDay_and_endDay.setStyleSheet("color: rgba(228, 107, 134, 1)")
            self.ui.btn_prosmotrPrognoz.setEnabled(True)

    # Закрываем окно настроек, открываем выбор раздела
    def viborRazdelaOpen(self):
        self.close()
        global WindowViborRazdela
        WindowViborRazdela = Windows.WindowsViborRazdela.WindowViborRazdela()
        WindowViborRazdela.show()

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

    def proverkaPerioda(self, period):
        self.check_db.thr_proverkaPerioda(period)
        return otvetPeriod

    def signal_period(self, value):
        global otvetPeriod
        if value == 'Пусто':
            otvetPeriod = 0
        elif value == 'За этот период есть прогноз':
            otvetPeriod = 1

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
            if self.ui.label_startDay_and_endDay.text() != 'За данный период уже создан прогноз!':
                self.bakeryTablesOpen(pathOLAP_P, pathOLAP_dayWeek_bakery, self.periodDay)

    # Закрываем выпечку, открываем таблицу для работы
    def bakeryTablesOpen(self, pathOLAP_P, pathOLAP_dayWeek_bakery, periodDay):
        self.hide()
        global WindowBakeryTables
        WindowBakeryTables = Windows.WindowsBakeryTables.WindowBakeryTables(pathOLAP_P, pathOLAP_dayWeek_bakery, periodDay)
        WindowBakeryTables.showMaximized()