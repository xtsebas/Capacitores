from PyQt5.QtWidgets import *
from PyQt5 import uic

import CilindricosForm
import EsfericosForm
import PlacasForm


class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI,self).__init__()
        uic.loadUi("mainscreen.ui",self)

        """
        Setting main screen buttons
        """
        self.paralelasButton.clicked.connect(self.openPlacasForm)
        self.esfericoButton.clicked.connect(self.openEsfericosForm)
        self.cilindricoButton.clicked.connect(self.openCilindricosForm)

        self.show()

    def openPlacasForm(self):

        self.form = PlacasForm.PlacasScreen(main_window=self)
        self.form.show()
        self.hide()

    def openEsfericosForm(self):
        self.form = EsfericosForm.EsfericosSreen(main_window=self)
        self.form.show()
        self.hide()

    def openCilindricosForm(self):
        self.form = CilindricosForm.CilindricosScreen(main_window=self)
        self.form.show()
        self.hide()



def main():
    print("Running applicatio")
    app = QApplication([])
    window = MyGUI()
    app.exec_()


if __name__ == "__main__":
    main()
