"""Main module of the file browser"""

import sys
import os
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

        self.source_directory = "D:\\Data\\workspaces\\example\\photos"
        self.analyze_directory()

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
        #file_name = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', 'All files (*.*)')
        directory_name = QtWidgets.QFileDialog.getExistingDirectory(self, 'Open directory', 'c:\\')
         #       directory_name = getExistingDirectory(self, 'Open directory', 'c:\\', QFileDialog::Options options = ShowDirsOnly)
        print('directory: ' + str(directory_name))
        """         print('file: ' + str(file_name))
        print('file name: ' + str(file_name[0]))        

        # print('window resized')
        width = self.image_label.width()
        height = self.image_label.height()
        # print('w:' + str(width) + '; h:' + str(height))

        self.current_image_path = file_name[0]

        # self.image_label.setScaledContents(True)
        pixmap = QPixmap(self.current_image_path)
        #self.image_label.setPixmap(pixmap)
        self.image_label.setPixmap(pixmap.scaled(width, height, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))                 """

    def analyze_directory(self):
        print('analyzing directory \'' + str(self.source_directory) + '\'')
        self.files = []

        self.scantree(self.source_directory)

        # print(self.files)
    
    def scantree(self, target_directory):
        with os.scandir(target_directory) as it:
            for entry in it:
                if entry.is_file():
                    file_name = (os.path.join(target_directory, entry.name))
                    print(file_name)
                    self.files.append(file_name)
                elif entry.is_dir():
                    self.scantree(os.path.join(target_directory, entry.name))

def main():
    """main executable"""
    print('start filebrowser')

    os.environ["QT_LOGGING_RULES"] = "qt.gui.icc=false"

    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    #Ui()
    app.exec_()
