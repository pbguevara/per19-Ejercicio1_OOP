class Rectangulo():
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def dame_area(self):
        area = self.base*self.altura
        return area
        
    def dame_per(self):
        per = 2*self.base+2*self.altura
        return per
        
class PruebaRectangulo(Rectangulo):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
        
rect1 = PruebaRectangulo(3,4)
rect2 = PruebaRectangulo(2,6)
rect3 = PruebaRectangulo(8,1)
rect4 = PruebaRectangulo(3,7)
rect5 = PruebaRectangulo(9,5)
rectangulos = [rect1, rect2, rect3, rect4, rect5]

for rectangulo in rectangulos:
    print("El area del rectangulo es", rectangulo.dame_area())
    print("El perimetro del rectangulo es", rectangulo.dame_per())
