# Form implementation generated from reading ui file 'bakery.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_WindowBakery(object):
    def setupUi(self, WindowBakery):
        WindowBakery.setObjectName("WindowBakery")
        WindowBakery.setEnabled(True)
        WindowBakery.resize(1240, 700)
        WindowBakery.setMinimumSize(QtCore.QSize(1240, 700))
        WindowBakery.setMaximumSize(QtCore.QSize(1240, 700))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../image/icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        WindowBakery.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(WindowBakery)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_OLAP_dayWeek_bakery = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_OLAP_dayWeek_bakery.setEnabled(False)
        self.lineEdit_OLAP_dayWeek_bakery.setGeometry(QtCore.QRect(20, 350, 691, 51))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        self.lineEdit_OLAP_dayWeek_bakery.setFont(font)
        self.lineEdit_OLAP_dayWeek_bakery.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.lineEdit_OLAP_dayWeek_bakery.setStyleSheet("padding-left: 5px")
        self.lineEdit_OLAP_dayWeek_bakery.setObjectName("lineEdit_OLAP_dayWeek_bakery")
        self.label_OLAP_P = QtWidgets.QLabel(self.centralwidget)
        self.label_OLAP_P.setGeometry(QtCore.QRect(20, 150, 771, 21))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        self.label_OLAP_P.setFont(font)
        self.label_OLAP_P.setObjectName("label_OLAP_P")
        self.lineEdit_OLAP_P = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_OLAP_P.setEnabled(False)
        self.lineEdit_OLAP_P.setGeometry(QtCore.QRect(20, 180, 691, 51))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        self.lineEdit_OLAP_P.setFont(font)
        self.lineEdit_OLAP_P.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.lineEdit_OLAP_P.setStyleSheet("padding-left: 5px")
        self.lineEdit_OLAP_P.setObjectName("lineEdit_OLAP_P")
        self.btn_path_OLAP_P = QtWidgets.QPushButton(self.centralwidget)
        self.btn_path_OLAP_P.setGeometry(QtCore.QRect(730, 180, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.btn_path_OLAP_P.setFont(font)
        self.btn_path_OLAP_P.setStyleSheet("QPushButton {\n"
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
        self.btn_path_OLAP_P.setCheckable(False)
        self.btn_path_OLAP_P.setObjectName("btn_path_OLAP_P")
        self.label_settings_title = QtWidgets.QLabel(self.centralwidget)
        self.label_settings_title.setGeometry(QtCore.QRect(20, 10, 631, 41))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(20)
        self.label_settings_title.setFont(font)
        self.label_settings_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_settings_title.setObjectName("label_settings_title")
        self.label_OLAP_dayWeek_bakery = QtWidgets.QLabel(self.centralwidget)
        self.label_OLAP_dayWeek_bakery.setGeometry(QtCore.QRect(20, 320, 771, 21))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        self.label_OLAP_dayWeek_bakery.setFont(font)
        self.label_OLAP_dayWeek_bakery.setObjectName("label_OLAP_dayWeek_bakery")
        self.btn_exit_bakery = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exit_bakery.setGeometry(QtCore.QRect(820, 620, 391, 61))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.btn_exit_bakery.setFont(font)
        self.btn_exit_bakery.setStyleSheet("QPushButton {\n"
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
        self.btn_exit_bakery.setCheckable(False)
        self.btn_exit_bakery.setObjectName("btn_exit_bakery")
        self.btn_path_dayWeek_bakery = QtWidgets.QPushButton(self.centralwidget)
        self.btn_path_dayWeek_bakery.setGeometry(QtCore.QRect(730, 350, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.btn_path_dayWeek_bakery.setFont(font)
        self.btn_path_dayWeek_bakery.setStyleSheet("QPushButton {\n"
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
        self.btn_path_dayWeek_bakery.setCheckable(False)
        self.btn_path_dayWeek_bakery.setObjectName("btn_path_dayWeek_bakery")
        self.btn_koeff_Prognoz = QtWidgets.QPushButton(self.centralwidget)
        self.btn_koeff_Prognoz.setEnabled(False)
        self.btn_koeff_Prognoz.setGeometry(QtCore.QRect(20, 240, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.btn_koeff_Prognoz.setFont(font)
        self.btn_koeff_Prognoz.setStyleSheet("QPushButton {\n"
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
        self.btn_koeff_Prognoz.setCheckable(False)
        self.btn_koeff_Prognoz.setObjectName("btn_koeff_Prognoz")
        self.label_startDay_and_endDay = QtWidgets.QLabel(self.centralwidget)
        self.label_startDay_and_endDay.setGeometry(QtCore.QRect(20, 60, 691, 21))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        self.label_startDay_and_endDay.setFont(font)
        self.label_startDay_and_endDay.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_startDay_and_endDay.setObjectName("label_startDay_and_endDay")
        self.label_startDay = QtWidgets.QLabel(self.centralwidget)
        self.label_startDay.setGeometry(QtCore.QRect(20, 100, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        self.label_startDay.setFont(font)
        self.label_startDay.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_startDay.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_startDay.setObjectName("label_startDay")
        self.label_EndDay = QtWidgets.QLabel(self.centralwidget)
        self.label_EndDay.setGeometry(QtCore.QRect(320, 100, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        self.label_EndDay.setFont(font)
        self.label_EndDay.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_EndDay.setObjectName("label_EndDay")
        self.dateEdit_startDay = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_startDay.setGeometry(QtCore.QRect(170, 100, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dateEdit_startDay.setFont(font)
        self.dateEdit_startDay.setCalendarPopup(True)
        self.dateEdit_startDay.setTimeSpec(QtCore.Qt.TimeSpec.LocalTime)
        self.dateEdit_startDay.setObjectName("dateEdit_startDay")
        self.dateEdit_EndDay = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_EndDay.setEnabled(False)
        self.dateEdit_EndDay.setGeometry(QtCore.QRect(460, 100, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dateEdit_EndDay.setFont(font)
        self.dateEdit_EndDay.setCalendarPopup(True)
        self.dateEdit_EndDay.setObjectName("dateEdit_EndDay")
        self.btn_prosmotrPrognoz = QtWidgets.QPushButton(self.centralwidget)
        self.btn_prosmotrPrognoz.setEnabled(False)
        self.btn_prosmotrPrognoz.setGeometry(QtCore.QRect(210, 240, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.btn_prosmotrPrognoz.setFont(font)
        self.btn_prosmotrPrognoz.setStyleSheet("QPushButton {\n"
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
        self.btn_prosmotrPrognoz.setCheckable(False)
        self.btn_prosmotrPrognoz.setObjectName("btn_prosmotrPrognoz")
        self.btn_editPrognoz = QtWidgets.QPushButton(self.centralwidget)
        self.btn_editPrognoz.setEnabled(False)
        self.btn_editPrognoz.setGeometry(QtCore.QRect(410, 240, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.btn_editPrognoz.setFont(font)
        self.btn_editPrognoz.setStyleSheet("QPushButton {\n"
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
        self.btn_editPrognoz.setCheckable(False)
        self.btn_editPrognoz.setObjectName("btn_editPrognoz")
        self.btn_editNormativ = QtWidgets.QPushButton(self.centralwidget)
        self.btn_editNormativ.setEnabled(False)
        self.btn_editNormativ.setGeometry(QtCore.QRect(280, 540, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.btn_editNormativ.setFont(font)
        self.btn_editNormativ.setStyleSheet("QPushButton {\n"
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
        self.btn_editNormativ.setCheckable(False)
        self.btn_editNormativ.setObjectName("btn_editNormativ")
        self.btn_Normativ = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Normativ.setEnabled(False)
        self.btn_Normativ.setGeometry(QtCore.QRect(20, 540, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.btn_Normativ.setFont(font)
        self.btn_Normativ.setStyleSheet("QPushButton {\n"
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
        self.btn_Normativ.setCheckable(False)
        self.btn_Normativ.setObjectName("btn_Normativ")
        self.btn_edit_koeff_DayWeek = QtWidgets.QPushButton(self.centralwidget)
        self.btn_edit_koeff_DayWeek.setEnabled(False)
        self.btn_edit_koeff_DayWeek.setGeometry(QtCore.QRect(410, 410, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.btn_edit_koeff_DayWeek.setFont(font)
        self.btn_edit_koeff_DayWeek.setStyleSheet("QPushButton {\n"
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
        self.btn_edit_koeff_DayWeek.setCheckable(False)
        self.btn_edit_koeff_DayWeek.setObjectName("btn_edit_koeff_DayWeek")
        self.btn_download = QtWidgets.QPushButton(self.centralwidget)
        self.btn_download.setEnabled(False)
        self.btn_download.setGeometry(QtCore.QRect(820, 520, 391, 71))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.btn_download.setFont(font)
        self.btn_download.setStyleSheet("QPushButton {\n"
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
        self.btn_download.setCheckable(False)
        self.btn_download.setObjectName("btn_download")
        self.label_OLAP_P_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_OLAP_P_2.setGeometry(QtCore.QRect(830, 20, 381, 31))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        self.label_OLAP_P_2.setFont(font)
        self.label_OLAP_P_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_OLAP_P_2.setObjectName("label_OLAP_P_2")
        self.line_1 = QtWidgets.QFrame(self.centralwidget)
        self.line_1.setGeometry(QtCore.QRect(820, 10, 401, 21))
        self.line_1.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_1.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_1.setObjectName("line_1")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(820, 460, 401, 21))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(1210, 20, 20, 451))
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(810, 20, 20, 451))
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_4.setObjectName("line_4")
        self.btn_prosmotr_koeff_DayWeek = QtWidgets.QPushButton(self.centralwidget)
        self.btn_prosmotr_koeff_DayWeek.setEnabled(False)
        self.btn_prosmotr_koeff_DayWeek.setGeometry(QtCore.QRect(210, 410, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.btn_prosmotr_koeff_DayWeek.setFont(font)
        self.btn_prosmotr_koeff_DayWeek.setStyleSheet("QPushButton {\n"
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
        self.btn_prosmotr_koeff_DayWeek.setCheckable(False)
        self.btn_prosmotr_koeff_DayWeek.setObjectName("btn_prosmotr_koeff_DayWeek")
        self.btn_deletePrognoz = QtWidgets.QPushButton(self.centralwidget)
        self.btn_deletePrognoz.setEnabled(False)
        self.btn_deletePrognoz.setGeometry(QtCore.QRect(600, 240, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.btn_deletePrognoz.setFont(font)
        self.btn_deletePrognoz.setStyleSheet("QPushButton {\n"
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
        self.btn_deletePrognoz.setCheckable(False)
        self.btn_deletePrognoz.setObjectName("btn_deletePrognoz")
        self.btn_delete_koeff_DayWeek = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete_koeff_DayWeek.setEnabled(False)
        self.btn_delete_koeff_DayWeek.setGeometry(QtCore.QRect(600, 410, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.btn_delete_koeff_DayWeek.setFont(font)
        self.btn_delete_koeff_DayWeek.setStyleSheet("QPushButton {\n"
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
        self.btn_delete_koeff_DayWeek.setCheckable(False)
        self.btn_delete_koeff_DayWeek.setObjectName("btn_delete_koeff_DayWeek")
        self.btn_koeff_DayWeek = QtWidgets.QPushButton(self.centralwidget)
        self.btn_koeff_DayWeek.setEnabled(False)
        self.btn_koeff_DayWeek.setGeometry(QtCore.QRect(20, 410, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.btn_koeff_DayWeek.setFont(font)
        self.btn_koeff_DayWeek.setStyleSheet("QPushButton {\n"
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
        self.btn_koeff_DayWeek.setCheckable(False)
        self.btn_koeff_DayWeek.setObjectName("btn_koeff_DayWeek")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(830, 60, 381, 401))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.gridPoints = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.gridPoints.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridPoints.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldGrowthPolicy.FieldsStayAtSizeHint)
        self.gridPoints.setRowWrapPolicy(QtWidgets.QFormLayout.RowWrapPolicy.WrapLongRows)
        self.gridPoints.setLabelAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.gridPoints.setFormAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.gridPoints.setContentsMargins(15, 5, 0, 0)
        self.gridPoints.setHorizontalSpacing(40)
        self.gridPoints.setVerticalSpacing(8)
        self.gridPoints.setObjectName("gridPoints")
        self.cb_begovaya = QtWidgets.QCheckBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_begovaya.setFont(font)
        self.cb_begovaya.setChecked(True)
        self.cb_begovaya.setObjectName("cb_begovaya")
        self.gridPoints.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cb_begovaya)
        self.cb_volsk = QtWidgets.QCheckBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_volsk.setFont(font)
        self.cb_volsk.setChecked(True)
        self.cb_volsk.setObjectName("cb_volsk")
        self.gridPoints.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cb_volsk)
        self.cb_gorkogo = QtWidgets.QCheckBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_gorkogo.setFont(font)
        self.cb_gorkogo.setChecked(True)
        self.cb_gorkogo.setObjectName("cb_gorkogo")
        self.gridPoints.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cb_gorkogo)
        self.cb_grand = QtWidgets.QCheckBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_grand.setFont(font)
        self.cb_grand.setChecked(True)
        self.cb_grand.setObjectName("cb_grand")
        self.gridPoints.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cb_grand)
        self.checkBox = QtWidgets.QCheckBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox.setFont(font)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.gridPoints.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.checkBox)
        self.cb_lenina = QtWidgets.QCheckBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_lenina.setFont(font)
        self.cb_lenina.setChecked(True)
        self.cb_lenina.setObjectName("cb_lenina")
        self.gridPoints.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cb_lenina)
        self.cb_magazin = QtWidgets.QCheckBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_magazin.setFont(font)
        self.cb_magazin.setChecked(True)
        self.cb_magazin.setObjectName("cb_magazin")
        self.gridPoints.setWidget(6, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cb_magazin)
        self.cb_madonna = QtWidgets.QCheckBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_madonna.setFont(font)
        self.cb_madonna.setObjectName("cb_madonna")
        self.gridPoints.setWidget(7, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cb_madonna)
        self.cb_marks = QtWidgets.QCheckBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_marks.setFont(font)
        self.cb_marks.setChecked(True)
        self.cb_marks.setObjectName("cb_marks")
        self.gridPoints.setWidget(8, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cb_marks)
        self.cb_michurina = QtWidgets.QCheckBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_michurina.setFont(font)
        self.cb_michurina.setCheckable(True)
        self.cb_michurina.setChecked(False)
        self.cb_michurina.setObjectName("cb_michurina")
        self.gridPoints.setWidget(9, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cb_michurina)
        self.cb_moskovskaya = QtWidgets.QCheckBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_moskovskaya.setFont(font)
        self.cb_moskovskaya.setChecked(True)
        self.cb_moskovskaya.setObjectName("cb_moskovskaya")
        self.gridPoints.setWidget(10, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cb_moskovskaya)
        self.cb_orang = QtWidgets.QCheckBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_orang.setFont(font)
        self.cb_orang.setChecked(True)
        self.cb_orang.setObjectName("cb_orang")
        self.gridPoints.setWidget(11, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cb_orang)
        self.cb_chehova = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.cb_chehova.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_chehova.setFont(font)
        self.cb_chehova.setCheckable(True)
        self.cb_chehova.setChecked(False)
        self.cb_chehova.setObjectName("cb_chehova")
        self.gridPoints.setWidget(11, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cb_chehova)
        self.cb_pobeda = QtWidgets.QCheckBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_pobeda.setFont(font)
        self.cb_pobeda.setChecked(False)
        self.cb_pobeda.setObjectName("cb_pobeda")
        self.gridPoints.setWidget(12, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cb_pobeda)
        self.cb_entuziastov = QtWidgets.QCheckBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_entuziastov.setFont(font)
        self.cb_entuziastov.setChecked(True)
        self.cb_entuziastov.setObjectName("cb_entuziastov")
        self.gridPoints.setWidget(12, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cb_entuziastov)
        self.cb_fridriha = QtWidgets.QCheckBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_fridriha.setFont(font)
        self.cb_fridriha.setChecked(True)
        self.cb_fridriha.setObjectName("cb_fridriha")
        self.gridPoints.setWidget(10, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cb_fridriha)
        self.cb_ust_kurdym = QtWidgets.QCheckBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_ust_kurdym.setFont(font)
        self.cb_ust_kurdym.setChecked(True)
        self.cb_ust_kurdym.setObjectName("cb_ust_kurdym")
        self.gridPoints.setWidget(9, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cb_ust_kurdym)
        self.cb_trnavskaya = QtWidgets.QCheckBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_trnavskaya.setFont(font)
        self.cb_trnavskaya.setChecked(True)
        self.cb_trnavskaya.setObjectName("cb_trnavskaya")
        self.gridPoints.setWidget(8, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cb_trnavskaya)
        self.cb_tarhova = QtWidgets.QCheckBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_tarhova.setFont(font)
        self.cb_tarhova.setChecked(False)
        self.cb_tarhova.setObjectName("cb_tarhova")
        self.gridPoints.setWidget(7, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cb_tarhova)
        self.cb_stepnaya = QtWidgets.QCheckBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_stepnaya.setFont(font)
        self.cb_stepnaya.setChecked(True)
        self.cb_stepnaya.setObjectName("cb_stepnaya")
        self.gridPoints.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cb_stepnaya)
        self.cb_stargrad = QtWidgets.QCheckBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_stargrad.setFont(font)
        self.cb_stargrad.setChecked(False)
        self.cb_stargrad.setObjectName("cb_stargrad")
        self.gridPoints.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cb_stargrad)
        self.cb_solnechnii = QtWidgets.QCheckBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_solnechnii.setFont(font)
        self.cb_solnechnii.setChecked(True)
        self.cb_solnechnii.setObjectName("cb_solnechnii")
        self.gridPoints.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cb_solnechnii)
        self.cb_svoboda = QtWidgets.QCheckBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_svoboda.setFont(font)
        self.cb_svoboda.setChecked(True)
        self.cb_svoboda.setObjectName("cb_svoboda")
        self.gridPoints.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cb_svoboda)
        self.cb_rokot = QtWidgets.QCheckBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_rokot.setFont(font)
        self.cb_rokot.setChecked(False)
        self.cb_rokot.setObjectName("cb_rokot")
        self.gridPoints.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cb_rokot)
        self.cb_rahova = QtWidgets.QCheckBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_rahova.setFont(font)
        self.cb_rahova.setChecked(True)
        self.cb_rahova.setObjectName("cb_rahova")
        self.gridPoints.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cb_rahova)
        self.cb_pavilon = QtWidgets.QCheckBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_pavilon.setFont(font)
        self.cb_pavilon.setObjectName("cb_pavilon")
        self.gridPoints.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cb_pavilon)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 140, 781, 20))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(10, 290, 781, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(780, 150, 20, 151))
        self.line_6.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(0, 150, 20, 151))
        self.line_7.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(780, 320, 20, 151))
        self.line_8.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(10, 310, 781, 20))
        self.line_9.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(10, 460, 781, 20))
        self.line_10.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setGeometry(QtCore.QRect(0, 320, 20, 151))
        self.line_11.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_11.setObjectName("line_11")
        self.btn_deleteNormativ = QtWidgets.QPushButton(self.centralwidget)
        self.btn_deleteNormativ.setEnabled(False)
        self.btn_deleteNormativ.setGeometry(QtCore.QRect(550, 540, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.btn_deleteNormativ.setFont(font)
        self.btn_deleteNormativ.setStyleSheet("QPushButton {\n"
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
        self.btn_deleteNormativ.setCheckable(False)
        self.btn_deleteNormativ.setObjectName("btn_deleteNormativ")
        self.label_OLAP_P_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_OLAP_P_3.setGeometry(QtCore.QRect(30, 500, 761, 21))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(15)
        self.label_OLAP_P_3.setFont(font)
        self.label_OLAP_P_3.setObjectName("label_OLAP_P_3")
        self.line_12 = QtWidgets.QFrame(self.centralwidget)
        self.line_12.setGeometry(QtCore.QRect(10, 480, 781, 20))
        self.line_12.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_12.setObjectName("line_12")
        self.line_13 = QtWidgets.QFrame(self.centralwidget)
        self.line_13.setGeometry(QtCore.QRect(10, 610, 781, 20))
        self.line_13.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_13.setObjectName("line_13")
        self.line_14 = QtWidgets.QFrame(self.centralwidget)
        self.line_14.setGeometry(QtCore.QRect(780, 490, 20, 131))
        self.line_14.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_14.setObjectName("line_14")
        self.line_15 = QtWidgets.QFrame(self.centralwidget)
        self.line_15.setGeometry(QtCore.QRect(0, 490, 20, 131))
        self.line_15.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_15.setObjectName("line_15")
        WindowBakery.setCentralWidget(self.centralwidget)

        self.retranslateUi(WindowBakery)
        QtCore.QMetaObject.connectSlotsByName(WindowBakery)

    def retranslateUi(self, WindowBakery):
        _translate = QtCore.QCoreApplication.translate
        WindowBakery.setWindowTitle(_translate("WindowBakery", "Настройка работы с Выпечкой"))
        self.label_OLAP_P.setText(_translate("WindowBakery", "Укажите путь к OLAP отчету по продажам"))
        self.btn_path_OLAP_P.setText(_translate("WindowBakery", "..."))
        self.label_settings_title.setText(_translate("WindowBakery", "Настройка подключения внешних данных"))
        self.label_OLAP_dayWeek_bakery.setText(_translate("WindowBakery", "Укажите путь к OLAP отчету по продажам по дням недели - выпечка"))
        self.btn_exit_bakery.setText(_translate("WindowBakery", "К ВЫБОРУ РАЗДЕЛА"))
        self.btn_path_dayWeek_bakery.setText(_translate("WindowBakery", "..."))
        self.btn_koeff_Prognoz.setText(_translate("WindowBakery", "Установить"))
        self.label_startDay_and_endDay.setText(_translate("WindowBakery", "Укажите начало периода для формирования данных"))
        self.label_startDay.setText(_translate("WindowBakery", "Начало периода"))
        self.label_EndDay.setText(_translate("WindowBakery", "Конец периода"))
        self.btn_prosmotrPrognoz.setText(_translate("WindowBakery", "Посмотреть"))
        self.btn_editPrognoz.setText(_translate("WindowBakery", "Редактировать"))
        self.btn_editNormativ.setText(_translate("WindowBakery", "Редактировать"))
        self.btn_Normativ.setText(_translate("WindowBakery", "Установить"))
        self.btn_edit_koeff_DayWeek.setText(_translate("WindowBakery", "Редактировать"))
        self.btn_download.setText(_translate("WindowBakery", "ВЫГРУЗИТЬ ПЛАНЫ"))
        self.label_OLAP_P_2.setText(_translate("WindowBakery", "Выберите кондитерские для автозаказа"))
        self.btn_prosmotr_koeff_DayWeek.setText(_translate("WindowBakery", "Посмотреть"))
        self.btn_deletePrognoz.setText(_translate("WindowBakery", "Удалить"))
        self.btn_delete_koeff_DayWeek.setText(_translate("WindowBakery", "Удалить"))
        self.btn_koeff_DayWeek.setText(_translate("WindowBakery", "Установить"))
        self.cb_begovaya.setText(_translate("WindowBakery", "Беговая"))
        self.cb_volsk.setText(_translate("WindowBakery", "Вольск"))
        self.cb_gorkogo.setText(_translate("WindowBakery", "Горького"))
        self.cb_grand.setText(_translate("WindowBakery", "Гранд"))
        self.checkBox.setText(_translate("WindowBakery", "Крытый рынок"))
        self.cb_lenina.setText(_translate("WindowBakery", "Ленина"))
        self.cb_magazin.setText(_translate("WindowBakery", "Магазин"))
        self.cb_madonna.setText(_translate("WindowBakery", "Мадонна"))
        self.cb_marks.setText(_translate("WindowBakery", "Маркс"))
        self.cb_michurina.setText(_translate("WindowBakery", "Мичурина"))
        self.cb_moskovskaya.setText(_translate("WindowBakery", "Московская"))
        self.cb_orang.setText(_translate("WindowBakery", "Оранж"))
        self.cb_chehova.setText(_translate("WindowBakery", "Чехова"))
        self.cb_pobeda.setText(_translate("WindowBakery", "Победа"))
        self.cb_entuziastov.setText(_translate("WindowBakery", "Энтузиастов"))
        self.cb_fridriha.setText(_translate("WindowBakery", "Фридриха 11"))
        self.cb_ust_kurdym.setText(_translate("WindowBakery", "Усть-Курдюмская"))
        self.cb_trnavskaya.setText(_translate("WindowBakery", "Трнавская"))
        self.cb_tarhova.setText(_translate("WindowBakery", "Тархова"))
        self.cb_stepnaya.setText(_translate("WindowBakery", "Степная"))
        self.cb_stargrad.setText(_translate("WindowBakery", "Старград"))
        self.cb_solnechnii.setText(_translate("WindowBakery", "Солнечный"))
        self.cb_svoboda.setText(_translate("WindowBakery", "Свобода"))
        self.cb_rokot.setText(_translate("WindowBakery", "Рокот"))
        self.cb_rahova.setText(_translate("WindowBakery", "Рахова"))
        self.cb_pavilon.setText(_translate("WindowBakery", "ПП(павильон)"))
        self.btn_deleteNormativ.setText(_translate("WindowBakery", "Удалить"))
        self.label_OLAP_P_3.setText(_translate("WindowBakery", "Нормативы пекарни"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WindowBakery = QtWidgets.QMainWindow()
    ui = Ui_WindowBakery()
    ui.setupUi(WindowBakery)
    WindowBakery.show()
    sys.exit(app.exec())
