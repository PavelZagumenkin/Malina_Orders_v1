import sys
from PyQt6 import QtCore, QtGui, QtWidgets
import win32com.client
from bakeryOrders import *
from main import Interface




class BakeryOrders(QtWidgets.QMainWindow):
    def bakeryTable(self, pathOLAP_P, pathOLAP_dayWeek_bakery):
        global WindowsBakery
        WindowsBakery = BakeryOrders()
        ui = Ui_Window_BakeryOrders()
        ui.setupUi(WindowsBakery)
        WindowsBakery.showMaximized()
        Excel = win32com.client.Dispatch("Excel.Application")
        wb = Excel.Workbooks.Open(pathOLAP_P)
        sheet = wb.ActiveSheet
        if sheet.Name != "OLAP по продажам ОБЩИЙ":
            print("Неверный отчет")
            wb.Close()
            Excel.Quit()
            WindowsBakery.close()
            Interface.closeSettings()
        else:
            print("Нормальный отчет")
