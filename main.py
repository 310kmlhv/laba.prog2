from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton, QMessageBox, QMenuBar, QMenu
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction

# Функции конвертации для различных физических величин
def convert_length(value, from_unit, to_unit):
    length_units = {'meters': 1, 'kilometers': 0.001, 'centimeters': 100, 'millimeters': 1000}
    try:
        result = float(value) * (length_units[to_unit] / length_units[from_unit])
        return result
    except KeyError:
        raise ValueError("Invalid units")

def convert_mass(value, from_unit, to_unit):
    mass_units = {'grams': 1, 'kilograms': 0.001, 'milligrams': 1000}
    try:
        result = float(value) * (mass_units[to_unit] / mass_units[from_unit])
        return result
    except KeyError:
        raise ValueError("Invalid units")

def convert_temperature(value, from_unit, to_unit):
    try:
        value = float(value)
        if from_unit == 'Celsius' and to_unit == 'Fahrenheit':
            return (value * 9/5) + 32
        elif from_unit == 'Fahrenheit' and to_unit == 'Celsius':
            return (value - 32) * 5/9
        elif from_unit == 'Celsius' and to_unit == 'Kelvin':
            return value + 273.15
        elif from_unit == 'Kelvin' and to_unit == 'Celsius':
            return value - 273.15
        else:
            raise ValueError("Invalid temperature conversion")
    except ValueError:
        raise ValueError("Invalid temperature value")

class UnitConverterApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Конвертер единиц")
        self.setGeometry(300, 200, 400, 300)  # Устанавливаем начальный размер окна

        # Главное меню
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("Меню")
        exit_action = QAction("Выход", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Основной виджет
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Основной вертикальный layout
        layout = QVBoxLayout()

        # Метка и поле для ввода значения
        self.label_value = QLabel("Введите значение:")
        layout.addWidget(self.label_value)

        self.entry_value = QLineEdit()
        layout.addWidget(self.entry_value)

        # Метка и выпадающий список для единицы измерения (из)
        self.label_from = QLabel("Из единицы:")
        layout.addWidget(self.label_from)

        self.from_unit = QComboBox()
        self.from_unit.addItems(["meters", "kilometers", "centimeters", "millimeters", "grams", "kilograms", "milligrams", "Celsius", "Fahrenheit", "Kelvin"])
        layout.addWidget(self.from_unit)

        # Метка и выпадающий список для единицы измерения (в)
        self.label_to = QLabel("В единицу:")
        layout.addWidget(self.label_to)

        self.to_unit = QComboBox()
        self.to_unit.addItems(["meters", "kilometers", "centimeters", "millimeters", "grams", "kilograms", "milligrams", "Celsius", "Fahrenheit", "Kelvin"])
        layout.addWidget(self.to_unit)

        # Кнопка для конвертации
        self.convert_button = QPushButton("Конвертировать")
        self.convert_button.clicked.connect(self.convert)
        layout.addWidget(self.convert_button)

        # Метка для вывода результата
        self.result_label = QLabel("")
        layout.addWidget(self.result_label)

        # Устанавливаем layout в центральный виджет
        central_widget.setLayout(layout)

    def convert(self):
        try:
            value = self.entry_value.text()
            from_unit = self.from_unit.currentText()
            to_unit = self.to_unit.currentText()

            # Проверяем тип измерений (длина, масса, температура)
            if from_unit in ["meters", "kilometers", "centimeters", "millimeters"]:
                result = convert_length(value, from_unit, to_unit)
            elif from_unit in ["grams", "kilograms", "milligrams"]:
                result = convert_mass(value, from_unit, to_unit)
            else:
                result = convert_temperature(value, from_unit, to_unit)

            self.result_label.setText(f"Результат: {result:.2f}")

        except ValueError as e:
            QMessageBox.critical(self, "Ошибка", f"Произошла ошибка: {e}")

# Основная часть программы
if __name__ == "__main__":
    app = QApplication([])

    window = UnitConverterApp()
    window.show()

    app.exec()
