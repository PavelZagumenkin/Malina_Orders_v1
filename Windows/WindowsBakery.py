import datetime
import os
import shutil
from math import ceil
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
import Windows.WindowsBakeryTablesDayWeekRedact
import Windows.WindowsBakeryNormativEdit
import Windows.WindowsBakeryNormativRedact


class WindowBakery(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_WindowBakery()
        self.ui.setupUi(self)
        self.check_db = CheckThread()
        self.check_db.period.connect(self.signal_period)
        self.check_db.prognoz.connect(self.signal_prognoz)
        self.check_db.normativ.connect(self.signal_normativ)
        self.check_db.normativdata.connect(self.signal_normativdata)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.setWindowIcon(icon)
        if self.proverkaData() != 0:
            TodayDate = QtCore.QDate(self.proverkaData()[0], self.proverkaData()[1], self.proverkaData()[2])
            self.ui.dateEdit_startDay.setDate(TodayDate)
            EndDay = TodayDate.addDays(6)
            self.ui.dateEdit_EndDay.setDate(EndDay)
        else:
            TodayDate = datetime.datetime.today()
            EndDay = datetime.datetime.today() + datetime.timedelta(days=6)
            self.ui.dateEdit_startDay.setDate(QtCore.QDate(TodayDate.year, TodayDate.month, TodayDate.day))
            self.ui.dateEdit_EndDay.setDate(QtCore.QDate(EndDay.year, EndDay.month, EndDay.day))
        self.periodDay = [self.ui.dateEdit_startDay.date(), self.ui.dateEdit_EndDay.date()]
        self.ui.progressBar.hide()
        self.ui.dateEdit_startDay.userDateChanged['QDate'].connect(self.setEndDay)
        self.ui.btn_exit_bakery.clicked.connect(self.viborRazdelaOpen)
        self.ui.btn_path_OLAP_P.clicked.connect(self.olap_p)
        self.ui.btn_path_dayWeek_bakery.clicked.connect(self.olap_dayWeek_bakery)
        self.ui.btn_koeff_Prognoz.clicked.connect(self.koeff_Prognoz)
        self.ui.btn_koeff_DayWeek.clicked.connect(self.koeff_DayWeek)
        self.proverkaPeriodaPrognozFunc()
        self.proverkaPeriodaKDayWeekFunc()
        self.proverkaNormativaFunc()
        self.ui.btn_prosmotrPrognoz.clicked.connect(self.prognozTablesView)
        self.ui.btn_editPrognoz.clicked.connect(self.prognozTablesRedact)
        self.ui.btn_deletePrognoz.clicked.connect(self.dialogDeletePrognoz)
        self.ui.btn_prosmotr_koeff_DayWeek.clicked.connect(self.dayWeekTablesView)
        self.ui.btn_edit_koeff_DayWeek.clicked.connect(self.dayWeekTablesRedact)
        self.ui.btn_delete_koeff_DayWeek.clicked.connect(self.dialogDeleteKDayWeek)
        self.ui.btn_Normativ.clicked.connect(self.normativ)
        self.ui.btn_editNormativ.clicked.connect(self.normativTablesRedact)
        self.ui.btn_deleteNormativ.clicked.connect(self.dialogDeleteNormativ)
        self.ui.btn_download_Normativ.clicked.connect(self.saveFileDialogNormativ)
        self.ui.btn_download_Layout.clicked.connect(self.saveFileDialogLayout)

    def proverkaData(self):
        if self.check_db.thr_proverkaData() == 0:
            return 0
        else:
            year = self.check_db.thr_proverkaData()[0][1]
            month = self.check_db.thr_proverkaData()[0][2]
            day = self.check_db.thr_proverkaData()[0][3]
            date = [year, month, day]
            return date

    def setEndDay(self):
        self.check_db.thr_savecookieData(int(self.ui.dateEdit_startDay.date().toString('yyyy')), int(self.ui.dateEdit_startDay.date().toString('MM')), int(self.ui.dateEdit_startDay.date().toString('dd')))
        self.ui.dateEdit_EndDay.setDate(self.ui.dateEdit_startDay.date().addDays(6))
        self.periodDay = [self.ui.dateEdit_startDay.date(), self.ui.dateEdit_EndDay.date()]
        self.proverkaPeriodaPrognozFunc()
        self.proverkaPeriodaKDayWeekFunc()
        self.proverkaNormativaFunc()

    def proverkaPeriodaPrognozFunc(self):
        if self.proverkaPerioda(self.periodDay) == 0:
            self.ui.btn_koeff_Prognoz.setEnabled(True)
            self.ui.btn_prosmotrPrognoz.setEnabled(False)
            self.ui.btn_editPrognoz.setEnabled(False)
            self.ui.btn_deletePrognoz.setEnabled(False)
            self.ui.btn_Normativ.setEnabled(False)
            self.ui.btn_download_Layout.setEnabled(False)
        elif self.proverkaPerioda(self.periodDay) == 1:
            self.ui.btn_koeff_Prognoz.setEnabled(False)
            self.ui.btn_prosmotrPrognoz.setEnabled(True)
            self.ui.btn_editPrognoz.setEnabled(True)
            self.ui.btn_deletePrognoz.setEnabled(True)
            if self.proverkaNormativa(self.periodDay) == 0 and self.proverkaPeriodaKDayWeek(self.periodDay) == 1:
                self.ui.btn_Normativ.setEnabled(True)
            if self.proverkaPeriodaKDayWeek(self.periodDay) == 1:
                self.ui.btn_download_Layout.setEnabled(True)
            else:
                self.ui.btn_download_Layout.setEnabled(False)

    def proverkaPeriodaKDayWeekFunc(self):
        if self.proverkaPeriodaKDayWeek(self.periodDay) == 0:
            self.ui.btn_koeff_DayWeek.setEnabled(True)
            self.ui.btn_prosmotr_koeff_DayWeek.setEnabled(False)
            self.ui.btn_edit_koeff_DayWeek.setEnabled(False)
            self.ui.btn_delete_koeff_DayWeek.setEnabled(False)
            self.ui.btn_download_Layout.setEnabled(False)
            self.ui.btn_Normativ.setEnabled(False)
        elif self.proverkaPeriodaKDayWeek(self.periodDay) == 1:
            self.ui.btn_koeff_DayWeek.setEnabled(False)
            self.ui.btn_prosmotr_koeff_DayWeek.setEnabled(True)
            self.ui.btn_edit_koeff_DayWeek.setEnabled(True)
            self.ui.btn_delete_koeff_DayWeek.setEnabled(True)
            if self.proverkaPerioda(self.periodDay) == 1:
                self.ui.btn_download_Layout.setEnabled(True)
                self.ui.btn_Normativ.setEnabled(True)
            else:
                self.ui.btn_download_Layout.setEnabled(False)

    def proverkaNormativaFunc(self):
        if self.proverkaNormativa(self.periodDay) == 0:
            self.ui.btn_editNormativ.setEnabled(False)
            self.ui.btn_download_Normativ.setEnabled(False)
            self.ui.btn_deleteNormativ.setEnabled(False)
        elif self.proverkaNormativa(self.periodDay) == 1:
            self.ui.btn_Normativ.setEnabled(False)
            self.ui.btn_editNormativ.setEnabled(True)
            self.ui.btn_deleteNormativ.setEnabled(True)
            self.ui.btn_download_Normativ.setEnabled(True)


    def proverkaNormativa(self, period):
        self.check_db.thr_proverkaNormativa(period)
        return otvetNormativ

    def signal_normativ(self, value):
        global otvetNormativ
        if value == 'Пусто':
            otvetNormativ = 0
        elif value == 'За этот период есть сформированный норматив':
            otvetNormativ = 1

    def proverkaPerioda(self, period):
        self.check_db.thr_proverkaPerioda(period)
        return otvetPeriod

    def proverkaPeriodaKDayWeek(self, period):
        self.check_db.thr_proverkaPeriodaKDayWeek(period)
        return otvetPeriod

    def signal_period(self, value):
        global otvetPeriod
        if value == 'Пусто':
            otvetPeriod = 0
        elif value == 'За этот период есть сформированный прогноз' or value == 'За этот период есть сформированные коэффициенты долей продаж':
            otvetPeriod = 1

    # Диалог выбора файла ОБЩЕГО отчета
    def olap_p(self):
        fileName = QFileDialog.getOpenFileName(self, 'Выберите файл OLAP по продажам', os.path.expanduser(
                '~') + r'\Desktop', 'Excel файл (*.xlsx)')
        self.ui.lineEdit_OLAP_P.setText(fileName[0])
        self.ui.lineEdit_OLAP_P.setStyleSheet("padding-left: 5px; color: rgb(0, 0, 0)")

    # Диалог выбора файла отчета по дням недели
    def olap_dayWeek_bakery(self):
        fileName = QFileDialog.getOpenFileName(self, 'Выберите файл OLAP по дням недели для пекарни', os.path.expanduser(
                '~') + r'\Desktop', 'Excel файл (*.xlsx)')
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
        if sheet_OLAP_P.Name != "OLAP отчет для Выпечки":
            wb_OLAP_P.Close()
            Excel.Quit()
            self.ui.lineEdit_OLAP_P.setStyleSheet("padding-left: 5px; color: rgba(228, 107, 134, 1)")
            self.ui.lineEdit_OLAP_P.setText('Файл отчета неверный, укажите OLAP по продажам за 7 дней')
        else:
            wb_OLAP_P.Close()
            Excel.Quit()
            self.prognozTablesOpen(pathOLAP_P, self.periodDay)

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
        if sheet_OLAP_DayWeek.Name != "OLAP по дням недели для Выпечки":
            wb_OLAP_DayWeek.Close()
            Excel.Quit()
            self.ui.lineEdit_OLAP_dayWeek_bakery.setStyleSheet("padding-left: 5px; color: rgba(228, 107, 134, 1)")
            self.ui.lineEdit_OLAP_dayWeek_bakery.setText(
                'Файл отчета неверный, укажите OLAP по продажам по дням недели для Выпечки пекарне')
        else:
            wb_OLAP_DayWeek.Close()
            Excel.Quit()
            self.dayWeekTablesOpen(pathOLAP_DayWeek, self.periodDay)

    def signal_prognoz(self, value):
        global headers
        headers = value[0][2]
        data = value[0][3]
        global fullData
        fullData = [headers, data]

    def poiskPrognoza(self, periodDay):
        self.check_db.thr_poiskPrognoza(periodDay)
        return (headers)

    def poiskKDayWeek(self, periodDay):
        self.check_db.thr_poiskDataPeriodaKdayWeek(periodDay)
        return (headers)

    def poiskPrognozaExcel(self, periodDay):
        self.check_db.thr_poiskPrognoza(periodDay)
        return (fullData)

    def poiskKDayWeekExcel(self, periodDay):
        self.check_db.thr_poiskDataPeriodaKdayWeek(periodDay)
        return (fullData)

    # Закрываем окно настроек, открываем выбор раздела
    def viborRazdelaOpen(self):
        self.close()
        global WindowViborRazdela
        WindowViborRazdela = Windows.WindowsViborRazdela.WindowViborRazdela()
        WindowViborRazdela.show()

    # Закрываем выпечку, открываем таблицу для работы
    def prognozTablesOpen(self, pathOLAP_P, periodDay):
        Excel = win32com.client.Dispatch("Excel.Application")
        wb_OLAP_P = Excel.Workbooks.Open(pathOLAP_P)
        sheet_OLAP_P = wb_OLAP_P.ActiveSheet
        firstOLAPRow = sheet_OLAP_P.Range("A:A").Find("Код блюда").Row
        pointsCheck = self.ui.formLayoutWidget.findChildren(QtWidgets.QCheckBox)
        if self.proverkaPeriodaKDayWeek(self.periodDay) == 0:
            points = []
            for i in range(len(pointsCheck)):
                if pointsCheck[i].isChecked():
                    ValidPoints = sheet_OLAP_P.Rows(firstOLAPRow).Find(pointsCheck[i].text())
                    if ValidPoints == None:
                        self.dialogNOvalidOLAP(pointsCheck[i].text())
                        return
                    points.append(pointsCheck[i].text())
            pointsNonCheck = []
            for i in range(len(pointsCheck)):
                if not pointsCheck[i].isChecked():
                    pointsNonCheck.append(pointsCheck[i].text())
        else:
            points = json.loads(self.poiskKDayWeek(self.periodDay).strip("\'"))
            del points[0:2]
            for i in range(len(points)):
                ValidPoints = sheet_OLAP_P.Rows(firstOLAPRow).Find(points[i])
                if ValidPoints == None:
                    self.dialogNOvalidOLAP(points[i])
                    return
            pointsNonCheck = []
            for i in range (len(pointsCheck)):
                if not (pointsCheck[i].text() in points):
                    pointsNonCheck.append(pointsCheck[i].text())
        self.hide()
        global WindowBakeryTablesEdit
        WindowBakeryTablesEdit = Windows.WindowsBakeryTablesEdit.WindowBakeryTablesEdit(pathOLAP_P, periodDay, pointsNonCheck)
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
        self.normativTablesDelete()
        self.hide()
        periodDay = self.periodDay
        global WindowBakeryTablesRedact
        WindowBakeryTablesRedact = Windows.WindowsBakeryTablesRedact.WindowBakeryTablesRedact(periodDay)
        WindowBakeryTablesRedact.showMaximized()

    def normativTablesRedact(self):
        self.hide()
        periodDay = self.periodDay
        global WindowNormativTablesRedact
        WindowNormativTablesRedact = Windows.WindowsBakeryNormativRedact.WindowBakeryNormativRedact(periodDay)
        WindowNormativTablesRedact.showMaximized()

    def dialogDeletePrognoz(self):
        dialogBox = QMessageBox()
        dialogBox.setText("Вы действительно хотите удалить сформированный прогноз и норматив(если сформирован) с изначальными данными?")
        dialogBox.setWindowIcon(QtGui.QIcon("image/icon.png"))
        dialogBox.setWindowTitle('Удаление прогноза продаж')
        dialogBox.setIcon(QMessageBox.Icon.Critical)
        dialogBox.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        dialogBox.buttonClicked.connect(self.dialogButtonClickedPrognoz)
        dialogBox.exec()

    def dialogButtonClickedPrognoz(self, button_clicked):
        if button_clicked.text() == "OK":
            self.prognozTablesDelete()
            self.normativTablesDelete()

    def dialogDeleteKDayWeek(self):
        dialogBox = QMessageBox()
        dialogBox.setText("Вы действительно хотите удалить сформированные коэффициенты по дням недели и норматив(если сформирован) с изначальными данными?")
        dialogBox.setWindowIcon(QtGui.QIcon("image/icon.png"))
        dialogBox.setWindowTitle('Удаление прогноза продаж')
        dialogBox.setIcon(QMessageBox.Icon.Critical)
        dialogBox.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        dialogBox.buttonClicked.connect(self.dialogButtonClickedKDayWeek)
        dialogBox.exec()

    def dialogButtonClickedKDayWeek(self, button_clicked):
        if button_clicked.text() == "OK":
            self.dayWeekTablesDelete()
            self.normativTablesDelete()

    def dialogDeleteNormativ(self):
        dialogBox = QMessageBox()
        dialogBox.setText("Вы действительно хотите удалить сформированный норматив с изначальными данными?")
        dialogBox.setWindowIcon(QtGui.QIcon("image/icon.png"))
        dialogBox.setWindowTitle('Удаление норматива')
        dialogBox.setIcon(QMessageBox.Icon.Critical)
        dialogBox.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        dialogBox.buttonClicked.connect(self.dialogButtonClickedNormativ)
        dialogBox.exec()

    def dialogButtonClickedNormativ(self, button_clicked):
        if button_clicked.text() == "OK":
            self.normativTablesDelete()

    def normativTablesDelete(self):
        period = self.periodDay
        if self.proverkaNormativa(self.periodDay) == 1:
            self.check_db.thr_deleteNormativ(period)
            self.proverkaNormativaFunc()
            self.proverkaPeriodaPrognozFunc()

    def prognozTablesDelete(self):
        period = self.periodDay
        self.check_db.thr_deletePrognoz(period)
        self.proverkaPeriodaPrognozFunc()
        self.proverkaNormativaFunc()

    def dayWeekTablesOpen(self, pathOLAP_DayWeek, periodDay):
        Excel = win32com.client.Dispatch("Excel.Application")
        wb_OLAP_dayWeek_bakery = Excel.Workbooks.Open(pathOLAP_DayWeek)
        sheet_OLAP_dayWeek_bakery = wb_OLAP_dayWeek_bakery.ActiveSheet
        firstOLAPRow = sheet_OLAP_dayWeek_bakery.Range("A:A").Find("День недели").Row
        pointsCheck = self.ui.formLayoutWidget.findChildren(QtWidgets.QCheckBox)
        if self.proverkaPerioda(self.periodDay) == 0:
            points = []
            for i in range(len(pointsCheck)):
                if pointsCheck[i].isChecked():
                    ValidPoints = sheet_OLAP_dayWeek_bakery.Rows(firstOLAPRow).Find(pointsCheck[i].text())
                    if ValidPoints == None:
                        self.dialogNOvalidOLAP(pointsCheck[i].text())
                        return
                    points.append(pointsCheck[i].text())
            pointsNonCheck = []
            for i in range(len(pointsCheck)):
                if not pointsCheck[i].isChecked():
                    pointsNonCheck.append(pointsCheck[i].text())
        else:
            points = json.loads(self.poiskPrognoza(self.periodDay).strip("\'"))
            del points[0:5]
            for i in range(len(points)):
                ValidPoints = sheet_OLAP_dayWeek_bakery.Rows(firstOLAPRow).Find(points[i])
                if ValidPoints == None:
                    self.dialogNOvalidOLAP(points[i])
                    return
            pointsNonCheck = []
            for i in range(len(pointsCheck)):
                if not (pointsCheck[i].text() in points):
                    pointsNonCheck.append(pointsCheck[i].text())
        self.hide()
        global WindowBakeryDayWeekEdit
        WindowBakeryDayWeekEdit = Windows.WindowsBakeryTablesDayWeekEdit.WindowBakeryTableDayWeekEdit(pathOLAP_DayWeek,
                                                                                         periodDay, pointsNonCheck)
        WindowBakeryDayWeekEdit.showMaximized()

    def dayWeekTablesView(self):
        self.hide()
        global WindowBakeryTablesDayWeekView
        WindowBakeryTablesDayWeekView = Windows.WindowsBakeryTablesDayWeekView.WindowBakeryTableDayWeekView(
            self.periodDay)
        WindowBakeryTablesDayWeekView.showMaximized()

    def dayWeekTablesRedact(self):
        self.normativTablesDelete()
        self.hide()
        periodDay = self.periodDay
        global WindowBakeryTablesDayWeekRedact
        WindowBakeryTablesDayWeekRedact = Windows.WindowsBakeryTablesDayWeekRedact.WindowBakeryTablesDayWeekRedact(
            periodDay)
        WindowBakeryTablesDayWeekRedact.showMaximized()

    def dayWeekTablesDelete(self):
        period = self.periodDay
        self.check_db.thr_deleteKDayWeek(period)
        self.proverkaPeriodaKDayWeekFunc()

    def normativ(self):
        self.hide()
        periodDay = self.periodDay
        global WindowNormativEdit
        WindowNormativEdit = Windows.WindowsBakeryNormativEdit.WindowBakeryNormativEdit(periodDay)
        WindowNormativEdit.showMaximized()

    def poiskNormativa(self, periodDay):
        self.check_db.thr_poiskNormativa(periodDay)
        return (otvetNormativ)

    def signal_normativdata(self, value):
        headers = value[0][2]
        data = value[0][3]
        global otvetNormativ
        otvetNormativ = [headers, data]

    def saveFileDialogNormativ(self):
        fileName, _ = QFileDialog.getSaveFileName(
            parent=self,
            caption="Сохранение данных",
            directory=os.path.expanduser(
                '~') + r'\Desktop' + f"\Нормативы для пекарни с {self.periodDay[0].toString('dd.MM.yyyy')} по {self.periodDay[1].toString('dd.MM.yyyy')}.xlsx",
            filter="Все файлы (*);")
        if fileName:
            self.ui.progressBar.show()
            self.setEnabled(False)
            progress = 0
            normativData = self.poiskNormativa(self.periodDay)
            headers = json.loads(normativData[0].strip("\'"))
            data = json.loads(normativData[1].strip("\'"))
            self.ui.progressBar.setValue(progress)
            self.ui.progressBar.setMinimum(0)
            self.ui.progressBar.setMaximum(len(data.keys()) - 3)
            Excel = win32com.client.Dispatch("Excel.Application")
            normativExcel = Excel.Workbooks.Add()
            sheet = normativExcel.ActiveSheet
            sheet.Columns(1).NumberFormat = "@"
            for col in range(2, len(headers)):
                sheet.Cells(1, col - 1).Value = headers[col]
            for col in range(2, len(data.keys())):
                for row in range(1, len(data.get(str(col)).keys())):
                    if col > 4:
                        sheet.Cells(int(row) + 1, col - 1).Value = round(data[str(col)][str(row)], 0)
                    else:
                        sheet.Cells(int(row) + 1, col - 1).Value = data[str(col)][str(row)]
                self.ui.progressBar.setValue(progress)
                progress += 1
            sheet.Columns.AutoFit()
            lastColumn = sheet.UsedRange.Columns.Count
            lastRow = sheet.UsedRange.Rows.Count
            sheet.Range("A1").AutoFilter(Field=1)
            for col in range(4, lastColumn + 1):
                sheet.Cells(lastRow + 1, col).Value = f"=SUM(R[{1 - lastRow}]C:R[-1]C)"
            sheet.Range(sheet.Cells(1, 1), sheet.Cells(lastRow + 1, lastColumn)).Borders(2).Weight = 2
            sheet.Range(sheet.Cells(1, 1), sheet.Cells(lastRow + 1, lastColumn)).Borders(4).Weight = 2
            sheet.Range(sheet.Cells(1, 1), sheet.Cells(lastRow + 1, lastColumn)).Borders(7).Weight = 3
            sheet.Range(sheet.Cells(1, 1), sheet.Cells(lastRow + 1, lastColumn)).Borders(8).Weight = 3
            sheet.Range(sheet.Cells(1, 1), sheet.Cells(lastRow + 1, lastColumn)).Borders(9).Weight = 3
            sheet.Range(sheet.Cells(1, 1), sheet.Cells(lastRow + 1, lastColumn)).Borders(10).Weight = 3
            fileName = fileName.replace('/', '\\')
            Excel.DisplayAlerts = False
            normativExcel.SaveAs(Filename=fileName)
            normativExcel.Close()
            Excel.Quit()
            self.setEnabled(True)
            self.ui.progressBar.hide()
            path_to_folder, file_name = os.path.split(fileName)
            os.startfile(path_to_folder)  # открытие папки

    def saveFileDialogLayout(self):
        folderName = QFileDialog.getExistingDirectory(
            parent=self,
            caption="Выберите папку для сохранения выкладки",
            directory=os.path.expanduser('~') + r'\Desktop')
        if folderName:
            self.ui.progressBar.show()
            self.setEnabled(False)
            progress = 0
            folderName = folderName.replace('/',
                                            '\\') + f"\Выкладка {self.periodDay[0].toString('dd.MM.yyyy')} по {self.periodDay[1].toString('dd.MM.yyyy')}"
            if os.path.exists(folderName) == True:
                shutil.rmtree(folderName)
            os.mkdir(folderName)
            prognoz = self.poiskPrognozaExcel(self.periodDay)
            headersPrognoz = json.loads(prognoz[0].strip("\'"))
            dataPrognoz = json.loads(prognoz[1].strip("\'"))
            kdayweek = self.poiskKDayWeekExcel(self.periodDay)
            headersKdayweek = json.loads(kdayweek[0].strip("\'"))
            dataKdayweek = json.loads(kdayweek[1].strip("\'"))
            del headersPrognoz[:5]
            keysDataPrognoz = ['0', '1', '2', '6']
            self.ui.progressBar.setValue(progress)
            self.ui.progressBar.setMinimum(0)
            self.ui.progressBar.setMaximum(len(headersPrognoz) - 1)
            for key in keysDataPrognoz:
                dataPrognoz.pop(key, None)
            keysDataKdayweek = ['0']
            for key in keysDataKdayweek:
                dataKdayweek.pop(key, None)
            Excel = win32com.client.Dispatch("Excel.Application")
            pointCounter = 7
            for point in headersPrognoz:
                pointExcel = Excel.Workbooks.Add()
                sheet = pointExcel.ActiveSheet
                sheet.Columns(1).NumberFormat = "@"
                sheet.Columns(6).NumberFormat = "@"
                sheet.Columns(11).NumberFormat = "@"
                sheet.Columns(16).NumberFormat = "@"
                sheet.Columns(21).NumberFormat = "@"
                sheet.Columns(26).NumberFormat = "@"
                sheet.Columns(31).NumberFormat = "@"
                dayCol = 1
                for day in range(0, 7):
                    DayInPeriod = self.periodDay[0].addDays(day)
                    date = (datetime.date(int(DayInPeriod.toString('yyyy')), int(DayInPeriod.toString('MM')),
                                          int(DayInPeriod.toString('dd')))).isoweekday()
                    sheet.Cells(1, dayCol).Value = point
                    sheet.Cells(1, dayCol + 2).Value = DayInPeriod.toString('dd.MM.yyyy')
                    sheet.Cells(2, dayCol).Value = "Код"
                    sheet.Columns(dayCol).ColumnWidth = 6
                    sheet.Cells(2, dayCol + 1).Value = "Наименование"
                    sheet.Columns(dayCol + 1).ColumnWidth = 45
                    sheet.Cells(2, dayCol + 2).Value = "Всего"
                    sheet.Columns(dayCol + 2).ColumnWidth = 6
                    sheet.Cells(2, dayCol + 3).Value = "Утро"
                    sheet.Columns(dayCol + 3).ColumnWidth = 6
                    sheet.Cells(2, dayCol + 4).Value = "День"
                    sheet.Columns(dayCol + 4).ColumnWidth = 6
                    sheet.Range(sheet.Cells(1, dayCol), sheet.Cells(1, dayCol + 1)).Merge()
                    sheet.Range(sheet.Cells(1, dayCol + 2), sheet.Cells(1, dayCol + 4)).Merge()
                    rowCount = 3
                    for poz in dataPrognoz['4']:
                        if poz != '0':
                            sheet.Cells(rowCount, dayCol).Value = dataPrognoz['4'][poz]
                            sheet.Cells(rowCount, dayCol + 1).Value = dataPrognoz['5'][poz]
                            itogo = (dataPrognoz[str(pointCounter)][poz] * dataKdayweek[str(headersKdayweek.index(point))][str(date)]) / dataPrognoz['3'][poz]
                            if itogo < 1:
                                itogo = ceil(itogo)
                            itogo = round(itogo * dataPrognoz['3'][poz])
                            sheet.Cells(rowCount, dayCol + 2).Value = itogo
                            morningLayout = round((itogo * 0.6) / dataPrognoz['3'][poz]) * dataPrognoz['3'][poz]
                            sheet.Cells(rowCount, dayCol + 3).Value = morningLayout
                            dayLayout = itogo - morningLayout
                            sheet.Cells(rowCount, dayCol + 4).Value = dayLayout
                            rowCount += 1
                    lastRow = rowCount
                    sheet.Cells(lastRow, dayCol + 2).Value = f"=SUM(R[{3 - lastRow}]C:R[-1]C)"
                    sheet.Cells(lastRow, dayCol + 3).Value = f"=SUM(R[{3 - lastRow}]C:R[-1]C)"
                    sheet.Cells(lastRow, dayCol + 4).Value = f"=SUM(R[{3 - lastRow}]C:R[-1]C)"
                    sheet.Range(sheet.Cells(1, dayCol), sheet.Cells(lastRow, dayCol+4)).Borders(2).Weight = 2
                    sheet.Range(sheet.Cells(1, dayCol), sheet.Cells(lastRow, dayCol+4)).Borders(4).Weight = 2
                    sheet.Range(sheet.Cells(1, dayCol), sheet.Cells(lastRow, dayCol+4)).Borders(7).Weight = 3
                    sheet.Range(sheet.Cells(1, dayCol), sheet.Cells(lastRow, dayCol+4)).Borders(8).Weight = 3
                    sheet.Range(sheet.Cells(1, dayCol), sheet.Cells(lastRow, dayCol+4)).Borders(9).Weight = 3
                    sheet.Range(sheet.Cells(1, dayCol), sheet.Cells(lastRow, dayCol+4)).Borders(10).Weight = 3
                    if dayCol != 1:
                        sheet.Columns(dayCol).PageBreak = True
                    dayCol += 5
                sortRange = sheet.Range(sheet.Cells(3, 1), sheet.Cells(sheet.UsedRange.Rows.Count, dayCol+4))
                sortRange.Sort(Key1=sortRange.Range("B3"), Order1=1, Orientation=1)  # Сортировка по возрастанию
                Excel.DisplayAlerts = False
                pointExcel.SaveAs(Filename=(folderName + '\\' + point + '.xlsx'))
                pointExcel.Close()
                Excel.Quit()
                self.ui.progressBar.setValue(progress)
                progress += 1
                pointCounter += 1
        self.setEnabled(True)
        self.ui.progressBar.hide()
        os.startfile(folderName)  # открытие папки

    def delCookieData(self):
        self.check_db.thr_deleteCookieData()

    def closeEvent(self, event):
        self.delCookieData()
        event.accept()