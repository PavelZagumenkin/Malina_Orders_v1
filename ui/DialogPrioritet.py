# Form implementation generated from reading ui file 'DialogPrioritet.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_DialogPrioritet(object):
    def setupUi(self, DialogPrioritet):
        DialogPrioritet.setObjectName("DialogPrioritet")
        DialogPrioritet.resize(370, 600)
        DialogPrioritet.setMinimumSize(QtCore.QSize(370, 600))
        DialogPrioritet.setMaximumSize(QtCore.QSize(370, 600))
        self.formLayoutWidget = QtWidgets.QWidget(parent=DialogPrioritet)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 70, 351, 451))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.gridPoints = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.gridPoints.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridPoints.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldGrowthPolicy.FieldsStayAtSizeHint)
        self.gridPoints.setRowWrapPolicy(QtWidgets.QFormLayout.RowWrapPolicy.WrapLongRows)
        self.gridPoints.setLabelAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.gridPoints.setFormAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.gridPoints.setContentsMargins(15, 5, 0, 0)
        self.gridPoints.setHorizontalSpacing(40)
        self.gridPoints.setVerticalSpacing(10)
        self.gridPoints.setObjectName("gridPoints")
        self.cb_astahanskaya = QtWidgets.QCheckBox(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_astahanskaya.setFont(font)
        self.cb_astahanskaya.setChecked(False)
        self.cb_astahanskaya.setObjectName("cb_astahanskaya")
        self.gridPoints.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cb_astahanskaya)
        self.cb_pobeda = QtWidgets.QCheckBox(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_pobeda.setFont(font)
        self.cb_pobeda.setChecked(False)
        self.cb_pobeda.setObjectName("cb_pobeda")
        self.gridPoints.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cb_pobeda)
        self.cb_volsk = QtWidgets.QCheckBox(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_volsk.setFont(font)
        self.cb_volsk.setChecked(False)
        self.cb_volsk.setObjectName("cb_volsk")
        self.gridPoints.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cb_volsk)
        self.cb_rahova = QtWidgets.QCheckBox(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_rahova.setFont(font)
        self.cb_rahova.setChecked(False)
        self.cb_rahova.setObjectName("cb_rahova")
        self.gridPoints.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cb_rahova)
        self.cb_svoboda = QtWidgets.QCheckBox(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_svoboda.setFont(font)
        self.cb_svoboda.setChecked(False)
        self.cb_svoboda.setObjectName("cb_svoboda")
        self.gridPoints.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cb_svoboda)
        self.cb_solnechnii = QtWidgets.QCheckBox(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_solnechnii.setFont(font)
        self.cb_solnechnii.setChecked(False)
        self.cb_solnechnii.setObjectName("cb_solnechnii")
        self.gridPoints.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cb_solnechnii)
        self.cb_stargrad = QtWidgets.QCheckBox(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_stargrad.setFont(font)
        self.cb_stargrad.setChecked(False)
        self.cb_stargrad.setObjectName("cb_stargrad")
        self.gridPoints.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cb_stargrad)
        self.cb_stepnaya = QtWidgets.QCheckBox(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_stepnaya.setFont(font)
        self.cb_stepnaya.setChecked(False)
        self.cb_stepnaya.setObjectName("cb_stepnaya")
        self.gridPoints.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cb_stepnaya)
        self.cb_topol = QtWidgets.QCheckBox(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_topol.setFont(font)
        self.cb_topol.setChecked(False)
        self.cb_topol.setObjectName("cb_topol")
        self.gridPoints.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cb_topol)
        self.cb_trnavskaya = QtWidgets.QCheckBox(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_trnavskaya.setFont(font)
        self.cb_trnavskaya.setChecked(False)
        self.cb_trnavskaya.setObjectName("cb_trnavskaya")
        self.gridPoints.setWidget(7, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cb_trnavskaya)
        self.cb_ust_kurdym = QtWidgets.QCheckBox(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_ust_kurdym.setFont(font)
        self.cb_ust_kurdym.setChecked(False)
        self.cb_ust_kurdym.setObjectName("cb_ust_kurdym")
        self.gridPoints.setWidget(8, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cb_ust_kurdym)
        self.cb_fridriha = QtWidgets.QCheckBox(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_fridriha.setFont(font)
        self.cb_fridriha.setChecked(False)
        self.cb_fridriha.setObjectName("cb_fridriha")
        self.gridPoints.setWidget(9, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cb_fridriha)
        self.cb_orgevskogo = QtWidgets.QCheckBox(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_orgevskogo.setFont(font)
        self.cb_orgevskogo.setChecked(False)
        self.cb_orgevskogo.setObjectName("cb_orgevskogo")
        self.gridPoints.setWidget(11, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cb_orgevskogo)
        self.cb_orang = QtWidgets.QCheckBox(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_orang.setFont(font)
        self.cb_orang.setChecked(False)
        self.cb_orang.setObjectName("cb_orang")
        self.gridPoints.setWidget(10, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cb_orang)
        self.cb_moskovskaya = QtWidgets.QCheckBox(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_moskovskaya.setFont(font)
        self.cb_moskovskaya.setChecked(False)
        self.cb_moskovskaya.setObjectName("cb_moskovskaya")
        self.gridPoints.setWidget(9, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cb_moskovskaya)
        self.cb_marks = QtWidgets.QCheckBox(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_marks.setFont(font)
        self.cb_marks.setChecked(False)
        self.cb_marks.setObjectName("cb_marks")
        self.gridPoints.setWidget(8, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cb_marks)
        self.cb_magazin = QtWidgets.QCheckBox(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_magazin.setFont(font)
        self.cb_magazin.setChecked(False)
        self.cb_magazin.setObjectName("cb_magazin")
        self.gridPoints.setWidget(7, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cb_magazin)
        self.cb_lenina = QtWidgets.QCheckBox(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_lenina.setFont(font)
        self.cb_lenina.setChecked(False)
        self.cb_lenina.setObjectName("cb_lenina")
        self.gridPoints.setWidget(6, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cb_lenina)
        self.cb_kr = QtWidgets.QCheckBox(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_kr.setFont(font)
        self.cb_kr.setChecked(False)
        self.cb_kr.setObjectName("cb_kr")
        self.gridPoints.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cb_kr)
        self.cb_grand = QtWidgets.QCheckBox(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_grand.setFont(font)
        self.cb_grand.setChecked(False)
        self.cb_grand.setObjectName("cb_grand")
        self.gridPoints.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cb_grand)
        self.cb_gorkogo = QtWidgets.QCheckBox(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_gorkogo.setFont(font)
        self.cb_gorkogo.setChecked(False)
        self.cb_gorkogo.setObjectName("cb_gorkogo")
        self.gridPoints.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cb_gorkogo)
        self.cb_gorpark = QtWidgets.QCheckBox(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_gorpark.setFont(font)
        self.cb_gorpark.setChecked(False)
        self.cb_gorpark.setObjectName("cb_gorpark")
        self.gridPoints.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cb_gorpark)
        self.cb_rahova_2 = QtWidgets.QCheckBox(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_rahova_2.setFont(font)
        self.cb_rahova_2.setChecked(False)
        self.cb_rahova_2.setObjectName("cb_rahova_2")
        self.gridPoints.setWidget(12, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cb_rahova_2)
        self.cb_entuziastov = QtWidgets.QCheckBox(parent=self.formLayoutWidget)
        self.cb_entuziastov.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_entuziastov.setFont(font)
        self.cb_entuziastov.setCheckable(True)
        self.cb_entuziastov.setChecked(False)
        self.cb_entuziastov.setObjectName("cb_entuziastov")
        self.gridPoints.setWidget(12, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cb_entuziastov)
        self.cb_chehova = QtWidgets.QCheckBox(parent=self.formLayoutWidget)
        self.cb_chehova.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_chehova.setFont(font)
        self.cb_chehova.setCheckable(True)
        self.cb_chehova.setChecked(False)
        self.cb_chehova.setObjectName("cb_chehova")
        self.gridPoints.setWidget(11, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cb_chehova)
        self.cb_centr = QtWidgets.QCheckBox(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_centr.setFont(font)
        self.cb_centr.setChecked(False)
        self.cb_centr.setObjectName("cb_centr")
        self.gridPoints.setWidget(10, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cb_centr)
        self.label_prioritet = QtWidgets.QLabel(parent=DialogPrioritet)
        self.label_prioritet.setGeometry(QtCore.QRect(10, 10, 351, 51))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        self.label_prioritet.setFont(font)
        self.label_prioritet.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_prioritet.setObjectName("label_prioritet")
        self.btn_save = QtWidgets.QPushButton(parent=DialogPrioritet)
        self.btn_save.setEnabled(True)
        self.btn_save.setGeometry(QtCore.QRect(10, 530, 351, 51))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(16)
        font.setBold(False)
        self.btn_save.setFont(font)
        self.btn_save.setStyleSheet("QPushButton {\n"
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
        self.btn_save.setCheckable(False)
        self.btn_save.setObjectName("btn_save")

        self.retranslateUi(DialogPrioritet)
        QtCore.QMetaObject.connectSlotsByName(DialogPrioritet)

    def retranslateUi(self, DialogPrioritet):
        _translate = QtCore.QCoreApplication.translate
        DialogPrioritet.setWindowTitle(_translate("DialogPrioritet", "Выберите приоритетные кондитерские"))
        self.cb_astahanskaya.setText(_translate("DialogPrioritet", "Астраханская"))
        self.cb_pobeda.setText(_translate("DialogPrioritet", "Победа"))
        self.cb_volsk.setText(_translate("DialogPrioritet", "Вольск"))
        self.cb_rahova.setText(_translate("DialogPrioritet", "Рахова"))
        self.cb_svoboda.setText(_translate("DialogPrioritet", "Свобода"))
        self.cb_solnechnii.setText(_translate("DialogPrioritet", "Солнечный"))
        self.cb_stargrad.setText(_translate("DialogPrioritet", "Старград"))
        self.cb_stepnaya.setText(_translate("DialogPrioritet", "Степная"))
        self.cb_topol.setText(_translate("DialogPrioritet", "Топольчанская"))
        self.cb_trnavskaya.setText(_translate("DialogPrioritet", "Трнавская"))
        self.cb_ust_kurdym.setText(_translate("DialogPrioritet", "Усть-Курдюмская"))
        self.cb_fridriha.setText(_translate("DialogPrioritet", "Фридриха 11"))
        self.cb_orgevskogo.setText(_translate("DialogPrioritet", "Оржевского"))
        self.cb_orang.setText(_translate("DialogPrioritet", "Оранж"))
        self.cb_moskovskaya.setText(_translate("DialogPrioritet", "Московская"))
        self.cb_marks.setText(_translate("DialogPrioritet", "Маркс"))
        self.cb_magazin.setText(_translate("DialogPrioritet", "Магазин"))
        self.cb_lenina.setText(_translate("DialogPrioritet", "Ленина"))
        self.cb_kr.setText(_translate("DialogPrioritet", "Крытый рынок"))
        self.cb_grand.setText(_translate("DialogPrioritet", "Гранд"))
        self.cb_gorkogo.setText(_translate("DialogPrioritet", "Горького"))
        self.cb_gorpark.setText(_translate("DialogPrioritet", "ГорПарк"))
        self.cb_rahova_2.setText(_translate("DialogPrioritet", "Радищева"))
        self.cb_entuziastov.setText(_translate("DialogPrioritet", "Энтузиастов"))
        self.cb_chehova.setText(_translate("DialogPrioritet", "Чехова"))
        self.cb_centr.setText(_translate("DialogPrioritet", "Центр"))
        self.label_prioritet.setText(_translate("DialogPrioritet", "Выберите приоритетные для распределения \n"
" кондитерские"))
        self.btn_save.setText(_translate("DialogPrioritet", "СОХРАНИТЬ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogPrioritet = QtWidgets.QDialog()
    ui = Ui_DialogPrioritet()
    ui.setupUi(DialogPrioritet)
    DialogPrioritet.show()
    sys.exit(app.exec())
