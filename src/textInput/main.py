from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

class MainApp(QMainWindow):
    def __init__(self, parent=None, *args):
        super(MainApp,self).__init__(parent = parent)
        
        
        self.setMinimumSize(500,300)    #tamaño mínimo
        self.setMaximumSize(1000,3000)  #tamaño máximo
        self.setWindowTitle('Input')   #titulo

        self.user_input = QLineEdit(self)   #caja de texto
        self.user_input.setPlaceholderText("password")
        self.user_input.setClearButtonEnabled(True)
        self.user_input.setGeometry(220,50,150,30)
        self.user_input.setMaxLength(10)
        self.user_input.setEchoMode(QLineEdit.Password)

if __name__=='__main__':
    app = QApplication([])
    window = MainApp()
    window.show()
    app.exec_()