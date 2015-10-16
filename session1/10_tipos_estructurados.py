# -*- coding: utf-8 -*-

print "#"*3 +" Tipos estructurados "+"#"*3

lista = [1, '2', ['tres', 4], '5', '6']
print "lista:",lista
for x in lista:
    print x

tupla = (1, '2', ('tres', 4), '5', '6')
print "\ntupla:",tupla
for x in tupla:
    print x

diccionario = {'clave1': 'valor1', 'clave2': 2, 'subdicc': {'x': 'd'}}
print "\ndiccionario:",diccionario
for x,y in diccionario.items():
    print "%s - %s" % (x, y)

print "#"*2 +" Operaciones "+"#"*2
lista[0] = 0
print "lista[0] = 0:",lista
lista.append('siete')
print "lista.append('siete'):",lista
lista.pop()
print "lista.pop():",lista
lista[2][0] = 3
print "lista[3][0] = 3:",lista
print "lista[1]:",lista[1]
print "lista[-2]:",lista[-2]
print "lista[2:]:",lista[2:]
print "lista[-2:1]:",lista[-2:1]
print "lista[:2]",lista[:2]
print "lista[:-2]",lista[:-2]
print "lista[1:4]",lista[1:4]
diccionario['clave1'] = 'nuevo_valor1'
print "diccionario:",diccionario
diccionario['subdicc']['x'] = 'new_value_sub_dicc'
print "diccionario:",diccionario
if 'clave1' in diccionario:
    print 'Si existe'

print "#"*2 +" Comprension de listas "+"#"*2
"""
lista_nueva = []
for x in range(10):
    if x%2 == 0:
        lista_nueva.append(x)
"""
lista_nueva = [x*2 for x in range(10) if x%2 == 0]
print "lista_nueva:",lista_nueva
