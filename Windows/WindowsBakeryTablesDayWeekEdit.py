from PyQt6 import QtWidgets, QtGui
import win32com.client
import json
from ui.bakeryTables import Ui_WindowBakeryTables
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtGui import QFont
from handler.check_db import CheckThread
import Windows.WindowsBakery


class WindowBakeryTableDayWeek(QtWidgets.QMainWindow):
    def __init__(self, pathOLAP_dayWeek_bakery, periodDay, points):
        super().__init__()
        self.ui = Ui_WindowBakeryTables()
        self.ui.setupUi(self)
        self.setWindowTitle("Продажи по дням недели")
        self.check_db = CheckThread()
        Excel = win32com.client.Dispatch("Excel.Application")
        wb_OLAP_dayWeek_bakery = Excel.Workbooks.Open(pathOLAP_dayWeek_bakery)
        sheet_OLAP_dayWeek_bakery = wb_OLAP_dayWeek_bakery.ActiveSheet
        firstOLAPRow = sheet_OLAP_dayWeek_bakery.Range("A:A").Find("День недели").Row
        # Фильтруем точки по Checkbox-сам
        for i in range(5, len(points)):
            ValidPoints = sheet_OLAP_dayWeek_bakery.Rows(firstOLAPRow).Find(points[i])
            if ValidPoints == None:
                sheet_OLAP_dayWeek_bakery.Columns(ValidPoints.Column).Delete()
        # Удаляем пустые столбцы и строки
        endOLAPCol = sheet_OLAP_dayWeek_bakery.Cells.Find("Выпечка пекарни всего").Column
        for a in range(endOLAPCol-1, 1, -1):
            if sheet_OLAP_dayWeek_bakery.Cells(firstOLAPRow, a).Value is None:
                sheet_OLAP_dayWeek_bakery.Columns(a).Delete()
        endOLAPCol = sheet_OLAP_dayWeek_bakery.Cells.Find("Выпечка пекарни всего").Column
        for _ in range(firstOLAPRow - 1):
            sheet_OLAP_dayWeek_bakery.Rows(1).Delete()
        endOLAPRow = sheet_OLAP_dayWeek_bakery.Range("A:A").Find("Итого").Row
        self.ui.tableWidget.setRowCount(endOLAPRow - 1)
        self.ui.tableWidget.setColumnCount(endOLAPCol)
        self.columnLables = list(sheet_OLAP_dayWeek_bakery.Range(sheet_OLAP_dayWeek_bakery.Cells(1, 1), sheet_OLAP_dayWeek_bakery.Cells(1, endOLAPCol - 1)).Value[0])
        self.columnLables.insert(0, "Коэфф. Дня")
        self.ui.tableWidget.setHorizontalHeaderLabels(self.columnLables)
        self.font = QtGui.QFont("Times", 10, QFont.Weight.Bold)
        self.ui.tableWidget.horizontalHeader().setFont(self.font)
        self.ui.tableWidget.setItem(0, 1, QTableWidgetItem("Кф. кондитерской"))
        self.ui.tableWidget.item(0, 1).setFont(self.font)
        for col_spin in range(2, self.ui.tableWidget.columnCount()):
            self.DspinboxCol = QtWidgets.QDoubleSpinBox()
            self.DspinboxCol.wheelEvent = lambda event: None
            self.ui.tableWidget.setCellWidget(0, col_spin, self.DspinboxCol)
            self.ui.tableWidget.cellWidget(0, col_spin).setValue(1.00)
            self.ui.tableWidget.cellWidget(0, col_spin).setSingleStep(0.05)
            self.ui.tableWidget.cellWidget(0, col_spin).valueChanged.connect(self.raschetDayWeek)
        for row_spin in range(1, self.ui.tableWidget.rowCount()):
            self.DspinboxRow = QtWidgets.QDoubleSpinBox()
            self.DspinboxRow.wheelEvent = lambda event: None
            self.ui.tableWidget.setCellWidget(row_spin, 0, self.DspinboxRow)
            self.ui.tableWidget.cellWidget(row_spin, 0).setValue(1.00)
            self.ui.tableWidget.cellWidget(row_spin, 0).setSingleStep(0.05)
            self.ui.tableWidget.cellWidget(row_spin, 0).valueChanged.connect(self.raschetDayWeek)
        for col in range(1, endOLAPCol):
            for row in range(2, endOLAPRow):
                item = sheet_OLAP_dayWeek_bakery.Cells(row, col).Value
                if item == None:
                    item = 0
                item = QTableWidgetItem(str(item))
                self.ui.tableWidget.setItem(row - 1, col, item)
        global saveZnach
        saveZnach = {}
        for col in range(2, self.ui.tableWidget.columnCount()):
             saveZnach[col] = {}
             for row in range(1, self.ui.tableWidget.rowCount()):
                 saveZnach[col][row] = float(self.ui.tableWidget.item(row, col).text())
        self.periodDay = periodDay
        self.SaveAndClose = QtWidgets.QPushButton()
        self.ui.tableWidget.setCellWidget(0, 0, self.SaveAndClose)
        self.ui.tableWidget.cellWidget(0, 0).setText('Сохранить и закрыть')
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        font.bold()
        font.setWeight(50)
        self.ui.tableWidget.cellWidget(0, 0).setFont(font)
        self.ui.tableWidget.cellWidget(0, 0).setStyleSheet("QPushButton {\n"
                                                           "background-color: rgb(228, 107, 134);\n"
                                                           "border: none;\n"
                                                           "border-radius: 10px}\n"
                                                           "\n"
                                                           "QPushButton:hover {\n"
                                                           "border: 1px solid  rgb(0, 0, 0);\n"
                                                           "background-color: rgba(228, 107, 134, 0.9)\n"
                                                           "}\n"
                                                           "\n"
                                                           "QPushButton:pressed {\n"
                                                           "border:3px solid  rgb(0, 0, 0);\n"
                                                           "background-color: rgba(228, 107, 134, 1)\n"
                                                           "}")
        self.ui.tableWidget.cellWidget(0, 0).clicked.connect(self.saveAndCloseDef)
        self.ui.tableWidget.setColumnWidth(0, 170)
        self.ui.tableWidget.setColumnWidth(1, 130)

    #Увеличение или уменьшение доли продаж.
    def raschetDayWeek(self):
        buttonClicked = self.sender()
        index = self.ui.tableWidget.indexAt(buttonClicked.pos())
        if index.row() == 0:
            for i in range(1, self.ui.tableWidget.rowCount()):
                result = round(float(saveZnach[index.column()][i]) * float(self.ui.tableWidget.cellWidget(0, index.column()).value()) * float(self.ui.tableWidget.cellWidget(i, 0).value()), 4)
                self.ui.tableWidget.setItem(i, index.column(), QTableWidgetItem(str(result)))
        else:
            for i in range(2, self.ui.tableWidget.columnCount()):
                result = round(float(saveZnach[i][index.row()]) * float(self.ui.tableWidget.cellWidget(index.row(), 0).value()) * float(self.ui.tableWidget.cellWidget(0, i).value()), 4)
                self.ui.tableWidget.setItem(index.row(), i, QTableWidgetItem(str(result)))

    # Сохранение в БД и закрытие таблицы
    def saveAndCloseDef(self):
        savePeriod = self.periodDay
        saveNull = saveZnach.copy()
        saveDB = {}
        for col in range(0, self.ui.tableWidget.columnCount()):
            saveDB[col] = {}
            for row in range(0, self.ui.tableWidget.rowCount()):
                if col == 0 or row == 0:
                    if (row == 0 and col == 0) or (row == 0 and col == 1):
                        saveDB[col][row] = 0
                    else:
                        saveDB[col][row] = float(self.ui.tableWidget.cellWidget(row, col).value())
                elif col == 1:
                    saveDB[col][row] = self.ui.tableWidget.item(row, col).text()
                else:
                    saveDB[col][row] = float(self.ui.tableWidget.item(row, col).text())
        self.insertInDB(savePeriod, json.dumps(saveDB, ensure_ascii=False), json.dumps(saveNull, ensure_ascii=False))
        self.close()

    def insertInDB(self, savePeriod, saveDB, saveNull):
        self.check_db.thr_saveDayWeek(savePeriod, saveDB, saveNull)

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
            event.accept()
            global WindowBakery
            WindowBakery = Windows.WindowsBakery.WindowBakery()
            WindowBakery.show()
        else:
            event.ignore()

