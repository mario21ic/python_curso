# -*- coding: utf-8 -*-

print "#"*3 +" Sobre escritura de métodos "+"#"*3

class Humano(object):
    def saludar(self, para):
        return "Hola " + para

class Persona(Humano):
    def __init__(self, nombre):
        self.nombre = nombre
    def presentarse(self):
        return "Me llamo "+self.nombre
    def saludar(self, para, *args, **kwargs):
        print "saludar hijo"
        return super(Persona, self).saludar(para)
        #return "Saludo para: " + para

juan_perez = Persona("Juan Perez")
print juan_perez.saludar("Pepito")
print juan_perez.presentarse()
