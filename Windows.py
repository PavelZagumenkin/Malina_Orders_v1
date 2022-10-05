import copy
from PyQt6 import QtCore, QtGui, QtWidgets
import win32com.client
from PyQt6.QtGui import *
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.QtGui import QFont
from main import Main
from ui.login import Ui_WindowLogin
from ui.viborRazdela import Ui_WindowViborRazdela
from ui.bakery import Ui_WindowBakery
from ui.bakeryTables import Ui_WindowBakeryTables


class WindowLogin(QtWidgets.QMainWindow, Main):
    def __init__(self):
        super().__init__()
        self.ui = Ui_WindowLogin()
        self.ui.setupUi(self)
        self.ui.label_login_password.setFocus()  # Фокус по умолчанию на тексте
        self.base_line_edit = [self.ui.line_login, self.ui.line_password]
        self.ui.btn_login.clicked.connect(self.login)


class WindowViborRazdela(QtWidgets.QMainWindow, Main):
    def __init__(self):
        super().__init__()
        self.ui = Ui_WindowViborRazdela()
        self.ui.setupUi(self)
        self.ui.btn_exit.clicked.connect(self.logout)
        self.ui.btn_bakery.clicked.connect(self.bakeryOpen)


class WindowBakery(QtWidgets.QMainWindow, Main):
    def __init__(self):
        super().__init__()
        self.ui = Ui_WindowBakery()
        self.ui.setupUi(self)
        self.ui.btn_exit_bakery.clicked.connect(self.viborRazdelaOpen)
        self.ui.btn_path_OLAP_P.clicked.connect(self.olap_p)
        self.ui.btn_path_dayWeek_bakery.clicked.connect(self.olap_dayWeek_bakery)
        self.ui.btn_koeff_bakery.clicked.connect(self.koeff_bakery_start)
        self.base_fileOLAP_bakery = [self.ui.lineEdit_OLAP_P, self.ui.lineEdit_OLAP_dayWeek_bakery]

    def olap_p(self):
        fileName = QFileDialog.getOpenFileName(self, 'Выберите файл OLAP по продажам', 'Отчеты', 'Excel файл (*.xlsx)')
        self.ui.lineEdit_OLAP_P.setText(fileName[0])
        self.ui.lineEdit_OLAP_P.setStyleSheet("padding-left: 5px; color: rgb(0, 0, 0)")

    def olap_dayWeek_bakery(self):
        fileName = QFileDialog.getOpenFileName(self, 'Выберите файл OLAP по дням недели для пекарни', 'Отчеты',
                                               'Excel файл (*.xlsx)')
        self.ui.lineEdit_OLAP_dayWeek_bakery.setText(fileName[0])
        self.ui.lineEdit_OLAP_dayWeek_bakery.setStyleSheet("padding-left: 5px; color: rgb(0, 0, 0)")

    # Проверяем на пустоту полей для отчетов
    def check_bakeryOLAP(funct_bakery):
        def wrapper(self):
            for line_edit in self.base_fileOLAP_bakery:
                if len(line_edit.text()) == 0 or line_edit.text() == 'Файл отчета неверный, укажите OLAP по продажам за 7 дней' or line_edit.text() == 'Файл отчета неверный, укажите OLAP по продажам по дня недели для Выпечки пекарни' or line_edit.text() == 'Вы выбрали одинаковые файлы отчета. Хватит издеваться над программой!':
                    line_edit.setStyleSheet("padding-left: 5px; color: rgba(228, 107, 134, 1)")
                    line_edit.setText('Не выбран файл отчета!')
                    return
                elif line_edit.text() == 'Не выбран файл отчета!':
                    return
            funct_bakery(self)

        return wrapper

    # Обрабытываем кнопку "Выпечка"
    @check_bakeryOLAP
    def koeff_bakery_start(self):
        pathOLAP_P = self.ui.lineEdit_OLAP_P.text()
        pathOLAP_dayWeek_bakery = self.ui.lineEdit_OLAP_dayWeek_bakery.text()
        if pathOLAP_P != pathOLAP_dayWeek_bakery:
            self.bakeryTable(pathOLAP_P, pathOLAP_dayWeek_bakery)
        else:
            self.ui.lineEdit_OLAP_P.setStyleSheet("padding-left: 5px; color: rgba(228, 107, 134, 1)")
            self.ui.lineEdit_OLAP_P.setText('Вы выбрали одинаковые файлы отчета. Хватит издеваться над программой!')
            self.ui.lineEdit_OLAP_dayWeek_bakery.setStyleSheet("padding-left: 5px; color: rgba(228, 107, 134, 1)")
            self.ui.lineEdit_OLAP_dayWeek_bakery.setText(
                'Вы выбрали одинаковые файлы отчета. Хватит издеваться над программой!')

    def bakeryTable(self, pathOLAP_P, pathOLAP_dayWeek_bakery):
        Excel = win32com.client.Dispatch("Excel.Application")
        wb_OLAP_P = Excel.Workbooks.Open(pathOLAP_P)
        wb_OLAP_dayWeek_bakery = Excel.Workbooks.Open(pathOLAP_dayWeek_bakery)
        sheet_OLAP_P = wb_OLAP_P.ActiveSheet
        sheet_OLAP_dayWeek_bakery = wb_OLAP_dayWeek_bakery.ActiveSheet

        if sheet_OLAP_P.Name != "OLAP по продажам ОБЩИЙ":
            wb_OLAP_P.Close()
            wb_OLAP_dayWeek_bakery.Close()
            Excel.Quit()
            self.ui.lineEdit_OLAP_P.setStyleSheet("padding-left: 5px; color: rgba(228, 107, 134, 1)")
            self.ui.lineEdit_OLAP_P.setText('Файл отчета неверный, укажите OLAP по продажам за 7 дней')
        elif sheet_OLAP_dayWeek_bakery.Name != "OLAP по дням недели для Пекарни":
            wb_OLAP_P.Close()
            wb_OLAP_dayWeek_bakery.Close()
            Excel.Quit()
            self.ui.lineEdit_OLAP_dayWeek_bakery.setStyleSheet("padding-left: 5px; color: rgba(228, 107, 134, 1)")
            self.ui.lineEdit_OLAP_dayWeek_bakery.setText(
                'Файл отчета неверный, укажите OLAP по продажам по дня недели для Выпечки пекарни')
        else:
            wb_OLAP_P.Close()
            wb_OLAP_dayWeek_bakery.Close()
            Excel.Quit()
            self.bakeryTablesOpen(pathOLAP_P, pathOLAP_dayWeek_bakery)


class WindowBakeryTables(QtWidgets.QMainWindow, Main):
    def __init__(self, pathOLAP_P, pathOLAP_dayWeek_bakery):
        super().__init__()
        self.ui = Ui_WindowBakeryTables()
        self.ui.setupUi(self)
        Excel = win32com.client.Dispatch("Excel.Application")
        wb_OLAP_P = Excel.Workbooks.Open(pathOLAP_P)
        wb_OLAP_dayWeek_bakery = Excel.Workbooks.Open(pathOLAP_dayWeek_bakery)
        sheet_OLAP_P = wb_OLAP_P.ActiveSheet
        sheet_OLAP_dayWeek_bakery = wb_OLAP_dayWeek_bakery.ActiveSheet
        firstOLAPRow = sheet_OLAP_P.Range("A:A").Find("Код блюда").Row
        for _ in range(firstOLAPRow - 1):
            sheet_OLAP_P.Rows(1).Delete()
        firstOLAPRow = sheet_OLAP_P.Range("A:A").Find("Код блюда").Row
        endOLAPRow = sheet_OLAP_P.Range("A:C").Find("Итого").Row
        endOLAPCol = sheet_OLAP_P.Cells.Find("Итого").Column
        for a in range(endOLAPCol, 1, -1):
            if sheet_OLAP_P.Cells(1, a).Value is None:
                sheet_OLAP_P.Columns(a).Delete()
        endOLAPCol = sheet_OLAP_P.Cells.Find("Итого").Column
        self.ui.tableWidget.setRowCount(endOLAPRow)
        self.ui.tableWidget.setColumnCount(endOLAPCol + 4)
        self.columnLables = list(sheet_OLAP_P.Range(sheet_OLAP_P.Cells(1, 1), sheet_OLAP_P.Cells(1, endOLAPCol - 1)).Value[0])
        self.columnLables.insert(0, "Выкладка")
        self.columnLables.insert(0, "Кф. пекарни")
        self.columnLables.insert(0, "Кф. товара")
        self.columnLables.insert(0, "")
        self.columnLables.insert(0, "")
        self.ui.tableWidget.setHorizontalHeaderLabels(self.columnLables)
        self.font = QtGui.QFont("Times", 10, QFont.Weight.Bold)
        self.ui.tableWidget.horizontalHeader().setFont(self.font)
        for col in range(1, endOLAPCol):
            for row in range(2, endOLAPRow + 1):
                item = sheet_OLAP_P.Cells(row, col).Value
                item = QTableWidgetItem(str(item))
                self.ui.tableWidget.setItem(row, col + 4, item)
        global saveZnach
        saveZnach = {}
        for col in range(8, self.ui.tableWidget.columnCount()):
            saveZnach[col] = {}
            for row in range(3, self.ui.tableWidget.rowCount()+1):
                saveZnach[col][row] = float(self.ui.tableWidget.item(row-1, col).text())
        self.ui.tableWidget.setItem(0, 7, QTableWidgetItem("Кф. кондитерской"))
        self.ui.tableWidget.item(0, 7).setFont(self.font)
        self.ui.tableWidget.setItem(1, 7, QTableWidgetItem("Кф. запаса дн."))
        self.ui.tableWidget.item(1, 7).setFont(self.font)
        for col_spin in range(8, self.ui.tableWidget.columnCount()):
            self.DspinboxCol1 = QtWidgets.QDoubleSpinBox()
            self.DspinboxCol1.wheelEvent = lambda event: None
            self.DspinboxCol2 = QtWidgets.QDoubleSpinBox()
            self.DspinboxCol2.wheelEvent = lambda event: None
            self.ui.tableWidget.setCellWidget(0, col_spin, self.DspinboxCol1)
            self.ui.tableWidget.cellWidget(0, col_spin).setValue(1.00)
            self.ui.tableWidget.cellWidget(0, col_spin).setSingleStep(0.05)
            self.ui.tableWidget.cellWidget(0, col_spin).valueChanged.connect(self.raschetPrognoz)
            self.ui.tableWidget.setCellWidget(1, col_spin, self.DspinboxCol2)
            self.ui.tableWidget.cellWidget(1, col_spin).setValue(1.00)
            self.ui.tableWidget.cellWidget(1, col_spin).setSingleStep(0.05)
        for row_spin in range(2, self.ui.tableWidget.rowCount()):
            self.DspinboxRow1 = QtWidgets.QDoubleSpinBox()
            self.DspinboxRow2 = QtWidgets.QDoubleSpinBox()
            self.spinboxRow = QtWidgets.QSpinBox()
            self.DspinboxRow1.wheelEvent = lambda event: None
            self.DspinboxRow2.wheelEvent = lambda event: None
            self.spinboxRow.wheelEvent = lambda event: None
            self.ui.tableWidget.setCellWidget(row_spin, 2, self.DspinboxRow1)
            self.ui.tableWidget.cellWidget(row_spin, 2).setValue(1.00)
            self.ui.tableWidget.cellWidget(row_spin, 2).setSingleStep(0.05)
            self.ui.tableWidget.cellWidget(row_spin, 2).valueChanged.connect(self.raschetPrognoz)
            self.ui.tableWidget.setCellWidget(row_spin, 3, self.DspinboxRow2)
            self.ui.tableWidget.cellWidget(row_spin, 3).setValue(1.00)
            self.ui.tableWidget.cellWidget(row_spin, 3).setSingleStep(0.05)
            self.ui.tableWidget.setCellWidget(row_spin, 4, self.spinboxRow)
            self.ui.tableWidget.cellWidget(row_spin, 4).setValue(1)
            self.ui.tableWidget.cellWidget(row_spin, 4).setSingleStep(1)
        for row_button in range(2, self.ui.tableWidget.rowCount()):
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
        self.ui.tableWidget.setColumnWidth(0, 20)
        self.ui.tableWidget.setColumnWidth(1, 20)
        self.ui.tableWidget.setColumnWidth(2, 90)
        self.ui.tableWidget.setColumnWidth(3, 90)
        self.ui.tableWidget.setColumnWidth(4, 90)
        self.ui.tableWidget.setColumnWidth(5, 90)
        self.ui.tableWidget.setColumnWidth(6, 290)
        self.ui.tableWidget.setColumnWidth(7, 130)

    def raschetPrognoz(self):
        buttonClicked = self.sender()
        index = self.ui.tableWidget.indexAt(buttonClicked.pos())
        if index.row() == 0:
            for i in range(3, self.ui.tableWidget.rowCount()+1):
                result = round(float(saveZnach[index.column()][i]) * float(self.ui.tableWidget.cellWidget(0, index.column()).value()) * float(self.ui.tableWidget.cellWidget(i-1, 2).value()), 2)
                self.ui.tableWidget.setItem(i - 1, index.column(), QTableWidgetItem(str(result)))
        else:
            for i in range(8, self.ui.tableWidget.columnCount()):
                result = round(float(saveZnach[i][index.row()+1]) * float(self.ui.tableWidget.cellWidget(index.row(), 2).value()) * float(self.ui.tableWidget.cellWidget(0, i).value()), 2)
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
        self.DspinboxRow1 = QtWidgets.QDoubleSpinBox()
        self.DspinboxRow2 = QtWidgets.QDoubleSpinBox()
        self.spinboxRow = QtWidgets.QSpinBox()
        self.DspinboxRow1.wheelEvent = lambda event: None
        self.DspinboxRow2.wheelEvent = lambda event: None
        self.spinboxRow.wheelEvent = lambda event: None
        self.ui.tableWidget.setCellWidget(rowPosition, 2, self.DspinboxRow1)
        self.ui.tableWidget.cellWidget(rowPosition, 2).setValue(1.00)
        self.ui.tableWidget.cellWidget(rowPosition, 2).setSingleStep(0.05)
        self.ui.tableWidget.cellWidget(rowPosition, 2).valueChanged.connect(self.raschetPrognoz)
        self.ui.tableWidget.setCellWidget(rowPosition, 3, self.DspinboxRow2)
        self.ui.tableWidget.cellWidget(rowPosition, 3).setValue(1.00)
        self.ui.tableWidget.cellWidget(rowPosition, 3).setSingleStep(0.05)
        self.ui.tableWidget.setCellWidget(rowPosition, 4, self.spinboxRow)
        self.ui.tableWidget.cellWidget(rowPosition, 4).setValue(1)
        self.ui.tableWidget.cellWidget(rowPosition, 4).setSingleStep(1)
        for c in range(7, 8):
            self.ui.tableWidget.setItem(rowPosition, c, QTableWidgetItem(self.ui.tableWidget.item(index.row(), c).text()))
        for c in range(8, self.ui.tableWidget.columnCount()):
            self.ui.tableWidget.setItem(rowPosition, c, QTableWidgetItem(str(saveZnach[c][index.row()+1])))
        for c in range(8, self.ui.tableWidget.columnCount()):
            saveZnach[c][rowPosition + 1] = float(self.ui.tableWidget.item(rowPosition, c).text())

    def deleteRow(self):
        buttonClicked = self.sender()
        index = self.ui.tableWidget.indexAt(buttonClicked.pos())
        self.ui.tableWidget.removeRow(index.row())
        for c in range(8, self.ui.tableWidget.columnCount()):
            del saveZnach[c][index.row() + 1]
        for c in range(8, self.ui.tableWidget.columnCount()):
            counter = index.row() + 2
            for r in range(index.row() + 1, self.ui.tableWidget.rowCount() + 1):
                saveZnach[c][r] = saveZnach[c].pop(counter)
                counter += 1


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
