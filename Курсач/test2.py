from PyQt6.QtWidgets import QApplication, QMainWindow, QTableView, QVBoxLayout, QWidget, QLineEdit, QLabel, QFormLayout, QPushButton
from PyQt6.QtGui import QStandardItemModel
from PyQt6.QtCore import Qt

class CustomWidget(QWidget):
    def __init__(self, column_names):
        super().__init__()

        layout = QFormLayout()
        self.line_edits = []

        for column_name in column_names:
            label = QLabel(column_name)
            line_edit = QLineEdit()
            self.line_edits.append(line_edit)

            layout.addRow(label, line_edit)

        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Создаем QStandardItemModel и QTableView (замените на свои объекты)
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["Column 1", "Column 2", "Column 3"])
        table_view = QTableView()
        table_view.setModel(model)

        # Получаем названия колонок из модели данных
        column_names = [model.headerData(i, Qt.Orientation.Horizontal, role=Qt.ItemDataRole.DisplayRole) for i in range(model.columnCount())]

        # Создаем CustomWidget с названиями колонок и полями ввода
        self.custom_widget = CustomWidget(column_names)

        # Добавляем QTableView и CustomWidget в главное окно
        central_widget = QWidget()
        layout = QVBoxLayout()

        # Создаем кнопку для отображения CustomWidget
        show_custom_widget_button = QPushButton("Show Custom Widget")
        show_custom_widget_button.clicked.connect(self.show_custom_widget)

        layout.addWidget(table_view)
        layout.addWidget(show_custom_widget_button)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def show_custom_widget(self):
        self.custom_widget.show()

if __name__ == "__main__":
    app = QApplication([])

    main_window = MainWindow()
    main_window.show()

    app.exec()
