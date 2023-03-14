from PyQt6 import QtWidgets, QtGui
import json
import textwrap
from ui.bakeryTables import Ui_WindowBakeryTables
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.QtWidgets import QMessageBox
from handler.check_db import CheckThread
import Windows.WindowsPie


class WindowPieTablesDayWeekRedact(QtWidgets.QMainWindow):
    def __init__(self, periodDay):
        super().__init__()
        self.ui = Ui_WindowBakeryTables()
        self.ui.setupUi(self)
        self.check_db = CheckThread()
        self.check_db.prognoz.connect(self.signal_prognoz)
        self.setWindowTitle("Редактирование коэффициентов долей продаж")
        self.kdayweek = self.poiskKdayWeek(periodDay)
        self.headers = json.loads(self.kdayweek[0].strip("\'"))
        self.data = json.loads(self.kdayweek[1].strip("\'"))
        global saveZnach
        saveZnach = json.loads(self.kdayweek[2].strip("\'"))
        self.ui.tableWidget.setRowCount(len(self.data['2']))
        self.ui.tableWidget.setColumnCount(len(self.headers))
        self.wrap = []
        for header in self.headers:
            wrap = textwrap.fill(header, width=7)
            self.wrap.append(wrap)
        self.ui.tableWidget.setHorizontalHeaderLabels(self.wrap)
        self.font = QtGui.QFont("Times", 10, QFont.Weight.Bold)
        self.ui.tableWidget.horizontalHeader().setFont(self.font)
        for col in self.data:
            for row in self.data.get(col):
                if self.data[col][row] == 0:
                    if row == '0' and int(col) < 2:
                        item = QTableWidgetItem('')
                    else:
                        item = QTableWidgetItem('0')
                else:
                    item = QTableWidgetItem(str(self.data[col][row]))
                self.ui.tableWidget.setItem(int(row), int(col), item)
        self.ui.tableWidget.setItem(0, 1, QTableWidgetItem("Кф. кондитерской"))
        self.ui.tableWidget.item(0, 1).setFont(self.font)
        for col_spin in range(2, self.ui.tableWidget.columnCount()):
            self.DspinboxCol = QtWidgets.QDoubleSpinBox()
            self.DspinboxCol.wheelEvent = lambda event: None
            self.ui.tableWidget.setCellWidget(0, col_spin, self.DspinboxCol)
            self.ui.tableWidget.cellWidget(0, col_spin).setValue(float(self.ui.tableWidget.item(0, col_spin).text()))
            self.ui.tableWidget.cellWidget(0, col_spin).setSingleStep(0.01)
            self.ui.tableWidget.cellWidget(0, col_spin).valueChanged.connect(self.raschetKDayWeek)
        for row_spin in range(1, self.ui.tableWidget.rowCount()):
            self.DspinboxRow = QtWidgets.QDoubleSpinBox()
            self.DspinboxRow.wheelEvent = lambda event: None
            self.ui.tableWidget.setCellWidget(row_spin, 0, self.DspinboxRow)
            self.ui.tableWidget.cellWidget(row_spin, 0).setValue(float(self.ui.tableWidget.item(row_spin, 0).text()))
            self.ui.tableWidget.cellWidget(row_spin, 0).setSingleStep(0.01)
            self.ui.tableWidget.cellWidget(row_spin, 0).valueChanged.connect(self.raschetKDayWeek)
        self.periodDay = periodDay
        self.SaveAndClose = QtWidgets.QPushButton()
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        font.bold()
        font.setWeight(50)
        self.ui.tableWidget.setCellWidget(0, 0, self.SaveAndClose)
        self.ui.tableWidget.cellWidget(0, 0).setText('Сохранить и закрыть')
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
        self.ui.tableWidget.resizeColumnsToContents()
        self.ui.tableWidget.setColumnWidth(0, 190)


    def signal_prognoz(self, value):
        headers = value[0][2]
        data = value[0][3]
        saveNull = value[0][4]
        global kdayweek
        kdayweek = [headers, data, saveNull]

    def poiskKdayWeek(self, periodDay):
        self.check_db.thr_poiskDataPeriodaKdayWeek(periodDay)
        return(kdayweek)

    def saveAndCloseDef(self):
        savePeriod = self.periodDay
        saveNull = saveZnach.copy()
        saveHeaders = self.headers.copy()
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
        self.updateInDB(savePeriod, json.dumps(saveHeaders, ensure_ascii=False), json.dumps(saveDB, ensure_ascii=False), json.dumps(saveNull, ensure_ascii=False))
        self.close()

    def raschetKDayWeek(self):
        buttonClicked = self.sender()
        index = self.ui.tableWidget.indexAt(buttonClicked.pos())
        if index.row() == 0:
            for i in range(1, self.ui.tableWidget.rowCount()):
                result = round(float(saveZnach[str(index.column())][str(i)]) + float(self.ui.tableWidget.cellWidget(0, index.column()).value()) + float(self.ui.tableWidget.cellWidget(i, 0).value()), 4)
                self.ui.tableWidget.setItem(i, index.column(), QTableWidgetItem(str(result)))
        else:
            for i in range(2, self.ui.tableWidget.columnCount()):
                result = round(float(saveZnach[str(i)][str(index.row())]) + float(self.ui.tableWidget.cellWidget(index.row(), 0).value()) + float(self.ui.tableWidget.cellWidget(0, i).value()), 4)
                self.ui.tableWidget.setItem(index.row(), i, QTableWidgetItem(str(result)))


    def updateInDB(self, savePeriod, saveHeaders, saveDB, saveNull):
        self.check_db.thr_updateDayWeek(savePeriod, saveHeaders, saveDB, saveNull)

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