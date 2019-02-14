class Coche():
    def __init__(self, color, marca, modelo, caballos, puertas, matricula):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.caballos = caballos
        self.puertas = puertas
        self.matricula = matricula
        
    def get_color(self):
        return self.color
        
    def get_marca(self):
        return self.marca
        
    def get_modelo(self):
        return self.modelo
        
    def get_caballos(self):
        return self.caballos
        
    def get_puertas(self):
        return self.puertas
        
    def get_matricula(self):
        return self.matricula
        
class PruebaCoche(Coche):
    def __init__(self, color, marca, modelo, caballos, puertas, matricula):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.caballos = caballos
        self.puertas = puertas
        self.matricula = matricula
        
    def set_color(self, nuevocolor):
        self.color = nuevocolor
        
coche = PruebaCoche("Rojo vino", "Nissan", "Sentra", 300, 4, "AFX3A1K2PS")
print("El color del coche es", coche.get_color())
print("La marca del coche es", coche.get_marca())
print("El modelo del coche es", coche.get_modelo())
print("El numero de caballos del coche es", coche.get_caballos())
print("El numero de puertas del coche es", coche.get_puertas())
print("La matricula del coche es", coche.get_matricula())
Nuevo_Color = coche.set_color("Azul")
print("El nuevo color del coche es", coche.get_color())
Nuevo_Color = coche.set_color("Gris")
print("El nuevo color del coche es", coche.get_color())
Nuevo_Color = coche.set_color("Verde")
print("El nuevo color del coche es", coche.get_color())
Nuevo_Color = coche.set_color("Blanco")
print("El nuevo color del coche es", coche.get_color())

