# -*- coding: utf-8 -*-

print "#"*3 +" Clases y Herencia"+"#"*3

class Humano(object):
    def saludar(self, para='mengano'):
        return "Hola " + para

class Persona(Humano):
    _apellido = 'Perez'
    def __pensar(self):
        return "pensando"
    def presentarse(self):
        print self.__pensar()
        return "Me llamo "+self.nombre + " " + self._apellido

juan_perez = Persona()
juan_perez.nombre = "Juan"
print juan_perez.saludar()
print juan_perez.saludar("Pepito")
print juan_perez.presentarse()
#juan_perez.__pensar()
