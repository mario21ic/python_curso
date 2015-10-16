# -*- coding: utf-8 -*-

print "#"*3 +" Condicionales "+"#"*3

print "if:"
if True:
    print "Example if"

print "\nelse:"
valor = int(raw_input("Ingrese valor < 10: "))
if valor > 10:
    print "Example if"
else:
    print "Example else"

print "\nelif:"
valor = int(raw_input("Ingrese valor < 10 y > 5: "))
if valor > 10:
    print "Example if"
elif valor > 5:
    print "Example elif"
else:
    print "Example else"

print "\nswitch case:"
valor = raw_input("Ingrese valor 10 o 5: ")
resultado = {
    '10': 'Example if',
    '5': 'Example elif'
}
print resultado[valor]

print "\nswitch case funciones:"
valor = int(raw_input("Ingrese valor 10 o 5: "))
def diez():
    print 'Example if'
def cinco():
    print 'Example elif'
resultado = {
    10: diez,
    5: cinco
}
try:
    resultado[valor]()
except:
    print 'Example else'
