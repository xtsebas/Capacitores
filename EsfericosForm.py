from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import PlacasParalelas


class EsfericosSreen(QMainWindow):

    def __init__(self,main_window=None):
        super(EsfericosSreen,self).__init__()
        uic.loadUi("esfericos_.ui",self)

        #Guardando variable
        self.main_window = main_window
        self.imageLabel.setVisible(False)
        self.setFixedSize(664, 709)


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


        #pixmap = QPixmap("image.png")

        #self.imageLabel.setPixmap(pixmap)
        #self.imageLabel.setScaledContents(True)

        batteryPixMap = QPixmap("battery.png")
        batteryPixMap = batteryPixMap.scaled(100, 100, Qt.KeepAspectRatio)

        self.batteryLabel.setPixmap(batteryPixMap)
        self.batteryLabel.setFixedSize(100, 100)


        self.show()


    """
    Funciones de display de parametros en vivo
    """
    def voltajeOnChange(self,voltaje):
        print(voltaje)
        self.voltajeLabel.setText(str(voltaje)+" V")
        self.voltajeBar.setValue(voltaje)

    def separationChange(self,separation):
        self.separacionLabel.setText(str(separation) + " cm")

    def anchoChange(self,ancho):
        self.anchoLabel.setText(str(ancho) + " cm")

    def largoChange(self,largo):
        self.largoLabel.setText(str(largo) + " cm")

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

        print("Realizando calculos....")
        self.imageLabel.setVisible(True)
        self.setFixedSize(1253, 709)

        #Obteniendo valores de usuario

        voltaje = self.dial.value()
        separacion = self.separacionSlider.value()
        ancho = self.anchoSlider.value()
        largo = self.largoSlider.value()

        print("Valor del voltaje: "+str(voltaje)+" "+str(type(voltaje)))
        print("Valor del separacion: " + str(separacion) + " " + str(type(separacion)))
        print("Valor del ancho: " + str(ancho) + " " + str(type(ancho)))
        print("Valor del largo: " + str(largo) + " " + str(type(largo)))




        #Selccionando imagen
        placa = self.dielectricoComboBox.currentText()
        print(placa)

        dimension = self.dimensionComboBox.currentText()
        print(dimension)

        if placa=="No":
            #Se escogio con vacio
            print("Capacitor con placas paralelas vacias")
            placas_vacias = QPixmap("placa_vacia.png")
            self.imageLabel.setPixmap(placas_vacias)
            self.imageLabel.setScaledContents(True)
            placa_vacia = PlacasParalelas.Placas(voltaje, separacion / 100, largo / 100, ancho / 100, 0)

            #Propiedades fisicas
            capacitancia = placa_vacia.Capacitancia()
            voltaje_placa = placa_vacia.voltaje
            carga_placa = placa_vacia.Carga()
            energia = placa_vacia.Energia()

            print("============\nPropiedades\n===============")
            print("Capacitancia" + str(capacitancia))
            print("voltaje_placa" + str(voltaje_placa))
            print("carga_placa" + str(carga_placa))
            print("energia" + str(energia))




        if placa=="Si" and dimension == "Completo":
            #Se escogio con vacio
            print("Capacitor con placas con dielectrico completo")
            placas_kcompleto= QPixmap("placa_kcompleto.png")
            self.imageLabel.setPixmap(placas_kcompleto)
            self.imageLabel.setScaledContents(True)
            placa_dieCom = PlacasParalelas.Placas(voltaje, separacion / 100, largo / 100, ancho / 100, 1)

            #Propiedades
            capacitancia = placa_dieCom.Capacitancia()
            voltaje_placa = placa_dieCom.voltaje
            carga_placa = placa_dieCom.Carga()
            energia = placa_dieCom.Energia()
            carga_libre = placa_dieCom.Densidad()
            carga_ligada = placa_dieCom.DensidadLigada()

            print("============\nPropiedades\n===============")
            print("Capacitancia" +str(capacitancia))
            print("voltaje_placa" + str(voltaje_placa))
            print("carga_placa" + str(carga_placa))
            print("energia" + str(energia))
            print("carga_libre" + str(carga_libre))
            print("carga_ligada" + str(carga_ligada))



        if placa == "Si" and dimension == "A la mitad":
            print("Capacitor con placas con dielectrico a la mitad")
            placas_kmitad = QPixmap("placa_kmitad.png")
            self.imageLabel.setPixmap(placas_kmitad)
            self.imageLabel.setScaledContents(True)
            placa_dieMitad = PlacasParalelas.Placas(voltaje, separacion / 100, largo / 100, ancho / 100, 2)

            # Propiedades
            capacitancia = placa_dieMitad.Capacitancia()
            voltaje_placa = placa_dieMitad.voltaje
            carga_placa = placa_dieMitad.Carga()
            energia = placa_dieMitad.Energia()
            carga_libre = placa_dieMitad.Densidad()
            carga_ligada = placa_dieMitad.DensidadLigada()


            print("============\nPropiedades\n===============")
            print("Capacitancia" + str(capacitancia))
            print("voltaje_placa" + str(voltaje_placa))
            print("carga_placa" + str(carga_placa))
            print("energia" + str(energia))
            print("carga_libre" + str(carga_libre))
            print("carga_ligada" + str(carga_ligada))

