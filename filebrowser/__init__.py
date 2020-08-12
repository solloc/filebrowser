"""Main module of the file browser"""

import sys
import os
import random
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtGui import QPixmap

__version__ = '0.1.0'

# Icon set: https://p.yusukekamiyamane.com/

class Ui(QtWidgets.QMainWindow):
    """UI main component"""
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('filebrowser/main.ui', self)



        # "D:\Data\workspaces\example\photos\amin-hasani-ma4EUsH56KQ-unsplash.jpg"

        self.menu_action_open = self.findChild(QtWidgets.QAction, 'actionOpen')
        self.menu_action_open.triggered.connect(self.action_open)

        self.tool_action_next = self.findChild(QtWidgets.QAction, 'action_next')
        self.tool_action_next.triggered.connect(self.next_image)

        # self.label_status_bar = self.findChild(QtWidgets.QStatusBar, 'label_status_bar')

        self.status_bar = self.findChild(QtWidgets.QStatusBar, 'status_bar')

        self.label_status_bar = QtWidgets.QLabel()

        self.status_bar.addPermanentWidget(self.label_status_bar)
        # self.status_bar.showMessage('some message')

        self.source_directory = "D:\\Data\\workspaces\\example\\photos"
        self.analyze_directory()

        self.image_label = self.findChild(QtWidgets.QLabel, 'imageLabel1')
        width = self.image_label.width()
        height = self.image_label.height()
        print('w:' + str(width) + '; h:' + str(height))

        # self.image_label.setScaledContents(True)
        # self.current_image_path = 'D:\\Data\\workspaces\\example\\photos\\marco-testi-g50urWL9A78-unsplash.jpg'
        image_index = random.randrange(0, len(self.files)-1)
        self.current_image_path = self.files[image_index]

        pixmap = QPixmap(self.current_image_path)
        #self.image_label.setPixmap(pixmap)
        self.image_label.setPixmap(pixmap.scaled(width, height, QtCore.Qt.KeepAspectRatio))        

        self.show()

    def push_button_pressed(self):
        """test method for button"""
        print('push button pressed')
        #self.label.setText('one more text')
    
    def resizeEvent(self, event):
        self.resize_image()
    
    def resize_image(self):
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
    
    def next_image(self):
        """ next image """
        # print('next image')
        # self.image_label.setScaledContents(True)
        # self.current_image_path = 'D:\\Data\\workspaces\\example\\photos\\marco-testi-g50urWL9A78-unsplash.jpg'

        total_images = len(self.files)

        image_index = random.randrange(0, total_images-1)
        self.label_status_bar.setText(str(image_index + 1) + '/' + str(total_images))
        self.current_image_path = self.files[image_index]

        pixmap = QPixmap(self.current_image_path)
        #self.image_label.setPixmap(pixmap)
        width = self.image_label.width()
        height = self.image_label.height()
        self.image_label.setPixmap(pixmap.scaled(width, height, QtCore.Qt.KeepAspectRatio))               

def main():
    """main executable"""
    print('start filebrowser')

    os.environ["QT_LOGGING_RULES"] = "qt.gui.icc=false"

    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    #Ui()
    app.exec_()
