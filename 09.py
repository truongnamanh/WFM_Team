# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 22:53:44 2023

@author: v3180901
"""

a = input("nhập vào số a: ")
print("kiểu dữ liệu của a: ",type(a))
a = float(a)
print("kiểu dữ liệu của a: ",type(a))

b = input("nhập vào số b: ")
print("kiểu dữ liệu của b: ",type(b))
b = float(b)
print("kiểu dữ liệu của a: ",type(b))

print("{0}+{1}={2}".format(a, b, a+b))
print("{0}-{1}={2}".format(a, b, a-b))
print("{0}*{1}={2}".format(a, b, a*b))
print("{0}/{1}={2}".format(a, b, a/b))
print("{0}%{1}={2}".format(a, b, a%b))
print("{0}**{1}={2}".format(a, b, a**b))
print("{0}//{1}={2}".format(a, b, a//b))


