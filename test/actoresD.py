# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ActoresDialog.ui'
#
# Created: Mon Jun 20 04:31:43 2016
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
        Dialog.resize(570, 250)
        self.groupBox_3 = QtGui.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 10, 551, 191))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.formLayoutWidget_3 = QtGui.QWidget(self.groupBox_3)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(10, 30, 301, 81))
        self.formLayoutWidget_3.setObjectName(_fromUtf8("formLayoutWidget_3"))
        self.formLayout_3 = QtGui.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setMargin(0)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label_13 = QtGui.QLabel(self.formLayoutWidget_3)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_13)
        self.lineEdit_5 = QtGui.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_5)
        self.label_14 = QtGui.QLabel(self.formLayoutWidget_3)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_14)
        self.lineEdit_6 = QtGui.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_6)
        self.label_15 = QtGui.QLabel(self.formLayoutWidget_3)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_15)
        self.dateEdit_5 = QtGui.QDateEdit(self.formLayoutWidget_3)
        self.dateEdit_5.setObjectName(_fromUtf8("dateEdit_5"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.dateEdit_5)
        self.label_12 = QtGui.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(430, 20, 111, 151))
        self.label_12.setStyleSheet(_fromUtf8(" border-style: solid;\n"
"     border-width: 2px;\n"
"     border-radius: 5px;\n"
"     border-color: black;"))
        self.label_12.setText(_fromUtf8(""))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_17 = QtGui.QLabel(self.groupBox_3)
        self.label_17.setGeometry(QtCore.QRect(10, 140, 70, 20))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.lineEdit_7 = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_7.setGeometry(QtCore.QRect(50, 140, 341, 20))
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.toolButton = QtGui.QToolButton(self.groupBox_3)
        self.toolButton.setGeometry(QtCore.QRect(390, 140, 25, 21))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.pushButton_5 = QtGui.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(400, 210, 71, 21))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(480, 210, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.groupBox_3.setTitle(_translate("Dialog", "Datos Actor", None))
        self.label_13.setText(_translate("Dialog", "Nombre", None))
        self.label_14.setText(_translate("Dialog", "País", None))
        self.label_15.setText(_translate("Dialog", "Fecha Nacmiento", None))
        self.label_17.setText(_translate("Dialog", "Imagen", None))
        self.toolButton.setText(_translate("Dialog", "...", None))
        self.pushButton_5.setText(_translate("Dialog", "Listo", None))
        self.pushButton.setText(_translate("Dialog", "Cancelar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

