# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FinalUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FinalUI(object):
    def setupUi(self, FinalUI):
        FinalUI.setObjectName("FinalUI")
        FinalUI.resize(813, 599)
        self.centralwidget = QtWidgets.QWidget(FinalUI)
        self.centralwidget.setObjectName("centralwidget")
        self.bg_lebel = QtWidgets.QLabel(self.centralwidget)
        self.bg_lebel.setGeometry(QtCore.QRect(-10, -20, 841, 711))
        self.bg_lebel.setText("")
        self.bg_lebel.setPixmap(QtGui.QPixmap("C:/Users/Pradeep Mishra/output//Jeeva_materials//background.jpg"))
        self.bg_lebel.setScaledContents(True)
        self.bg_lebel.setObjectName("bg_lebel")
        self.siri_label = QtWidgets.QLabel(self.centralwidget)
        self.siri_label.setGeometry(QtCore.QRect(320,20,161,151))
        self.siri_label.setText("")
        self.siri_label.setPixmap(QtGui.QPixmap("C:/Users/Pradeep Mishra/output/Jeeva_materials/jeeva.png"))
        self.siri_label.setScaledContents(True)
        self.siri_label.setObjectName("siri_label")
        self.Mic_Label = QtWidgets.QLabel(self.centralwidget)
        self.Mic_Label.setGeometry(QtCore.QRect(310, 380, 191, 181))
        self.Mic_Label.setText("")
        self.Mic_Label.setPixmap(QtGui.QPixmap("C:/Users/Pradeep Mishra/output/Jeeva_materials/microphone.png"))
        self.Mic_Label.setScaledContents(True)
        self.Mic_Label.setObjectName("Mic_Label")
        self.recognition_label = QtWidgets.QLabel(self.centralwidget)
        self.recognition_label.setGeometry(QtCore.QRect(170, 280, 481, 81))
        self.recognition_label.setText("")
        self.recognition_label.setPixmap(QtGui.QPixmap("C:/Users/Pradeep Mishra/output/Jeeva_materials/middle.gif"))
        self.recognition_label.setScaledContents(True)
        self.recognition_label.setObjectName("recognition_label")
        self.start_push = QtWidgets.QPushButton(self.centralwidget)
        self.start_push.setGeometry(QtCore.QRect(370, 430, 71, 71))
        self.start_push.setStyleSheet("color: rgb(0, 147, 147);\n"
"font: 12pt \"Copperplate Gothic Bold\";\n"
"background-color: Transparent;\n"
"")
        self.start_push.setText("")
        self.start_push.setObjectName("start_push")
        self.Exit_push = QtWidgets.QPushButton(self.centralwidget)
        self.Exit_push.setGeometry(QtCore.QRect(630,440,111,41))
        self.Exit_push.setStyleSheet("color: rgb(0, 147, 147);\n"
"font: 12pt \"Copperplate Gothic Bold\";\n"
"background-color: Transparent;\n"
"")
        self.Exit_push.setObjectName("Exit_push")
        self.Exit_Label = QtWidgets.QLabel(self.centralwidget)
        self.Exit_Label.setGeometry(QtCore.QRect(630,440,111,41))
        self.Exit_Label.setStyleSheet("")
        self.Exit_Label.setText("")
        self.Exit_Label.setPixmap(QtGui.QPixmap("C:/Users/Pradeep Mishra/output/Jeeva_materials/exit_background.png"))
        self.Exit_Label.setScaledContents(True)
        self.Exit_Label.setObjectName("Exit_Label")
        self.Date_lable = QtWidgets.QLabel(self.centralwidget)
        self.Date_lable.setGeometry(QtCore.QRect(40, 50, 191, 51))
        self.Date_lable.setStyleSheet("")
        self.Date_lable.setText("")
        self.Date_lable.setPixmap(QtGui.QPixmap("C:/Users/Pradeep Mishra/output/Jeeva_materials/exit_background.png"))
        self.Date_lable.setScaledContents(True)
        self.Date_lable.setObjectName("Date_lable")

        self.Time_label = QtWidgets.QLabel(self.centralwidget)
        self.Time_label.setGeometry(QtCore.QRect(590, 50, 191, 51))
        self.Time_label.setStyleSheet("")
        self.Time_label.setText("")
        self.Time_label.setPixmap(QtGui.QPixmap("C:/Users/Pradeep Mishra/output/Jeeva_materials/exit_background.png"))
        self.Time_label.setScaledContents(True)
        self.Time_label.setObjectName("Time_label")
        self.Date_text = QtWidgets.QTextBrowser(self.centralwidget)
        self.Date_text.setGeometry(QtCore.QRect(50, 60, 171, 41))
        self.Date_text.setStyleSheet("color: rgb(0, 147, 147);\n"
"font: 10pt \"Copperplate Gothic Bold\";\n"
"background-color: Transparent;\n"
"border-radius: none;")
        self.Date_text.setObjectName("Date_text")
        self.Time_text = QtWidgets.QTextBrowser(self.centralwidget)
        self.Time_text.setGeometry(QtCore.QRect(600, 60, 171, 41))
        self.Time_text.setStyleSheet("color: rgb(0, 147, 147);\n"
"font: 10pt \"Copperplate Gothic Bold\";\n"
"background-color: Transparent;\n"
"border-radius: none;")
        self.Time_text.setObjectName("Time_text")
        self.App_Lable = QtWidgets.QLabel(self.centralwidget)

        self.App_Lable.setGeometry(QtCore.QRect(350,200,111,31))
        self.App_Lable.setStyleSheet("")
        self.App_Lable.setText("")
        self.App_Lable.setPixmap(QtGui.QPixmap("C:/Users/Pradeep Mishra/output/Jeeva_materials/exit_background.png"))
        self.App_Lable.setScaledContents(True)
        self.App_Lable.setObjectName("App_Lable")
        self.App_push = QtWidgets.QPushButton(self.centralwidget)
        self.App_push.setGeometry(QtCore.QRect(340, 200, 131, 31))
        self.App_push.setStyleSheet("color: rgb(0, 147, 147);\n"
"font: 12pt \"Copperplate Gothic Bold\";\n"
"background-color: Transparent;\n"
"")
        self.App_push.setObjectName("App_push")
        self.bg_lebel.raise_()
        self.recognition_label.raise_()
        self.siri_label.raise_()
        self.Mic_Label.raise_()
        self.start_push.raise_()
        self.Exit_Label.raise_()
        self.Exit_push.raise_()
        self.Date_lable.raise_()
        self.Time_label.raise_()
       
        self.Date_text.raise_()
        self.Time_text.raise_()
        self.App_Lable.raise_()
        self.App_push.raise_()
        FinalUI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FinalUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 813, 21))
        self.menubar.setObjectName("menubar")
        FinalUI.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FinalUI)
        self.statusbar.setObjectName("statusbar")
        FinalUI.setStatusBar(self.statusbar)

        self.retranslateUi(FinalUI)
        QtCore.QMetaObject.connectSlotsByName(FinalUI)

    def retranslateUi(self, FinalUI):
        _translate = QtCore.QCoreApplication.translate
        FinalUI.setWindowTitle(_translate("FinalUI", "Jeeva AI Voice Assistant"))
        self.Exit_push.setText(_translate("FinalUI", "Exit"))
        self.App_push.setText(_translate("FinalUI", "J e e v a"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FinalUI = QtWidgets.QMainWindow()
    ui = Ui_FinalUI()
    ui.setupUi(FinalUI)
    FinalUI.show()
    sys.exit(app.exec_())
