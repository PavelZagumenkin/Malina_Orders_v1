# Form implementation generated from reading ui file 'bakeryTables.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_WindowBakeryTables(object):
    def setupUi(self, WindowBakeryTables):
        WindowBakeryTables.setObjectName("WindowBakeryTables")
        WindowBakeryTables.resize(1203, 811)
        self.centralwidget = QtWidgets.QWidget(parent=WindowBakeryTables)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        WindowBakeryTables.setCentralWidget(self.centralwidget)

        self.retranslateUi(WindowBakeryTables)
        QtCore.QMetaObject.connectSlotsByName(WindowBakeryTables)

    def retranslateUi(self, WindowBakeryTables):
        _translate = QtCore.QCoreApplication.translate
        WindowBakeryTables.setWindowTitle(_translate("WindowBakeryTables", "Работа с коэффициентами"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WindowBakeryTables = QtWidgets.QMainWindow()
    ui = Ui_WindowBakeryTables()
    ui.setupUi(WindowBakeryTables)
    WindowBakeryTables.show()
    sys.exit(app.exec())
