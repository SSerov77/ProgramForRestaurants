# подключение библиотек
import csv
import sys
import sqlite3

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidgetItem, QMessageBox

# подключение файлов
from ui_py_files.UI_prod_win import Ui_Dialog
import main_window
from main_files import add_window_products


class SecondWindow(QDialog, Ui_Dialog):
    def __init__(self):
        try:
            super().__init__()
            self.setupUi(self)
            # кнопки
            self.find.clicked.connect(self.to_find)
            self.apend.clicked.connect(self.to_append)
            self.back.clicked.connect(self.to_back)
            self.upload.clicked.connect(self.to_upload)
            self.upload.setStyleSheet("background-color: #30AB0D")
            self.tableWidget.itemChanged.connect(self.item_changed)

            # Запрещенные символы
            self.bed_simbols = ['"', "'", '/', ';', ':', '&', '?', '!', '@', '#', '№', '$', '%', '^', '*', '(', ')',
                                '[',
                                ']', '{', '}', '>', '<', '`', '~']

            # Символы проверки на текст
            self.text_simbols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщъыьэюя' \
                                'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ~`!@#$%^&*()_+-=№:;></"'
            self.text_simbols2 = "'"
            self.modified = {}
            self.titles = None
            # Подключение БД
            self.conn = sqlite3.connect('ProductDeliveries.sqlite')
            self.cur = self.conn.cursor()

            self.db()
        except Exception:
            QMessageBox.about(self, "Ошибка", "Произошла ошибка!")

        # Функция Загрузки БД в таблице окна

    def db(self):
        try:
            res = self.cur.execute('''SELECT * FROM Products''').fetchall()
            self.tableWidget.setColumnCount(7)

            for i in range(6):
                self.tableWidget.setColumnWidth(i, 160)  # постороения таблицы
            self.tableWidget.setHorizontalHeaderLabels(
                ['Номер', 'Вид', 'Название', 'Количество', 'Цена', 'Сумма', 'Дата'])
            rowcount = self.cur.execute('''SELECT COUNT(*) FROM Products''').fetchone()[0]

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
                self.tableWidget.setItem(tab, 5, QTableWidgetItem(row[5]))
                self.tableWidget.setItem(tab, 6, QTableWidgetItem(row[6]))
                tab += 1
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
                    self.cur.execute("DELETE FROM Products WHERE id IN (" + ", ".join(
                        '?' * len(ids)) + ")", ids)
                    self.conn.commit()
                self.db()
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

    # Функция поиска
    def to_find(self):
        try:
            text = self.line_find.text().lower().strip()  # введёный текст
            text = text.capitalize()

            # запросы с БД
            result = self.cur.execute('''SELECT view FROM Products''').fetchall()
            result_2 = self.cur.execute('''SELECT name FROM Products''').fetchall()
            prod = []
            prod_2 = []

            # обработка полученных данных
            for i in result:
                prod.append(i[0])
            for i in result_2:
                prod_2.append(i[0])

                # основная часть функции - поиск
            if text in prod or text in prod_2 or text == '':
                if text in prod or text == '':
                    if text != '':
                        res = self.cur.execute(f"SELECT * FROM Products WHERE view='{text}'").fetchall()
                    else:
                        res = self.cur.execute(f"SELECT * FROM Products").fetchall()

                    if text != '':
                        rowcount = self.cur.execute(f"SELECT COUNT(*) FROM Products WHERE view='{text}'").fetchone()[0]
                    else:

                        rowcount = self.cur.execute(f"SELECT COUNT(*) FROM Products").fetchone()[0]
                elif text in prod_2:
                    res = self.cur.execute(f"SELECT * FROM Products WHERE name='{text}'").fetchall()
                    rowcount = self.cur.execute(f"SELECT COUNT(*) FROM Products WHERE name='{text}'").fetchone()[0]
                self.db_res(res, rowcount)
            else:
                QMessageBox.about(self, "Ошибка", "Ничего не найдено!")
        except Exception:
            QMessageBox.about(self, "Ошибка", "Произошла ошибка!")

    # Функция добавления
    def to_append(self):
        try:
            self.open = add_window_products.AddWindow()
            self.open.show()
        except Exception:
            QMessageBox.about(self, "Ошибка", "Произошла ошибка!")

    # Функция выгрузки данных таблицы в Excel-файл
    def to_upload(self):
        try:
            with open('ProductDeliveries.csv', 'w', newline='') as csvfile:
                writer = csv.writer(
                    csvfile, delimiter=';', quotechar='"',
                    quoting=csv.QUOTE_MINIMAL)
                # Получение списка заголовков
                writer.writerow(
                    [self.tableWidget.horizontalHeaderItem(i).text()
                     for i in range(1, self.tableWidget.columnCount())])
                for i in range(self.tableWidget.rowCount()):
                    row = []
                    for j in range(1, self.tableWidget.columnCount()):
                        item = self.tableWidget.item(i, j)
                        if item is not None:
                            row.append(item.text())
                    writer.writerow(row)
        except Exception:
            QMessageBox.about(self, "Ошибка", "Произошла ошибка!")

    # # Функция редактирования ячеек таблицы
    def item_changed(self, item):
        try:
            tot = []
            self.pays = {}
            self.total = self.cur.execute(f'''SELECT * FROM Products''').fetchall()

            # получение данных в ячейках
            self.titles = [description[0] for description in self.cur.description]
            for i in self.total:
                tot.append(i[0])
            tot.sort()
            for j in range(len(tot)):
                self.pays[j] = tot[j]
            self.modified[self.titles[item.column()]] = [item.text(), item.row()]

            # обновление БД
            que = "UPDATE Products SET\n"
            que += ", ".join([f"{key}='{self.modified.get(key)[0]}'"
                              for key in self.modified.keys()])
            que += f"WHERE id = {self.pays[[self.modified.get(key)[1] for key in self.modified.keys()][0]]}"

            self.cur.execute(que)
            self.conn.commit()
            self.modified.clear()
        except Exception:
            QMessageBox.about(self, "Ошибка", "Произошла ошибка!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SecondWindow()
    ex.show()
    sys.exit(app.exec())
