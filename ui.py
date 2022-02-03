import sys
import ui_pyqt
import os
from PyQt5 import QtWidgets
import shutil
import tkinter as tk
from tkinter import filedialog
from commands import install_, build_, remove_layer_, add_layer_, add_file_, remove_file_, select_mode_, change_rarity


class doctors_nft(QtWidgets.QMainWindow, ui_pyqt.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.layer_name = ''

        self.enter.clicked.connect(self.get_text)

        self.build.clicked.connect(build_)
        self.install.clicked.connect(install_)

        self.remove_layer.clicked.connect(remove_layer_)
        self.add_layer.clicked.connect(lambda: add_layer_(self.layer_name))

        self.add_image.clicked.connect(add_file_)
        self.remove_image.clicked.connect(remove_file_)

        self.add_mode.clicked.connect(select_mode_)

    def get_text(self):
        self.layer_name = self.enter_text.toPlainText()
        self.enter_text.clear()


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = doctors_nft()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    while True:
        main()  # то запускаем функцию main()

