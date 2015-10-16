# -*- coding: utf-8 -*-

print "#"*3 +" Clases abstractas "+"#"*3

from abc import ABCMeta, abstractmethod

class Abstracto(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def metodo(self):
        pass


class Heredado(Abstracto):
    def metodo(self):
        print "heredado"

#x = Abstracto()
x = Heredado()
x.metodo()
