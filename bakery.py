import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from BakeryOrders import *
import win32com.client




class BakeryOrders(QtWidgets.QMainWindow):

    def bakeryTable(self, pathOLAP_P, pathOLAP_dayWeek_bakery):
        Excel = win32com.client.Dispatch("Excel.Application")
        wb = Excel.Workbooks.Open(pathOLAP_P)
        sheet = wb.ActiveSheet
        

        #закрываем ее
        # wb.Close()

        #закрываем COM объект
        # Excel.Quit()
