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
        if(self.dielectrico==1):
            Q=self.voltaje * (self.Capacitancia() /self.k)

        elif(self.dielectrico==2):
            Q= (2*self.Capacitancia()/(self.k+1))*self.voltaje

        else:
            Q= self.voltaje * self.Capacitancia()

        return Q

    def Energia(self):
        if  (self.dielectrico==1):
            U = ((self.Capacitancia()) * ((self.voltaje/self.k) **2))/2

        elif (self.dielectrico ==2):
            U = ((self.voltaje**2) * (4* np.pi*self.e0 *( (self.Re*self.Ri)/(self.Re - self.Ri)))/2)/2 + (((self.voltaje/self.k)**2)* (self.Capacitancia()/2))/2

        else:
            U = ((self.voltaje**2) * self.Capacitancia())/2

        return U

    def Densidad(self, a):
        if (self.dielectrico == 1):
            if (a==1):
                D = (self.Carga()) / (4 * np.pi * (self.Ri**2))
            else:
                D = self.Densidad(1) * (1 - 1 / self.k)
        elif(self.dielectrico==2):
            if(a==1):
                D = self.Carga()/(2*np.pi*(self.Ri**2)*(self.k+1))

            elif(a==2):
                D = self.Carga()/(2*np.pi*(self.Re**2)*(self.k+1))

            elif (a == 3):
                D = (self.Carga()*self.k)/(2*np.pi*(self.Ri**2)*(self.k+1))

            else:
                D = (self.Carga() * self.k) / (2 * np.pi * (self.Re ** 2) * (self.k + 1))

        else:
            D=0

        return D

    def DensidadLigada(self, a):
        if (self.dielectrico == 1):
            if (a==1):
                D = self.Carga() / (4 * np.pi * (self.Re**2))
            else:
                D = self.DensidadLigada(1) * (1 - 1/self.k)

        elif(self.dielectrico==2):
            if(a==1):
                D = self.Densidad(3) * (1 - 1 / self.k)
            else:
                D = self.Densidad(4) * (1 - 1 / self.k)
        else:
            D=0
        return D