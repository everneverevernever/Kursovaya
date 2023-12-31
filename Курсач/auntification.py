# Form implementation generated from reading ui file 'auntification.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_authorization_form(object):
    def setupUi(self, authorization_form):
        authorization_form.setObjectName("authorization_form")
        authorization_form.resize(400, 360)
        authorization_form.setAccessibleName("")
        authorization_form.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        authorization_form.setStyleSheet("QWidget\n"
" {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"                                stop:0 rgb(148, 87, 235), stop:1 rgb(87, 37, 138));\n"
"}")
        self.layoutWidget = QtWidgets.QWidget(parent=authorization_form)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 230, 261, 111))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.loginButton = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.loginButton.setStyleSheet("/* Стиль для QPushButton */\n"
"QPushButton {\n"
"    background-color: rgba(255, 255, 255, 50);; /* Фиолетовый цвет фона */\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 10px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 16px;\n"
"    margin: 4px 2px;\n"
"    cursor: pointer;\n"
"    border-radius: 4px; /* Закругленные углы */\n"
"}\n"
"\n"
"/* Стиль для QPushButton при наведении */\n"
"QPushButton:hover {\n"
"    background-color: #8e44ad;\n"
"}")
        self.loginButton.setObjectName("loginButton")
        self.verticalLayout.addWidget(self.loginButton)
        self.registrationButton = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.registrationButton.setStyleSheet("/* Стиль для QPushButton */\n"
"QPushButton {\n"
"    background-color: rgba(255, 255, 255, 50);; /* Фиолетовый цвет фона */\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 10px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 16px;\n"
"    margin: 4px 2px;\n"
"    cursor: pointer;\n"
"    border-radius: 4px; /* Закругленные углы */\n"
"}\n"
"\n"
"/* Стиль для QPushButton при наведении */\n"
"QPushButton:hover {\n"
"    background-color: #8e44ad;\n"
"}")
        self.registrationButton.setObjectName("registrationButton")
        self.verticalLayout.addWidget(self.registrationButton)
        self.label_login = QtWidgets.QLabel(parent=authorization_form)
        self.label_login.setGeometry(QtCore.QRect(120, 10, 161, 51))
        self.label_login.setStyleSheet("QLabel\n"
" {\n"
"    background-color: rgba(255, 255, 255, 50); /* Фиолетовый цвет фона */\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 10px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 16px;\n"
"    margin: 4px 2px;\n"
"    cursor: pointer;\n"
"    border-radius: 4px; /* Закругленные углы */\n"
"}\n"
"")
        self.label_login.setObjectName("label_login")
        self.lineEdit_password_login = QtWidgets.QLineEdit(parent=authorization_form)
        self.lineEdit_password_login.setGeometry(QtCore.QRect(40, 150, 311, 51))
        self.lineEdit_password_login.setStyleSheet("QLineEdit\n"
" {\n"
"    background-color: rgba(255, 255, 255, 50); /* Фиолетовый цвет фона */\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 10px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 16px;\n"
"    margin: 4px 2px;\n"
"    cursor: pointer;\n"
"    border-radius: 4px; /* Закругленные углы */\n"
"}\n"
"")
        self.lineEdit_password_login.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_password_login.setText("")
        self.lineEdit_password_login.setObjectName("lineEdit_password_login")
        self.lineEdit_user_mail = QtWidgets.QLineEdit(parent=authorization_form)
        self.lineEdit_user_mail.setGeometry(QtCore.QRect(40, 80, 311, 51))
        self.lineEdit_user_mail.setStyleSheet("QLineEdit\n"
" {\n"
"    background-color: rgba(255, 255, 255, 50); /* Фиолетовый цвет фона */\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 10px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 16px;\n"
"    margin: 4px 2px;\n"
"    cursor: pointer;\n"
"    border-radius: 4px; /* Закругленные углы */\n"
"}\n"
"")
        self.lineEdit_user_mail.setText("")
        self.lineEdit_user_mail.setObjectName("lineEdit_user_mail")

        self.retranslateUi(authorization_form)
        QtCore.QMetaObject.connectSlotsByName(authorization_form)

    def retranslateUi(self, authorization_form):
        _translate = QtCore.QCoreApplication.translate
        authorization_form.setWindowTitle(_translate("authorization_form", "Авторизация"))
        self.loginButton.setText(_translate("authorization_form", "Войти"))
        self.registrationButton.setText(_translate("authorization_form", "Зарегистрироваться"))
        self.label_login.setText(_translate("authorization_form", "Вход в аккаунт"))
        self.lineEdit_password_login.setPlaceholderText(_translate("authorization_form", "Пароль:"))
        self.lineEdit_user_mail.setPlaceholderText(_translate("authorization_form", "Имя пользователя или почта:"))



