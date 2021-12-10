import sys
import sqlite3
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5 import uic


class Progr(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect('coffee.sqlite')
        self.pushButton.clicked.connect(self.load)
        self.load()

    def load(self):
        res = self.con.cursor().execute("""SELECT 
                                            id,
                                            name,
                                            roast,
                                            look,
                                            taste,
                                            price,
                                            volume
                                            from coffeeinfo""").fetchall()
        self.tableWidget.setColumnCount(len(res[0]))
        self.tableWidget.setHorizontalHeaderLabels(
            ['id', 'Сорт', 'Обжарка', 'Вид', 'Вкус', 'Цена, руб.', 'Упаковка, г'])
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))
        self.tableWidget.resizeColumnsToContents()

    def closeEvent(self, event):
        self.con.close()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Progr()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
