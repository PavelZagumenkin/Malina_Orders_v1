import datetime
import win32com.client
import json
from PyQt6 import QtCore, QtWidgets, QtGui
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtWidgets import QMessageBox
from ui.bakery import Ui_WindowBakery
from handler.check_db import CheckThread
import Windows.WindowsViborRazdela
import Windows.WindowsBakeryTablesEdit
import Windows.WindowsBakeryTablesView
import Windows.WindowsBakeryTablesRedact
import Windows.WindowsBakeryTablesDayWeekEdit
import Windows.WindowsBakeryTablesDayWeekView

class WindowBakery(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_WindowBakery()
        self.ui.setupUi(self)
        self.check_db = CheckThread()
        self.check_db.period.connect(self.signal_period)
        self.check_db.prognoz.connect(self.signal_prognoz)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.setWindowIcon(icon)
        TodayDate = datetime.datetime.today()
        EndDay = datetime.datetime.today() + datetime.timedelta(days=6)
        self.ui.dateEdit_startDay.setDate(QtCore.QDate(TodayDate.year, TodayDate.month, TodayDate.day))
        self.ui.dateEdit_EndDay.setDate(QtCore.QDate(EndDay.year, EndDay.month, EndDay.day))
        self.periodDay = [self.ui.dateEdit_startDay.date(), self.ui.dateEdit_EndDay.date()]
        self.ui.dateEdit_startDay.userDateChanged['QDate'].connect(self.setEndDay)
        self.ui.btn_exit_bakery.clicked.connect(self.viborRazdelaOpen)
        self.ui.btn_path_OLAP_P.clicked.connect(self.olap_p)
        self.ui.btn_path_dayWeek_bakery.clicked.connect(self.olap_dayWeek_bakery)
        self.ui.btn_koeff_Prognoz.clicked.connect(self.koeff_Prognoz)
        self.ui.btn_koeff_DayWeek.clicked.connect(self.koeff_DayWeek)
        self.proverkaPeriodaFunc()
        self.ui.btn_prosmotrPrognoz.clicked.connect(self.prognozTablesView)
        self.ui.btn_editPrognoz.clicked.connect(self.prognozTablesRedact)
        self.ui.btn_deletePrognoz.clicked.connect(self.dialogDeletePrognoz)
        self.ui.btn_prosmotr_koeff_DayWeek.clicked.connect(self.dayWeekTablesView)

    def setEndDay(self):
        self.ui.dateEdit_EndDay.setDate(self.ui.dateEdit_startDay.date().addDays(6))
        self.periodDay = [self.ui.dateEdit_startDay.date(), self.ui.dateEdit_EndDay.date()]
        self.proverkaPeriodaFunc()

    def proverkaPeriodaFunc(self):
        if self.proverkaPerioda(self.periodDay) == 0:
            self.ui.label_startDay_and_endDay.setText("Укажите начало периода для формирования данных")
            self.ui.label_startDay_and_endDay.setStyleSheet("color: rgba(0, 0, 0, 1)")
            self.ui.btn_koeff_Prognoz.setEnabled(True)
            self.ui.btn_prosmotrPrognoz.setEnabled(False)
            self.ui.btn_editPrognoz.setEnabled(False)
            self.ui.btn_deletePrognoz.setEnabled(False)
            self.ui.btn_koeff_DayWeek.setEnabled(False)
            self.ui.btn_prosmotr_koeff_DayWeek.setEnabled(False)
            self.ui.btn_edit_koeff_DayWeek.setEnabled(False)
            self.ui.btn_delete_koeff_DayWeek.setEnabled(False)
        elif self.proverkaPerioda(self.periodDay) == 1:
            self.ui.label_startDay_and_endDay.setText('За данный период уже создан прогноз!')
            self.ui.label_startDay_and_endDay.setStyleSheet("color: rgba(228, 107, 134, 1)")
            self.ui.btn_koeff_Prognoz.setEnabled(False)
            self.ui.btn_prosmotrPrognoz.setEnabled(True)
            self.ui.btn_editPrognoz.setEnabled(True)
            self.ui.btn_deletePrognoz.setEnabled(True)
            self.ui.btn_koeff_DayWeek.setEnabled(True)
            self.ui.btn_prosmotr_koeff_DayWeek.setEnabled(False)
            self.ui.btn_edit_koeff_DayWeek.setEnabled(False)
            self.ui.btn_delete_koeff_DayWeek.setEnabled(False)
        elif self.proverkaPerioda(self.periodDay) == 2:
            self.ui.label_startDay_and_endDay.setText(
                'За данный период уже сформированны и прогноз и коэффициенты по дням недели!')
            self.ui.label_startDay_and_endDay.setStyleSheet("color: rgba(228, 107, 134, 1)")
            self.ui.btn_koeff_Prognoz.setEnabled(False)
            self.ui.btn_prosmotrPrognoz.setEnabled(True)
            self.ui.btn_editPrognoz.setEnabled(True)
            self.ui.btn_deletePrognoz.setEnabled(True)
            self.ui.btn_koeff_DayWeek.setEnabled(False)
            self.ui.btn_prosmotr_koeff_DayWeek.setEnabled(True)
            self.ui.btn_edit_koeff_DayWeek.setEnabled(True)
            self.ui.btn_delete_koeff_DayWeek.setEnabled(True)

    def proverkaPerioda(self, period):
        self.check_db.thr_proverkaPerioda(period)
        return otvetPeriod

    def signal_period(self, value):
        global otvetPeriod
        if value == 'Пусто':
            otvetPeriod = 0
        elif value == 'За этот период есть сформированный прогноз':
            otvetPeriod = 1
        elif value == 'Есть и то и то':
            otvetPeriod = 2

    # Диалог выбора файла ОБЩЕГО отчета
    def olap_p(self):
        fileName = QFileDialog.getOpenFileName(self, 'Выберите файл OLAP по продажам', 'Отчеты', 'Excel файл (*.xlsx)')
        self.ui.lineEdit_OLAP_P.setText(fileName[0])
        self.ui.lineEdit_OLAP_P.setStyleSheet("padding-left: 5px; color: rgb(0, 0, 0)")

    # Диалог выбора файла отчета по дням недели
    def olap_dayWeek_bakery(self):
        fileName = QFileDialog.getOpenFileName(self, 'Выберите файл OLAP по дням недели для пекарни', 'Отчеты',
                                               'Excel файл (*.xlsx)')
        self.ui.lineEdit_OLAP_dayWeek_bakery.setText(fileName[0])
        self.ui.lineEdit_OLAP_dayWeek_bakery.setStyleSheet("padding-left: 5px; color: rgb(0, 0, 0)")

    # Проверяем на пустоту поле для OLAP отчета ОБЩИЙ
    def check_prognozOLAP(funct_bakery):
        def wrapper(self):
            if len(self.ui.lineEdit_OLAP_P.text()) == 0 or self.ui.lineEdit_OLAP_P.text() == 'Файл отчета неверный, укажите OLAP по продажам за 7 дней':
                self.ui.lineEdit_OLAP_P.setStyleSheet("padding-left: 5px; color: rgba(228, 107, 134, 1)")
                self.ui.lineEdit_OLAP_P.setText('Не выбран файл отчета!')
                return
            elif self.ui.lineEdit_OLAP_P.text() == 'Не выбран файл отчета!':
                return
            funct_bakery(self)

        return wrapper

    # Обрабытываем кнопку "Установить" для ОБЩЕГО отчета
    @check_prognozOLAP
    def koeff_Prognoz(self):
        pathOLAP_P = self.ui.lineEdit_OLAP_P.text()
        self.prognozTable(pathOLAP_P)

    # Проверка на правильность отчета и запуск таблици с коэффициентами
    def prognozTable(self, pathOLAP_P):
        Excel = win32com.client.Dispatch("Excel.Application")
        wb_OLAP_P = Excel.Workbooks.Open(pathOLAP_P)
        sheet_OLAP_P = wb_OLAP_P.ActiveSheet
        if sheet_OLAP_P.Name != "OLAP отчет для Пекарни":
            wb_OLAP_P.Close()
            Excel.Quit()
            self.ui.lineEdit_OLAP_P.setStyleSheet("padding-left: 5px; color: rgba(228, 107, 134, 1)")
            self.ui.lineEdit_OLAP_P.setText('Файл отчета неверный, укажите OLAP по продажам за 7 дней')
        else:
            wb_OLAP_P.Close()
            Excel.Quit()
            points = self.ui.formLayoutWidget.findChildren(QtWidgets.QCheckBox)
            if self.ui.label_startDay_and_endDay.text() != 'За данный период уже создан прогноз!':
                self.prognozTablesOpen(pathOLAP_P, self.periodDay, points)


    # Проверяем на пустоту поля для отчета по дням недели
    def check_DayWeek(funct_bakery):
        def wrapper(self):
            if len(self.ui.lineEdit_OLAP_dayWeek_bakery.text()) == 0 or self.ui.lineEdit_OLAP_dayWeek_bakery.text() == 'Файл отчета неверный, укажите OLAP по продажам по дням недели за 7 дней':
                self.ui.lineEdit_OLAP_dayWeek_bakery.setStyleSheet("padding-left: 5px; color: rgba(228, 107, 134, 1)")
                self.ui.lineEdit_OLAP_dayWeek_bakery.setText('Не выбран файл отчета!')
                return
            elif self.ui.lineEdit_OLAP_dayWeek_bakery.text() == 'Не выбран файл отчета!':
                return
            funct_bakery(self)

        return wrapper

    # Обрабытываем кнопку "Установить" для отчета по дням недели
    @check_DayWeek
    def koeff_DayWeek(self):
        pathOLAP_DayWeek = self.ui.lineEdit_OLAP_dayWeek_bakery.text()
        self.dayWeekTable(pathOLAP_DayWeek)

    # Проверка на правильность отчета и запуск таблици с коэффициентами
    def dayWeekTable(self, pathOLAP_DayWeek):
        Excel = win32com.client.Dispatch("Excel.Application")
        wb_OLAP_DayWeek = Excel.Workbooks.Open(pathOLAP_DayWeek)
        sheet_OLAP_DayWeek = wb_OLAP_DayWeek.ActiveSheet
        if sheet_OLAP_DayWeek.Name != "OLAP продажи по дням недели для":
            wb_OLAP_DayWeek.Close()
            Excel.Quit()
            self.ui.lineEdit_OLAP_dayWeek_bakery.setStyleSheet("padding-left: 5px; color: rgba(228, 107, 134, 1)")
            self.ui.lineEdit_OLAP_dayWeek_bakery.setText('Файл отчета неверный, укажите OLAP по продажам по дням недели для Выпечки пекарне')
        else:
            wb_OLAP_DayWeek.Close()
            Excel.Quit()
            pointsForDayWeek = json.loads(self.poiskPrognoza(self.periodDay).strip("\'"))
            self.dayWeekTablesOpen(pathOLAP_DayWeek, self.periodDay, pointsForDayWeek)

    def signal_prognoz(self, value):
        global headers
        headers = value[0][2]

    def poiskPrognoza(self, periodDay):
        self.check_db.thr_poiskPrognoza(periodDay)
        return(headers)

    # Закрываем окно настроек, открываем выбор раздела
    def viborRazdelaOpen(self):
        self.close()
        global WindowViborRazdela
        WindowViborRazdela = Windows.WindowsViborRazdela.WindowViborRazdela()
        WindowViborRazdela.show()

    # Закрываем выпечку, открываем таблицу для работы
    def prognozTablesOpen(self, pathOLAP_P, periodDay, points):
        Excel = win32com.client.Dispatch("Excel.Application")
        wb_OLAP_P = Excel.Workbooks.Open(pathOLAP_P)
        sheet_OLAP_P = wb_OLAP_P.ActiveSheet
        firstOLAPRow = sheet_OLAP_P.Range("A:A").Find("Код блюда").Row
        for i in range(len(points)):
            if points[i].isChecked():
                ValidPoints = sheet_OLAP_P.Rows(firstOLAPRow).Find(points[i].text())
                if ValidPoints == None:
                    self.dialogNOvalidOLAP(points[i].text())
                    return
        self.hide()
        global WindowBakeryTablesEdit
        WindowBakeryTablesEdit = Windows.WindowsBakeryTablesEdit.WindowBakeryTablesEdit(pathOLAP_P, periodDay, points)
        WindowBakeryTablesEdit.showMaximized()

    def dialogNOvalidOLAP(self, pointsNoOLAP):
        dialogBox = QMessageBox()
        dialogBox.setText(f"В OLAP-отчете отсутствует кондитерская {pointsNoOLAP}")
        dialogBox.setWindowIcon(QtGui.QIcon("image/icon.png"))
        dialogBox.setWindowTitle('Прекращение работы!')
        dialogBox.setIcon(QMessageBox.Icon.Critical)
        dialogBox.setStandardButtons(QMessageBox.StandardButton.Ok)
        dialogBox.exec()

    def prognozTablesView(self):
        self.hide()
        periodDay = self.periodDay
        global WindowBakeryTablesView
        WindowBakeryTablesView = Windows.WindowsBakeryTablesView.WindowBakeryTableView(periodDay)
        WindowBakeryTablesView.showMaximized()

    def prognozTablesRedact(self):
        self.hide()
        periodDay = self.periodDay
        global WindowBakeryTablesRedact
        WindowBakeryTablesRedact = Windows.WindowsBakeryTablesRedact.WindowBakeryTablesRedact(periodDay)
        WindowBakeryTablesRedact.showMaximized()

    def dialogDeletePrognoz(self):
        dialogBox = QMessageBox()
        dialogBox.setText("Вы действительно хотите удалить сформированный прогноз с изначальными данными?")
        dialogBox.setWindowIcon(QtGui.QIcon("image/icon.png"))
        dialogBox.setWindowTitle('Удаление прогноза продаж')
        dialogBox.setIcon(QMessageBox.Icon.Critical)
        dialogBox.setStandardButtons(QMessageBox.StandardButton.Ok|QMessageBox.StandardButton.Cancel)
        dialogBox.buttonClicked.connect(self.dialogButtonClicked)
        dialogBox.exec()

    def dialogButtonClicked(self, button_clicked):
        if button_clicked.text() == "OK":
            self.prognozTablesDelete()

    def prognozTablesDelete(self):
        period = self.periodDay
        self.check_db.thr_deletePrognoz(period)
        self.proverkaPeriodaFunc()

    def dayWeekTablesOpen(self, pathOLAP_DayWeek, periodDay, points):
        Excel = win32com.client.Dispatch("Excel.Application")
        wb_OLAP_dayWeek_bakery = Excel.Workbooks.Open(pathOLAP_DayWeek)
        sheet_OLAP_dayWeek_bakery = wb_OLAP_dayWeek_bakery.ActiveSheet
        firstOLAPRow = sheet_OLAP_dayWeek_bakery.Range("A:A").Find("День недели").Row
        for i in range(5, len(points)):
            ValidPoints = sheet_OLAP_dayWeek_bakery.Rows(firstOLAPRow).Find(points[i])
            if ValidPoints == None:
                self.dialogNOvalidOLAP(points[i])
                return
        self.hide()
        global WindowBakeryDayWeek
        WindowBakeryDayWeek = Windows.WindowsBakeryTablesDayWeek.WindowBakeryTableDayWeek(pathOLAP_DayWeek, periodDay, points)
        WindowBakeryDayWeek.showMaximized()

    def dayWeekTablesView(self):
        self.hide()
        global WindowBakeryTablesDayWeekView
        WindowBakeryTablesDayWeekView = Windows.WindowsBakeryTablesDayWeekView.WindowBakeryTableDayWeekView(self.periodDay)
        WindowBakeryTablesDayWeekView.showMaximized()

    def dayWeekTablesRedact(self):
        pass