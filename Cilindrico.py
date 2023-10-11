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
            C = self.k  * ((2*np.pi*self.e0*self.largo)/(np.log((self.Re/self.Ri))))

        elif (self.dielectrico == 2):

            C1 = self.k  * ((np.pi*self.e0*self.largo)/(np.log((self.Re/self.Ri))))

            C2 = (np.pi*self.e0*self.largo)/(np.log((self.Re/self.Ri)))

            C = C1 + C2

        else:
            C = (2*np.pi*self.e0*self.largo)/(np.log((self.Re/self.Ri)))

        return C

    def Carga(self):
        if (self.dielectrico == 1):
            Q = self.voltaje * (self.Capacitancia() / self.k)

        elif (self.dielectrico == 2):
            Q = (2 * self.Capacitancia() / (self.k + 1)) * self.voltaje

        else:
            Q = self.voltaje * self.Capacitancia()

        return Q

    def Energia(self):
        if  (self.dielectrico==1):
            U = ((self.Capacitancia()) * ((self.voltaje/self.k) **2))/2

        elif (self.dielectrico ==2):
            U = ((self.voltaje**2) * ((2*np.pi*self.e0*self.largo)/(np.log((self.Re/self.Ri))))/2)/2 + (((self.voltaje/self.k)**2)* (self.Capacitancia()/2))/2

        else:
            U = (self.voltaje * self.Carga())/2

        return U

    def Densidad(self, a):
        if (self.dielectrico == 1):
            if (a == 1):
                D = (self.Carga()) / (2 * np.pi * self.Ri * self.largo)
            else:
                D = (self.Carga()) / (2 * np.pi * self.Re * self.largo)

        elif (self.dielectrico == 2):
            if (a == 1):
                D = (self.Carga()) / (np.pi * self.Ri * self.largo * (self.k +1))

            elif (a == 2):
                D = (self.Carga()) / (np.pi * self.Re * self.largo * (self.k +1))

            elif (a == 3):
                D = (self.Carga() * self.k) / (np.pi * self.Ri * self.largo * (self.k +1))

            else:
                D = (self.Carga() * self.k) / (np.pi * self.Re * self.largo * (self.k +1))

        else:
            D = 0

        return D

    def DensidadLigada(self, a):
        if (self.dielectrico == 1):
            if (a == 1):
                D = self.Densidad(1)*(1-1/self.k)
            else:
                D = self.Densidad(2)*(1-1/self.k)

        elif (self.dielectrico == 2):
            if (a == 1):
                D = self.Densidad(3) * (1 - 1 / self.k)
            else:
                D = self.Densidad(4) * (1 - 1 / self.k)
        else:
            D = 0
        return D