# -*- coding: utf-8 -*-

print "#"*3 +" Tipos especiales "+"#"*3

print ""
print "## Ordenados ##"""
from collections import OrderedDict
markers = OrderedDict()
markers['ms123'] = 23.9
markers['mk31'] = 12.8
markers['ms92'] = 32.1
print "markers:",markers

print ""
print "## Arrays ##"""
import array
miarray = array.array("i", [1,2,3])
miarray.append(4)
print "miarray:",miarray

print ""
print "## Deque ##"""
from collections import deque
mideque = deque("abc")
print "mideque:",mideque
mideque.appendleft('x')
print "mideque.appendleft('x'):",mideque
mideque.popleft()
print "mideque.popleft():",mideque
mideque.extendleft(['x', 'y'])
print "mideque.extendleft(['x', 'y']):",mideque

print ""
print "## Counter ##"""
from collections import Counter
cnt = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1
print "cnt:",cnt
