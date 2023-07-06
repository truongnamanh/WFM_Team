# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 23:40:19 2023

@author: v3180901
"""

x = int(input("x: "))
y = int(input("y: "))


#True or False
print("{0}<{1} là {2}".format(x, y, x<y))

print("{0}>{1} là {2}".format(x, y, x>y))

print("{0}={1} là {2}".format(x, y, x==y))

print("{0}!={1} là {2}".format(x, y, x!=y))

print("{0}<={1} là {2}".format(x, y, x<=y))

print("{0}>={1} là {2}".format(x, y, x>=y))

print("Ví dụ về toán tử logic: ")

z = int(input("z: "))
print("({0}<{1} and {2}<{3}) = {4}".format(x, y, y, z, (x<y) and (y<z)))
print("({0}<{1} and {2}<{3}) = {4}".format(x, y, y, z, (x<y) or (y<z)))
print("not ({0}>{1}) = {2}".format(x,z, not (x>z)))