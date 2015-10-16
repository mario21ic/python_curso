# -*- coding: utf-8 -*-

print "#"*3 +" Listas operaciones "+"#"*3

print ""
print "## Eliminar ##"""
lista = [1, '2', ['tres', 4], '5', '6']
del(lista[2])
print "del(lista[2]):",lista

print ""
print "## Fusionar ##"""
lista = lista + ['x','d'] + ['x','y']
print "lista:",lista

print ""
print "## Copiar ##"""
a = [3, 4, 5, 6]
b = a
print "b = a\na is b:",a is b
b = a[:]
print "b = a[:]\na is b:",a is b
b = list(a)
print "b = list(a)\na is b:",a is b

print ""
print "## Comparacion ##"""
print "[1, 2, 3] == [1, 2] => ",[1, 2, 3] == [1, 2]
print "[1, 2, 3] == [1, 2, 3] => ",[1, 2, 3] == [1, 2, 3]
print "[1, 2, 3] == [1, 2, 4] => ",[1, 2, 3] == [1, 2, 4]
print "[1, 2, 3] < [1, 3, 2] => ",[1, 2, 3] < [1, 3, 2]
print "[10, 20, 30] > [1, 3, 2] => ",[10, 20, 30] > [1, 3, 2]
print "[1, 2, 3] < [1, 2] => ",[1, 2, 3] < [1, 2]
