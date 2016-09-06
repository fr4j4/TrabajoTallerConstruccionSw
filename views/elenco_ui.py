# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/ElencoDialog.ui'
#
# Created: Mon Sep  5 13:19:14 2016
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
        self.BCerrar = QtGui.QPushButton(Dialog)
        self.BCerrar.setGeometry(QtCore.QRect(540, 440, 85, 27))
        self.BCerrar.setObjectName(_fromUtf8("BCerrar"))
        self.tabla = QtGui.QTableWidget(Dialog)
        self.tabla.setGeometry(QtCore.QRect(10, 240, 611, 161))
        self.tabla.setObjectName(_fromUtf8("tabla"))
        self.tabla.setColumnCount(0)
        self.tabla.setRowCount(0)
        self.CPelicula = QtGui.QComboBox(Dialog)
        self.CPelicula.setGeometry(QtCore.QRect(90, 20, 511, 25))
        self.CPelicula.setObjectName(_fromUtf8("CPelicula"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 23, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 60, 611, 151))
        self.groupBox.setStyleSheet(_fromUtf8(""))
        self.groupBox.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.CPersonaje = QtGui.QComboBox(self.groupBox)
        self.CPersonaje.setGeometry(QtCore.QRect(130, 70, 241, 25))
        self.CPersonaje.setObjectName(_fromUtf8("CPersonaje"))
        self.CActor = QtGui.QComboBox(self.groupBox)
        self.CActor.setGeometry(QtCore.QRect(130, 40, 241, 25))
        self.CActor.setObjectName(_fromUtf8("CActor"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(40, 70, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(40, 40, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.BPersonajes = QtGui.QPushButton(self.groupBox)
        self.BPersonajes.setGeometry(QtCore.QRect(400, 70, 161, 27))
        self.BPersonajes.setStyleSheet(_fromUtf8(""))
        self.BPersonajes.setObjectName(_fromUtf8("BPersonajes"))
        self.BAgregar = QtGui.QPushButton(self.groupBox)
        self.BAgregar.setGeometry(QtCore.QRect(230, 120, 141, 27))
        self.BAgregar.setObjectName(_fromUtf8("BAgregar"))
        self.message_label = QtGui.QLabel(self.groupBox)
        self.message_label.setGeometry(QtCore.QRect(160, 10, 431, 16))
        self.message_label.setStyleSheet(_fromUtf8("color:red;"))
        self.message_label.setText(_fromUtf8(""))
        self.message_label.setObjectName(_fromUtf8("message_label"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 220, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.BEliminar = QtGui.QPushButton(Dialog)
        self.BEliminar.setGeometry(QtCore.QRect(10, 410, 151, 27))
        self.BEliminar.setObjectName(_fromUtf8("BEliminar"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.BCerrar.setText(_translate("Dialog", "Cerrar", None))
        self.label_2.setText(_translate("Dialog", "Película", None))
        self.groupBox.setTitle(_translate("Dialog", "Agregar actor al elenco", None))
        self.label_3.setText(_translate("Dialog", "Personaje", None))
        self.label.setText(_translate("Dialog", "Actor", None))
        self.BPersonajes.setText(_translate("Dialog", "Administrar personajes...", None))
        self.BAgregar.setText(_translate("Dialog", "Agregar al elenco!", None))
        self.label_4.setText(_translate("Dialog", "Elenco", None))
        self.BEliminar.setText(_translate("Dialog", "Quitar actor seleccionado", None))

