class Tiempo():
    def __init__(self, hora, minuto = None, segundo = None):
        self.hora = hora
        if not (hora <= 0) and (hora >=23):
            return "Introduzca una hora válida"
        if not minuto:
            self.minuto = 00
        else:
            self.minuto = minuto
        if not segundo:
            self.segundo = 00
        else:
            self.segundo = segundo
        
    def set_hora(self, horanueva):
        self.hora = horanueva
        
class PruebaTiempo(Tiempo):
    def __init__(self, hora, minuto = None, segundo = None):
        self.hora = hora
        if not minuto:
            self.minuto = 00
        else:
            self.minuto = minuto
        if not segundo:
            self.segundo = 00
        else:
            self.segundo = segundo
                  
    def get_hora(self):
        if not (self.hora <= 0) and (self.hora >=23):
            return "Introduzca una hora válida"
        elif not (self.minuto <= 0) and (self.minuto >=59):
            return "Introduzca un valor válido para los minutos"
        elif not (self.segundo <= 0) and (self.segundo >=59):
            return "Introduzca un valor valido para los segundos"
        else:
            return "Hora actual: {}:{}:{}".format(self.hora, self.minuto, self.segundo)
            
            
momento1 = PruebaTiempo(22, 30, 52)
print(momento1.get_hora())
Hora_Nueva = momento1.set_hora(8)
print(momento1.get_hora())
momento2 = PruebaTiempo(12, 333)
print(momento2.get_hora())
momento3 = PruebaTiempo(00)
print(momento3.get_hora())
Hora_Nueva2 = momento3.set_hora(1)
print(momento3.get_hora())
Hora_Nueva3 = momento3.set_hora(48)
print(momento3.get_hora())
