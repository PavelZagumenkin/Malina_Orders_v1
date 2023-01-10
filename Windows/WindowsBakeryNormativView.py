from PyQt6 import QtWidgets, QtGui, QtCore
import json
from ui.bakeryTables import Ui_WindowBakeryTables
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.QtWidgets import QInputDialog
from PyQt6.QtWidgets import QMessageBox
from handler.check_db import CheckThread
import Windows.WindowsBakery


class WindowBakeryNormativView(QtWidgets.QMainWindow):
    def __init__(self, periodDay):
        super().__init__()
        self.ui = Ui_WindowBakeryTables()
        self.ui.setupUi(self)
        self.check_db = CheckThread()
        self.check_db.prognoz.connect(self.signal_prognoz)
        self.check_db.kfBakery.connect(self.signal_kfBakery)
        self.check_db.kfSklada.connect(self.signal_kfSklada)
        self.setWindowTitle("Просмотр норматива приготовления")
        self.prognoz = self.poiskPrognoza(periodDay)
        self.headers = json.loads(self.prognoz[0].strip("\'"))
        self.data = json.loads(self.prognoz[1].strip("\'"))
        self.ui.tableWidget.setRowCount(len(self.data['2']))
        self.ui.tableWidget.setColumnCount(len(self.headers))
        self.headers[0] = 'Кф. пекарни'
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
                elif int(row) == 0:
                    sklad = self.headers[int(col)-2]
                    item = QTableWidgetItem(str(self.raschetNormativovSklada(sklad)))
                    self.ui.tableWidget.setItem(int(row), int(col) - 2, item)
                elif int(col) == 2:
                    kod = self.data['4'][row]
                    tovar = self.data['5'][row]
                    item = QTableWidgetItem(str(self.raschetNormativovBakery(kod, tovar)))
                    self.ui.tableWidget.setItem(int(row), int(col) - 2, item)
                else:
                    item = QTableWidgetItem(str(self.data[col][row]))
                self.ui.tableWidget.setItem(int(row), int(col) - 2, item)
                if (int(col) != 0 and int(row) != 0) or (int(col) != 1 and int(row) != 0) or (int(col) != 2 and int(row) != 0) or (int(col) != 3 and int(row) != 0):
                    self.ui.tableWidget.item(int(row), int(col) - 2).setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.ui.tableWidget.setItem(0, 4, QTableWidgetItem("Кф. склада кондитерской"))
        self.ui.tableWidget.item(0, 4).setFont(self.font)
        self.ui.tableWidget.item(0, 4).setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled)


    def signal_prognoz(self, value):
        headers = value[0][2]
        data = value[0][3]
        global prognoz
        prognoz = [headers, data]

    def poiskPrognoza(self, periodDay):
        self.check_db.thr_poiskPrognoza(periodDay)
        return(prognoz)

    def signal_kfBakery(self, value):
        global kfBakery
        if value != 'КФ отсутствует в БД':
            kfBakery = value
        else:
            kfBakery = self.dialogAddKfBakery()

    def raschetNormativovBakery(self, kod, tovar):
        global kod_text
        kod_text = kod
        global tovar_text
        tovar_text = tovar
        self.check_db.thr_poisk_kfBakery(kod)
        return(kfBakery)

    def dialogAddKfBakery(self):
        kol, ok = QInputDialog.getDouble(self, "Отсуствует коэффициент пекарни", f"Введите коэффициент пекарни для {tovar_text} код изделия {kod_text}:")
        if ok:
            self.check_db.thr_updateKfBakery(kod_text, float(kol))
            return(float(kol))
        else:
            self.check_db.thr_updateKfBakery(kod_text, 1.0)
            return(1.0)

    def signal_kfSklada(self, value):
        global kfSklada
        if value != 'Склад отсутствует в БД':
            kfSklada = value
        else:
            self.dialogNetSklada()
            kfSklada = 1.0

    def raschetNormativovSklada(self, sklad):
        global name_sklada
        name_sklada = sklad
        self.check_db.thr_poisk_sklada(sklad)
        return(kfSklada)

    def dialogNetSklada(self):
        dialogBox = QMessageBox()
        dialogBox.setText(f"В базе данных отсутствует склад кондитерской {name_sklada}, пожалуйста обратитесь к администратору приложения.")
        dialogBox.setWindowIcon(QtGui.QIcon("image/icon.png"))
        dialogBox.setWindowTitle('Критическая ошибка!')
        dialogBox.setIcon(QMessageBox.Icon.Critical)
        dialogBox.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        dialogBox.exec()