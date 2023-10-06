from PyQt5.QtWidgets import *
from PyQt5 import uic




class Form(QMainWindow):
    def __init__(self,main_window=None):
        super(Form,self).__init__()
        uic.loadUi("capacitor.ui",self)

        #Guardando variable
        self.main_window = main_window


        self.backButton.clicked.connect(self.backToMenu)


        """
        Setting form buttons 
        """

        self.show()



    def backToMenu(self):
        self.hide()
        if self.main_window:
            self.main_window.show()

    def closeEvent(self, event):
        """This method is triggered when the Form window is closed."""
        self.backToMenu()
        event.accept()
