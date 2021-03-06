from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys


class MainApp(QMainWindow):
    def __init__(self, parent=None, *args):
        super(MainApp,self).__init__(parent = parent)
    
        self.setMinimumSize(500,300)
        self.setMaximumSize(1000,3000)
        self.setWindowTitle('Hola Mundo')
        self.widget = QWidget(self)


        width = self.frameGeometry().width()
        height = self.frameGeometry().height()
        label = QLabel("Label 1",self.widget)
        #label.setGeometry(20, 20, width,height)
        label.setStyleSheet("color:red; background:grey;")
        self.setCentralWidget(label)


if __name__=='__main__':
    app = QApplication([])
    ventana = MainApp()
    ventana.show()
    app.exec_()
