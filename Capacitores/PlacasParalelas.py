
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
            C1 = self.k  * ((self.e0 * self.Area()) / 2 * self.distancia)
            C2 = (self.e0 * self.Area())/ 2 * self.distancia
            C = C1 + C2

        else:
            C = (self.e0 * self.Area())/ self.distancia

        return C

    def Carga(self):
        return self.voltaje * self.Capacitancia()

    def Energia(self):
        return ((self.voltaje**2) * self.Capacitancia())/2

    def Area(self):
        return self.lado * self.ancho
