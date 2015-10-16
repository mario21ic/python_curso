# -*- coding: utf-8 -*-

print "#"*3 +" Numericos "+"#"*3
i = 2
print "integer:",i
f = 5.0
print "float:",f
c = 52.3j
print "complex:",c

print ""
print "#"*3 +" Cadenas "+"#"*3
print 'comilla simple'
print "comilla doble"
print """comilla triple
  multi linea"""
print "Formateo\nSegunda: %s \t tab entero %d\nlista: %s" % ('xD', 12, ['xd', 21])
print u'Unicode'
print r'c:\\RawString'

print ""
print "#"*3 +" Logicos "+"#"*3
print True
print False
print None

print "#"*3 +" Operaciones "+"#"*3
print "#"*2 +" Float "+"#"*2
flotante = 12.0
print "is_integer:",flotante.is_integer()

print "#"*2 +" Cadena "+"#"*2
cadena = "Hola mundo"
print "cadena:",cadena
print "lower:",cadena.lower()
print "upper:",cadena.upper()
print "find mundo:",cadena.find('mundo')
print "find e:",cadena.find('e')
print "index mundo:",cadena.index('mundo')
#print "index e:",cadena.index('e')
for c in cadena:
    print c

print ""
print "#"*2 +" *Casting "+"#"*2
flotante = float('12.2')
print "string from flotante:",str(flotante)
print "float from string:",flotante
print "integer from string:",int(flotante)
print "integer from float:",int('12')

print ""
print "#"*2 +" *Otros "+"#"*2
print "len:",len(cadena)
print "type:",type(cadena)
