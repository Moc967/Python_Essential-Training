#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# >> shift to right the number of bits on the right field
# << shift to left the number of bits on the right field
#  ^ exclusive or operand
#  & and
#  | or

x = 0x0a
y = 0x04
z = x << y

print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')
