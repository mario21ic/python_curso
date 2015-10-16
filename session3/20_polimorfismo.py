# -*- coding: utf-8 -*-

print "#"*3 +" Polimorfismo "+"#"*3

class Pajaro():
    def desplazar(self):
        print("Volar")

class Vibora():
    def desplazar(self):
        print("Arrastrarse")

def mover(animal):
    animal.desplazar()

#p = Pajaro()
#v = Vibora()
#p.desplazar()
#v.desplazar()
# Polimorfismo
mover(Pajaro())
mover(Vibora())
