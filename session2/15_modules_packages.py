# -*- coding: utf-8 -*-

print "#"*3 +" Modulos & Packages"+"#"*3

print ""
print "## Modulos ##"""
from mimodulo import mivariable,mifuncion, mifuncion2
print mifuncion()
print mifuncion2("Hello module - mifunction2")

print ""
print "## Packages ##"""
from mipackage.mimodulo import mi_package_funcion,mi_package_funcion2
print mi_package_funcion()
print mi_package_funcion2("Hello mi package funcion2")
