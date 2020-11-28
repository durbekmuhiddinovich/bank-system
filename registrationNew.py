from PyQt5 import QtCore,QtGui,QtWidgets
import sqlite3
from MainLogin import Ui_LoginWindow
from PyQt5.QtWidgets import QMessageBox
dbb = sqlite3.connect("BankNH.db")
c = dbb.cursor()

class Ui_registrationPage(object):
    def setupUi(self,registrationPage):
        registrationPage.setObjectName("registrationPage")
        registrationPage.resize(591,486)
        registrationPage.setstyleSheet("background -color: rgb(12,31,45);\n")
        self.centralWidget = QtWidgets.QWidgat(registrationPage)
        self.centralWidget.setObjectName("centralwidgate")
        self.fromLayout_2 = QtWidgets.QFormLayout(self.centralWidget)
        self.fromLayout_2.setObjectName("formLayout_2")
        self.fromLayout = QtWidgets.QFormLayout()
        self.fromLayout.setLabelAlignment(QtCore.Qt.AlignCentr)
        self.fromLayout.setFormAlignment(QtCore.Qt.AlignCentr)
        self.fromLayout.setObjectName("fromLayout")
        # Username
        self.label_username = QtWidgets.QLabel(self.centralWidget)
        self.label_username.setStyleSheet("font:75 10pt \"Verdana\";\n"
        "color: rgb(252,252,252);")
        self.label_username.setObjectName("label_username")
        self.fromLayout.setWidget(0, QtWidgets,QFormLayout.LabelRole, self.label_username)
        self.lineEdit_Username = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_Username.setstyleSheet("font: 75 10pt \"Verdana\";\n"
        "background-color: rgb(240,240,240);")
        self.lineEdit_Username.setObjectName("lineEdit_Username")
        self.fromLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole,self.lineEdit_Username)
        # Firstname
        self.label_fname = QtWidgets.QLabel(self.centralWidget)
        self.label_fname.setStyleSheet("font:75 10pt \"Verdana\";\n"
        "color: rgb(252,252,252);")
        self.label_fname.setObjectName("label_fname")
        self.fromLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole,self.lineEdit_fname)
        self.lineEdit_Firstname = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_Firstname.setstyleSheet("font: 75 10pt \"Verdana\";\n"
        "background-color: rgb(240,240,240);")
        self.lineEdit_Firstname.setObjectName("lineEdit_Firstname")
        self.fromLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole,self.lineEdit_Firstname)
        # Lastname
        self.label_Lastname = QtWidgets.QLabel(self.centralWidget)
        self.label_Lastname.setStyleSheet("font:75 10pt \"Verdana\";\n"
        "color: rgb(252,252,252);")
        self.label_Lastname.setObjectName("label_Lastname")
        self.fromLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole,self.lineEdit_Lastname)
        self.lineEdit_Lastname = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_Lastname.setstyleSheet("font: 75 10pt \"Verdana\";\n"
        "background-color: rgb(240,240,240);")
        self.lineEdit_Lastname.setObjectName("lineEdit_Lastname")
        self.fromLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole,self.lineEdit_Lastname)
        # Email
        self.label_Email = QtWidgets.QLabel(self.centralWidget)
        self.label_Email.setStyleSheet("font:75 10pt \"Verdana\";\n"
        "color: rgb(252,252,252);")
        self.label_Email.setObjectName("label_Email")
        self.fromLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole,self.lineEdit_Email)
        self.lineEdit_Email = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_Email.setstyleSheet("font: 75 10pt \"Verdana\";\n"
        "background-color: rgb(240,240,240);")
        self.lineEdit_Email.setObjectName("lineEdit_Email")
        self.fromLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole,self.lineEdit_Email)
        # password
        self.label_password = QtWidgets.QLabel(self.centralWidget)
        self.label_password.setStyleSheet("font:75 10pt \"Verdana\";\n"
        "color: rgb(252,252,252);")
        self.label_password.setObjectName("label_password")
        self.fromLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole,self.lineEdit_password)
        self.lineEdit_password = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_password.setstyleSheet("font: 75 10pt \"Verdana\";\n"
        "background-color: rgb(240,240,240);")
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.fromLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole,self.lineEdit_password)
        # confirm
        self.label_confirmPassword = QtWidgets.QLabel(self.centralWidget)
        self.label_confirmPassword.setStyleSheet("font:75 10pt \"Verdana\";\n"
        "color: rgb(252,252,252);")
        self.label_confirm.setObjectName("label_confirmPassword")
        self.fromLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole,self.lineEdit_confirmPassword)
        self.lineEdit_confirmPassword = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_confirmPassword.setstyleSheet("font: 75 10pt \"Verdana\";\n"
        "background-color: rgb(240,240,240);")
        self.lineEdit_confirmPassword.setObjectName("lineEdit_confirmPassword")
        self.fromLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole,self.lineEdit_confirmPassword)
        # phone
        self.label_phone = QtWidgets.QLabel(self.centralWidget)
        self.label_phone.setStyleSheet("font:75 10pt \"Verdana\";\n"
        "color: rgb(252,252,252);")
        self.label_phone.setObjectName("label_phone")
        self.fromLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole,self.lineEdit_phone)
        self.lineEdit_phone = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_phone.setstyleSheet("font: 75 10pt \"Verdana\";\n"
        "background-color: rgb(240,240,240);")
        self.lineEdit_phone.setObjectName("lineEdit_phone")
        self.fromLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole,self.lineEdit_phone)
        # sex
        self.label_sex = QtWidgets.QLabel(self.centralWidget)
        self.label_sex.setStyleSheet("font:75 10pt \"Verdana\";\n"
        "color: rgb(252,252,252);")
        self.label_sex.setObjectName("label_sex")
        self.fromLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole,self.lineEdit_sex)
        self.lineEdit_sex = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_sex.setstyleSheet("font: 75 10pt \"Verdana\";\n"
        "background-color: rgb(240,240,240);")
        self.lineEdit_sex.setObjectName("lineEdit_sex")
        self.fromLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole,self.lineEdit_sex)
        # addrees
        self.label_address = QtWidgets.QLabel(self.centralWidget)
        self.label_address.setStyleSheet("font:75 10pt \"Verdana\";\n"
        "color: rgb(252,252,252);")
        self.label_address.setObjectName("label_address")
        self.fromLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole,self.lineEdit_address)
        self.lineEdit_address = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_address.setstyleSheet("font: 75 10pt \"Verdana\";\n"
        "background-color: rgb(240,240,240);")
        self.lineEdit_address.setObjectName("lineEdit_address")
        self.fromLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole,self.lineEdit_address)
        # Registr push button
        self.pushButton_Register = QtWidgets.QPushButton(self.centralwidgat)
        self.pushButton_Register.setstyleSheet("font:75 10pt \"Verdand\";\n"
        "color: rgb(240,240,240);")
        ("font:75 10pt \"MS Shell Dig 2\";\n"
        "background-color: rgb(78,78,78);")
        self.pushButton_Register.setObjectName("pushBytton_Register")
        self.fromLayout.setWidget(11, QtWidgets.QFormLayout.SpanningRole,self.pushButton_Register)
        # reglogin
        self.pushButton_reglogin = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_Register.setstyleSheet("font:75 10pt \"Verdana\";\n"
        "color: rgb(240,240,240);"
        "font:75 10pt \"MS Shell Dig 2\";\n"
        "background-color: rgb(78,78,78);")
        self.pushButton_reglogin.setObjectName("pushBytton_reglogin")
        self.fromLayout.setWidget(12, QtWidgets.QFormLayout.SpanningRole,self.pushButton_reglogin)
        self.fromLayout_2.setLayout(1, QtWidgets.QFormLayout.SpanningRole,self.fromLayout)
        self.label_10.QtWidgets.QLabel(self.centralWidget)
        self.label_10.setStyleSheet("color: rgb(252,252,252); font:75 10pt \"MS Shell Dlg 2\";\n")
        self.label_10.setAlignment(QtCore.Qt.AlignCentr)
        self.label_10.setObjectName("label_10")
        self.fromLayout_2.setWidget(0, QtWidgets.QFormLayout.SpanningRole,self.label_10)
        registrationPage.setcentralWidget(self.centralWidget)
        self.statusbar = QtWidgets.QtStatusbar(registrationPage)
        self.statusbar.setObjectName("statusbar")
        registrationPage.setStatusbar(self.statusbar)

        self.retranslateUi(registrationPage)
        QtCore.QtMetaObject.connectSlotsByName(registrationPage)
        self.pushButton_Register.clicked.connect(self.createDB)
        self.pushButton_reglogin.clicked.connect(self.login)

    def general_messaga(self,title,message):
        msg = QMessageBox
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(QMessageBox.Question)
        msg.exec_()

    def CreatDB(self):
        c.execute('''CREATE TABLE IF NOT EXISTS NEWBANK (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            USERNAME CHAR(20) NOT NULL,
            FIRSTNAME SRT NOT NULL,
            LASTNAME STR NOT NULL,
            EMAIL STR NOT NULL,
            PASSWORD STR NOT NULL,
            CONFIRM STR NOT NULL,
            PHONE CHAR(11) NOT NULL,
            SEX STR,
            ADDRESS CHAR(50),
            BAL REAL(200) );
            ''')
        self.insertdb()

    def insertdb(self):
        username = self.lineEdit_Username.text()
        firstname = self.lineEdit_Firstname.text()
        lastname = self.lineEdit_Lastname.text()
        email = self.lineEdit_Email.text()
        if '@' not in email:
            self.general_messaga("invalid email")
            return email
        else:
            password = self.lineEdit_password.text()
            confirmPass = self.lineEdit_confirmPassword.text()
            if password != confirmPass:
                self.general_messaga("password error")
                return password and confirmPass
            elif len(password) != len(confirmPass):
                self.general_messaga("password error")
                return password and confirmPass
            else:
                phone = self.lineEdit_phone.text()
                if len(phone) != 13:
                    self.general_messaga("phone number error!")
                    return phone
                else:
                    sex = self.lineEdit_sex.text()
                    address = self.lineEdit_address.text()
                    c.execute("INSERT INTO NEWBANK(USERNAME,FIRSTNAME,LASTNAME,EMAIL,PASSWORD,CONFIRM,PHONE,SEX,ADDDRESS) VALUES(?,?,?,?,?,?,?,?,?)",(str(username),str(firstname),str(lastname),str(email),str(password),str(confirmPass),str(phone),str(sex),str(address)))
                    print("insert done")
                    dbb.commit()
                    dbb.close()
                    self.login()
    def login(self):
        self.LoginWindow = QtWidgets.QtMainWindow()
        self.ui = Ui_LoginWindow()
        self.ui.beginLogin(self.LoginWindow)
        self.LoginWindow.show()

    def retranslateUi(self, registrationPage):
        _translate = QtCore.QtCoreApplication.translate
        registrationPage.setWindowTitle(_translate("registrationPage","registration Page"))
        self.label_username.setText(_translate("registrationPage","Username"))
        self.lineEdit_Username.setPlecoholder(_translate("registrationPage","Username"))
        self.label_firstname.setText(_translate("registrationPage","Firstname"))
        self.lineEdit_firstname.setPlecoholder(_translate("registrationPage","Firstname"))
        self.label_lastname.setText(_translate("registrationPage","Lastname"))
        self.lineEdit_lastname.setPlecoholder(_translate("registrationPage","Lastname"))
        self.label_Email.setText(_translate("registrationPage","Email"))
        self.lineEdit_Email.setPlecoholder(_translate("registrationPage","Email"))
        self.label_password.setText(_translate("registrationPage","Password"))
        self.lineEdit_password.setPlecoholder(_translate("registrationPage","Password"))
        self.label_confirm.setText(_translate("registrationPage","Confirm"))
        self.lineEdit_confirm.setPlecoholder(_translate("registrationPage","Confirm"))
        self.label_phone.setText(_translate("registrationPage","Phone"))
        self.lineEdit_phone.setPlecoholder(_translate("registrationPage","Phone"))
        self.label_sex.setText(_translate("registrationPage","Sex"))
        self.lineEdit_sex.setPlecoholder(_translate("registrationPage","Sex"))
        self.label_username.setText(_translate("registrationPage","Username"))
        self.lineEdit_Username.setPlecoholder(_translate("registrationPage","Username"))