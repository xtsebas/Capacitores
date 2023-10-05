import numpy as np

class Esfera:
    def __init__(self, voltaje, Ri, Re, dielectrico):
        self.voltaje = voltaje
        self.Ri = Ri
        self.Re = Re
        self.dielectrico = dielectrico
        self.e0 = 8.854e-12
        self.k = 3.40

    def Capacitancia(self):
        if (self.dielectrico == 1):
            C = self.k  * (4* np.pi * self.e0 *((self.Re * self.Ri)/(self.Re - self.Ri)))

        elif (self.dielectrico == 2):

            C1 = self.k  * (2* np.pi * self.e0 *((self.Re * self.Ri)/(self.Re - self.Ri)))

            C2 = (2* np.pi * self.e0 *((self.Re * self.Ri)/(self.Re - self.Ri)))
            C = C1 + C2

        else:
            C = 4* np.pi * self.e0 *((self.Re * self.Ri)/(self.Re - self.Ri))

        return C

    def Carga(self):
        return self.voltaje * self.Capacitancia()

    def Energia(self):
        return (self.Carga() * self.voltaje)/2

    def Densidad(self, a):
        if (self.dielectrico != 0):
            if (a==1):
                D = self.Carga() / (2 * np.pi * (self.Ri**2))
            else:
                D = self.Carga() / (2 * np.pi * (self.Re ** 2))
        else:
            D=0
        return D

    def DensidadLigada(self, a):
        if (self.dielectrico != 0):
            if (a==1):
                D = self.Densidad()(1 - 1 / self.k)
            else:
                D = self.Densidad() (1 - 1/self.k)

        else:
            D=0
        return D