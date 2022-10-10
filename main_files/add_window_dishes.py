# подключение библиотек
import sys
import sqlite3
import datetime as dt

from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox

from ui_py_files.UI_soldDish_win import Ui_Dialog


class AddWindow(QDialog, Ui_Dialog):
    def __init__(self):
        try:
            super().__init__()
            self.setupUi(self)
            # кнопки
            self.ok.clicked.connect(self.save)
            self.cancel.clicked.connect(self.not_save)

            # Запрещенные символы
            self.bed_simbols = ['"', "'", '/', ';', ':', '&', '?', '!', '@', '#', '№', '$', '%', '^', '*', '(', ')',
                                '[',
                                ']', '{', '}', '>', '<', '`', '~', '-', '_', '=', '+']

            # Символы проверки на текст
            self.text_simbols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщъыьэюя' \
                                'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ~`!@#$%^&*()_+-=№:;></"'
            self.text_simbols2 = "'"

            # Подключение БД
            self.conn = sqlite3.connect('ProductDeliveries.sqlite')
            self.cur = self.conn.cursor()
        except Exception:
            QMessageBox.about(self, "Ошибка", "Произошла ошибка!")

    # Функция добавления значений в БД
    def save(self):
        try:
            view = self.view.text().lower().strip()  # Вид из введных данных
            view = view.capitalize()

            name = self.name.text().lower().strip()  # Имя из введеных данных
            name = name.capitalize()

            kolvo = self.quantity.text().replace(',', '.').strip()  # количество из введеных данных
            price = self.pricee.text().replace(',', '.').strip()  # цена из введеных данных

            data = dt.datetime.now().date()  # получение даты с ПК

            # флаги для условий
            main_flag = True
            digit_flag = True
            tot_flag = False

            if view == '' or name == '' or kolvo == '' or price == '':  # проверка введеных данных
                QMessageBox.about(self, "Ошибка", "Данные не заполнены или заполнены неверно")
                main_flag = False

                # проверка на запрещенные символы
            if main_flag:
                for i in kolvo:
                    if i in self.text_simbols or i in self.text_simbols2:
                        digit_flag = False
                        break
                for i in price:
                    if i in self.text_simbols or i in self.text_simbols2:
                        digit_flag = False
                        break
                for i in name:
                    if i in self.bed_simbols:
                        digit_flag = False
                        break
                for i in view:
                    if i in self.bed_simbols:
                        digit_flag = False
                        break

                    # преобразование в другой тип данных
                if digit_flag:
                    price = float(price)
                    price = f'{price:.2f}'
                    kolvo = int(kolvo)
                    tot_flag = True
                else:
                    QMessageBox.about(self, "Ошибка", "Введены запрещенные символы!")

            # основная часть функции - добавление данных в БД
            if tot_flag:
                summ = float(kolvo) * float(price)
                summ = f'{summ:.2f}'
                tot = [str(kolvo), str(price), str(summ)]
                tot_2 = []
                for i in tot:
                    a = ''
                    for j in i:
                        if j == '.':
                            a += ','
                        else:
                            a += j
                    tot_2.append(a)
                total = (view, name, tot_2[0], tot_2[1], tot_2[2], data)
                self.cur.execute("INSERT INTO SoldDishes(type, name, quant, price, summ, date) "
                                 "VALUES(?, ?, ?, ?, ?, ?);", total)
                self.view.setText('')
                self.quantity.setText('')
                self.pricee.setText('')
                self.name.setText('')
                self.conn.commit()
                self.conn.close()
                self.close()
        except Exception:
            QMessageBox.about(self, "Ошибка", "Произошла ошибка!")

    # Функция закрытия окна
    def not_save(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AddWindow()
    ex.show()
    sys.exit(app.exec())
