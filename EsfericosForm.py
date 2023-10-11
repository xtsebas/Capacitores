from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import Esferico


class EsfericosSreen(QMainWindow):
    def __init__(self,main_window=None):
        self.y=742
        super(EsfericosSreen,self).__init__()
        uic.loadUi("esfericos_.ui",self)

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


        #pixmap = QPixmap("image.png")

        #self.imageLabel.setPixmap(pixmap)
        #self.imageLabel.setScaledContents(True)

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

    def largoChange(self,largo):
        self.largoLabel.setText(str(largo) + " m")

    """
    Funciones de navegacion
    """
    def backToMenu(self):
        self.hide()
        if self.main_window:
            self.main_window.show()

    def closeEvent(self, event):
        """This method is triggered when the Form window is closed."""
        self.backToMenu()
        event.accept()

    def mostrarCalculos(self):

        #Obteniendo valores de usuario

        voltaje = self.dial.value() #Voltaje
        radioA = self.radioASlider.value() ##Interno
        radioB = self.radioBSlider.value() #Externo

        #Selccionando imagen
        esfera = self.dielectricoComboBox.currentText()
        dimension = self.dimensionComboBox.currentText()

        if radioA >= radioB:

            self.adviseLabel.setVisible(True)
        else:

            #Dimensionando
            self.imageLabel.setVisible(True)
            self.setFixedSize(1253, self.y)
            self.adviseLabel.setVisible(False)

            if esfera=="No":
                self.setFixedSize(1253, self.y)

                #Modificando tamano de frame
                self.informationLabel.resize(551, 171)

                #Se escogio con vacio

                placas_vacias = QPixmap("esferico_.png") #Cambiar por esferico
                self.imageLabel.setPixmap(placas_vacias)
                self.imageLabel.setScaledContents(True)

                esfera = Esferico.Esfera(voltaje, radioA, radioB, 0)



                #Label values
                self.capacitanciaLabel.setText(str(esfera.Capacitancia()) + " F")
                self.cargaLabel.setText(str(esfera.Carga()) + " C")
                self.energiaLabel.setText(str(esfera.Energia()) + " J")

            if esfera=="Si" and dimension == "Completo":

                esferafull = Esferico.Esfera(voltaje, radioA, radioB ,1)
                self.resize(1250,918)

                self.informationLabel.resize(551, 371)

                placas_kcompleto= QPixmap("esfericocompleto_.png")
                self.imageLabel.setPixmap(placas_kcompleto)
                self.imageLabel.setScaledContents(True)

                self.capacitanciaLabel.setText(str(esferafull.Capacitancia()) + " F")
                self.cargaLabel.setText(str(esferafull.Carga()) + " C")
                self.energiaLabel.setText(str(esferafull.Energia()) + " J")

                self.cargalibreLabel.setText("(R interno superior) " + str(esferafull.Densidad(1)) + " C/m^2")
                self.cargaLibre2Label.setText("(R externo inferior) " + str(esferafull.DensidadLigada(1)) + "C/m^2")

                self.cargaLigada1Label.setText("(R interior inferior) " + str(esferafull.Densidad(2)) + " C/m^2")
                self.cargaLigada2Label.setText("(R exterior inferior) " + str(esferafull.DensidadLigada(2)) + " C/m^2")


            if esfera == "Si" and dimension == "A la mitad":
                self.setFixedSize(1255, 890)
                self.informationLabel.resize(561,481)

                esferahalf = Esferico.Esfera(voltaje, radioA, radioB, 2)

                self.informationLabel.resize(551, 481)

                placas_kmitad = QPixmap("esfericomitad_.png")
                self.imageLabel.setPixmap(placas_kmitad)
                self.imageLabel.setScaledContents(True)


                self.capacitanciaLabel.setText(str(esferahalf.Capacitancia()) + " F")
                self.cargaLabel.setText(str(esferahalf.Carga()) + " C")
                self.energiaLabel.setText(str(esferahalf.Energia()) + " J")

                self.cargalibreLabel.setText("(R interno superior) "+str(esferahalf.Densidad(1))+" C/m^2")
                self.cargaLibre2Label.setText("(R externo inferior) "+str(esferahalf.Densidad(2))+"C/m^2")

                self.cargaLigada1Label.setText("(R interior inferior) "+str(esferahalf.DensidadLigada(1))+" C/m^2")
                self.cargaLigada2Label.setText("(R exterior inferior) "+str(esferahalf.DensidadLigada(2))+" C/m^2")

                self.cargaLibre3Label.setText("(R interno inferior) "+str(esferahalf.Densidad(3))+" C/m^2")
                self.cargaLibre4Label.setText("(R externo inferior) "+str(esferahalf.Densidad(4))+" C/m^2")


