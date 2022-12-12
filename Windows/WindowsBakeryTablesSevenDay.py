from PyQt6 import QtWidgets, QtGui
import win32com.client
from ui.bakeryTables import Ui_WindowBakeryTables
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtGui import QFont
import Windows.WindowsBakery


class WindowBakeryTableSevenDay(QtWidgets.QMainWindow):
    def __init__(self, pathOLAP_dayWeek_bakery, periodDay, points):
        super().__init__()
        self.ui = Ui_WindowBakeryTables()
        self.ui.setupUi(self)
        self.setWindowTitle("Продажи по дням недели")
        self.Excel = win32com.client.Dispatch("Excel.Application")
        self.wb_OLAP_dayWeek_bakery = self.Excel.Workbooks.Open(pathOLAP_dayWeek_bakery)
        sheet_OLAP_dayWeek_bakery = self.wb_OLAP_dayWeek_bakery.ActiveSheet
        firstOLAPRow = sheet_OLAP_dayWeek_bakery.Range("A:A").Find("День недели").Row
        # Фильтруем точки по Checkbox-сам
        for i in range(len(points)):
            if not points[i].isChecked():
                ValidPoints = sheet_OLAP_dayWeek_bakery.Rows(firstOLAPRow).Find(points[i].text())
                if ValidPoints != None:
                    sheet_OLAP_dayWeek_bakery.Columns(ValidPoints.Column).Delete()
        # Удаляем пустые столбцы и строки
        endOLAPCol = sheet_OLAP_dayWeek_bakery.Cells.Find("Выпечка пекарни всего").Column
        for a in range(endOLAPCol-1, 1, -1):
            if sheet_OLAP_dayWeek_bakery.Cells(firstOLAPRow, a).Value is None:
                sheet_OLAP_dayWeek_bakery.Columns(a).Delete()
        endOLAPCol = sheet_OLAP_dayWeek_bakery.Cells.Find("Выпечка пекарни всего").Column
        for _ in range(firstOLAPRow - 1):
            sheet_OLAP_dayWeek_bakery.Rows(1).Delete()
        endOLAPRow = sheet_OLAP_dayWeek_bakery.Range("A:A").Find("Итого").Row
        self.ui.tableWidget.setRowCount(endOLAPRow)
        self.ui.tableWidget.setColumnCount(endOLAPCol - 1)
        self.columnLables = list(sheet_OLAP_dayWeek_bakery.Range(sheet_OLAP_dayWeek_bakery.Cells(1, 1), sheet_OLAP_dayWeek_bakery.Cells(1, endOLAPCol - 1)).Value[0])
        self.ui.tableWidget.setHorizontalHeaderLabels(self.columnLables)
        self.font = QtGui.QFont("Times", 10, QFont.Weight.Bold)
        self.ui.tableWidget.horizontalHeader().setFont(self.font)

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

