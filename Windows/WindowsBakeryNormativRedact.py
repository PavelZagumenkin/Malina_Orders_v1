from PyQt6 import QtWidgets, QtGui, QtCore
import json
import textwrap
from ui.bakeryTables import Ui_WindowBakeryTables
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.QtWidgets import QMessageBox
from handler.check_db import CheckThread
import Windows.WindowsBakery


class WindowBakeryNormativRedact(QtWidgets.QMainWindow):
    def __init__(self, periodDay):
        super().__init__()
        self.ui = Ui_WindowBakeryTables()
        self.ui.setupUi(self)
        self.check_db = CheckThread()
        self.check_db.normativdata.connect(self.signal_normativ)
        self.setWindowTitle("Редактор норматива приготовления")
        self.normativ = self.poiskNormativa(periodDay)
        self.headers = json.loads(self.normativ[0].strip("\'"))
        self.data = json.loads(self.normativ[1].strip("\'"))
        global saveZnach
        saveZnach =json.loads(self.normativ[2].strip("\'"))
        self.ui.tableWidget.setRowCount(len(self.data['0'])+1)
        self.ui.tableWidget.setColumnCount(len(self.headers)+1)
        self.headers.append('ИТОГО')
        self.wrap = []
        for header in self.headers:
            wrap = textwrap.fill(header, width=7)
            self.wrap.append(wrap)
        self.ui.tableWidget.setHorizontalHeaderLabels(self.wrap)
        self.font = QtGui.QFont("Times", 10, QFont.Weight.Bold)
        self.ui.tableWidget.horizontalHeader().setFont(self.font)
        self.periodDay = periodDay
        # Установливаем значения в таблицу
        for col in self.data:
            for row in self.data.get(col):
                if self.data[col][row] == 0:
                    if int(row) == 0:
                        item = QTableWidgetItem('')
                    else:
                        if int(col) != 0:
                            item = QTableWidgetItem('0.0')
                        else:
                            item = QTableWidgetItem('0,00')
                    self.ui.tableWidget.setItem(int(row), int(col), item)
                elif int(row) == 0:
                    self.DspinboxRow = QtWidgets.QDoubleSpinBox()
                    self.DspinboxRow.wheelEvent = lambda event: None
                    self.ui.tableWidget.setCellWidget(0, int(col), self.DspinboxRow)
                    self.ui.tableWidget.cellWidget(0, int(col)).setValue(float(self.data[col][row]))
                    self.ui.tableWidget.cellWidget(0, int(col)).setSingleStep(0.01)
                    self.ui.tableWidget.cellWidget(0, int(col)).valueChanged.connect(self.raschetNormativov)
                elif int(col) == 0:
                    self.DspinboxCol = QtWidgets.QDoubleSpinBox()
                    self.DspinboxCol.wheelEvent = lambda event: None
                    self.ui.tableWidget.setCellWidget(int(row), 0, self.DspinboxCol)
                    self.ui.tableWidget.cellWidget(int(row), 0).setValue(float(self.data[col][row]))
                    self.ui.tableWidget.cellWidget(int(row), 0).setSingleStep(0.01)
                    self.ui.tableWidget.cellWidget(int(row), 0).valueChanged.connect(self.raschetNormativov)
                else:
                    item = QTableWidgetItem(str(self.data[col][row]))
                    self.ui.tableWidget.setItem(int(row), int(col), item)
        # Вставляем кнопку Сохранить и закрыть
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
        self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount() - 1, 4, QTableWidgetItem("ИТОГО"))
        self.ui.tableWidget.cellChanged.connect(lambda row, col: self.on_cell_changed(row, col))
        self.ui.tableWidget.item(0, 4).setFont(self.font)
        self.ui.tableWidget.item(0, 4).setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.ui.tableWidget.resizeColumnsToContents()
        self.row_summ()
        self.col_summ()

    def row_summ(self):
        for col in range(5, self.ui.tableWidget.columnCount()):
            column_summ = 0
            for row in range(1, self.ui.tableWidget.rowCount()-1):
                item = self.ui.tableWidget.item(row, col)
                if item is not None:
                    column_summ += float(self.ui.tableWidget.item(row, col).text())
            self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount()-1, col, QTableWidgetItem(str(column_summ)))

    def col_summ(self):
        for row in range(1, self.ui.tableWidget.rowCount()):
            row_summ = 0
            for col in range(5, self.ui.tableWidget.columnCount()-1):
                item = self.ui.tableWidget.item(row, col)
                if item is not None:
                    row_summ += float(self.ui.tableWidget.item(row, col).text())
            self.ui.tableWidget.setItem(row, self.ui.tableWidget.columnCount()-1, QTableWidgetItem(str(row_summ)))


    def on_cell_changed(self, row, col):
        if row >= 1 and col >= 5:
            # Получаем содержимое ячейки и проверяем, является ли оно числом
            try:
                value = float(self.ui.tableWidget.item(row, col).text())
            except ValueError:
                value = None

            # Если содержимое не является числом, то заменяем его на 0.0
            if value is None:
                QtWidgets.QMessageBox.information(self, "Error", 'Вы ввели не число')
                self.ui.tableWidget.setItem(row, col, QTableWidgetItem(str(0.0)))
        else:
            return

    def raschetNormativov(self):
        buttonClicked = self.sender()
        index = self.ui.tableWidget.indexAt(buttonClicked.pos())
        if index.row() == 0:
            for i in range(1, self.ui.tableWidget.rowCount()-1):
                result = round(float(saveZnach[str(index.column()+2)][str(i)]) * float(self.ui.tableWidget.cellWidget(0, index.column()).value()) * float(self.ui.tableWidget.cellWidget(i, 0).value()), 0)
                self.ui.tableWidget.setItem(i, index.column(), QTableWidgetItem(str(result)))
        else:
            for i in range(5, self.ui.tableWidget.columnCount()-1):
                result = round(float(saveZnach[str(i+2)][str(index.row())]) * float(self.ui.tableWidget.cellWidget(index.row(), 0).value()) * float(self.ui.tableWidget.cellWidget(0, i).value()), 0)
                self.ui.tableWidget.setItem(index.row(), i, QTableWidgetItem(str(result)))
        self.row_summ()
        self.col_summ()


    def saveAndCloseDef(self):
        savePeriod = self.periodDay
        saveNull = saveZnach.copy()
        saveHeaders = self.headers.copy()
        saveHeaders.remove('ИТОГО')
        saveDB = {}
        for col in range(0, self.ui.tableWidget.columnCount()-1):
            saveDB[col] = {}
            for row in range(0, self.ui.tableWidget.rowCount()-1):
                if col == 0 or row == 0:
                    if self.ui.tableWidget.cellWidget(row, col) == None:
                        saveDB[col][row] = 0
                    elif (row == 0 and col == 3) or (row == 0 and col == 4):
                        saveDB[col][row] = 0
                    else:
                        saveDB[col][row] = float(self.ui.tableWidget.cellWidget(row, col).value())
                elif col == 2 or col == 3 or col == 4:
                    saveDB[col][row] = self.ui.tableWidget.item(row, col).text()
                else:
                    saveDB[col][row] = float(self.ui.tableWidget.item(row, col).text())
        self.insertNormativInDB(savePeriod, json.dumps(saveHeaders, ensure_ascii=False),
                                json.dumps(saveDB, ensure_ascii=False), json.dumps(saveNull, ensure_ascii=False))
        for row in range(1, self.ui.tableWidget.rowCount()-1):
            self.saveKfBakeryInDB(self.ui.tableWidget.item(row, 2).text(), self.ui.tableWidget.item(row, 3).text(),
                                  round(float(self.ui.tableWidget.cellWidget(row, 0).value()), 3))
        for col in range(5, self.ui.tableWidget.columnCount()-1):
            self.saveKfSkladaInDB(self.ui.tableWidget.horizontalHeaderItem(col).text(), round(float(self.ui.tableWidget.cellWidget(0, col).value()), 2))
        self.close()

    def poiskNormativa(self, periodDay):
        self.check_db.thr_poiskNormativa(periodDay)
        return(otvetNormativ)

    def signal_normativ(self, value):
        headers = value[0][2]
        data = value[0][3]
        saveNull = value[0][4]
        global otvetNormativ
        otvetNormativ = [headers, data, saveNull]

    def insertNormativInDB(self, savePeriod, saveHeaders, saveDB, saveNull):
        self.check_db.thr_updateNormativ(savePeriod, saveHeaders, saveDB, saveNull)

    def saveKfBakeryInDB(self, kod, name, layout):
        self.check_db.thr_saveKfBakeryInDB(kod, name, layout)

    def saveKfSkladaInDB(self, sklad, kf):
        self.check_db.thr_saveKfSkladaInDB(sklad, kf)


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