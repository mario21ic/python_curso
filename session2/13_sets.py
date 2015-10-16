# -*- coding: utf-8 -*-

print "#"*3 +" Sets "+"#"*3

print ""
print "## Definiendo ##"""
mi_set = set()
mi_set.add('juan')
mi_set.add('viki')
mi_set.add('nati')
print "mi_set:",mi_set
otro = set(['juan', 'karina', 'diana'])
print "otro:",otro

print ""
print "## Operaciones ##"""
print "mi_set.intersection(otro)",mi_set.intersection(otro)
print "mi_set.union(otro)",mi_set.union(otro)
print "mi_set.difference(otro)",mi_set.difference(otro)
