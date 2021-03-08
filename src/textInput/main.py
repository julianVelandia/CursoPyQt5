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


        '''
        Campo de texto y  de contraseña
        '''
        self.user_input = QLineEdit(self)   #caja de texto
        self.user_input.setPlaceholderText("User")
        self.user_input.setClearButtonEnabled(True)
        self.user_input.setGeometry(220,10,150,30)
        self.user_input.setMaxLength(15)

        self.user_password = QLineEdit(self)   #caja de texto
        self.user_password.setPlaceholderText("Password")
        self.user_password.setClearButtonEnabled(True)
        self.user_password.setGeometry(220,50,150,30)
        self.user_password.setMaxLength(10)
        self.user_password.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton('Login',self)
        self.login_button.setGeometry(220, 90, 150, 30)

        '''
        Triggers
        '''
        self.user_input.returnPressed.connect(self.show_text)

    def show_text(self):
        print(self.user_input.text())




if __name__=='__main__':
    app = QApplication([])
    window = MainApp()
    window.show()
    app.exec_()