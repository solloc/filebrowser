from PyQt5 import QtWidgets, uic
import sys

__version__ = '0.1.0'

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('filebrowser/main.ui', self)

        self.button = self.findChild(QtWidgets.QPushButton, 'pushButton1')
        self.button.clicked.connect(self.pushButtonPressed)

        self.label = self.findChild(QtWidgets.QLabel, 'label1')

        self.show()

    def pushButtonPressed(self):
        print('push button pressed')
        self.label.setText('one more text')


def main():
    print('start filebrowser')
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    #Ui()
    app.exec_()
