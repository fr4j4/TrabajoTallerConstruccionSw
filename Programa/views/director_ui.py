# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DirectorDialog.ui'
#
# Created: Wed Aug 31 16:43:03 2016
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
        Dialog.resize(645, 229)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 541, 211))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayoutWidget = QtGui.QWidget(self.groupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 40, 521, 128))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.formLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.LNombre = QtGui.QLineEdit(self.formLayoutWidget)
        self.LNombre.setObjectName(_fromUtf8("LNombre"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.LNombre)
        self.label_2 = QtGui.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.LPais = QtGui.QLineEdit(self.formLayoutWidget)
        self.LPais.setObjectName(_fromUtf8("LPais"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.LPais)
        self.label_3 = QtGui.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.LNacimiento = QtGui.QDateEdit(self.formLayoutWidget)
        self.LNacimiento.setObjectName(_fromUtf8("LNacimiento"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.LNacimiento)
        self.label_4 = QtGui.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.LDefuncion = QtGui.QDateEdit(self.formLayoutWidget)
        self.LDefuncion.setObjectName(_fromUtf8("LDefuncion"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.LDefuncion)
        self.BListo = QtGui.QPushButton(self.groupBox)
        self.BListo.setGeometry(QtCore.QRect(380, 180, 71, 21))
        self.BListo.setObjectName(_fromUtf8("BListo"))
        self.BCancelar = QtGui.QPushButton(self.groupBox)
        self.BCancelar.setGeometry(QtCore.QRect(460, 180, 75, 23))
        self.BCancelar.setObjectName(_fromUtf8("BCancelar"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.groupBox.setTitle(_translate("Dialog", "Datos Director", None))
        self.label.setText(_translate("Dialog", "Nombre", None))
        self.label_2.setText(_translate("Dialog", "País", None))
        self.label_3.setText(_translate("Dialog", "Fecha Nacimiento", None))
        self.label_4.setText(_translate("Dialog", "Fecha Defunción", None))
        self.BListo.setText(_translate("Dialog", "Listo", None))
        self.BCancelar.setText(_translate("Dialog", "Cancelar", None))

