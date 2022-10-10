# подключение библиотек
import sys

from ui_py_files.UI_main_win import Ui_MainWindow
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox

# подключение файлов
from main_files import product_deliveris
from main_files import sold_dishes
from main_files import menu_window


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        try:
            super().__init__()
            self.setupUi(self)

            # кнопки
            self.pushButton.clicked.connect(self.products_window)
            self.pushButton_3.clicked.connect(self.dishes_window)
            self.pushButton_2.clicked.connect(self.menu_window)
        except Exception:
             QMessageBox.about(self, "Ошибка", "Произошла ошибка!")

    # кнопка перехода к окну 'закупка продуктов'
    def products_window(self):
        try:
            self.open = product_deliveris.SecondWindow()
            self.open.show()
            self.close()
        except Exception:
            QMessageBox.about(self, "Ошибка", "Произошла ошибка!")

    # кнопка перехода к окну 'проданные блюда'
    def dishes_window(self):
        try:
            self.open = sold_dishes.ThirdWindow()
            self.open.show()
            self.close()
        except Exception:
            QMessageBox.about(self, "Ошибка", "Произошла ошибка!")

    # кнопка перехода к окну 'меню заведения'
    def menu_window(self):
        try:
            self.open = menu_window.Menu()
            self.open.show()
            self.close()
        except Exception:
            QMessageBox.about(self, "Ошибка", "Произошла ошибка!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())
