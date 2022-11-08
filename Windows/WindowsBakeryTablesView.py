from PyQt6 import QtWidgets, QtGui
import json
from ui.bakeryTables import Ui_WindowBakeryTables
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.QtWidgets import QMessageBox
from handler.check_db import CheckThread
import Windows.WindowsBakery


class WindowBakeryTableView(QtWidgets.QMainWindow):
    def __init__(self, periodDay):
        super().__init__()
        self.ui = Ui_WindowBakeryTables()
        self.ui.setupUi(self)
        self.check_db = CheckThread()
        self.check_db.prognoz.connect(self.signal_prognoz)
        self.setWindowTitle("Просмотр прогноза продаж")
        self.prognoz = self.poiskPrognoza(periodDay)
        self.headers = json.loads(self.prognoz[0].strip("\'"))
        self.data = json.loads(self.prognoz[1].strip("\'"))
        self.ui.tableWidget.setRowCount(len(self.data['2']))
        self.ui.tableWidget.setColumnCount(len(self.headers))
        self.ui.tableWidget.setHorizontalHeaderLabels(self.headers)
        self.ui.tableWidget.setColumnWidth(0, 90)
        self.ui.tableWidget.setColumnWidth(1, 90)
        self.ui.tableWidget.setColumnWidth(2, 110)
        self.ui.tableWidget.setColumnWidth(3, 290)
        self.ui.tableWidget.setColumnWidth(4, 130)
        self.font = QtGui.QFont("Times", 10, QFont.Weight.Bold)
        self.ui.tableWidget.horizontalHeader().setFont(self.font)
        for col in self.data:
            for row in self.data.get(col):
                if self.data[col][row] == 0:
                    item = QTableWidgetItem('')
                else:
                    item = QTableWidgetItem(str(self.data[col][row]))
                self.ui.tableWidget.setItem(int(row), int(col) - 2, item)
        self.ui.tableWidget.setItem(0, 4, QTableWidgetItem("Кф. кондитерской"))
        self.ui.tableWidget.item(0, 4).setFont(self.font)

    def signal_prognoz(self, value):
        headers = value[0][2]
        data = value[0][3]
        global prognoz
        prognoz = [headers, data]

    def poiskPrognoza(self, periodDay):
        self.check_db.thr_poiskPrognoza(periodDay)
        return(prognoz)

    # Закрываем таблицу выпечки и возвращаемся к настройкам
    def closeWindowBakeryTables(self):
        self.close()
        global WindowBakery
        WindowBakery = Windows.WindowsBakery.WindowBakery()
        WindowBakery.show()

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