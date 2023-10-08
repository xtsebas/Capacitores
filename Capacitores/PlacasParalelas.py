
class Placas:

    def __init__(self, voltaje, distancia, lado, ancho, dielectrico):
        self.voltaje = voltaje
        self.distancia = distancia
        self.lado = lado
        self.ancho = ancho
        self.dielectrico = dielectrico
        self.e0 = 8.854e-12
        self.k = 3.40

    def Capacitancia(self):
        if (self.dielectrico == 1):
            C = self.k  * ((self.e0 * self.Area()) / self.distancia)

        elif (self.dielectrico == 2):
            C2 = (self.e0 * (self.lado / 2) * self.ancho) / self.distancia
            C1 = self.k  * C2
            C = C1 + C2

        else:
            C = (self.e0 * self.Area())/ self.distancia

        return C

    def Carga(self):
        return self.voltaje * ((self.e0*self.Area())/self.distancia)

    def Energia(self):
        if  (self.dielectrico==1):
            U = ((self.Capacitancia()) * ((self.voltaje/self.k) **2))/2

        elif (self.dielectrico ==2):
            U = ((self.voltaje**2) * ((self.e0 * self.Area())/self.distancia)/2)/2 + (( (self.voltaje/self.k)**2)*(self.Capacitancia()/2))/2

        else:
            U = ((self.voltaje**2) * self.Capacitancia())/2

        return U

    def Area(self):
        return self.lado * self.ancho

    # Tenes que ingresar un numero, 1 para encontrar la densidad del vacio, y 2 para encontrar la densidad del dielectrico
    def Densidad(self, a):
        if (self.dielectrico != 0):
            if  (self.dielectrico == 1):
                D = self.Carga() / self.Area()
            else:
                if(a==1):
                    D = (self.Carga() / (self.k + 1))/(self.Area()/2)
                else:
                    D= ((self.Carga() * self.k) / (self.k + 1))/(self.Area()/2)
        else:
            D=0
        return D

    def DensidadLigada(self):
        if (self.dielectrico != 0):
            D = self.Densidad(2) * (1 - (1/self.k))
        else:
            D=0
        return D