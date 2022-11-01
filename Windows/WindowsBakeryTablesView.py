from PyQt6 import QtWidgets, QtGui
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
        # self.prognoz = self.poiskPrognoza(periodDay)
        # self.headers = self.prognoz[0].split(sep="', '")
        # self.data = self.prognoz[1].split()
        # self.ui.tableWidget.setRowCount(3)
        # self.ui.tableWidget.setColumnCount(len(self.headers))
        # self.ui.tableWidget.setHorizontalHeaderLabels(self.headers)
        # self.font = QtGui.QFont("Times", 10, QFont.Weight.Bold)
        # self.ui.tableWidget.horizontalHeader().setFont(self.font)
        # for col in range(1, endOLAPCol):
        #     for row in range(2, endOLAPRow):
        #         item = sheet_OLAP_P.Cells(row, col).Value
        #         item = QTableWidgetItem(str(item))
        #         self.ui.tableWidget.setItem(row - 1, col + 3, item)
        # global saveZnach
        # saveZnach = {}
        # for col in range(7, self.ui.tableWidget.columnCount()):
        #     saveZnach[col] = {}
        #     for row in range(1, self.ui.tableWidget.rowCount()):
        #         saveZnach[col][row] = float(self.ui.tableWidget.item(row, col).text())
        # self.ui.tableWidget.setItem(0, 6, QTableWidgetItem("Кф. кондитерской"))
        # self.ui.tableWidget.item(0, 6).setFont(self.font)
        # for col_spin in range(7, self.ui.tableWidget.columnCount()):
        #     self.DspinboxCol = QtWidgets.QDoubleSpinBox()
        #     self.DspinboxCol.wheelEvent = lambda event: None
        #     self.ui.tableWidget.setCellWidget(0, col_spin, self.DspinboxCol)
        #     self.ui.tableWidget.cellWidget(0, col_spin).setValue(1.00)
        #     self.ui.tableWidget.cellWidget(0, col_spin).setSingleStep(0.05)
        #     self.ui.tableWidget.cellWidget(0, col_spin).valueChanged.connect(self.raschetPrognoz)
        # for row_spin in range(1, self.ui.tableWidget.rowCount()):
        #     self.DspinboxRow = QtWidgets.QDoubleSpinBox()
        #     self.SpinboxRow = QtWidgets.QSpinBox()
        #     self.DspinboxRow.wheelEvent = lambda event: None
        #     self.SpinboxRow.wheelEvent = lambda event: None
        #     self.ui.tableWidget.setCellWidget(row_spin, 2, self.DspinboxRow)
        #     self.ui.tableWidget.cellWidget(row_spin, 2).setValue(1.00)
        #     self.ui.tableWidget.cellWidget(row_spin, 2).setSingleStep(0.05)
        #     self.ui.tableWidget.cellWidget(row_spin, 2).valueChanged.connect(self.raschetPrognoz)
        #     self.ui.tableWidget.setCellWidget(row_spin, 3, self.SpinboxRow)
        #     self.ui.tableWidget.cellWidget(row_spin, 3).setValue(self.poisk_kod(self.ui.tableWidget.item(row_spin, 4).text()))
        #     self.ui.tableWidget.cellWidget(row_spin, 3).setSingleStep(1)
        # for row_button in range(1, self.ui.tableWidget.rowCount()):
        #     self.copyRowButton = QtWidgets.QPushButton()
        #     self.ui.tableWidget.setCellWidget(row_button, 0, self.copyRowButton)
        #     self.ui.tableWidget.cellWidget(row_button, 0).setText('')
        #     iconCopy = QtGui.QIcon()
        #     iconCopy.addPixmap(QtGui.QPixmap("image/copy.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        #     self.ui.tableWidget.cellWidget(row_button, 0).setIcon(iconCopy)
        #     self.ui.tableWidget.cellWidget(row_button, 0).clicked.connect(self.copyRow)
        #     self.deleteRowButton = QtWidgets.QPushButton()
        #     self.ui.tableWidget.setCellWidget(row_button, 1, self.deleteRowButton)
        #     self.ui.tableWidget.cellWidget(row_button, 1).setText('')
        #     iconCross = QtGui.QIcon()
        #     iconCross.addPixmap(QtGui.QPixmap("image/cross.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        #     self.ui.tableWidget.cellWidget(row_button, 1).setIcon(iconCross)
        #     self.ui.tableWidget.cellWidget(row_button, 1).clicked.connect(self.deleteRow)
        # self.periodDay = periodDay
        # self.SaveAndNext = QtWidgets.QPushButton()
        # self.SaveAndClose = QtWidgets.QPushButton()
        # self.ui.tableWidget.setCellWidget(0, 4, self.SaveAndNext)
        # self.ui.tableWidget.cellWidget(0, 4).setText('Продолжить')
        # font = QtGui.QFont()
        # font.setFamily("Trebuchet MS")
        # font.setPointSize(12)
        # font.bold()
        # font.setWeight(50)
        # self.ui.tableWidget.cellWidget(0, 4).setFont(font)
        # self.ui.tableWidget.cellWidget(0, 4).setStyleSheet("QPushButton {\n"
        #                                     "background-color: rgb(228, 107, 134);\n"
        #                                     "border: none;\n"
        #                                     "border-radius: 10px}\n"
        #                                     "\n"
        #                                     "QPushButton:hover {\n"
        #                                     "border: 1px solid  rgb(0, 0, 0);\n"
        #                                     "background-color: rgba(228, 107, 134, 0.9)\n"
        #                                     "}\n"
        #                                     "\n"
        #                                     "QPushButton:pressed {\n"
        #                                     "border:3px solid  rgb(0, 0, 0);\n"
        #                                     "background-color: rgba(228, 107, 134, 1)\n"
        #                                     "}")
        # self.ui.tableWidget.cellWidget(0, 4).clicked.connect(self.saveAndNextDef)
        # self.ui.tableWidget.setCellWidget(0, 5, self.SaveAndClose)
        # self.ui.tableWidget.cellWidget(0, 5).setText('Сохранить и закрыть')
        # self.ui.tableWidget.cellWidget(0, 5).setFont(font)
        # self.ui.tableWidget.cellWidget(0, 5).setStyleSheet("QPushButton {\n"
        #                                     "background-color: rgb(228, 107, 134);\n"
        #                                     "border: none;\n"
        #                                     "border-radius: 10px}\n"
        #                                     "\n"
        #                                     "QPushButton:hover {\n"
        #                                     "border: 1px solid  rgb(0, 0, 0);\n"
        #                                     "background-color: rgba(228, 107, 134, 0.9)\n"
        #                                     "}\n"
        #                                     "\n"
        #                                     "QPushButton:pressed {\n"
        #                                     "border:3px solid  rgb(0, 0, 0);\n"
        #                                     "background-color: rgba(228, 107, 134, 1)\n"
        #                                     "}")
        # self.ui.tableWidget.cellWidget(0, 5).clicked.connect(self.saveAndCloseDef)
        # self.ui.tableWidget.setColumnWidth(0, 20)
        # self.ui.tableWidget.setColumnWidth(1, 20)
        # self.ui.tableWidget.setColumnWidth(2, 90)
        # self.ui.tableWidget.setColumnWidth(3, 90)
        # self.ui.tableWidget.setColumnWidth(4, 110)
        # self.ui.tableWidget.setColumnWidth(5, 290)
        # self.ui.tableWidget.setColumnWidth(6, 130)

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