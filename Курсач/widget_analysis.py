# Form implementation generated from reading ui file 'widget_analysis.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_tablewidgetanalysis_form(object):
    def setupUi(self, tablewidgetanalysis_form):
        tablewidgetanalysis_form.setObjectName("tablewidgetanalysis_form")
        tablewidgetanalysis_form.resize(380, 310)
        tablewidgetanalysis_form.setAccessibleName("")
        tablewidgetanalysis_form.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        tablewidgetanalysis_form.setStyleSheet("QWidget\n"
" {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"                                stop:0 rgb(148, 87, 235), stop:1 rgb(87, 37, 138));\n"
"}")
        self.label_tables = QtWidgets.QLabel(parent=tablewidgetanalysis_form)
        self.label_tables.setGeometry(QtCore.QRect(140, 0, 101, 51))
        self.label_tables.setStyleSheet("QLabel\n"
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
        self.label_tables.setObjectName("label_tables")
        self.push_all_agreements = QtWidgets.QPushButton(parent=tablewidgetanalysis_form)
        self.push_all_agreements.setGeometry(QtCore.QRect(0, 160, 381, 50))
        self.push_all_agreements.setStyleSheet("/* Стиль для QPushButton */\n"
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
        self.push_all_agreements.setObjectName("push_all_agreements")
        self.push_med_balance = QtWidgets.QPushButton(parent=tablewidgetanalysis_form)
        self.push_med_balance.setGeometry(QtCore.QRect(0, 110, 381, 50))
        self.push_med_balance.setStyleSheet("/* Стиль для QPushButton */\n"
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
        self.push_med_balance.setObjectName("push_med_balance")
        self.push_clients_tarifs = QtWidgets.QPushButton(parent=tablewidgetanalysis_form)
        self.push_clients_tarifs.setGeometry(QtCore.QRect(0, 60, 381, 51))
        self.push_clients_tarifs.setStyleSheet("/* Стиль для QPushButton */\n"
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
        self.push_clients_tarifs.setObjectName("push_clients_tarifs")

        self.retranslateUi(tablewidgetanalysis_form)
        QtCore.QMetaObject.connectSlotsByName(tablewidgetanalysis_form)

    def retranslateUi(self, tablewidgetanalysis_form):
        _translate = QtCore.QCoreApplication.translate
        tablewidgetanalysis_form.setWindowTitle(_translate("tablewidgetanalysis_form", "Анализ"))
        self.label_tables.setText(_translate("tablewidgetanalysis_form", "Анализ"))
        self.push_all_agreements.setText(_translate("tablewidgetanalysis_form", "Количество всех договоров"))
        self.push_med_balance.setText(_translate("tablewidgetanalysis_form", "Средний баланс всех пользователей"))
        self.push_clients_tarifs.setText(_translate("tablewidgetanalysis_form", "Количество клиентов определенного тарифа"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tablewidgetanalysis_form = QtWidgets.QWidget()
    ui = Ui_tablewidgetanalysis_form()
    ui.setupUi(tablewidgetanalysis_form)
    tablewidgetanalysis_form.show()
    sys.exit(app.exec())
