# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/LoginDialog.ui'
#
# Created: Mon Sep  5 21:42:22 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(570, 389)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 541, 401))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayoutWidget_3 = QtGui.QWidget(self.groupBox)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(130, 180, 271, 85))
        self.formLayoutWidget_3.setObjectName(_fromUtf8("formLayoutWidget_3"))
        self.formLayout_3 = QtGui.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setMargin(0)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label_13 = QtGui.QLabel(self.formLayoutWidget_3)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_13)
        self.label_14 = QtGui.QLabel(self.formLayoutWidget_3)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_14)
        self.LPass = QtGui.QLineEdit(self.formLayoutWidget_3)
        self.LPass.setEchoMode(QtGui.QLineEdit.Password)
        self.LPass.setObjectName(_fromUtf8("LPass"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.LPass)
        self.LUser = QtGui.QLineEdit(self.formLayoutWidget_3)
        self.LUser.setObjectName(_fromUtf8("LUser"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.LUser)
        self.BIngresar = QtGui.QPushButton(self.groupBox)
        self.BIngresar.setGeometry(QtCore.QRect(220, 310, 71, 31))
        self.BIngresar.setObjectName(_fromUtf8("BIngresar"))
        self.error_label = QtGui.QLabel(self.groupBox)
        self.error_label.setGeometry(QtCore.QRect(10, 280, 521, 21))
        self.error_label.setStyleSheet(_fromUtf8("color:red;\n"
"font-weight:bold;"))
        self.error_label.setText(_fromUtf8(""))
        self.error_label.setAlignment(QtCore.Qt.AlignCenter)
        self.error_label.setObjectName(_fromUtf8("error_label"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(230, 150, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("color:black;"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.BSalir = QtGui.QPushButton(self.groupBox)
        self.BSalir.setGeometry(QtCore.QRect(450, 340, 85, 31))
        self.BSalir.setObjectName(_fromUtf8("BSalir"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(40, 10, 471, 121))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("color:black;"))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.LUser, self.LPass)
        Dialog.setTabOrder(self.LPass, self.BIngresar)
        Dialog.setTabOrder(self.BIngresar, self.BSalir)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_13.setText(_translate("Dialog", "Usuario", None))
        self.label_14.setText(_translate("Dialog", "Contrasena", None))
        self.BIngresar.setText(_translate("Dialog", "Ingresar", None))
        self.label_2.setText(_translate("Dialog", " Login", None))
        self.BSalir.setText(_translate("Dialog", "Salir", None))
        self.label_3.setText(_translate("Dialog", "KanguroMovies", None))

