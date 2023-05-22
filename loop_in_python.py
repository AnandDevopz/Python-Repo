#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 20:43:46 2023

@author: saumyabm
"""

a=[10,20,30]

print(a)
a.append(100)
a.append(1000)
a.append(123)
a.append(123)
a.append(123)
a.append(123)
a.append(123)

a.remove(123)


print(a)

for value in a:
    print(value)