from PyQt6 import QtWidgets, QtGui
import json
from ui.bakeryTables import Ui_WindowBakeryTables
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.QtWidgets import QMessageBox
from handler.check_db import CheckThread
import Windows.WindowsBakery


class WindowBakeryTablesRedact(QtWidgets.QMainWindow):
    def __init__(self, periodDay):
        super().__init__()
        self.ui = Ui_WindowBakeryTables()
        self.ui.setupUi(self)
        self.check_db = CheckThread()
        self.check_db.prognoz.connect(self.signal_prognoz)
        self.setWindowTitle("Редактирование прогноза")
        self.prognoz = self.poiskPrognoza(periodDay)
        self.headers = json.loads(self.prognoz[0].strip("\'"))
        self.data = json.loads(self.prognoz[1].strip("\'"))
        global saveZnach
        saveZnach = json.loads(self.prognoz[2].strip("\'"))
        self.headers.insert(0, "")
        self.headers.insert(0, "")
        self.ui.tableWidget.setRowCount(len(self.data['2']))
        self.ui.tableWidget.setColumnCount(len(self.headers))
        self.ui.tableWidget.setHorizontalHeaderLabels(self.headers)
        self.font = QtGui.QFont("Times", 10, QFont.Weight.Bold)
        self.ui.tableWidget.horizontalHeader().setFont(self.font)
        for col in self.data:
            for row in self.data.get(col):
                if self.data[col][row] == 0:
                    item = QTableWidgetItem('')
                else:
                    item = QTableWidgetItem(str(self.data[col][row]))
                self.ui.tableWidget.setItem(int(row), int(col), item)
        self.ui.tableWidget.setItem(0, 6, QTableWidgetItem("Кф. кондитерской"))
        self.ui.tableWidget.item(0, 6).setFont(self.font)
        for col_spin in range(7, self.ui.tableWidget.columnCount()):
            self.DspinboxCol = QtWidgets.QDoubleSpinBox()
            self.DspinboxCol.wheelEvent = lambda event: None
            self.ui.tableWidget.setCellWidget(0, col_spin, self.DspinboxCol)
            self.ui.tableWidget.cellWidget(0, col_spin).setValue(float(self.ui.tableWidget.item(0, col_spin).text()))
            self.ui.tableWidget.cellWidget(0, col_spin).setSingleStep(0.05)
            self.ui.tableWidget.cellWidget(0, col_spin).valueChanged.connect(self.raschetPrognoz)
        for row_spin in range(1, self.ui.tableWidget.rowCount()):
            self.DspinboxRow = QtWidgets.QDoubleSpinBox()
            self.SpinboxRow = QtWidgets.QSpinBox()
            self.DspinboxRow.wheelEvent = lambda event: None
            self.SpinboxRow.wheelEvent = lambda event: None
            self.ui.tableWidget.setCellWidget(row_spin, 2, self.DspinboxRow)
            self.ui.tableWidget.cellWidget(row_spin, 2).setValue(float(self.ui.tableWidget.item(row_spin, 2).text()))
            self.ui.tableWidget.cellWidget(row_spin, 2).setSingleStep(0.05)
            self.ui.tableWidget.cellWidget(row_spin, 2).valueChanged.connect(self.raschetPrognoz)
            self.ui.tableWidget.setCellWidget(row_spin, 3, self.SpinboxRow)
            self.ui.tableWidget.cellWidget(row_spin, 3).setValue(int(float(self.ui.tableWidget.item(row_spin, 3).text())))
            self.ui.tableWidget.cellWidget(row_spin, 3).setSingleStep(1)
        for row_button in range(1, self.ui.tableWidget.rowCount()):
            self.copyRowButton = QtWidgets.QPushButton()
            self.ui.tableWidget.setCellWidget(row_button, 0, self.copyRowButton)
            self.ui.tableWidget.cellWidget(row_button, 0).setText('')
            iconCopy = QtGui.QIcon()
            iconCopy.addPixmap(QtGui.QPixmap("image/copy.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            self.ui.tableWidget.cellWidget(row_button, 0).setIcon(iconCopy)
            self.ui.tableWidget.cellWidget(row_button, 0).clicked.connect(self.copyRow)
            self.deleteRowButton = QtWidgets.QPushButton()
            self.ui.tableWidget.setCellWidget(row_button, 1, self.deleteRowButton)
            self.ui.tableWidget.cellWidget(row_button, 1).setText('')
            iconCross = QtGui.QIcon()
            iconCross.addPixmap(QtGui.QPixmap("image/cross.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            self.ui.tableWidget.cellWidget(row_button, 1).setIcon(iconCross)
            self.ui.tableWidget.cellWidget(row_button, 1).clicked.connect(self.deleteRow)
        self.periodDay = periodDay
        self.SaveAndNext = QtWidgets.QPushButton()
        self.SaveAndClose = QtWidgets.QPushButton()
        self.ui.tableWidget.setCellWidget(0, 4, self.SaveAndNext)
        self.ui.tableWidget.cellWidget(0, 4).setText('Продолжить')
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        font.bold()
        font.setWeight(50)
        self.ui.tableWidget.cellWidget(0, 4).setFont(font)
        self.ui.tableWidget.cellWidget(0, 4).setStyleSheet("QPushButton {\n"
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
        self.ui.tableWidget.cellWidget(0, 4).clicked.connect(self.saveAndNextDef)
        self.ui.tableWidget.setCellWidget(0, 5, self.SaveAndClose)
        self.ui.tableWidget.cellWidget(0, 5).setText('Сохранить и закрыть')
        self.ui.tableWidget.cellWidget(0, 5).setFont(font)
        self.ui.tableWidget.cellWidget(0, 5).setStyleSheet("QPushButton {\n"
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
        self.ui.tableWidget.cellWidget(0, 5).clicked.connect(self.saveAndCloseDef)
        self.ui.tableWidget.setColumnWidth(0, 20)
        self.ui.tableWidget.setColumnWidth(1, 20)
        self.ui.tableWidget.setColumnWidth(2, 90)
        self.ui.tableWidget.setColumnWidth(3, 90)
        self.ui.tableWidget.setColumnWidth(4, 110)
        self.ui.tableWidget.setColumnWidth(5, 290)
        self.ui.tableWidget.setColumnWidth(6, 130)


    def signal_prognoz(self, value):
        headers = value[0][2]
        data = value[0][3]
        saveNull = value[0][4]
        global prognoz
        prognoz = [headers, data, saveNull]

    def poiskPrognoza(self, periodDay):
        self.check_db.thr_poiskPrognoza(periodDay)
        return(prognoz)

    def saveAndNextDef(self):
        savePeriod = self.periodDay
        headers = self.headers.copy()
        saveNull = saveZnach.copy()
        del headers[0:2]
        saveHeaders = headers
        saveDB = {}
        for col in range(2, self.ui.tableWidget.columnCount()):
            saveDB[col] = {}
            for row in range(0, self.ui.tableWidget.rowCount()):
                if col == 2 or col == 3 or row == 0:
                    if self.ui.tableWidget.cellWidget(row, col) == None:
                        saveDB[col][row] = 0
                    elif (row == 0 and col == 4) or (row == 0 and col == 5):
                        saveDB[col][row] = 0
                    else:
                        saveDB[col][row] = float(self.ui.tableWidget.cellWidget(row, col).value())
                elif col == 4 or col == 5 or col == 6:
                    saveDB[col][row] = self.ui.tableWidget.item(row, col).text()
                else:
                    saveDB[col][row] = float(self.ui.tableWidget.item(row, col).text())
        self.updateInDB(savePeriod, json.dumps(saveHeaders, ensure_ascii=False), json.dumps(saveDB, ensure_ascii=False), json.dumps(saveNull, ensure_ascii=False))
        # Продолжение работы с коэффициентами дня недели

    def saveAndCloseDef(self):
        savePeriod = self.periodDay
        headers = self.headers.copy()
        saveNull = saveZnach.copy()
        del headers[0:2]
        saveHeaders = headers
        saveDB = {}
        for col in range(2, self.ui.tableWidget.columnCount()):
            saveDB[col] = {}
            for row in range(0, self.ui.tableWidget.rowCount()):
                if col == 2 or col == 3 or row == 0:
                    if self.ui.tableWidget.cellWidget(row, col) == None:
                        saveDB[col][row] = 0
                    elif (row == 0 and col == 4) or (row == 0 and col == 5):
                        saveDB[col][row] = 0
                    else:
                        saveDB[col][row] = float(self.ui.tableWidget.cellWidget(row, col).value())
                elif col == 4 or col == 5 or col == 6:
                    saveDB[col][row] = self.ui.tableWidget.item(row, col).text()
                else:
                    saveDB[col][row] = float(self.ui.tableWidget.item(row, col).text())
        self.updateInDB(savePeriod, json.dumps(saveHeaders, ensure_ascii=False), json.dumps(saveDB, ensure_ascii=False), json.dumps(saveNull, ensure_ascii=False))
        self.closeWindowBakeryTables()

    def raschetPrognoz(self):
        buttonClicked = self.sender()
        index = self.ui.tableWidget.indexAt(buttonClicked.pos())
        if index.row() == 0:
            for i in range(1, self.ui.tableWidget.rowCount()):
                result = round(float(saveZnach[str(index.column())][str(i)]) * float(self.ui.tableWidget.cellWidget(0, index.column()).value()) * float(self.ui.tableWidget.cellWidget(i, 2).value()), 2)
                self.ui.tableWidget.setItem(i, index.column(), QTableWidgetItem(str(result)))
        else:
            for i in range(7, self.ui.tableWidget.columnCount()):
                result = round(float(saveZnach[str(i)][str(index.row())]) * float(self.ui.tableWidget.cellWidget(index.row(), 2).value()) * float(self.ui.tableWidget.cellWidget(0, i).value()), 2)
                self.ui.tableWidget.setItem(index.row(), i, QTableWidgetItem(str(result)))

    def copyRow(self):
        buttonClicked = self.sender()
        index = self.ui.tableWidget.indexAt(buttonClicked.pos())
        rowPosition = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(rowPosition)
        self.copyRowButton = QtWidgets.QPushButton()
        self.ui.tableWidget.setCellWidget(rowPosition, 0, self.copyRowButton)
        self.ui.tableWidget.cellWidget(rowPosition, 0).setText('')
        iconCopy = QtGui.QIcon()
        iconCopy.addPixmap(QtGui.QPixmap("image/copy.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.ui.tableWidget.cellWidget(rowPosition, 0).setIcon(iconCopy)
        self.ui.tableWidget.cellWidget(rowPosition, 0).clicked.connect(self.copyRow)
        self.deleteRowButton = QtWidgets.QPushButton()
        self.ui.tableWidget.setCellWidget(rowPosition, 1, self.deleteRowButton)
        self.ui.tableWidget.cellWidget(rowPosition, 1).setText('')
        iconCross = QtGui.QIcon()
        iconCross.addPixmap(QtGui.QPixmap("image/cross.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.ui.tableWidget.cellWidget(rowPosition, 1).setIcon(iconCross)
        self.ui.tableWidget.cellWidget(rowPosition, 1).clicked.connect(self.deleteRow)
        self.DspinboxRow = QtWidgets.QDoubleSpinBox()
        self.SpinboxRow = QtWidgets.QSpinBox()
        self.DspinboxRow.wheelEvent = lambda event: None
        self.SpinboxRow.wheelEvent = lambda event: None
        self.ui.tableWidget.setCellWidget(rowPosition, 2, self.DspinboxRow)
        self.ui.tableWidget.cellWidget(rowPosition, 2).setValue(1.00)
        self.ui.tableWidget.cellWidget(rowPosition, 2).setSingleStep(0.05)
        self.ui.tableWidget.cellWidget(rowPosition, 2).valueChanged.connect(self.raschetPrognoz)
        self.ui.tableWidget.setCellWidget(rowPosition, 3, self.SpinboxRow)
        self.ui.tableWidget.cellWidget(rowPosition, 3).setValue(1)
        self.ui.tableWidget.cellWidget(rowPosition, 3).setSingleStep(1)
        for c in range(6, 7):
            self.ui.tableWidget.setItem(rowPosition, c, QTableWidgetItem(self.ui.tableWidget.item(index.row(), c).text()))
        for c in range(7, self.ui.tableWidget.columnCount()):
            self.ui.tableWidget.setItem(rowPosition, c, QTableWidgetItem(str(round(saveZnach[str(c)][str(index.row())] * float(self.ui.tableWidget.cellWidget(0, c).value()), 2))))
        for c in range(7, self.ui.tableWidget.columnCount()):
            saveZnach[str(c)][str(rowPosition)] = round(float(self.ui.tableWidget.item(rowPosition, c).text()) / float(self.ui.tableWidget.cellWidget(0, c).value()), 2)

    def deleteRow(self):
        buttonClicked = self.sender()
        index = self.ui.tableWidget.indexAt(buttonClicked.pos())
        self.ui.tableWidget.removeRow(index.row())
        for c in range(7, self.ui.tableWidget.columnCount()):
            del saveZnach[str(c)][str(index.row())]
        for c in range(7, self.ui.tableWidget.columnCount()):
            counter = index.row() + 1
            for r in range(index.row(), self.ui.tableWidget.rowCount()):
                saveZnach[str(c)][str(r)] = saveZnach[str(c)].pop(str(counter))
                counter += 1

    def updateInDB(self, savePeriod, saveHeaders, saveDB, saveNull):
        self.check_db.thr_updatePrognoz(savePeriod, saveHeaders, saveDB, saveNull)

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