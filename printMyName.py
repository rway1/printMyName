#!/usr/bin/python3

a = 34/3
b = -99/2
c = 271/6
d = 17
print("".join([chr(int(a * x ** 3 + b * x **2 + c * x + d)+65) for x in range(0,4)]))
