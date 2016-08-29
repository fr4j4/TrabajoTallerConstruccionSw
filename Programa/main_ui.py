# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Mon Aug 29 18:44:27 2016
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
        MainWindow.resize(640, 335)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 621, 281))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.Peliculas = QtGui.QWidget()
        self.Peliculas.setObjectName(_fromUtf8("Peliculas"))
        self.checkBox = QtGui.QCheckBox(self.Peliculas)
        self.checkBox.setGeometry(QtCore.QRect(480, 200, 121, 17))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.comboBox = QtGui.QComboBox(self.Peliculas)
        self.comboBox.setGeometry(QtCore.QRect(480, 220, 121, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.pelicula_image = QtGui.QLabel(self.Peliculas)
        self.pelicula_image.setGeometry(QtCore.QRect(480, 30, 111, 151))
        self.pelicula_image.setStyleSheet(_fromUtf8(" border-style: solid;\n"
"     border-width: 2px;\n"
"     border-radius: 5px;\n"
"     border-color: black;"))
        self.pelicula_image.setText(_fromUtf8(""))
        self.pelicula_image.setScaledContents(True)
        self.pelicula_image.setObjectName(_fromUtf8("pelicula_image"))
        self.BNuevo = QtGui.QPushButton(self.Peliculas)
        self.BNuevo.setGeometry(QtCore.QRect(10, 220, 121, 23))
        self.BNuevo.setObjectName(_fromUtf8("BNuevo"))
        self.BEliminar = QtGui.QPushButton(self.Peliculas)
        self.BEliminar.setGeometry(QtCore.QRect(340, 220, 121, 23))
        self.BEliminar.setObjectName(_fromUtf8("BEliminar"))
        self.BEditar = QtGui.QPushButton(self.Peliculas)
        self.BEditar.setGeometry(QtCore.QRect(180, 220, 121, 23))
        self.BEditar.setObjectName(_fromUtf8("BEditar"))
        self.tabla_peliculas = QtGui.QTableWidget(self.Peliculas)
        self.tabla_peliculas.setGeometry(QtCore.QRect(10, 10, 451, 201))
        self.tabla_peliculas.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tabla_peliculas.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tabla_peliculas.setObjectName(_fromUtf8("tabla_peliculas"))
        self.tabla_peliculas.setColumnCount(0)
        self.tabla_peliculas.setRowCount(0)
        self.tabWidget.addTab(self.Peliculas, _fromUtf8(""))
        self.Actores = QtGui.QWidget()
        self.Actores.setObjectName(_fromUtf8("Actores"))
        self.actor_image = QtGui.QLabel(self.Actores)
        self.actor_image.setGeometry(QtCore.QRect(480, 30, 111, 151))
        self.actor_image.setStyleSheet(_fromUtf8(" border-style: solid;\n"
"     border-width: 2px;\n"
"     border-radius: 5px;\n"
"     border-color: black;"))
        self.actor_image.setText(_fromUtf8(""))
        self.actor_image.setScaledContents(True)
        self.actor_image.setObjectName(_fromUtf8("actor_image"))
        self.BEliminar_2 = QtGui.QPushButton(self.Actores)
        self.BEliminar_2.setGeometry(QtCore.QRect(340, 220, 121, 23))
        self.BEliminar_2.setObjectName(_fromUtf8("BEliminar_2"))
        self.BEditar_2 = QtGui.QPushButton(self.Actores)
        self.BEditar_2.setGeometry(QtCore.QRect(180, 220, 121, 23))
        self.BEditar_2.setObjectName(_fromUtf8("BEditar_2"))
        self.comboBox_2 = QtGui.QComboBox(self.Actores)
        self.comboBox_2.setGeometry(QtCore.QRect(150, 20, 121, 22))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.checkBox_2 = QtGui.QCheckBox(self.Actores)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 20, 131, 17))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.BNuevo_2 = QtGui.QPushButton(self.Actores)
        self.BNuevo_2.setGeometry(QtCore.QRect(10, 220, 121, 23))
        self.BNuevo_2.setObjectName(_fromUtf8("BNuevo_2"))
        self.tabla_actores = QtGui.QTableWidget(self.Actores)
        self.tabla_actores.setGeometry(QtCore.QRect(10, 50, 451, 161))
        self.tabla_actores.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tabla_actores.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tabla_actores.setObjectName(_fromUtf8("tabla_actores"))
        self.tabla_actores.setColumnCount(0)
        self.tabla_actores.setRowCount(0)
        self.tabWidget.addTab(self.Actores, _fromUtf8(""))
        self.Directores = QtGui.QWidget()
        self.Directores.setObjectName(_fromUtf8("Directores"))
        self.BNuevo_3 = QtGui.QPushButton(self.Directores)
        self.BNuevo_3.setGeometry(QtCore.QRect(10, 220, 121, 23))
        self.BNuevo_3.setObjectName(_fromUtf8("BNuevo_3"))
        self.BEditar_3 = QtGui.QPushButton(self.Directores)
        self.BEditar_3.setGeometry(QtCore.QRect(180, 220, 121, 23))
        self.BEditar_3.setObjectName(_fromUtf8("BEditar_3"))
        self.BEliminar_3 = QtGui.QPushButton(self.Directores)
        self.BEliminar_3.setGeometry(QtCore.QRect(340, 220, 121, 23))
        self.BEliminar_3.setObjectName(_fromUtf8("BEliminar_3"))
        self.director_image = QtGui.QLabel(self.Directores)
        self.director_image.setGeometry(QtCore.QRect(480, 30, 111, 151))
        self.director_image.setStyleSheet(_fromUtf8(" border-style: solid;\n"
"     border-width: 2px;\n"
"     border-radius: 5px;\n"
"     border-color: black;"))
        self.director_image.setText(_fromUtf8(""))
        self.director_image.setScaledContents(True)
        self.director_image.setObjectName(_fromUtf8("director_image"))
        self.tabla_directores = QtGui.QTableWidget(self.Directores)
        self.tabla_directores.setGeometry(QtCore.QRect(10, 10, 451, 201))
        self.tabla_directores.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tabla_directores.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tabla_directores.setObjectName(_fromUtf8("tabla_directores"))
        self.tabla_directores.setColumnCount(0)
        self.tabla_directores.setRowCount(0)
        self.tabWidget.addTab(self.Directores, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Administración", None))
        self.checkBox.setText(_translate("MainWindow", "Filtrar por Actor?", None))
        self.BNuevo.setText(_translate("MainWindow", "Nueva Película...", None))
        self.BEliminar.setText(_translate("MainWindow", "Eliminar Seleccionado", None))
        self.BEditar.setText(_translate("MainWindow", "Editar Seleccionado...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Peliculas), _translate("MainWindow", "Películas", None))
        self.BEliminar_2.setText(_translate("MainWindow", "Eliminar Seleccionado", None))
        self.BEditar_2.setText(_translate("MainWindow", "Editar Seleccionado...", None))
        self.checkBox_2.setText(_translate("MainWindow", "Filtrar por película?", None))
        self.BNuevo_2.setText(_translate("MainWindow", "Nuevo Actor...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Actores), _translate("MainWindow", "Actores", None))
        self.BNuevo_3.setText(_translate("MainWindow", "Nuevo Director...", None))
        self.BEditar_3.setText(_translate("MainWindow", "Editar Seleccionado...", None))
        self.BEliminar_3.setText(_translate("MainWindow", "Eliminar Seleccionado", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Directores), _translate("MainWindow", "Directores", None))

