from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys


class MainApp(QMainWindow):
    def __init__(self, parent=None, *args):
        super(MainApp,self).__init__(parent = parent)
    
        self.setMinimumSize(500,300)    #tamaño mínimo
        self.setMaximumSize(1000,3000)  #tamaño máximo
        self.setWindowTitle('Hola Mundo')   #titulo
        self.widget = QWidget(self)


        #width = self.frameGeometry().width()  #define el largo
        #height = self.frameGeometry().height()  #define el ancho
        #label = QLabel("Label 1",self.widget)  #etiqueta que se asigna al widget
        #label.setGeometry(20, 20, width,height), Ubicación del label
        #label.setStyleSheet("color:red; background:grey;")  #css
        #self.setCentralWidget(label)

        mensaje = "mensaje"
        self.btn1 = QPushButton("send data", self)
        self.btn2 = QPushButton("show info", self)


        self.btn1.setGeometry(0,0,80,40)
        self.btn2.setGeometry(60,60,80,40)


        self.btn1.clicked.connect(lambda: self.slot1(mensaje))
        self.btn2.clicked.connect(lambda: self.slot2())

        self.label = QLabel('label1',self)
        self.label.setGeometry(0, 120, 150, 150)
        self.label.mousePressEvent = self.slot2()
    
    def slot1(self, mensaje):
        print(mensaje)

    def slot2(self,event):
        print(event)
        print('hola')



if __name__=='__main__':
    app = QApplication([])
    ventana = MainApp()
    ventana.show()
    app.exec_()
