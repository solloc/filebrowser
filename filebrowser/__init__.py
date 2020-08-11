"""Main module of the file browser"""

import sys
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtGui import QPixmap

__version__ = '0.1.0'

# Icon set: https://p.yusukekamiyamane.com/

class Ui(QtWidgets.QMainWindow):
    """UI main component"""
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('filebrowser/main.ui', self)

        self.image_label = self.findChild(QtWidgets.QLabel, 'imageLabel1')
        width = self.image_label.width()
        height = self.image_label.height()
        print('w:' + str(width) + '; h:' + str(height))

        # self.image_label.setScaledContents(True)
        self.current_image_path = 'D:\\Data\\workspaces\\example\\photos\\marco-testi-g50urWL9A78-unsplash.jpg'
        pixmap = QPixmap(self.current_image_path)
        #self.image_label.setPixmap(pixmap)
        self.image_label.setPixmap(pixmap.scaled(width, height, QtCore.Qt.KeepAspectRatio))

        # "D:\Data\workspaces\example\photos\amin-hasani-ma4EUsH56KQ-unsplash.jpg"

        self.menu_action_open = self.findChild(QtWidgets.QAction, 'actionOpen')
        self.menu_action_open.triggered.connect(self.action_open)

        self.show()

    def push_button_pressed(self):
        """test method for button"""
        print('push button pressed')
        #self.label.setText('one more text')
    
    def resizeEvent(self, event):
        # print('window resized')
        width = self.image_label.width()
        height = self.image_label.height()
        # print('w:' + str(width) + '; h:' + str(height))

        # self.image_label.setScaledContents(True)
        pixmap = QPixmap(self.current_image_path)
        #self.image_label.setPixmap(pixmap)
        self.image_label.setPixmap(pixmap.scaled(width, height, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))        
    
    def action_open(self):
        print('open file')
        file_name = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', 'All files (*.*)')
        print('file: ' + str(file_name))
        print('file name: ' + str(file_name[0]))        

        # print('window resized')
        width = self.image_label.width()
        height = self.image_label.height()
        # print('w:' + str(width) + '; h:' + str(height))

        self.current_image_path = file_name[0]

        # self.image_label.setScaledContents(True)
        pixmap = QPixmap(self.current_image_path)
        #self.image_label.setPixmap(pixmap)
        self.image_label.setPixmap(pixmap.scaled(width, height, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))                




def main():
    """main executable"""
    print('start filebrowser')
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    #Ui()
    app.exec_()
