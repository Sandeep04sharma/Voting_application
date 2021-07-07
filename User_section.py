# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'User_section.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

class Ui_MainWindow(object):
    # fn for data base connection
    def dbconnect(self):
        con = pymysql.connect(host="localhost", user="root", password="", db="votingdb")
        return con

    # fn for message
    def message(self, title, msg):
        window = QtWidgets.QMessageBox()
        window.setWindowTitle(title)
        window.setText(msg)
        window.setStandardButtons(QtWidgets.QMessageBox.Ok)
        window.exec_()

    #fn for vote submit
    def submitVote(self):
        con=self.dbconnect()
        cursor=con.cursor()
    #storing for vote submission
        voterName=self.lineEdit.text()
        voterIdCard=self.lineEdit_2.text()
    #checking voter data in voter table
        checkReg="select * from voters where VoterIdCard =%s"
        cursor.execute(checkReg,(voterIdCard))
        countReg=cursor.rowcount
    # checking vote in voters
        checkVote="select * from votes where VoterIdCard=%s"
        cursor.execute(checkVote,(voterIdCard))
        countVote=cursor.rowcount

        # checking user registration and vote
        # also checking radio buttons
        if countReg!=1:
            self.message("Error","You are not earlier registered voter")
        elif countVote==1:
            self.message("Error","You have already submitted ur vote")
        # BJP vote
        elif self.radioButton.isChecked():
            vote="BJP"
            insert="insert into votes (VoteParty,VoterName,VoterIdCard) values(%s,%s,%s)"
            run=cursor.execute(insert,(vote,voterName,voterIdCard))
            if run:
                self.message("Submitted","Your vote submitted succesfully, Thank you !!")

            # NCL vote
        elif self.radioButton_2.isChecked():
            vote = "NCL"
            insert = "insert into votes (VoteParty,VoterName,VoterIdCard) values(%s,%s,%s)"
            run = cursor.execute(insert, (vote,voterName,voterIdCard))
            if run:
                self.message("Submitted", "Your vote submitted succesfully, Thank you !!")
        # AAp vote
        elif self.radioButton_3.isChecked():
            vote = "AAP"
            insert = "insert into votes (VoteParty,VoterName,VoterIdCard) values(%s,%s,%s)"
            run = cursor.execute(insert, (vote,voterName,voterIdCard))
            if run:
                self.message("Submitted", "Your vote submitted succesfully, Thank you !!")
        con.commit()
        con.close()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 350)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(185, 18, 250, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 91, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(180, 80, 265, 30))
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("background-color: rgb(253, 255, 254);")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 150, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 220, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 150, 265, 30))
        self.lineEdit_2.setAutoFillBackground(False)
        self.lineEdit_2.setStyleSheet("background-color: rgb(253, 255, 254);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(180, 220, 75, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setAutoFillBackground(False)
        self.radioButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(270, 220, 75, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setAutoFillBackground(False)
        self.radioButton_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(360, 220, 80, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setAutoFillBackground(False)
        self.radioButton_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_3.setObjectName("radioButton_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 280, 265, 30))
        self.pushButton.clicked.connect(self.submitVote)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "User Section -Version 1.2.1"))
        self.label.setText(_translate("MainWindow", "Voting Application"))
        self.label_2.setText(_translate("MainWindow", "Name :"))
        self.label_3.setText(_translate("MainWindow", "I\'D Card No :"))
        self.label_4.setText(_translate("MainWindow", "Select Vote :"))
        self.radioButton.setText(_translate("MainWindow", "BJP"))
        self.radioButton_2.setText(_translate("MainWindow", "NCL"))
        self.radioButton_3.setText(_translate("MainWindow", "AAP"))
        self.pushButton.setText(_translate("MainWindow", "Submit Vote"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
