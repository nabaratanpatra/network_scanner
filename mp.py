#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from socket import *

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
        MainWindow.resize(334, 562)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 321, 541))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.lineEdit = QtGui.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(70, 40, 171, 31))
        self.lineEdit.setText(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(80, 10, 161, 27))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.toolButton = QtGui.QToolButton(self.tab)
        self.toolButton.setGeometry(QtCore.QRect(70, 80, 171, 35))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.textEdit = QtGui.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(10, 130, 291, 351))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(70, 40, 171, 31))
        self.lineEdit_3.setText(_fromUtf8(""))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.toolButton_3 = QtGui.QToolButton(self.tab_2)
        self.toolButton_3.setGeometry(QtCore.QRect(70, 160, 171, 35))
        self.toolButton_3.setObjectName(_fromUtf8("toolButton_3"))
        self.label_4 = QtGui.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(80, 10, 161, 27))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit_5 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(80, 110, 61, 31))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.lineEdit_6 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(170, 110, 61, 31))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.label_5 = QtGui.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(110, 80, 101, 27))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(150, 110, 16, 27))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.textEdit_3 = QtGui.QTextEdit(self.tab_2)
        self.textEdit_3.setGeometry(QtCore.QRect(10, 210, 291, 281))
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(90, 540, 161, 27))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setScaledContents(False)
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionOpen_Result = QtGui.QAction(MainWindow)
        self.actionOpen_Result.setObjectName(_fromUtf8("actionOpen_Result"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionExit_2 = QtGui.QAction(MainWindow)
        self.actionExit_2.setObjectName(_fromUtf8("actionExit_2"))

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
  	QtCore.QObject.connect(self.toolButton, QtCore.SIGNAL(_fromUtf8("clicked()")), check1)
	QtCore.QObject.connect(self.toolButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), check2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Mini project 5th sem", None))
        self.label_2.setText(_translate("MainWindow", "Enter IP Address:", None))
        self.toolButton.setText(_translate("MainWindow", "Scan", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "IP Scanner", None))
        self.toolButton_3.setText(_translate("MainWindow", "Scan", None))
        self.label_4.setText(_translate("MainWindow", "Enter IP Address:", None))
        self.label_5.setText(_translate("MainWindow", "Port Range:", None))
        self.label_6.setText(_translate("MainWindow", "-", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Port Scanner", None))
        self.label.setText(_translate("MainWindow", "GUI scanner with python", None))
        self.actionOpen_Result.setText(_translate("MainWindow", "Open ", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionExit_2.setText(_translate("MainWindow", "Exit", None))


def IP_Address(addr):
	for x in range (80,81):
		s=socket(AF_INET,SOCK_STREAM)
		s.settimeout(0.01)
		if not s.connect_ex((addr,x)):
			s.close()
			return "TRUE"
		else:
			s.close()

def check1():
	user_IP=ui.lineEdit.text()
	x=str(user_IP.split(".")[0])+"."+str(user_IP.split(".")[1])+"."+str(user_IP.split(".")[2])+"."
	for ip in range(1,255):
		addr=str(x)+str(ip)
		if IP_Address(addr):
			printing=("%s - %s"%(addr,getfqdn(addr)))
			ui.textEdit.setText(printing)
def Port(host_IP,frst,last):
	for ports in range(frst,last):
		sockt=socket(AF_INET,SOCK_STREAM)
		sockt.settimeout(0.6)
		result = sockt.connect_ex((host_IP,ports))
		if(result == 0) :
			port_s=(' Port %d   ->     OPEN' % (ports))
			ui.textEdit_3.append(port_s)
	sockt.close()

def check2():
	import socket
	ui.textEdit_3.clear()
	user_IP=ui.lineEdit_3.text()
	x=str(user_IP.split(".")[0])+"."+str(user_IP.split(".")[1])+"."+str(user_IP.split(".")[2])+"."+str(user_IP.split(".")[3])
	frst_port=int(ui.lineEdit_5.text())
	last_port=int(ui.lineEdit_6.text())
	Port(x,frst_port,last_port)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
