# -*- coding: utf-8 -*-

print "#"*3 +" Excepciones "+"#"*3

def fetcher(obj, index):
    return obj[index]

x = 'spam'
print fetcher(x, 3)
#print fetcher(x, 4)


print ""
print "#"*2 + " Exception simple " + "#"*2
try:
    fetcher(x, 4)
except IndexError:
    print 'got expception'

print "#"*2 + " Exception raised and caught  " + "#"*2
try:
    x = 'spam'[99]
except IndexError:
    print 'except IndexError run'
finally:
    print 'finally run'


print ""
print "#"*2 + " No exception raised " + "#"*2
try:
    x = 'spam'[3]
except IndexError:
    print('except IndexError run')
finally:
    print('finally run')


print ""
print "#"*2 + " No exception raised with else " + "#"*2
try:
    x = 'spam'[3]
except IndexError:
    print('except IndexError run')
else:
    print('else run')
finally:
    print('finally run')


print ""
print "#"*2 + " Exception raised but not caught " + "#"*2
try:
    x = 1 / 0
except IndexError:
    print('except IndexError run')
except ZeroDivisionError:
    print('except ZeroDivisionError run')
finally:
    print('finally run')


print ""
print "#"*2 + " Exception customized " + "#"*2
class AlreadyGotOne(Exception):
    pass

def grail():
    raise AlreadyGotOne()

try:
    grail()
except AlreadyGotOne:
    print 'got exception customized'


print ""
print "#"*2 + " Exception customized2 " + "#"*2
class NuevaException(Exception):
    def __str__(self):
        return 'Esta es una nueva excepcion'

raise NuevaException
