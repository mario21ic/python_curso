# -*- coding: utf-8 -*-

print "#"*3 +" Operador corto circuito "+"#"*3

persona = True
#if persona:
#    nombre = 'Juan Perez'
nombre = persona and 'Juan Perez'
print "nombre:",nombre

#nombre = False
"""
if nombre:
    encargado = nombre
else:
    encargado = 'Algun nombre'
"""
encargado = nombre or 'Algun nombre'
print "encargado:",encargado
