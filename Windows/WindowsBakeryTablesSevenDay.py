from PyQt6 import QtWidgets, QtGui
import win32com.client
from ui.bakeryTables import Ui_WindowBakeryTables
from PyQt6.QtWidgets import QMessageBox
import Windows.WindowsBakery


class WindowBakeryTableSevenDay(QtWidgets.QMainWindow):
    def __init__(self, pathOLAP_dayWeek_bakery, periodDay):
        super().__init__()
        self.ui = Ui_WindowBakeryTables()
        self.ui.setupUi(self)
        self.setWindowTitle("Продажи по дням недели")
        Excel = win32com.client.Dispatch("Excel.Application")
        wb_OLAP_dayWeek_bakery = Excel.Workbooks.Open(pathOLAP_dayWeek_bakery)
        sheet_OLAP_dayWeek_bakery = wb_OLAP_dayWeek_bakery.ActiveSheet

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
            event.accept()
        else:
            event.ignore()

