from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from PyQt6.QtGui import QStandardItem, QStandardItemModel
import sqlite3 as sql


class Database:
    def __init__(self):
        super(Database, self).__init__()
        self.create_connection()

    def create_connection(self):
        self.model = QStandardItemModel()
        db_view = QSqlDatabase.addDatabase('QSQLITE')
        db_view.setDatabaseName('telecom_database.db')
        self.db = sql.connect('telecom_database.db')
        self.cursor = self.db.cursor()

    def execute_query_with_params(self, sql_query, values_query=None):
        try:
            if values_query is not None:
                self.cursor.execute(sql_query, values_query)
            else:
                self.cursor.execute(sql_query)
            self.db.commit()
        except Exception as e:
            print(f"Ошибка при выполнении запроса: {e}")

    def query_login_check(self, username, password):
        sql_query = '''SELECT access_level FROM Staff WHERE username=? AND password=?'''
        self.execute_query_with_params(sql_query, [username, password])
        data = self.cursor.fetchall()
        return data

    def query_reg_check(self, username):
        sql_query = '''SELECT access_level FROM Staff WHERE username=?'''
        self.execute_query_with_params(sql_query, [username])
        data = self.cursor.fetchall()
        return data

    def data_from_db(self, table_name):
        self.cursor.execute("SELECT * FROM table_name")
        rows = self.cursor.fetchall()
    def query_add_new_column(self, id, name, surname, patronymic, login, password, position, date_birth, phone):
        sql_query = '''INSERT INTO workers (ID, Имя, Фамилия, Отчество, Логин, Пароль, Должность, Дата, 
                    Номер) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);'''

        self.execute_query_with_params(sql_query, [id, name, surname, patronymic, login, password, position, date_birth, phone])

    def query_update_column(self, id, name, surname, patronymic, login, password, position, date_birth, phone):
        sql_query = '''UPDATE workers SET Имя=?, Фамилия=?, Отчество=?, Логин=?, Пароль=?, Должность=?, Дата=?, 
        Номер=? WHERE ID=?;'''
        self.execute_query_with_params(sql_query, [name, surname, patronymic, login, password, position, date_birth, phone, id])

    def query_delete_column(self, id):
        sql_query = 'DELETE FROM workers WHERE ID=?'
        self.execute_query_with_params(sql_query, [id])

    def query_entry(self, login, password, position):
        sql_query = 'SELECT Логин, Пароль, Должность FROM workers where Логин = ? and Пароль = ? and Должность=?'
        self.execute_query_with_params(sql_query, [login, password, position])
        data = self.cursor.fetchall()
        return data

    def query_search_column(self, id):
        sql_query = '''SELECT ID, Имя, Фамилия, Отчество, Логин, Пароль, Должность, Дата, 
                    Номер FROM workers WHERE ID=?'''
        self.execute_query_with_params(sql_query, [id])
        data = self.cursor.fetchall()
        for row in data:
            items = [QStandardItem(str(item)) for item in row]
            self.model.appendRow(items)


    def query_data_view(self):

        sql_query = 'SELECT * FROM workers'
        self.execute_query_with_params(sql_query)
        data = self.cursor.fetchall()
        for row in data:
            items = [QStandardItem(str(item)) for item in row]
            self.model.appendRow(items)

    def update_id(self, id):
        sql_query = '''UPDATE workers SET id = id - 1 WHERE id > ?;'''
        self.execute_query_with_params(sql_query, [id])

    def incr(self, table_name):
        self.execute_query_with_params(f'SELECT MAX(id) FROM {table_name}')
        data = self.cursor.fetchone()[0]
        incr_id = 1 if data == None else data + 1
        return incr_id