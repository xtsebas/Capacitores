from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import Cilindrico


class CilindricosScreen(QMainWindow):
    def __init__(self,main_window=None):
        self.y=894
        super(CilindricosScreen,self).__init__()
        uic.loadUi("cilindricos_.ui",self)

        #Guardando variable
        self.main_window = main_window
        self.imageLabel.setVisible(False)
        self.setFixedSize(664, self.y)


        """
        Ajustes de botones
        """
        self.calculateButton.clicked.connect(self.mostrarCalculos)


        """
        Ajudstes de sliders
        """
        self.radioASlider.valueChanged.connect(self.separationChange)
        self.radioBSlider.valueChanged.connect(self.anchoChange)
        self.largoSlider.valueChanged.connect(self.largoOnChange)


        """
        Dial setting (Voltaje)
        """
        self.dial.valueChanged.connect(self.voltajeOnChange)

        """
        Ajustes de comboBoxes 
        """
        self.dielectricoComboBox.addItems(["No", "Si"])
        self.dimensionComboBox.addItems(["Completo","A la mitad"])

        self.voltajeBar.setTextVisible(False)
        self.adviseLabel.setVisible(False)

        batteryPixMap = QPixmap("battery.png")
        batteryPixMap= batteryPixMap.scaled(80, 80, Qt.KeepAspectRatio)

        self.batteryLabel.setPixmap(batteryPixMap)
        self.batteryLabel.setFixedSize(80, 80)

        self.show()


    """
    Funciones de display de parametros en vivo
    """
    def voltajeOnChange(self,voltaje):
        self.voltajeLabel.setText(str(voltaje)+" V")
        self.voltajeBar.setValue(voltaje)

    def separationChange(self,separation):
        self.separacionLabel.setText(str(separation) + " m")

    def anchoChange(self,ancho):
        self.anchoLabel.setText(str(ancho) + " m")

    def largoOnChange(self,largo):
        self.largoLabel.setText(str(largo) + " m")

    """
    Funciones de navegacion
    """
    def backToMenu(self):
        self.hide()
        if self.main_window:
            self.main_window.show()

    """
    Funcion de cierre de ventana
    """
    def closeEvent(self, event):
        self.backToMenu()
        event.accept()

    def mostrarCalculos(self):

        #Obteniendo valores de usuario
        voltaje = self.dial.value() #Voltaje
        radioA = self.radioASlider.value() ##Interno
        radioB = self.radioBSlider.value() #Externo
        largo = self.largoSlider.value()

        cilindro_ = self.dielectricoComboBox.currentText()
        dimension = self.dimensionComboBox.currentText() #Dimension dielectrico

        if radioA >= radioB:
            self.adviseLabel.setVisible(True)

        else:

            #Dimensionando
            self.imageLabel.setVisible(True)
            self.setFixedSize(1253, self.y)
            self.adviseLabel.setVisible(False)

            if cilindro_=="No":
                #Resize
                self.setFixedSize(1253, self.y)
                self.informationLabel.resize(551, 171)

                placas_vacias = QPixmap("cilindricoNormal.png") #Cambiar por esferico
                self.imageLabel.setPixmap(placas_vacias)
                self.imageLabel.setScaledContents(True)

                Cilindro = Cilindrico.Cilindrico(voltaje, radioA, radioB,largo, 0)

                #Label values
                self.capacitanciaLabel.setText(str(Cilindro.Capacitancia()) + " F")
                self.cargaLabel.setText(str(Cilindro.Carga()) + " C")
                self.energiaLabel.setText(str(Cilindro.Energia()) + " J")

            if cilindro_=="Si" and dimension == "Completo":

                self.resize(1250,918)
                self.informationLabel.resize(551, 371)

                placas_kcompleto= QPixmap("cilindricoCompleto.png")

                #Resize
                self.imageLabel.setPixmap(placas_kcompleto)
                self.imageLabel.setScaledContents(True)

                Cilindrofull = Cilindrico.Cilindrico(voltaje, radioA, radioB, largo, 1)

                self.capacitanciaLabel.setText(str(Cilindrofull.Capacitancia()) + " F")
                self.cargaLabel.setText(str(Cilindrofull.Carga()) + " C")
                self.energiaLabel.setText(str(Cilindrofull.Energia()) + " J")

                self.cargalibreLabel.setText("(R interno aire) " + str(Cilindrofull.Densidad(1)) + " C/m^2")
                self.cargaLibre2Label.setText("(R externo aire) " + str(Cilindrofull.Densidad(2)) + "C/m^2")

                self.cargaLigada1Label.setText("(R interior) " + str(Cilindrofull.DensidadLigada(1)) + " C/m^2")
                self.cargaLigada2Label.setText("(R exterior) " + str(Cilindrofull.DensidadLigada(2)) + " C/m^2")


            if cilindro_ == "Si" and dimension == "A la mitad":
                self.setFixedSize(1255, 890)
                self.informationLabel.resize(561,481)
                self.informationLabel.resize(551, 481)

                placas_kmitad = QPixmap("cilindricoMitad.png")
                self.imageLabel.setPixmap(placas_kmitad)
                self.imageLabel.setScaledContents(True)

                Cilindrohalf = Cilindrico.Cilindrico(voltaje, radioA, radioB, largo ,2)

                #LabelValues
                self.capacitanciaLabel.setText(str(Cilindrohalf.Capacitancia()) + " F")
                self.cargaLabel.setText(str(Cilindrohalf.Carga()) + " C")
                self.energiaLabel.setText(str(Cilindrohalf.Energia()) + " J")

                self.cargalibreLabel.setText("(R interno superior) " + str(Cilindrohalf.Densidad(1)) + " C/m^2")
                self.cargaLibre2Label.setText("(R externo superior) " + str(Cilindrohalf.Densidad(2)) + "C/m^2")
                
                self.cargaLigada1Label.setText("(R interior inferior) " + str(Cilindrohalf.DensidadLigada(1)) + " C/m^2")
                self.cargaLigada2Label.setText("(R exterior inferior)  " + str(Cilindrohalf.DensidadLigada(2)) + " C/m^2")

                self.cargaLibre3Label.setText("(R interno inferior) " + str(Cilindrohalf.Densidad(3)) + " C/m^2")
                self.cargaLibre4Label.setText("(R externo inferior) " + str(Cilindrohalf.Densidad(4)) + " C/m^2")

