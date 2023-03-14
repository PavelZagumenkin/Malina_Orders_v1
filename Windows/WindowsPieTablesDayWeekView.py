from PyQt6 import QtWidgets, QtGui, QtCore
import json
import textwrap
from ui.bakeryTables import Ui_WindowBakeryTables
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.QtWidgets import QMessageBox
from handler.check_db import CheckThread
import Windows.WindowsPie


class WindowPieTableDayWeekView(QtWidgets.QMainWindow):
    def __init__(self, periodDay):
        super().__init__()
        self.ui = Ui_WindowBakeryTables()
        self.ui.setupUi(self)
        self.check_db = CheckThread()
        self.check_db.prognoz.connect(self.signal_prognoz)
        self.setWindowTitle("Просмотр коэффициентов долей продаж")
        self.prognoz = self.poiskPrognoza(periodDay)
        self.headers = json.loads(self.prognoz[0].strip("\'"))
        self.data = json.loads(self.prognoz[1].strip("\'"))
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
                if int(col) == 0 and int(row) == 0:
                    item = QTableWidgetItem("")
                elif int(col) == 1:
                    item = QTableWidgetItem(str(self.data[col][row]))
                elif (int(col) != 0 and int(row) == 0) or (int(col) != 1 and int(row) == 0) or (int(col) == 0 and int(row) != 0):
                    item = QTableWidgetItem(str(round(float(self.data[col][row]), 2)))
                else:
                    item = QTableWidgetItem(str(self.data[col][row]))
                self.ui.tableWidget.setItem(int(row), int(col), item)
                if (int(col) != 0 and int(row) != 0) or (int(col) != 1 and int(row) != 0):
                    self.ui.tableWidget.item(int(row), int(col)).setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.ui.tableWidget.setItem(0, 1, QTableWidgetItem("Кф. кондитерской"))
        self.ui.tableWidget.item(0, 1).setFont(self.font)
        self.ui.tableWidget.resizeColumnsToContents()

    def signal_prognoz(self, value):
        headers = value[0][2]
        data = value[0][3]
        global prognoz
        prognoz = [headers, data]

    def poiskPrognoza(self, periodDay):
        self.check_db.thr_poiskDataPeriodaKdayWeek(periodDay)
        return(prognoz)

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