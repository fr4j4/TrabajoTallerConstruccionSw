# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NuevoActorDialog.ui'
#
# Created: Sun Sep  4 19:45:30 2016
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
        Dialog.resize(645, 325)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 621, 301))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayoutWidget_3 = QtGui.QWidget(self.groupBox)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(10, 40, 441, 101))
        self.formLayoutWidget_3.setObjectName(_fromUtf8("formLayoutWidget_3"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget_3)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_1 = QtGui.QLabel(self.formLayoutWidget_3)
        self.label_1.setObjectName(_fromUtf8("label_1"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_1)
        self.LNombre = QtGui.QLineEdit(self.formLayoutWidget_3)
        self.LNombre.setObjectName(_fromUtf8("LNombre"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.LNombre)
        self.label_3 = QtGui.QLabel(self.formLayoutWidget_3)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.LFecha = QtGui.QDateEdit(self.formLayoutWidget_3)
        self.LFecha.setObjectName(_fromUtf8("LFecha"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.LFecha)
        self.label_5 = QtGui.QLabel(self.formLayoutWidget_3)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_5)
        self.LGenero = QtGui.QComboBox(self.formLayoutWidget_3)
        self.LGenero.setObjectName(_fromUtf8("LGenero"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.LGenero)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 150, 51, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.LImagen = QtGui.QLineEdit(self.groupBox)
        self.LImagen.setGeometry(QtCore.QRect(137, 150, 289, 20))
        self.LImagen.setObjectName(_fromUtf8("LImagen"))
        self.toolButton = QtGui.QToolButton(self.groupBox)
        self.toolButton.setGeometry(QtCore.QRect(425, 150, 25, 21))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.BListo = QtGui.QPushButton(self.groupBox)
        self.BListo.setGeometry(QtCore.QRect(456, 260, 71, 21))
        self.BListo.setObjectName(_fromUtf8("BListo"))
        self.BCancelar = QtGui.QPushButton(self.groupBox)
        self.BCancelar.setGeometry(QtCore.QRect(530, 260, 75, 23))
        self.BCancelar.setObjectName(_fromUtf8("BCancelar"))
        self.Display = QtGui.QLabel(self.groupBox)
        self.Display.setGeometry(QtCore.QRect(490, 40, 111, 161))
        self.Display.setStyleSheet(_fromUtf8(" border-style: solid;\n"
"     border-width: 2px;\n"
"     border-radius: 5px;\n"
"     border-color: black;"))
        self.Display.setText(_fromUtf8(""))
        self.Display.setScaledContents(True)
        self.Display.setObjectName(_fromUtf8("Display"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.groupBox.setTitle(_translate("Dialog", "Datos Actor", None))
        self.label_1.setText(_translate("Dialog", "Nombre", None))
        self.label_3.setText(_translate("Dialog", "Fecha Nacimiento", None))
        self.LFecha.setDisplayFormat(_translate("Dialog", "yyyy-MM-dd", None))
        self.label_5.setText(_translate("Dialog", "Genero", None))
        self.label_4.setText(_translate("Dialog", "Imagen", None))
        self.toolButton.setText(_translate("Dialog", "...", None))
        self.BListo.setText(_translate("Dialog", "Listo", None))
        self.BCancelar.setText(_translate("Dialog", "Cancelar", None))

