from PyQt5.QtWidgets import *
from PyQt5 import uic
from screens import Form



class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI,self).__init__()
        uic.loadUi("mainscreen.ui",self)

        """
        Setting main screen buttons
        """
        self.paralelasButton.clicked.connect(self.openForm)
        self.esfericoButton.clicked.connect(self.openForm)
        self.cilindricoButton.clicked.connect(self.openForm)



        self.show()

    def openForm(self):
        print("JustClicked!")
        self.form = Form(main_window=self)
        self.form.show()
        self.hide()



def main():
    print("Running applicatio")
    app = QApplication([])
    window = MyGUI()
    app.exec_()


if __name__ == "__main__":
    main()
