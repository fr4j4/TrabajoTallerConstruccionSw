# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NuevaPeliculaDialog.ui'
#
# Created: Sun Sep  4 19:41:06 2016
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
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 621, 301))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayoutWidget_3 = QtGui.QWidget(self.groupBox)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(10, 40, 441, 191))
        self.formLayoutWidget_3.setObjectName(_fromUtf8("formLayoutWidget_3"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget_3)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_1 = QtGui.QLabel(self.formLayoutWidget_3)
        self.label_1.setObjectName(_fromUtf8("label_1"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_1)
        self.label_2 = QtGui.QLabel(self.formLayoutWidget_3)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.LEstreno = QtGui.QDateEdit(self.formLayoutWidget_3)
        self.LEstreno.setObjectName(_fromUtf8("LEstreno"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.LEstreno)
        self.label_3 = QtGui.QLabel(self.formLayoutWidget_3)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtGui.QLabel(self.formLayoutWidget_3)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.LDescripcion = QtGui.QTextEdit(self.formLayoutWidget_3)
        self.LDescripcion.setObjectName(_fromUtf8("LDescripcion"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.LDescripcion)
        self.LNombre = QtGui.QLineEdit(self.formLayoutWidget_3)
        self.LNombre.setObjectName(_fromUtf8("LNombre"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.LNombre)
        self.LPais = QtGui.QLineEdit(self.formLayoutWidget_3)
        self.LPais.setObjectName(_fromUtf8("LPais"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.LPais)
        self.BListo = QtGui.QPushButton(self.groupBox)
        self.BListo.setGeometry(QtCore.QRect(300, 270, 71, 21))
        self.BListo.setObjectName(_fromUtf8("BListo"))
        self.BCancelar = QtGui.QPushButton(self.groupBox)
        self.BCancelar.setGeometry(QtCore.QRect(374, 270, 75, 23))
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
        self.LDisplay = QtGui.QLineEdit(self.groupBox)
        self.LDisplay.setGeometry(QtCore.QRect(80, 240, 351, 20))
        self.LDisplay.setObjectName(_fromUtf8("LDisplay"))
        self.BBox = QtGui.QToolButton(self.groupBox)
        self.BBox.setGeometry(QtCore.QRect(427, 239, 25, 21))
        self.BBox.setObjectName(_fromUtf8("BBox"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 236, 65, 26))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.groupBox.setTitle(_translate("Dialog", "Nueva Película", None))
        self.label_1.setText(_translate("Dialog", "Nombre", None))
        self.label_2.setText(_translate("Dialog", "Estreno", None))
        self.LEstreno.setDisplayFormat(_translate("Dialog", "yyyy-MM-dd", None))
        self.label_3.setText(_translate("Dialog", "Pais", None))
        self.label_4.setText(_translate("Dialog", "Descripción", None))
        self.BListo.setText(_translate("Dialog", "Listo", None))
        self.BCancelar.setText(_translate("Dialog", "Cancelar", None))
        self.BBox.setText(_translate("Dialog", "...", None))
        self.label_5.setText(_translate("Dialog", "Imagen", None))

