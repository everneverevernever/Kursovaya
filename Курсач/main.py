from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QDialog
from PyQt6.QtSql import QSqlTableModel, QSqlQueryModel, QSqlQuery
from PyQt6.QtGui import QStandardItem, QStandardItemModel
from mainwindow import Ui_MainWindow
from database import Database
from clients_add_widget import Ui_clients_addWidget
from auntification import Ui_authorization_form
from registration import Ui_registration_form
from table_widget import  Ui_tablewidgetadd_form
from clients_change_widget import Ui_clients_ChangeWidget
from error_widget import Ui_error_widget
from widget_analysis import Ui_tablewidgetanalysis_form

class Auntification(QDialog, Ui_authorization_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.datab = Database()
        self.mainWindow = MainWindow()
        self.registration_widget = WidgetRegistration()
        self.error_widget1 = WidgetError()
        self.loginButton.clicked.connect(self.authenticate)
        self.registrationButton.clicked.connect(self.show_registration)
        self.registration_widget.push_registration.clicked.connect(self.registration)
        self.registration_widget.push_login.clicked.connect(self.show_auntification)
    def authenticate(self):
        username = self.lineEdit_user_mail.text()
        password = self.lineEdit_password_login.text()

        try:
            access_level = [item[0] for item in self.datab.query_login_check(username, password)]
            access_level = access_level[0]
            if access_level >= 2:

                self.openMainWindow(access_level)
                self.close()
                self.mainWindow.show()
            else:
                self.error_widget1.label_text_error.setText('Ваш уровень доступа слишком мал для\n'
                                                            'доступа к программе.\n'
                                                            'Дождитесь назначения вас модератором')
                self.error_widget1.show()
        except:
            self.error_widget1.label_text_error.setText('Неправильное имя пользователя или пароль')
            self.error_widget1.show()

    def show_registration(self):
        self.close()
        self.registration_widget.show()

    def show_auntification(self):
        self.registration_widget.close()
        self.show()
    def registration(self):

        self.username_reg = self.registration_widget.lineEdit_nameuser.text()
        self.data = [self.registration_widget.lineEdit_nameuser.text(),
                     self.registration_widget.lineEdit_fullname.text(),
                     self.registration_widget.lineEdit_mailregist.text(),
                     self.registration_widget.lineEdit_passwordregistr.text(), '1']

        try:
            access_level = [item[0] for item in self.datab.query_reg_check(self.username_reg)]
            access_level = access_level[0]
            if access_level:
                self.error_widget1.label_error.setText('Регистрация')
                self.error_widget1.label_text_error.setText('Этот пользователь уже существует, выберите другого')
                self.error_widget1.show()
        except:
            if self.registration_widget.lineEdit_nameuser.text() == '' or self.registration_widget.lineEdit_fullname.text() == '' or self.registration_widget.lineEdit_mailregist.text() == '' or self.registration_widget.lineEdit_passwordregistr.text() == '':
                self.error_widget1.label_error.setText('Регистрация')
                self.error_widget1.label_text_error.setText('Введите все поля для регистрации')
                self.error_widget1.show()
            else:
                self.mainWindow.view_data_TableView('Agreements')
                self.mainWindow.create_query('Staff', self.data)
                self.error_widget1.label_error.setText('Регистрация')
                self.error_widget1.label_text_error.setText('Успешная регистрация')
                self.error_widget1.show()
                self.show_auntification()



    def openMainWindow(self, access_level):
        self.mainWindow = MainWindow()

        if access_level == 3:
            self.mainWindow.show()
        else:
            print('Ваш уровень доступа слишком мал для этой программы')



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.id = None
        self.setupUi(self)
        self.setWindowTitle("Главное окно")
        self.datab = Database()

        self.analysis_widget = WidgetAnalysis()
        self.error_widget = WidgetError()
        self.clients_add_widget = WidgetAddDataTable()
        self.clients_change_widget = WidgetChangeDataTable()


        self.table_name = 'Clients'


        self.pushButton_analysis.clicked.connect(self.openWidgetAnalysisTable)
        self.pushButton_table.clicked.connect(self.openWidgetAddTable)
        self.tableView.clicked.connect(self.set_col)
        self.pushButton_add_table.clicked.connect(self.openWidgetAddDataTable)


        self.pyshbutton_info.clicked.connect(self.msg_info)

        self.pushButton_delete_table.clicked.connect(self.del_column)

        self.clients_add_widget.push_add_saveClient.clicked.connect(self.insertDataTable)

        self.analysis_widget.push_clients_tarifs.clicked.connect(self.analys_tarif)
        self.analysis_widget.push_med_balance.clicked.connect(self.average_balance)
        self.analysis_widget.push_all_agreements.clicked.connect(self.count_agreements)
    def openWidgetAddTable(self):
        self.widget_add_table = WidgetAddTable()
        self.widget_add_table.push_clients.clicked.connect(lambda: self.view_data_TableView('Clients'))
        self.widget_add_table.push_serviceTypes.clicked.connect(lambda: self.view_data_TableView('ServiceTypes'))
        self.widget_add_table.push_services.clicked.connect(lambda: self.view_data_TableView('Services'))
        self.widget_add_table.pusg_agreements.clicked.connect(lambda: self.view_data_TableView('Agreements'))
        self.widget_add_table.push_staff.clicked.connect(lambda: self.view_data_TableView('Staff'))
        self.widget_add_table.show()

    def standart_widget(self):
        self.clients_add_widget.lineEdit_NumberDogovor.setPlaceholderText('Номер договора')
        self.clients_add_widget.lineEdit_FullName.setPlaceholderText('ФИО')
        self.clients_add_widget.lineEdit_Balance.setPlaceholderText('Баланс')
        self.clients_add_widget.lineEdit_PhoneNumber.setPlaceholderText('Номер телефона')
        self.clients_add_widget.lineEdit_Email.setPlaceholderText('Электронная почта')
        self.clients_add_widget.lineEdit_Address.setPlaceholderText('Адрес')
        self.clients_add_widget.lineEdit_FullName.show()
        self.clients_add_widget.lineEdit_Balance.show()
        self.clients_add_widget.lineEdit_PhoneNumber.show()
        self.clients_add_widget.lineEdit_Email.show()
        self.clients_add_widget.lineEdit_Address.show()

    def msg_info(self):
        self.error_widget.setWindowTitle('Информация')
        self.error_widget.label_error.setText('Информация')
        self.error_widget.label_text_error.setText('Чтобы удалить колонку выберите id')
        self.error_widget.show()

    def openWidgetAddDataTable(self):
        if self.table_name == 'Clients':
            self.standart_widget()
        elif self.table_name == 'ServiceTypes':
            self.standart_widget()
            self.clients_add_widget.lineEdit_NumberDogovor.setPlaceholderText('Тип сервиса')
            self.clients_add_widget.lineEdit_FullName.hide()
            self.clients_add_widget.lineEdit_Balance.hide()
            self.clients_add_widget.lineEdit_PhoneNumber.hide()
            self.clients_add_widget.lineEdit_Email.hide()
            self.clients_add_widget.lineEdit_Address.hide()
        elif self.table_name == 'Services':
            self.standart_widget()
            self.clients_add_widget.lineEdit_NumberDogovor.setPlaceholderText('ID_Тип_сервиса')
            self.clients_add_widget.lineEdit_FullName.setPlaceholderText('Описание')
            self.clients_add_widget.lineEdit_Balance.setPlaceholderText('Цена')
            self.clients_add_widget.lineEdit_FullName.show()
            self.clients_add_widget.lineEdit_Balance.show()
            self.clients_add_widget.lineEdit_PhoneNumber.hide()
            self.clients_add_widget.lineEdit_Email.hide()
            self.clients_add_widget.lineEdit_Address.hide()
        elif self.table_name == 'Agreements':
            self.standart_widget()
            self.clients_add_widget.lineEdit_NumberDogovor.setPlaceholderText('ID_Клиента')
            self.clients_add_widget.lineEdit_FullName.setPlaceholderText('ID_Сервиса')
            self.clients_add_widget.lineEdit_Balance.setPlaceholderText('Дата_договора')
            self.clients_add_widget.lineEdit_FullName.show()
            self.clients_add_widget.lineEdit_Balance.show()
            self.clients_add_widget.lineEdit_PhoneNumber.hide()
            self.clients_add_widget.lineEdit_Email.hide()
            self.clients_add_widget.lineEdit_Address.hide()
        elif self.table_name == 'Staff':
            self.standart_widget()
            self.clients_add_widget.lineEdit_NumberDogovor.setPlaceholderText('Имя пользователя')
            self.clients_add_widget.lineEdit_FullName.setPlaceholderText('ФИО')
            self.clients_add_widget.lineEdit_Balance.setPlaceholderText('Почта')
            self.clients_add_widget.lineEdit_PhoneNumber.setPlaceholderText('Пароль')
            self.clients_add_widget.lineEdit_Email.setPlaceholderText('Уровень доступа')
            self.clients_add_widget.lineEdit_Address.hide()

        self.clients_add_widget.show()

    def openWidgetChangeDataTable(self):
        self.clients_change_widget.show()

    def openWidgetAnalysisTable(self):
        self.analysis_widget.show()
    def insertDataTable(self):
        if self.table_name == 'Clients':
            self.data_input = [self.clients_add_widget.lineEdit_NumberDogovor.text(),
                               self.clients_add_widget.lineEdit_FullName.text(),
                               self.clients_add_widget.lineEdit_Balance.text(),
                               self.clients_add_widget.lineEdit_PhoneNumber.text(),
                               self.clients_add_widget.lineEdit_Email.text(),
                               self.clients_add_widget.lineEdit_Address.text()]
        elif self.table_name == 'ServiceTypes':
            self.data_input = [self.clients_add_widget.lineEdit_NumberDogovor.text()]

        elif self.table_name == 'Services':
            self.data_input = [self.clients_add_widget.lineEdit_NumberDogovor.text(),
                               self.clients_add_widget.lineEdit_FullName.text(),
                               self.clients_add_widget.lineEdit_Balance.text()]

        elif self.table_name == 'Agreements':
            self.data_input = [self.clients_add_widget.lineEdit_NumberDogovor.text(),
                               self.clients_add_widget.lineEdit_FullName.text(),
                               self.clients_add_widget.lineEdit_Balance.text()]
        elif self.table_name == 'Staff':
            self.data_input = [self.clients_add_widget.lineEdit_NumberDogovor.text(),
                               self.clients_add_widget.lineEdit_FullName.text(),
                               self.clients_add_widget.lineEdit_Balance.text(),
                               self.clients_add_widget.lineEdit_PhoneNumber.text(),
                               self.clients_add_widget.lineEdit_Email.text()]
        self.create_query(self.table_name, self.data_input)

    def set_col(self):

        selected_indexes = self.tableView.selectedIndexes()
        ind = self.tableView.selectedIndexes()[0]
        for index in selected_indexes:
            self.column = index.column()
        if self.column == 0:
            self.id = str(self.tableView.model().data(ind))
            if self.id == 'None':
                self.id = ''
        


    def average_balance(self):
        try:
            self.view_data_TableView('Agreements')
            model = QStandardItemModel()

            # Устанавливаем заголовки столбцов
            model.setHorizontalHeaderLabels(["Средний баланс клиентов"])

            query = QSqlQuery()
            query.exec("SELECT AVG(balance) FROM Clients")

            if query.next():
                average_balance = query.value(0)
                print("Average Balance:", average_balance)

                # Создаем новый объект QStandardItem
                average_balance_item = QStandardItem(str(average_balance))

                model.appendRow([average_balance_item])
                # Устанавливаем модель данных для QTableView
                self.tableView.setModel(model)
                self.analysis_widget.close()
        except Exception as e:
            print(e)

    def count_agreements(self):
        try:
            self.view_data_TableView('Agreements')
            model = QStandardItemModel()

            # Устанавливаем заголовки столбцов
            model.setHorizontalHeaderLabels(["Количество договоров"])

            query = QSqlQuery()
            query.exec("SELECT COUNT(*) FROM Agreements")

            if query.next():
                agreements_count = query.value(0)
                print("Количество договоров:", agreements_count)

                # Создаем новый объект QStandardItem
                agreements_count_item = QStandardItem(str(agreements_count))

                model.appendRow([agreements_count_item])
                # Устанавливаем модель данных для QTableView
                self.tableView.setModel(model)
                self.analysis_widget.close()

        except Exception as e:
            print(e)

    def analys_tarif(self):
        try:
            self.view_data_TableView('Agreements')
            model = QStandardItemModel()
            # Устанавливаем заголовки столбцов
            model.setHorizontalHeaderLabels(["Тарифы", "Количество клиентов"])

            self.item1 = 'Телевидение'
            self.item2 = '3'
            query = QSqlQuery()
            query.exec("SELECT COUNT(*) FROM Agreements WHERE service_id = 1")
            while query.next():
                result = query.value(0)
                self.item2 = str(result)

            print("Result:", self.item2)
            self.item3 = 'Интернет'
            self.item4 = '4'
            query = QSqlQuery()
            query.exec("SELECT COUNT(*) FROM Agreements WHERE service_id = 2")

            while query.next():
                result = query.value(0)
                self.item4 = str(result)

            self.item5 = 'Телефония'
            self.item6 = '5'
            query = QSqlQuery()
            query.exec("SELECT COUNT(*) FROM Agreements WHERE service_id = 3")

            while query.next():
                result = query.value(0)
                self.item6 = str(result)

            # Создаем новые объекты QStandardItem для каждого элемента
            item1 = QStandardItem(self.item1)
            item2 = QStandardItem(self.item2)
            item3 = QStandardItem(self.item3)
            item4 = QStandardItem(self.item4)
            item5 = QStandardItem(self.item5)
            item6 = QStandardItem(self.item6)

            model.appendRow([item1, item2])
            model.appendRow([item3, item4])
            model.appendRow([item5, item6])
            # Устанавливаем модель данных для QTableView
            self.tableView.setModel(model)
            self.analysis_widget.close()
        except Exception as e:
            print('ворк')

    def test(self):
        self.create_query(self.table_name, self.data_input)

    def create_query(self, table_name, data):
        try:
            self.table_name = table_name
            self.data = data
            query = QSqlQuery()

            columns_query = f"PRAGMA table_info({self.table_name})"
            query.exec(columns_query)
            columns = []
            while query.next():
                column_name = query.value(1)
                columns.append(column_name)
            columns = columns[1:]
            print(columns)
            # Создание запроса на добавление данных
            insert_query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(['{}'.format('?') for column in range(len(columns))])})"
            print(insert_query)

            # Привязка данных к параметрам запроса
            query.prepare(insert_query)
            for value in self.data:
                print(value)
                query.addBindValue(value)

            # Выполнение запроса
            if query.exec():
                print("Данные успешно добавлены.")
            else:
                print("Ошибка при добавлении данных:", query.lastError().text())
            self.view_data_TableView(self.table_name)
            self.clients_add_widget.close()
            self.clear_add_widget()

        except Exception as e:
            print(e)

    def clear_add_widget(self):
        self.clients_add_widget.lineEdit_NumberDogovor.clear()
        self.clients_add_widget.lineEdit_FullName.clear()
        self.clients_add_widget.lineEdit_Balance.clear()
        self.clients_add_widget.lineEdit_PhoneNumber.clear()
        self.clients_add_widget.lineEdit_Email.clear()
        self.clients_add_widget.lineEdit_Address.clear()

    def add_new_column(self, data):
        query = QSqlQuery()
        self.data = data
        # Генерация id
        id = self.datab.incr(self.table_name)
        print(id)
        # Подготовка запроса
        query.prepare(
            f"INSERT INTO {self.table_name} (id, contract_number, full_name, balance, phone_number, email, address) VALUES (?, ?, ?, ?, ?, ?, ?)")
        # Установка значения параметра
        query.addBindValue(id)
        for value in self.data:
            print(value)
            query.addBindValue(value)
        # Выполнение запроса
        if not query.exec():
            print("Ошибка выполнения запроса")
            return
        self.view_data_TableView(self.table_name)
        print("Данные добавлены в базу данных")
        self.clients_add_widget.close()

    def del_column(self):
        query = QSqlQuery()
    # Подготовка запроса
        query.prepare(
            f'DELETE FROM {self.table_name} WHERE id = {self.id}')
        if not query.exec():
            self.id = ''
            self.error_widget.label_error.setText('Ошибка!')
            self.error_widget.label_text_error.setText('Ошибка, выберите ID')
            self.error_widget.show()
        self.view_data_TableView(self.table_name)
        self.id = ''

    def view_data_TableView(self, table_name):
        try:
            # Создание модели данных
            self.table_name = table_name
            model = QSqlTableModel()
            model.setTable(self.table_name)
            model.select()
            # Создание таблицы и установка модели данных
            self.widget_add_table.close()
            self.tableView.setModel(model)
        except Exception as e:
            if e == "'MainWindow' object has no attribute 'widget_add_table'":
                print(e)
            else:
                print('')



class WidgetRegistration(QDialog, Ui_registration_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class WidgetAddTable(QDialog, Ui_tablewidgetadd_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setModal(True)

class WidgetAnalysis(QDialog, Ui_tablewidgetanalysis_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class WidgetAddDataTable(QDialog, Ui_clients_addWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setModal(True)

class WidgetChangeDataTable(QDialog, Ui_clients_ChangeWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setModal(True)

class WidgetError(QDialog, Ui_error_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setModal(True)

def main():
    app = QApplication([])
    window = Auntification()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
