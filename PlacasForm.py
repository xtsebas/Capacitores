from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import PlacasParalelas
from PyQt5.QtCore import Qt



class PlacasScreen(QMainWindow):

    def __init__(self,main_window=None):
        self.y=881
        super(PlacasScreen,self).__init__()
        uic.loadUi("placas_paralelas.ui",self)

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
        self.separacionSlider.valueChanged.connect(self.separationChange)
        self.anchoSlider.valueChanged.connect(self.anchoChange)
        self.largoSlider.valueChanged.connect(self.largoChange)


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
        self.imageLabel.setVisible(True)
        self.setFixedSize(1253, self.y)

        #Obteniendo valores de usuario

        voltaje = self.dial.value()
        separacion = self.separacionSlider.value()
        ancho = self.anchoSlider.value()
        largo = self.largoSlider.value()

        #Selccionando imagen
        placa = self.dielectricoComboBox.currentText()
        dimension = self.dimensionComboBox.currentText()


        if placa=="No":
            self.setFixedSize(1253, self.y)

            #Modificando tamano de frame
            self.informationLabel.resize(521, 271)

            placas_vacias = QPixmap("placa_vacia.png")
            self.imageLabel.setPixmap(placas_vacias)
            self.imageLabel.setScaledContents(True)
            placa_vacia = PlacasParalelas.Placas(voltaje, separacion, largo, ancho, 0)

            #Propiedades fisicas
            capacitancia = placa_vacia.Capacitancia()
            voltaje_placa = placa_vacia.voltaje
            carga_placa = placa_vacia.Carga()
            energia = placa_vacia.Energia()

            self.capacitanciaLabel.setText(str(capacitancia)+" F")
            self.cargaLabel.setText(str(carga_placa) + " C")
            self.energiaLabel.setText(str(energia) + " J")


        if placa=="Si" and dimension == "Completo":

            self.informationLabel.resize(521, 431)
            placas_kcompleto= QPixmap("placa_kcompleto.png")
            self.imageLabel.setPixmap(placas_kcompleto)
            self.imageLabel.setScaledContents(True)
            placa_dieCom = PlacasParalelas.Placas(voltaje, separacion, largo, ancho, 1)


            self.capacitanciaLabel.setText(str(placa_dieCom.Capacitancia()) + " F")
            self.cargaLabel.setText(str(placa_dieCom.Carga()) + " C")
            self.energiaLabel.setText(str(placa_dieCom.Energia()) + " J")
            self.cargalibreLabel.setText(str(placa_dieCom.Densidad(0)) + " C/m^2")
            self.cargaligadaLabel.setText(str(placa_dieCom.DensidadLigada()) + " C/m^2")

        if placa == "Si" and dimension == "A la mitad":
            self.setFixedSize(1253,966)

            self.informationLabel.resize(521, 521)

            placas_kmitad = QPixmap("placa_kmitad.png")
            self.imageLabel.setPixmap(placas_kmitad)
            self.imageLabel.setScaledContents(True)
            placa_dieMitad = PlacasParalelas.Placas(voltaje, separacion, largo, ancho , 2)

            self.capacitanciaLabel.setText(str(placa_dieMitad.Capacitancia())+" F")
            self.cargaLabel.setText(str(placa_dieMitad.Carga())+" C")
            self.energiaLabel.setText(str(placa_dieMitad.Energia())+" J")
            self.cargalibreLabel.setText("(aire) "+str(placa_dieMitad.Densidad(1))+" C/m^2")
            self.cargaligadaLabel.setText(str(placa_dieMitad.DensidadLigada())+" C/m^2")
            self.librePlexiLabel.setText("(plexiglas) "+str(placa_dieMitad.Densidad(2))+" C/m^2")

