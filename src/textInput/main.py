import sqlite3

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


        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)


        '''
        Campo de texto y  de contraseña
        '''
        self.user_input = QLineEdit(self.centralWidget)   #caja de texto
        self.user_input.setPlaceholderText("UserName")
        self.user_input.setClearButtonEnabled(True)
        self.user_input.setGeometry(220,10,150,30)
        self.user_input.setMaxLength(15)

        self.user_password = QLineEdit(self.centralWidget)   #caja de texto
        self.user_password.setPlaceholderText("Password")
        self.user_password.setClearButtonEnabled(True)
        self.user_password.setGeometry(220,50,150,30)
        self.user_password.setMaxLength(10)
        self.user_password.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton('Login',self.centralWidget)
        self.login_button.setGeometry(220, 90, 150, 30)

        '''
        Triggers
        '''
        self.login_button.clicked.connect(self.login)

    def login(self):
        user_name = self.user_input.text()
        password = self.user_password.text()
        if user_name != '' and password != '' :
            print('correcto')




if __name__=='__main__':
    app = QApplication([])
    window = MainApp()
    window.show()
    app.exec_()