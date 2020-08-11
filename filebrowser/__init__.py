"""Main module of the file browser"""

import sys
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtGui import QPixmap

__version__ = '0.1.0'


class Ui(QtWidgets.QMainWindow):
    """UI main component"""
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('filebrowser/main.ui', self)

        self.button = self.findChild(QtWidgets.QPushButton, 'pushButton1')
        self.button.clicked.connect(self.push_button_pressed)

        self.label = self.findChild(QtWidgets.QLabel, 'label1')

        self.image_label = self.findChild(QtWidgets.QLabel, 'imageLabel1')
        width = self.image_label.width()
        height = self.image_label.height()

        # self.image_label.setScaledContents(True)
        pixmap = QPixmap('D:\\Data\\workspaces\\example\\photos\\marco-testi-g50urWL9A78-unsplash.jpg')
        self.image_label.setPixmap(pixmap.scaled(width, height, QtCore.Qt.KeepAspectRatio))

        # "D:\Data\workspaces\example\photos\amin-hasani-ma4EUsH56KQ-unsplash.jpg"

        self.show()

    def push_button_pressed(self):
        """test method for button"""
        print('push button pressed')
        self.label.setText('one more text')


def main():
    """main executable"""
    print('start filebrowser')
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    #Ui()
    app.exec_()
