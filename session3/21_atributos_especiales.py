# -*- coding: utf-8 -*-

print "#"*3 +" Modulos & Packages"+"#"*3

print ""
print "## Atributos y metodos especiales ##"""
class Humano(object):
    def saludar(self, para):
        return "Hola " + para

class Persona(Humano):
    def __init__(self, nombre):
        self.nombre = nombre
    def presentarse(self):
        return "Me llamo "+self.nombre
    def __str__(self):
        return self.nombre + " xD"

juan_perez = Persona("Juan Perez")
print juan_perez.__class__
print juan_perez.__class__.__name__
print juan_perez.__dict__
print juan_perez
