# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test1.ui'
#
# Created: Mon Jun 20 04:28:09 2016
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(640, 340)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 621, 281))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tableView_4 = QtGui.QTableView(self.tab)
        self.tableView_4.setGeometry(QtCore.QRect(10, 10, 451, 201))
        self.tableView_4.setObjectName(_fromUtf8("tableView_4"))
        self.checkBox_2 = QtGui.QCheckBox(self.tab)
        self.checkBox_2.setGeometry(QtCore.QRect(480, 200, 121, 17))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.comboBox_2 = QtGui.QComboBox(self.tab)
        self.comboBox_2.setGeometry(QtCore.QRect(480, 220, 121, 22))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.label_16 = QtGui.QLabel(self.tab)
        self.label_16.setGeometry(QtCore.QRect(480, 30, 111, 151))
        self.label_16.setStyleSheet(_fromUtf8(" border-style: solid;\n"
"     border-width: 2px;\n"
"     border-radius: 5px;\n"
"     border-color: black;"))
        self.label_16.setText(_fromUtf8(""))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.pushButton_15 = QtGui.QPushButton(self.tab)
        self.pushButton_15.setGeometry(QtCore.QRect(10, 220, 121, 23))
        self.pushButton_15.setObjectName(_fromUtf8("pushButton_15"))
        self.pushButton_16 = QtGui.QPushButton(self.tab)
        self.pushButton_16.setGeometry(QtCore.QRect(340, 220, 121, 23))
        self.pushButton_16.setObjectName(_fromUtf8("pushButton_16"))
        self.pushButton_17 = QtGui.QPushButton(self.tab)
        self.pushButton_17.setGeometry(QtCore.QRect(180, 220, 121, 23))
        self.pushButton_17.setObjectName(_fromUtf8("pushButton_17"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tableView_3 = QtGui.QTableView(self.tab_2)
        self.tableView_3.setGeometry(QtCore.QRect(10, 50, 451, 161))
        self.tableView_3.setObjectName(_fromUtf8("tableView_3"))
        self.label_12 = QtGui.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(480, 30, 111, 151))
        self.label_12.setStyleSheet(_fromUtf8(" border-style: solid;\n"
"     border-width: 2px;\n"
"     border-radius: 5px;\n"
"     border-color: black;"))
        self.label_12.setText(_fromUtf8(""))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.pushButton_6 = QtGui.QPushButton(self.tab_2)
        self.pushButton_6.setGeometry(QtCore.QRect(340, 220, 121, 23))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(self.tab_2)
        self.pushButton_7.setGeometry(QtCore.QRect(180, 220, 121, 23))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.comboBox = QtGui.QComboBox(self.tab_2)
        self.comboBox.setGeometry(QtCore.QRect(130, 20, 121, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.checkBox = QtGui.QCheckBox(self.tab_2)
        self.checkBox.setGeometry(QtCore.QRect(10, 20, 121, 17))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.pushButton_12 = QtGui.QPushButton(self.tab_2)
        self.pushButton_12.setGeometry(QtCore.QRect(10, 220, 121, 23))
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.tableView = QtGui.QTableView(self.tab_3)
        self.tableView.setGeometry(QtCore.QRect(10, 10, 451, 201))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.pushButton_13 = QtGui.QPushButton(self.tab_3)
        self.pushButton_13.setGeometry(QtCore.QRect(10, 220, 121, 23))
        self.pushButton_13.setObjectName(_fromUtf8("pushButton_13"))
        self.pushButton_14 = QtGui.QPushButton(self.tab_3)
        self.pushButton_14.setGeometry(QtCore.QRect(180, 220, 121, 23))
        self.pushButton_14.setObjectName(_fromUtf8("pushButton_14"))
        self.pushButton_8 = QtGui.QPushButton(self.tab_3)
        self.pushButton_8.setGeometry(QtCore.QRect(340, 220, 121, 23))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.label_14 = QtGui.QLabel(self.tab_3)
        self.label_14.setGeometry(QtCore.QRect(480, 30, 111, 151))
        self.label_14.setStyleSheet(_fromUtf8(" border-style: solid;\n"
"     border-width: 2px;\n"
"     border-radius: 5px;\n"
"     border-color: black;"))
        self.label_14.setText(_fromUtf8(""))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Administración", None))
        self.checkBox_2.setText(_translate("MainWindow", "Filtrar por Actor?", None))
        self.pushButton_15.setText(_translate("MainWindow", "Nueva Película...", None))
        self.pushButton_16.setText(_translate("MainWindow", "Eliminar Seleccionado", None))
        self.pushButton_17.setText(_translate("MainWindow", "Editar Seleccionado...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Películas", None))
        self.pushButton_6.setText(_translate("MainWindow", "Eliminar Seleccionado", None))
        self.pushButton_7.setText(_translate("MainWindow", "Editar Seleccionado...", None))
        self.checkBox.setText(_translate("MainWindow", "Filtrar por película?", None))
        self.pushButton_12.setText(_translate("MainWindow", "Nuevo Actor...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Actores", None))
        self.pushButton_13.setText(_translate("MainWindow", "Nuevo Director...", None))
        self.pushButton_14.setText(_translate("MainWindow", "Editar Seleccionado...", None))
        self.pushButton_8.setText(_translate("MainWindow", "Eliminar Seleccionado", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Directores", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

