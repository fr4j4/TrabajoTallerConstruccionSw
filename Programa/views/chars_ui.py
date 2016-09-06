# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/CharacterDialog.ui'
#
# Created: Mon Sep  5 20:51:26 2016
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
        Dialog.resize(640, 480)
        self.comboBox = QtGui.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(110, 40, 381, 25))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 40, 111, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.in_descripcion = QtGui.QTextEdit(Dialog)
        self.in_descripcion.setGeometry(QtCore.QRect(110, 170, 481, 161))
        self.in_descripcion.setObjectName(_fromUtf8("in_descripcion"))
        self.in_nombre = QtGui.QLineEdit(Dialog)
        self.in_nombre.setGeometry(QtCore.QRect(110, 110, 481, 27))
        self.in_nombre.setObjectName(_fromUtf8("in_nombre"))
        self.check_new = QtGui.QCheckBox(Dialog)
        self.check_new.setGeometry(QtCore.QRect(110, 350, 141, 20))
        self.check_new.setObjectName(_fromUtf8("check_new"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 170, 71, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.BGuardar = QtGui.QPushButton(Dialog)
        self.BGuardar.setGeometry(QtCore.QRect(510, 350, 85, 27))
        self.BGuardar.setObjectName(_fromUtf8("BGuardar"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 110, 61, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.BCerrar = QtGui.QPushButton(Dialog)
        self.BCerrar.setGeometry(QtCore.QRect(540, 440, 85, 27))
        self.BCerrar.setObjectName(_fromUtf8("BCerrar"))
        self.message_label = QtGui.QLabel(Dialog)
        self.message_label.setGeometry(QtCore.QRect(110, 70, 471, 31))
        self.message_label.setStyleSheet(_fromUtf8("color:blue;"))
        self.message_label.setText(_fromUtf8(""))
        self.message_label.setObjectName(_fromUtf8("message_label"))
        self.BEliminar = QtGui.QPushButton(Dialog)
        self.BEliminar.setGeometry(QtCore.QRect(500, 40, 85, 27))
        self.BEliminar.setObjectName(_fromUtf8("BEliminar"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Personaje", None))
        self.check_new.setText(_translate("Dialog", "Guardar como nuevo", None))
        self.label_2.setText(_translate("Dialog", "Descripción", None))
        self.BGuardar.setText(_translate("Dialog", "Guardar", None))
        self.label_3.setText(_translate("Dialog", "Nombre", None))
        self.BCerrar.setText(_translate("Dialog", "Cerrar", None))
        self.BEliminar.setText(_translate("Dialog", "Eliminar", None))

