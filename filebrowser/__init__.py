"""Main module of the file browser"""

import sys
import os
import random

from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtGui import QPixmap

from .file_model import FileModel

__version__ = '0.1.0'

# Icon set: https://p.yusukekamiyamane.com/

class Ui(QtWidgets.QMainWindow):
    """UI main component"""
    def __init__(self):
        super(Ui, self).__init__()

        main_form = resource_path('filebrowser/main.ui')

        # uic.loadUi('./filebrowser/main.ui', self)
        uic.loadUi(main_form, self)

        self.file = FileModel()
        self.file.root_dir = "D:\\Data\\workspaces\\example\\photos"

        self.menu_action_open = self.findChild(QtWidgets.QAction, 'actionOpen')
        self.menu_action_open.triggered.connect(self.action_open)

        self.tool_action_next = self.findChild(QtWidgets.QAction, 'action_next')
        self.tool_action_next.triggered.connect(self.next_image)

        self.status_bar = self.findChild(QtWidgets.QStatusBar, 'status_bar')

        self.label_status_bar = QtWidgets.QLabel()

        self.status_bar.addPermanentWidget(self.label_status_bar)

        self.image_label = self.findChild(QtWidgets.QLabel, 'imageLabel1')
        width = self.image_label.width()
        height = self.image_label.height()
        print('w:' + str(width) + '; h:' + str(height))

        pixmap = QPixmap(self.file.get_current_file().name)
        self.image_label.setPixmap(pixmap.scaled(width, height, QtCore.Qt.KeepAspectRatio))

        self.show()

    def resizeEvent(self, event):
        self.resize_image()

    def resize_image(self):
        width = self.image_label.width()
        height = self.image_label.height()
        pixmap = QPixmap(self.file.get_current_file().name)
        self.image_label.setPixmap(pixmap.scaled(
            width, height, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))

    def action_open(self):
        print('open file')
        directory_name = QtWidgets.QFileDialog.getExistingDirectory(self, 'Open directory', 'c:\\')
        self.file.root_dir = directory_name

    def next_image(self):
        """ next image """
        self.file.next()
        self.label_status_bar.setText(
            str(self.file.get_current_file_number())
            + '/' +
            str(self.file.get_total_file_number()))

        pixmap = QPixmap(self.file.get_current_file().name)
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

# Define function to import external files when using PyInstaller.
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)