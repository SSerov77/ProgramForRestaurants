# подключение библиотек
import os
import sys
import sqlite3

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QMessageBox, QTableWidgetItem

from ui_py_files.UI_menu_win import Ui_Dialog

import main_window


class Menu(QDialog, Ui_Dialog):
    def __init__(self):
        try:
            super().__init__()
            self.setupUi(self)

            # Запрещенные символы
            self.bed_simbols = ['"', "'", '/', ';', ':', '&', '?', '!', '@', '#', '№', '$', '%', '^', '*', '(', ')',
                                '[',
                                ']', '{', '}', '>', '<', '`', '~', '-', '_', '+', '=']

            # Символы проверки на текст
            self.text_simbols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщъыьэюя' \
                                'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ~`!@#$%^&*()_+-=№:;></"'
            self.text_simbols2 = "'"
            self.modified = {}
            self.titles = None
            self.fname = ''

            # кнопки и функции
            self.back.clicked.connect(self.to_back)
            self.make_dish.clicked.connect(self.add_dish)
            self.make_photo.clicked.connect(self.add_photo)
            self.find.clicked.connect(self.to_find)
            self.tableWidget.itemClicked.connect(self.on_cell_item_clicked)
            self.tableWidget.itemChanged.connect(self.item_changed)

            # Подключение БД
            self.conn = sqlite3.connect('ProductDeliveries.sqlite')
            self.cur = self.conn.cursor()

            self.db()
        except Exception:
            QMessageBox.about(self, "Ошибка", "Произошла ошибка!")

    # Функция удаления
    def keyPressEvent(self, event):
        try:
            if event.key() == Qt.Key_Delete:  # проверка нажатия
                rows = list(set([i.row() for i in self.tableWidget.selectedItems()]))
                ids = [self.tableWidget.item(i, 0).text() for i in rows]  # получение выделенных id
                name = [self.tableWidget.item(i, 2).text() for i in rows]  # получение названия

                valid = QMessageBox.question(  # всплывающее окно с уточнением
                    self, '', "Вы действительно хотите удалить " + ",".join(name) + '?',
                    QMessageBox.Yes, QMessageBox.No)

                if valid == QMessageBox.Yes:  # Проверка ответа
                    self.cur.execute("DELETE FROM Menu WHERE id IN (" + ", ".join(
                        '?' * len(ids)) + ")", ids)
                    self.conn.commit()
                self.db()
        except Exception:
            QMessageBox.about(self, "Ошибка", "Произошла ошибка!")

    # Функция Загрузки БД в таблице окна
    def db(self):
        try:
            res = self.cur.execute('''SELECT * FROM Menu''').fetchall()  # получение данных из БД
            self.tableWidget.setColumnCount(6)

            for i in range(4):  # постороение таблицы
                self.tableWidget.setColumnWidth(i, 120)
            self.tableWidget.setHorizontalHeaderLabels(
                ['Номер', 'Тип', 'Название', 'Описание', 'Цена', 'Фото'])
            rowcount = self.cur.execute('''SELECT COUNT(*) FROM Menu''').fetchone()[0]

            self.db_res(res, rowcount)
        except Exception:
            QMessageBox.about(self, "Ошибка", "Произошла ошибка!")

    # Функция обновления отображаемых данных в таблице окна
    def db_res(self, result, rowcou):
        try:
            self.tableWidget.setRowCount(rowcou)
            tab = 0
            for row in result:
                self.tableWidget.setItem(tab, 0, QTableWidgetItem(str(row[0])))
                self.tableWidget.setItem(tab, 1, QTableWidgetItem(row[1]))
                self.tableWidget.setItem(tab, 2, QTableWidgetItem(row[2]))
                self.tableWidget.setItem(tab, 3, QTableWidgetItem(row[3]))
                self.tableWidget.setItem(tab, 4, QTableWidgetItem(row[4]))
                self.tableWidget.setItem(tab, 5, QTableWidgetItem(row[6]))

                tab += 1
        except Exception:
            QMessageBox.about(self, "Ошибка", "Произошла ошибка!")

    # Функция возврата в 'Главное меню'
    def to_back(self):
        try:
            self.open = main_window.Window()
            self.open.show()
            self.close()
        except Exception:
            QMessageBox.about(self, "Ошибка", "Произошла ошибка!")

    # Функция добавления фото
    def add_photo(self):
        try:
            self.fname = QFileDialog.getOpenFileName(
                self, 'Выбрать картинку', '',  # выбор картинки на ПК
                'Картинка (*.jpg);;Картинка (*.png);;Все файлы (*)')[0]
            self.pixmap = QPixmap(self.fname)
            self.pixmap = self.pixmap.scaled(200, 400, aspectRatioMode=1)
            self.label.setPixmap(self.pixmap)  # картику в label
        except Exception:
            QMessageBox.about(self, 'Ошибка', 'Произошла ошибка!')

    # Функция добавления
    def add_dish(self):
        try:
            view = self.view.text().lower().strip()  # Вид из введных данных
            view = view.capitalize()

            name = self.name.text().lower().strip()  # Имя из введеных данных
            name = name.capitalize()

            description = self.textEdit.toPlainText().strip()  # описание
            price = self.pricee.text().replace(',', '.').strip()  # цена из введеных данных

            # флаги проверки на условия
            main_flag = True
            digit_flag = True
            tot_flag = False

            # проверка введеных данных на коррекцию
            if view == '' or name == '' or description == '' or price == '':
                QMessageBox.about(self, "Ошибка", "Данные не заполнены или заполнены неверно")
                main_flag = False

            # проверка на запрещеннеы символы
            if main_flag:
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
                if digit_flag:
                    price = float(price)
                    price = f'{price:.2f}'
                    tot_flag = True
                else:
                    QMessageBox.about(self, "Ошибка", "Введены запрещенные символы!")

                if tot_flag:
                    if self.fname == '':
                        QMessageBox.about(self, 'Ошибка', 'Вы не добавили фото!')
                    else:
                        # Конвертируем данные
                        with open(self.fname, 'rb') as file:
                            blob_data = file.read()
                        np = self.fname.split('/')
                        name_photo = np[-1]
                        print(name_photo)
                        total = [str(view), str(name), str(description), str(price), blob_data, name_photo]
                        self.cur.execute("INSERT INTO Menu(type, name, description, price, photo, name_photo) "
                                         "VALUES(?, ?, ?, ?, ?, ?);", total)
                        self.conn.commit()
                        self.textEdit.setText('')
                        self.view.setText('')
                        self.name.setText('')
                        self.pricee.setText('')
                        self.label.setText('Фото блюда')
                    self.db()
        except Exception:
            QMessageBox.about(self, "Ошибка", "Произошла ошибка!")

    # Функция показывания фото
    def on_cell_item_clicked(self, item):
        try:
            res = self.cur.execute('''SELECT * FROM Menu''').fetchall()
            rows = list(set([i.row() for i in self.tableWidget.selectedItems()]))
            ids = [self.tableWidget.item(i, 0).text() for i in rows]

            # получение допа.
            for row in res:
                if str(row[0]) == str(ids[0]):
                    name = row[2]
                    photo = row[5]
                    photo_path = os.path.join("C:\YandexLuceym", name + ".jpg")
                    text = f"C:\YandexLuceym\{name}.jpg"
                    with open(photo_path, 'wb') as file:
                        file.write(photo)
                    self.pixmap = QPixmap(text)
                    self.pixmap = self.pixmap.scaled(200, 400, aspectRatioMode=1)
                    self.label.setPixmap(self.pixmap)
        except Exception:
            QMessageBox.about(self, "Ошибка", "Произошла ошибка!")

    # Функция редактирования ячеек таблицы
    def item_changed(self, item):
        try:
            tot = []
            self.pays = {}
            self.total = self.cur.execute(
                f'''SELECT id, type, name, description, price, name_photo FROM Menu''').fetchall()

            # получение данных из ячеек таюлицы
            self.titles = [description[0] for description in self.cur.description]
            for i in self.total:
                tot.append(i[0])
            tot.sort()
            for j in range(len(tot)):
                self.pays[j] = tot[j]
            self.modified[self.titles[item.column()]] = [item.text(), item.row()]

            #  обновление БД
            que = "UPDATE Menu SET\n"
            que += ", ".join([f"{key}='{self.modified.get(key)[0]}'"
                              for key in self.modified.keys()])
            que += f"WHERE id = {self.pays[[self.modified.get(key)[1] for key in self.modified.keys()][0]]}"

            self.cur.execute(que)
            self.conn.commit()
            self.modified.clear()
        except Exception:
            QMessageBox.about(self, "Ошибка", "Произошла ошибка!")

    # Функция поиска
    def to_find(self):
        try:
            text = self.lineEdit_5.text().lower().strip()  # введеные данные
            text = text.capitalize()

            # получение данных из БД
            result = self.cur.execute('''SELECT type FROM Menu''').fetchall()
            result_2 = self.cur.execute('''SELECT name FROM Menu''').fetchall()
            prod = []
            prod_2 = []

            for i in result:
                prod.append(i[0])
            for i in result_2:
                prod_2.append(i[0])

            if text in prod or text in prod_2 or text == '':  # проверка условий
                if text in prod or text == '':
                    if text != '':
                        res = self.cur.execute(f"SELECT * FROM Menu WHERE type='{text}'").fetchall()
                    else:
                        res = self.cur.execute(f"SELECT * FROM Menu").fetchall()

                    if text != '':
                        rowcount = self.cur.execute(f"SELECT COUNT(*) FROM Menu WHERE type='{text}'").fetchone()[0]
                    else:
                        rowcount = self.cur.execute(f"SELECT COUNT(*) FROM Menu").fetchone()[0]
                        print(rowcount)
                elif text in prod_2:
                    res = self.cur.execute(f"SELECT * FROM Menu WHERE name='{text}'").fetchall()
                    rowcount = self.cur.execute(f"SELECT COUNT(*) FROM Menu WHERE name='{text}'").fetchone()[0]
                self.db_res(res, rowcount)
            else:
                QMessageBox.about(self, "Ошибка", "Ничего не найдено!")
        except Exception:
            QMessageBox.about(self, "Ошибка", "Произошла ошибка!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Menu()
    ex.show()
    sys.exit(app.exec())
