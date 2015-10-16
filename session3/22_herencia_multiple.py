# -*- coding: utf-8 -*-

print "#"*3 +" Herencia multiple "+"#"*3

class C1(object):
    def metodo1(self):
        return "metodo 1"
    def metodo3(self, parametro):
        return "metodo 3"

class C2(object):
    def metodo2(self):
        return "metodo 2"
    def metodo3(self):
        return "metodo 3.1"

class C3(C1,C2):
    pass

objeto = C3()
print objeto.metodo1()
print objeto.metodo2()
print objeto.metodo3()
