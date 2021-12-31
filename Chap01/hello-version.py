#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import platform

print('This is python version {}'.format(platform.python_version()))
pontos = 0
n = 4
for i in n:
    pontos = pontos + i
print(pontos)