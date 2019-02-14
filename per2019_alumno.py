class Alumno():
    def __init__(self, matricula, nombre, nota1, nota2, nota3):
        self.matricula = matricula
        self.nombre = nombre
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        
    def dame_matricula(self):
        return self.matricula
        
    def dame_nombre(self):
        return self.nombre
        
    def dame_notafinal(self):
        global nota_final
        nota_final = (self.nota1 + self.nota2 + self.nota3)/3
        return round(nota_final,2)
        
    def dame_condicion(self):
        if nota_final >= 4.8:
            return "El alumno ha aprobado."
        else:
            return "El alumno no ha aprobado."
        
        
alum1 = Alumno(26739858, "Paola Guevara", 7, 4.5, 6.2)
alum2 = Alumno(54638647, "Andrea Revete", 8, 9, 7.2)
alum3 = Alumno(37327874, "Mounat El Jarmouni", 6, 2.9, 3)
alumnos = [alum1, alum2, alum3]

for alumno in alumnos:
    print("La matricula del alumno es", alumno.dame_matricula())
    print("El nombre del alumno es", alumno.dame_nombre())
    print("La nota final del alumno es", alumno.dame_notafinal())
    print(alumno.dame_condicion())

