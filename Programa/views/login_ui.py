# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginDialog.ui'
#
# Created: Wed Aug 31 14:50:04 2016
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
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayoutWidget_3 = QtGui.QWidget(self.groupBox)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(120, 210, 271, 85))
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
        self.BIngresar.setGeometry(QtCore.QRect(220, 340, 71, 21))
        self.BIngresar.setObjectName(_fromUtf8("BIngresar"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 501, 141))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("rikolin.jpg")))
        self.label.setObjectName(_fromUtf8("label"))
        self.error_label = QtGui.QLabel(self.groupBox)
        self.error_label.setGeometry(QtCore.QRect(230, 310, 52, 15))
        self.error_label.setStyleSheet(_fromUtf8("color:red"))
        self.error_label.setText(_fromUtf8(""))
        self.error_label.setObjectName(_fromUtf8("error_label"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(220, 0, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("color:black;"))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.groupBox.setTitle(_translate("Dialog", "                                                                 ", None))
        self.label_13.setText(_translate("Dialog", "Usuario", None))
        self.label_14.setText(_translate("Dialog", "Contrasena", None))
        self.BIngresar.setText(_translate("Dialog", "Ingresar", None))
        self.label_2.setText(_translate("Dialog", " Login", None))

