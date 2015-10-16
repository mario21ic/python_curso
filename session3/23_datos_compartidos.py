# -*- coding: utf-8 -*-

print "#"*3 +" Datos compartidos "+"#"*3

class SharedData(object):
    spam = 42

x = SharedData()
y = SharedData()
print "x.spam: %s - y: %s" % (x.spam, y.spam)
x.spam +=1
print "x.spam +=1: %s - y: %s" % (x.spam, y.spam)
SharedData.spam = 99
print "SharedData.spam = 99"
print "x.spam: %s - y: %s" % (x.spam, y.spam)
