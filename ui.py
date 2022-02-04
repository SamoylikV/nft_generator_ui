import sys
import ui_pyqt
from PyQt5 import QtWidgets
from commands import install_, build_, remove_layer_, add_layer_, add_file_, remove_file_, select_mode_, change_rarity_


class doctors_nft(QtWidgets.QMainWindow, ui_pyqt.Ui_DartDocotr_nft_genrator):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.layer_name = ''
        self.rarity = ''

        self.enter.clicked.connect(self.get_text)
        self.enter_2.clicked.connect(self.get_rarity)

        self.build.clicked.connect(build_)
        self.install.clicked.connect(install_)

        self.remove_layer.clicked.connect(remove_layer_)
        self.add_layer.clicked.connect(lambda: add_layer_(self.layer_name))

        self.add_rarity.clicked.connect(lambda: change_rarity_(self.rarity))

        self.add_image.clicked.connect(add_file_)
        self.remove_image.clicked.connect(remove_file_)

        self.add_mode.clicked.connect(select_mode_)

    def get_text(self):
        self.layer_name = self.enter_text.toPlainText()
        self.enter_text.clear()

    def get_rarity(self):
        self.rarity = self.enter_text_2.toPlainText()
        self.enter_text_2.clear()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = doctors_nft()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
