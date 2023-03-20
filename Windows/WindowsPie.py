import datetime
import os
import shutil
from math import ceil
import win32com.client
import json
from PyQt6 import QtCore, QtWidgets, QtGui
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtWidgets import QMessageBox
from ui.pie import Ui_WindowPie
from ui.DialogPrioritet import Ui_DialogPrioritet
from handler.check_db import CheckThread
import Windows.WindowsViborRazdela
import Windows.WindowsPieTablesEdit
import Windows.WindowsPieTablesView
import Windows.WindowsPieTablesRedact
import Windows.WindowsPieTablesDayWeekEdit
import Windows.WindowsPieTablesDayWeekView
import Windows.WindowsPieTablesDayWeekRedact

class DialogPrioritet(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DialogPrioritet()
        self.ui.setupUi(self)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.setWindowIcon(icon)

    def savePrioritet(self):
        pointsCheck = self.ui.formLayoutWidget.findChildren(QtWidgets.QCheckBox)
        pointsPrioritet = []
        for i in range(len(pointsCheck)):
            if pointsCheck[i].isChecked():
                pointsPrioritet.append(pointsCheck[i].text())
        self.close()
        return pointsPrioritet

class WindowPie(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_WindowPie()
        self.ui.setupUi(self)
        self.check_db = CheckThread()
        self.check_db.period.connect(self.signal_period)
        self.check_db.prognoz.connect(self.signal_prognoz)
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
        self.ui.btn_exit_pie.clicked.connect(self.viborRazdelaOpen)
        self.ui.btn_path_OLAP_P.clicked.connect(self.olap_p)
        self.ui.btn_path_dayWeek_pie.clicked.connect(self.olap_dayWeek_pie)
        self.ui.btn_koeff_Prognoz.clicked.connect(self.koeff_Prognoz)
        self.ui.btn_koeff_DayWeek.clicked.connect(self.koeff_DayWeek)
        self.proverkaPeriodaPrognozFunc()
        self.proverkaPeriodaKDayWeekFunc()
        self.ui.btn_prosmotrPrognoz.clicked.connect(self.prognozTablesView)
        self.ui.btn_editPrognoz.clicked.connect(self.prognozTablesRedact)
        self.ui.btn_deletePrognoz.clicked.connect(self.dialogDeletePrognoz)
        self.ui.btn_prosmotr_koeff_DayWeek.clicked.connect(self.dayWeekTablesView)
        self.ui.btn_edit_koeff_DayWeek.clicked.connect(self.dayWeekTablesRedact)
        self.ui.btn_delete_koeff_DayWeek.clicked.connect(self.dialogDeleteKDayWeek)
        self.ui.btn_prioritet.clicked.connect(self.dialogPrioritet)
        self.ui.btn_download_plans.clicked.connect(self.saveFileDialogPlan)
        global pointsPrioritet
        pointsPrioritet = []


    def dialogPrioritet(self):
        global WindowsDialogPrioritet
        WindowsDialogPrioritet = DialogPrioritet()
        WindowsDialogPrioritet.ui.btn_save.clicked.connect(self.getPointsPrioritet)
        WindowsDialogPrioritet.show()

    def getPointsPrioritet(self):
        global pointsPrioritet
        pointsPrioritet = WindowsDialogPrioritet.savePrioritet()
        while self.ui.grid_prioritet.count():
            item = self.ui.grid_prioritet.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
        row = 0
        col = 0
        for i in pointsPrioritet:
            font = QtGui.QFont()
            font.setPointSize(11)
            lable = QtWidgets.QLabel(f'{i}')
            lable.setFont(font)
            lable.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
            if col <= 3:
                self.ui.grid_prioritet.addWidget(lable, row, col)
                col += 1
            else:
                row += 1
                col = 0
                self.ui.grid_prioritet.addWidget(lable, row, col)
                col += 1

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

    def proverkaPeriodaPrognozFunc(self):
        if self.proverkaPerioda(self.periodDay) == 0:
            self.ui.btn_koeff_Prognoz.setEnabled(True)
            self.ui.btn_prosmotrPrognoz.setEnabled(False)
            self.ui.btn_editPrognoz.setEnabled(False)
            self.ui.btn_deletePrognoz.setEnabled(False)
            self.ui.btn_download_plans.setEnabled(False)
        elif self.proverkaPerioda(self.periodDay) == 1:
            self.ui.btn_koeff_Prognoz.setEnabled(False)
            self.ui.btn_prosmotrPrognoz.setEnabled(True)
            self.ui.btn_editPrognoz.setEnabled(True)
            self.ui.btn_deletePrognoz.setEnabled(True)
            if self.proverkaPeriodaKDayWeek(self.periodDay) == 1:
                self.ui.btn_download_plans.setEnabled(True)
            else:
                self.ui.btn_download_plans.setEnabled(False)

    def proverkaPeriodaKDayWeekFunc(self):
        if self.proverkaPeriodaKDayWeek(self.periodDay) == 0:
            self.ui.btn_koeff_DayWeek.setEnabled(True)
            self.ui.btn_prosmotr_koeff_DayWeek.setEnabled(False)
            self.ui.btn_edit_koeff_DayWeek.setEnabled(False)
            self.ui.btn_delete_koeff_DayWeek.setEnabled(False)
            self.ui.btn_download_plans.setEnabled(False)
        elif self.proverkaPeriodaKDayWeek(self.periodDay) == 1:
            self.ui.btn_koeff_DayWeek.setEnabled(False)
            self.ui.btn_prosmotr_koeff_DayWeek.setEnabled(True)
            self.ui.btn_edit_koeff_DayWeek.setEnabled(True)
            self.ui.btn_delete_koeff_DayWeek.setEnabled(True)
            if self.proverkaPerioda(self.periodDay) == 1:
                self.ui.btn_download_plans.setEnabled(True)
            else:
                self.ui.btn_download_plans.setEnabled(False)

    def proverkaPerioda(self, period):
        self.check_db.thr_proverkaPeriodaPie(period)
        return otvetPeriod

    def proverkaPeriodaKDayWeek(self, period):
        self.check_db.thr_proverkaPeriodaKDayWeekPie(period)
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
    def olap_dayWeek_pie(self):
        fileName = QFileDialog.getOpenFileName(self, 'Выберите файл OLAP по дням недели для пекарни', os.path.expanduser(
                '~') + r'\Desktop', 'Excel файл (*.xlsx)')
        self.ui.lineEdit_OLAP_dayWeek_pie.setText(fileName[0])
        self.ui.lineEdit_OLAP_dayWeek_pie.setStyleSheet("padding-left: 5px; color: rgb(0, 0, 0)")

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
        if sheet_OLAP_P.Name != "OLAP отчет для Пирожных":
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
            if len(self.ui.lineEdit_OLAP_dayWeek_pie.text()) == 0 or self.ui.lineEdit_OLAP_dayWeek_pie.text() == 'Файл отчета неверный, укажите OLAP по продажам по дням недели за 7 дней':
                self.ui.lineEdit_OLAP_dayWeek_pie.setStyleSheet("padding-left: 5px; color: rgba(228, 107, 134, 1)")
                self.ui.lineEdit_OLAP_dayWeek_pie.setText('Не выбран файл отчета!')
                return
            elif self.ui.lineEdit_OLAP_dayWeek_pie.text() == 'Не выбран файл отчета!':
                return
            funct_bakery(self)

        return wrapper

    # Обрабытываем кнопку "Установить" для отчета по дням недели
    @check_DayWeek
    def koeff_DayWeek(self):
        pathOLAP_DayWeek = self.ui.lineEdit_OLAP_dayWeek_pie.text()
        self.dayWeekTable(pathOLAP_DayWeek)

    # Проверка на правильность отчета и запуск таблици с коэффициентами
    def dayWeekTable(self, pathOLAP_DayWeek):
        Excel = win32com.client.Dispatch("Excel.Application")
        wb_OLAP_DayWeek = Excel.Workbooks.Open(pathOLAP_DayWeek)
        sheet_OLAP_DayWeek = wb_OLAP_DayWeek.ActiveSheet
        if sheet_OLAP_DayWeek.Name != "OLAP по дням недели для програм":
            wb_OLAP_DayWeek.Close()
            Excel.Quit()
            self.ui.lineEdit_OLAP_dayWeek_pie.setStyleSheet("padding-left: 5px; color: rgba(228, 107, 134, 1)")
            self.ui.lineEdit_OLAP_dayWeek_pie.setText(
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
        self.check_db.thr_poiskPrognozaPie(periodDay)
        return (headers)

    def poiskKDayWeek(self, periodDay):
        self.check_db.thr_poiskDataPeriodaKdayWeekPie(periodDay)
        return (headers)

    def poiskPrognozaExcel(self, periodDay):
        self.check_db.thr_poiskPrognozaPie(periodDay)
        return (fullData)

    def poiskKDayWeekExcel(self, periodDay):
        self.check_db.thr_poiskDataPeriodaKdayWeekPie(periodDay)
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
        if self.proverkaPeriodaKDayWeek(self.periodDay) == 0:
            pointsCheck = self.ui.formLayoutWidget.findChildren(QtWidgets.QCheckBox)
            points = []
            for i in range(len(pointsCheck)):
                if pointsCheck[i].isChecked():
                    ValidPoints = sheet_OLAP_P.Rows(firstOLAPRow).Find(pointsCheck[i].text())
                    if ValidPoints == None:
                        self.dialogNOvalidOLAP(pointsCheck[i].text())
                        return
                    points.append(pointsCheck[i].text())
        else:
            points = json.loads(self.poiskKDayWeek(self.periodDay).strip("\'"))
            del points[0:2]
            for i in range(len(points)):
                ValidPoints = sheet_OLAP_P.Rows(firstOLAPRow).Find(points[i])
                if ValidPoints == None:
                    self.dialogNOvalidOLAP(points[i])
                    return
        self.hide()
        global WindowPieTablesEdit
        WindowPieTablesEdit = Windows.WindowsPieTablesEdit.WindowPieTablesEdit(pathOLAP_P, periodDay, points)
        WindowPieTablesEdit.showMaximized()

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
        global WindowPieTablesView
        WindowPieTablesView = Windows.WindowsPieTablesView.WindowPieTableView(periodDay)
        WindowPieTablesView.showMaximized()

    def prognozTablesRedact(self):
        self.hide()
        periodDay = self.periodDay
        global WindowPieTablesRedact
        WindowPieTablesRedact = Windows.WindowsPieTablesRedact.WindowPieTablesRedact(periodDay)
        WindowPieTablesRedact.showMaximized()

    def dialogDeletePrognoz(self):
        dialogBox = QMessageBox()
        dialogBox.setText("Вы действительно хотите удалить сформированный прогноз?")
        dialogBox.setWindowIcon(QtGui.QIcon("image/icon.png"))
        dialogBox.setWindowTitle('Удаление прогноза продаж')
        dialogBox.setIcon(QMessageBox.Icon.Critical)
        dialogBox.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        dialogBox.buttonClicked.connect(self.dialogButtonClickedPrognoz)
        dialogBox.exec()

    def dialogButtonClickedPrognoz(self, button_clicked):
        if button_clicked.text() == "OK":
            self.prognozTablesDelete()

    def dialogDeleteKDayWeek(self):
        dialogBox = QMessageBox()
        dialogBox.setText("Вы действительно хотите удалить сформированные коэффициенты по дням недели?")
        dialogBox.setWindowIcon(QtGui.QIcon("image/icon.png"))
        dialogBox.setWindowTitle('Удаление коэффициентов по дням недели')
        dialogBox.setIcon(QMessageBox.Icon.Critical)
        dialogBox.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        dialogBox.buttonClicked.connect(self.dialogButtonClickedKDayWeek)
        dialogBox.exec()

    def dialogButtonClickedKDayWeek(self, button_clicked):
        if button_clicked.text() == "OK":
            self.dayWeekTablesDelete()

    def prognozTablesDelete(self):
        period = self.periodDay
        self.check_db.thr_deletePrognozPie(period)
        self.proverkaPeriodaPrognozFunc()

    def dayWeekTablesOpen(self, pathOLAP_DayWeek, periodDay):
        Excel = win32com.client.Dispatch("Excel.Application")
        wb_OLAP_dayWeek_pie = Excel.Workbooks.Open(pathOLAP_DayWeek)
        sheet_OLAP_dayWeek_pie = wb_OLAP_dayWeek_pie.ActiveSheet
        firstOLAPRow = sheet_OLAP_dayWeek_pie.Range("A:A").Find("День недели").Row
        if self.proverkaPerioda(self.periodDay) == 0:
            pointsCheck = self.ui.formLayoutWidget.findChildren(QtWidgets.QCheckBox)
            points = []
            for i in range(len(pointsCheck)):
                if pointsCheck[i].isChecked():
                    ValidPoints = sheet_OLAP_dayWeek_pie.Rows(firstOLAPRow).Find(pointsCheck[i].text())
                    if ValidPoints == None:
                        self.dialogNOvalidOLAP(pointsCheck[i].text())
                        return
                    points.append(pointsCheck[i].text())
        else:
            points = json.loads(self.poiskPrognoza(self.periodDay).strip("\'"))
            del points[0:6]
            for i in range(len(points)):
                ValidPoints = sheet_OLAP_dayWeek_pie.Rows(firstOLAPRow).Find(points[i])
                if ValidPoints == None:
                    self.dialogNOvalidOLAP(points[i])
                    return
        self.hide()
        global WindowPieDayWeekEdit
        WindowPieDayWeekEdit = Windows.WindowsPieTablesDayWeekEdit.WindowPieTableDayWeekEdit(pathOLAP_DayWeek, periodDay, points)
        WindowPieDayWeekEdit.showMaximized()

    def dayWeekTablesView(self):
        self.hide()
        global WindowPieTablesDayWeekView
        WindowPieTablesDayWeekView = Windows.WindowsPieTablesDayWeekView.WindowPieTableDayWeekView(
            self.periodDay)
        WindowPieTablesDayWeekView.showMaximized()

    def dayWeekTablesRedact(self):
        self.hide()
        periodDay = self.periodDay
        global WindowPieTablesDayWeekRedact
        WindowPieTablesDayWeekRedact = Windows.WindowsPieTablesDayWeekRedact.WindowPieTablesDayWeekRedact(
            periodDay)
        WindowPieTablesDayWeekRedact.showMaximized()

    def dayWeekTablesDelete(self):
        period = self.periodDay
        self.check_db.thr_deleteKDayWeekPie(period)
        self.proverkaPeriodaKDayWeekFunc()

    def saveFileDialogPlan(self):
        folderName = QFileDialog.getExistingDirectory(
            parent=self,
            caption="Выберите папку для сохранения планов на Пирожные",
            directory=os.path.expanduser('~') + r'\Desktop')
        if folderName:
            self.ui.progressBar.show()
            self.setEnabled(False)
            progress = 0
            folderName = folderName.replace('/',
                                            '\\') + f"\Планы для Пирожных {self.periodDay[0].toString('dd.MM.yyyy')} по {self.periodDay[1].toString('dd.MM.yyyy')}"
            if os.path.exists(folderName) == True:
                shutil.rmtree(folderName)
            os.mkdir(folderName)
            prognoz = self.poiskPrognozaExcel(self.periodDay)
            headersPrognoz = json.loads(prognoz[0].strip("\'"))
            dataPrognoz = json.loads(prognoz[1].strip("\'"))
            kdayweek = self.poiskKDayWeekExcel(self.periodDay)
            headersKdayweek = json.loads(kdayweek[0].strip("\'"))
            dataKdayweek = json.loads(kdayweek[1].strip("\'"))
            del headersPrognoz[:6]
            keysDataPrognoz = ['0', '1', '2', '7']
            self.ui.progressBar.setValue(progress)
            self.ui.progressBar.setMinimum(0)
            self.ui.progressBar.setMaximum(8)
            for key in keysDataPrognoz:
                dataPrognoz.pop(key, None)
            keysDataKdayweek = ['0']
            for key in keysDataKdayweek:
                dataKdayweek.pop(key, None)
            Excel = win32com.client.Dispatch("Excel.Application")
            # for point in headersPrognoz:
            #     pointExcel = Excel.Workbooks.Add()
            #     sheet = pointExcel.ActiveSheet
            #     sheet.Columns(1).NumberFormat = "@"
            #     dayCol = 1
            svodExcel = Excel.Workbooks.Add()
            sheetSvod = svodExcel.ActiveSheet
            sheetSvod.Columns(1).NumberFormat = "@"
            for day in range(0, 7):
                dayExcel = Excel.Workbooks.Add()
                sheetDay = dayExcel.ActiveSheet
                sheetDay.Columns(1).NumberFormat = "@"
                DayInPeriod = self.periodDay[0].addDays(day)
                date = (datetime.date(int(DayInPeriod.toString('yyyy')), int(DayInPeriod.toString('MM')), int(DayInPeriod.toString('dd')))).isoweekday()
                sheetDay.Cells(1, 2).Value = 'Дата производства'
                sheetDay.Cells(1, 3).Value = DayInPeriod.addDays(-1).toString('dd.MM.yyyy')
                sheetDay.Cells(2, 2).Value = 'Дата отгрузки'
                sheetDay.Cells(2, 3).Value = DayInPeriod.toString('dd.MM.yyyy')
                sheetDay.Cells(3, 1).Value = 'Код блюда'
                sheetDay.Cells(3, 2).Value = 'Блюдо'
                sheetDay.Cells(3, 3).Value = 'Участок приготовления'
                sheetDay.Cells(3, len(headersPrognoz) + 4).Value = 'ПЛАН'
                sheetDay.Cells(3, len(headersPrognoz) + 5).Value = 'ФАКТ'
                sheetDay.Cells(3, len(headersPrognoz) + 6).Value = 'РАЗНИЦА'
                col = 4
                for point in headersPrognoz:
                    sheetDay.Cells(3, col).Value = point
                    col += 1
                row = 4
                for key in dataPrognoz['5']:
                    if key != '0':
                        sheetDay.Cells(row, 1).Value = dataPrognoz['5'][key]
                        sheetDay.Cells(row, 2).Value = dataPrognoz['6'][key]
                        sheetDay.Cells(row, 3).Value = 'Участок пирожных'
                        summBludaToKvant = 0
                        for col in range(4, len(headersPrognoz) + 4):
                            point = sheetDay.Cells(3, col).Value
                            sheetDay.Cells(row, col).Value = ceil(dataPrognoz[str(headersPrognoz.index(point) + 8)][key] * dataKdayweek[str(headersKdayweek.index(point))][str(date)] / dataPrognoz['3'][key]) * dataPrognoz['3'][key]
                            summBludaToKvant += sheetDay.Cells(row, col).Value
                        summBludaToZames = ceil(summBludaToKvant / dataPrognoz['4'][key]) * dataPrognoz['4'][key]
                        while summBludaToZames < summBludaToKvant:
                            summBludaToZames += dataPrognoz['4'][key]
                        sheetDay.Cells(row, len(headersPrognoz) + 4).Value = summBludaToZames
                        if summBludaToZames - summBludaToKvant > 0:
                            raspred = (summBludaToZames - summBludaToKvant) / dataPrognoz['3'][key]
                            spisokZnachToKvant = list(sheetDay.Range(sheetDay.Cells(row, 4), sheetDay.Cells(row, len(headersPrognoz) + 3)).Value[0])
                            # Инициализируем список с парами (индекс, значение)
                            indexed_values = list(enumerate(spisokZnachToKvant))
                            # Сортируем список по убыванию значений
                            sorted_values = sorted(indexed_values, key=lambda x: x[1], reverse=True)
                            # Получаем список индексов первых n_max максимальных значений
                            max_indexes = [x[0] for x in sorted_values[:int(raspred)]]
                            max_znach = [x[1] for x in sorted_values[:int(raspred)]]
                            # Выводим список с индексами максимальных значений
                            print(int(raspred))
                            print(max_indexes)
                            print(max_znach)
                            for i in max_indexes:
                                print(headersPrognoz[i], end="")
                            print(*pointsPrioritet)
                        row += 1

            #         sheet.Cells(1, dayCol + 2).Value = DayInPeriod.toString('dd.MM.yyyy')
            #         sheet.Cells(2, dayCol).Value = "Код"
            #         sheet.Columns(dayCol).ColumnWidth = 6
            #         sheet.Cells(2, dayCol + 1).Value = "Наименование"
            #         sheet.Columns(dayCol + 1).ColumnWidth = 45
            #         sheet.Cells(2, dayCol + 2).Value = "Всего"
            #         sheet.Columns(dayCol + 2).ColumnWidth = 6
            #         sheet.Cells(2, dayCol + 3).Value = "Утро"
            #         sheet.Columns(dayCol + 3).ColumnWidth = 6
            #         sheet.Cells(2, dayCol + 4).Value = "День"
            #         sheet.Columns(dayCol + 4).ColumnWidth = 6
            #         sheet.Range(sheet.Cells(1, dayCol), sheet.Cells(1, dayCol + 1)).Merge()
            #         sheet.Range(sheet.Cells(1, dayCol + 2), sheet.Cells(1, dayCol + 4)).Merge()
            #         rowCount = 3
            #         for poz in dataPrognoz['4']:
            #             if poz != '0':
            #                 sheet.Cells(rowCount, dayCol).Value = dataPrognoz['4'][poz]
            #                 sheet.Cells(rowCount, dayCol + 1).Value = dataPrognoz['5'][poz]
            #                 itogo = (dataPrognoz[str(pointCounter)][poz] * dataKdayweek[str(headersKdayweek.index(point))][str(date)]) / dataPrognoz['3'][poz]
            #                 if itogo < 1:
            #                     itogo = ceil(itogo)
            #                 itogo = round(itogo * dataPrognoz['3'][poz])
            #                 sheet.Cells(rowCount, dayCol + 2).Value = itogo
            #                 morningLayout = round((itogo * 0.6) / dataPrognoz['3'][poz]) * dataPrognoz['3'][poz]
            #                 sheet.Cells(rowCount, dayCol + 3).Value = morningLayout
            #                 dayLayout = itogo - morningLayout
            #                 sheet.Cells(rowCount, dayCol + 4).Value = dayLayout
            #                 rowCount += 1
            #         lastRow = rowCount
            #         sheet.Cells(lastRow, dayCol + 2).Value = f"=SUM(R[{3 - lastRow}]C:R[-1]C)"
            #         sheet.Cells(lastRow, dayCol + 3).Value = f"=SUM(R[{3 - lastRow}]C:R[-1]C)"
            #         sheet.Cells(lastRow, dayCol + 4).Value = f"=SUM(R[{3 - lastRow}]C:R[-1]C)"
            #         sheet.Range(sheet.Cells(1, dayCol), sheet.Cells(lastRow, dayCol+4)).Borders(2).Weight = 2
            #         sheet.Range(sheet.Cells(1, dayCol), sheet.Cells(lastRow, dayCol+4)).Borders(4).Weight = 2
            #         sheet.Range(sheet.Cells(1, dayCol), sheet.Cells(lastRow, dayCol+4)).Borders(7).Weight = 3
            #         sheet.Range(sheet.Cells(1, dayCol), sheet.Cells(lastRow, dayCol+4)).Borders(8).Weight = 3
            #         sheet.Range(sheet.Cells(1, dayCol), sheet.Cells(lastRow, dayCol+4)).Borders(9).Weight = 3
            #         sheet.Range(sheet.Cells(1, dayCol), sheet.Cells(lastRow, dayCol+4)).Borders(10).Weight = 3
            #         if dayCol != 1:
            #             sheet.Columns(dayCol).PageBreak = True
            #         dayCol += 5
                Excel.DisplayAlerts = False
                dayExcel.SaveAs(Filename=(folderName + '\\' + f'Пирожные {DayInPeriod.toString("dd.MM.yyyy")}' + '.xlsx'))
                dayExcel.Close()
                progress += 1
                self.ui.progressBar.setValue(progress)
            svodExcel.SaveAs(Filename=(folderName + '\\' + f'Сводная по пирожным {self.periodDay[0].toString("dd.MM.yyyy")} - {self.periodDay[1].toString("dd.MM.yyyy")}' + '.xlsx'))
            svodExcel.Close()
            Excel.Quit()
            progress += 1
            self.ui.progressBar.setValue(progress)
            #     pointCounter += 1
        self.setEnabled(True)
        self.ui.progressBar.hide()

    def delCookieData(self):
        self.check_db.thr_deleteCookieData()

    def closeEvent(self, event):
        self.delCookieData()
        event.accept()