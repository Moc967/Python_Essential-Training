#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

a = True
b = False
x = ( 'bear', 'bunny', 'tree', 'sky', 'rain' )
y = 'bear'

if a and b:
    print('expression is true')
else:
    print('expression is false')

#print (id(<variable>)) shows the position where the variable is stored

print(id(x[0]))
print(id(y))