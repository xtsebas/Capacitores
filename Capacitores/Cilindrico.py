import numpy as np

class Cilindrico:
    def __init__(self, voltaje, Ri, Re, largo, dielectrico):
        self.voltaje = voltaje
        self.Ri = Ri
        self.Re = Re
        self.largo = largo
        self.dielectrico = dielectrico
        self.e0 = 8.854e-12
        self.k = 3.40

    def Capacitancia(self):
        if (self.dielectrico == 1):
            C = self.k  * ((2*np.pi*self.e0*self.largo)/(np.log((self.Ri/self.Re))))

        elif (self.dielectrico == 2):

            C1 = self.k  * ((np.pi*self.e0*self.largo)/(np.log((self.Ri/self.Re))))

            C2 = (np.pi*self.e0*self.largo)/(np.log((self.Ri/self.Re)))

            C = C1 + C2

        else:
            C = (2*np.pi*self.e0*self.largo)/(np.log((self.Ri/self.Re)))

        return C

    def Carga(self):
        return self.voltaje * self.Capacitancia()

    def Energia(self):
        return (self.voltaje * self.Carga())/2

    def Densidad(self, a):
        if (self.dielectrico != 0):
            if (a == 1):
                D = self.Carga() / (2 * np.pi * self.Ri *(self.Ri + self.largo))
            else:
                D = self.Carga() / (2 * np.pi * self.Ri *(self.Re + self.largo))
        else:
            D = 0
        return D

    def DensidadLigada(self, a):
        if (self.dielectrico != 0):
            if (a == 1):
                D = self.Densidad()(1 - 1 / self.k)
            else:
                D = self.Densidad()(1 - 1 / self.k)

        else:
            D = 0
        return D