from PyQt6 import QtWidgets, QtGui, QtCore
import json
from ui.bakeryTables import Ui_WindowBakeryTables
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.QtWidgets import QInputDialog
from PyQt6.QtWidgets import QMessageBox
from handler.check_db import CheckThread
import Windows.WindowsBakery


class WindowBakeryNormativEdit(QtWidgets.QMainWindow):
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
        global data
        data = self.data
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
                    self.ui.tableWidget.setItem(int(row), int(col) - 2, item)
                elif int(row) == 0:
                    self.DspinboxRow = QtWidgets.QDoubleSpinBox()
                    self.DspinboxRow.wheelEvent = lambda event: None
                    sklad = self.headers[int(col)-2]
                    self.ui.tableWidget.setCellWidget(0, int(col)-2, self.DspinboxRow)
                    self.ui.tableWidget.cellWidget(0, int(col)-2).setValue(float(self.raschetNormativovSklada(sklad)))
                    self.ui.tableWidget.cellWidget(0, int(col)-2).setSingleStep(0.10)
                    self.ui.tableWidget.cellWidget(0, int(col)-2).valueChanged.connect(self.raschetNormativov)
                elif int(col) == 2:
                    self.DspinboxCol = QtWidgets.QDoubleSpinBox()
                    self.DspinboxCol.wheelEvent = lambda event: None
                    kod = self.data['4'][row]
                    tovar = self.data['5'][row]
                    self.ui.tableWidget.setCellWidget(int(row), 0, self.DspinboxCol)
                    self.ui.tableWidget.cellWidget(int(row), 0).setValue(float(self.raschetNormativovBakery(kod, tovar)))
                    self.ui.tableWidget.cellWidget(int(row), 0).setSingleStep(0.10)
                    self.ui.tableWidget.cellWidget(int(row), 0).valueChanged.connect(self.raschetNormativov)
                else:
                    item = QTableWidgetItem(str(self.data[col][row]))
                    self.ui.tableWidget.setItem(int(row), int(col) - 2, item)
        self.SaveAndClose = QtWidgets.QPushButton()
        self.ui.tableWidget.setCellWidget(0, 3, self.SaveAndClose)
        self.ui.tableWidget.cellWidget(0, 3).setText('Сохранить и закрыть')
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        font.bold()
        font.setWeight(50)
        self.ui.tableWidget.cellWidget(0, 3).setFont(font)
        self.ui.tableWidget.cellWidget(0, 3).setStyleSheet("QPushButton {\n"
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
        self.ui.tableWidget.cellWidget(0, 3).clicked.connect(self.saveAndCloseDef)
        self.ui.tableWidget.setItem(0, 4, QTableWidgetItem("Кф. склада кондитерской"))
        self.ui.tableWidget.item(0, 4).setFont(self.font)
        self.ui.tableWidget.item(0, 4).setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled)

    def raschetNormativov(self):
        buttonClicked = self.sender()
        index = self.ui.tableWidget.indexAt(buttonClicked.pos())
        if index.row() == 0:
            for i in range(1, self.ui.tableWidget.rowCount()):
                result = round(float(data[str(index.column()+2)][str(i)]) * float(self.ui.tableWidget.cellWidget(0, index.column()).value()) * float(self.ui.tableWidget.cellWidget(i, 0).value()), 2)
                self.ui.tableWidget.setItem(i, index.column(), QTableWidgetItem(str(result)))
        else:
            for i in range(5, self.ui.tableWidget.columnCount()):
                result = round(float(data[str(i+2)][str(index.row())]) * float(self.ui.tableWidget.cellWidget(index.row(), 0).value()) * float(self.ui.tableWidget.cellWidget(0, i).value()), 2)
                self.ui.tableWidget.setItem(index.row(), i, QTableWidgetItem(str(result)))

    def saveAndCloseDef(self):
        pass

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
            # if self.proverkaPerioda(self.periodDay) == 0:
            #     self.delPeriodInDB(self.periodDay)
            global WindowBakery
            WindowBakery = Windows.WindowsBakery.WindowBakery()
            WindowBakery.show()
        else:
            event.ignore()