# -*- coding: utf-8 -*-

print "#"*3 +" Funciones "+"#"*3

print ""
print "## Simple ##"""
def funcion_simple():
    return "Funcion simple"

print funcion_simple()


print ""
print "## Parametros ##"""
def funcion_parametros(cadena):
    if cadena is not None:
        return cadena
    return False

print funcion_parametros("Funcion parametros")


print ""
print "## Parametros default ##"""
def funcion_param_default(cadena1, cadena2='cad2', cadena3='cad3'):
    return cadena1 + " " + cadena2 + " " + cadena3

print funcion_param_default('micad1', cadena3='micad3')
print funcion_param_default('micad1', 'franco')


print ""
print "## Multi parametros ##"""
def funcion_multi_param(cadena1, cadena2='cad2', cadena3='cad3', *args):
    print "args:",args
    return cadena1+" "+cadena2+" "+cadena3

print funcion_multi_param('xD', 'micad2', 'micad3', 'micad4', 'micad5')


print ""
print "## Multi key parametros ##"""
def funcion_multi_key_param(cadena1, cadena2='cad2', cadena3='cad3', **kwargs):
    print "kwargs:",kwargs
    return cadena1+" "+cadena2+" "+cadena3

print funcion_multi_key_param('xD', 'micad2', 'micad3', cad4='micad4', cad5='micad5')
