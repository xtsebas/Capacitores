import Capacitores.Esferico
import Capacitores.PlacasParalelas
import Capacitores.Cilindrico

placas = Capacitores.PlacasParalelas.Placas(10, 1, 1, 2, 0)
placasfull = Capacitores.PlacasParalelas.Placas(10, 1, 1, 2, 1)
placashalf = Capacitores.PlacasParalelas.Placas(10, 1, 1, 2, 2)
print("////////////PLACAS////////////////////////////////////////// \nPlaca sin dielectrico:")
#Sin dielectrico
print(placas.Capacitancia())
print(placas.Carga())
print(placas.Energia())

#Dielectrico a la mitad
print(" \nPlaca dielectrico a la mitad:")
print(placashalf.Capacitancia())
print(placashalf.Carga())
print(placashalf.Energia())
print(placashalf.Densidad(1))       #Libre de aire
print(placashalf.Densidad(2))       #Libre de plexiglas
print(placashalf.DensidadLigada())  #Ligada de plexiglas

#DIelectrico completo
print("\nPlaca Dielectrica:")
print(placasfull.Capacitancia())
print(placasfull.Carga())
print(placasfull.Energia())
print(placasfull.Densidad(0))       #Libre
print(placasfull.DensidadLigada())  #Ligada
###################################################################################333

esfera= Capacitores.Esferico.Esfera(10, 3, 6, 0)
esferahalf= Capacitores.Esferico.Esfera(10, 3, 6, 2)
esferafull= Capacitores.Esferico.Esfera(10, 3, 6, 1)
print("\n/////////////////////////////ESFERAS/////////////////////////////")
#Sin dielectrico
print("Esfera")
print(esfera.Capacitancia())
print(esfera.Carga())
print(esfera.Energia())

#Esfera dielectrica a la mitad
print("\nEsfera a la mitad:")
print(esferahalf.Capacitancia())
print(esferahalf.Carga())
print(esferahalf.Energia())
print(esferahalf.Densidad(1))           #libre Ra superior
print(esferahalf.Densidad(2))           #Libre Rb superior
print(esferahalf.Densidad(3))           #Libre Ra inferior
print(esferahalf.Densidad(4))           #Libre Rb inferior
print(esferahalf.DensidadLigada(1))     #Ligada Ra inferior
print(esferahalf.DensidadLigada(2))     #Ligada Rb inferior

#ESfera dielectrica
print("\nEsfera Dielectrica:")
print(esferafull.Capacitancia())
print(esferafull.Carga())
print(esferafull.Energia())
print(esferafull.Densidad(1))           #Libre Ra
print(esferafull.DensidadLigada(1))     #Libre Rb
print(esferafull.Densidad(2))           #Ligada Ra
print(esferafull.DensidadLigada(2))     #Ligada Rb


Cilindro= Capacitores.Cilindrico.Cilindrico(10, 3, 6, 5, 0)
Cilindrofull= Capacitores.Cilindrico.Cilindrico(10, 3, 6, 5, 1)
Cilindrohalf= Capacitores.Cilindrico.Cilindrico(10, 3, 6, 5, 2)
print("\n/////////////////////////////CILINDROS/////////////////////////////")
#Sin dielectrico
print("Cilindro")
print(Cilindro.Capacitancia())
print(Cilindro.Carga())
print(Cilindro.Energia())

#Cilindro a la mitad
print("\nCilindro dielectrico a al mitad:")
print(Cilindrohalf.Capacitancia())
print(Cilindrohalf.Carga())
print(Cilindrohalf.Energia())
print(Cilindrohalf.Densidad(1))         #Libre Ra superior
print(Cilindrohalf.Densidad(2))         #Libre Rb superior
print(Cilindrohalf.Densidad(3))         #Libre Ra inferior
print(Cilindrohalf.Densidad(4))         #Libre Rb inferior
print(Cilindrohalf.DensidadLigada(1))   #Ligada Ra inferior
print(Cilindrohalf.DensidadLigada(2))   #Ligada Rb inferior

#Cilindro dielectrico
print("\nCilindro dielectrico:")
print(Cilindrofull.Capacitancia())
print(Cilindrofull.Carga())
print(Cilindrofull.Energia())
print(Cilindrofull.Densidad(1))         #Libre Ra
print(Cilindrofull.Densidad(2))         #Libre Rb
print(Cilindrofull.DensidadLigada(1))   #Ligada Ra
print(Cilindrofull.DensidadLigada(2))   #Ligada Rb