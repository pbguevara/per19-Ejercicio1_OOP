class Empleado():
    def __init__(self, nombre, salario, tiempo):
        self.nombre = nombre
        self.salario = salario
        self.tiempo = tiempo
        
    def get_name(self):
        return self.nombre
        
    def get_salario(self):
        return self.salario
        
    def get_tiempo(self):
        return self.tiempo
        
    def get_bono(self):
        if self.tiempo >= 7:
            bono = self.salario*0.4
            return "El bono de este empleado es de {}".format(bono)
        else:
            return "Este empleado no tiene bono"
       
emp1 = Empleado("Paola", 10000, 8)
emp2 = Empleado("Laura", 11000, 5)
emp3 = Empleado("Mounat", 7000, 9)
empleados = [emp1, emp2, emp3]

for empleado in empleados:
    print("El nombre del empleado es", empleado.get_name())
    print("El salario del empleado es", empleado.get_salario())
    print("El tiempo que este empleado ha estado en la empresa es de", empleado.get_tiempo(), "años")
    print(empleado.get_bono())
