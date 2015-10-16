# -*- coding: utf-8 -*-

print "#"*3 +" Iterativos "+"#"*3

print "while:"
x = 0
while x <= 5:
    print x
    x += 1

print "\nfor-in:"
for x in range(5):
    print x

print "\nbreak:"
for x in range(5):
    if x == 2:
        break
    print x

print "\ncontinue:"
nuevo = ""
for x in "abac":
    if x != "a":
        continue
    nuevo += x
print nuevo
