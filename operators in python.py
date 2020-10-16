"""Operators in Python
Arithmetic Operators
Assignment
Comparison
Logical
Identity
Membership
Bitwise"""

#Arithmetic Operators
print("5+6 is ", 5+6)
print("5-6 is ", 5-6)
print("5*6 is ", 5*6)
print("5/6 is ", 5/6)
print("15//6 is ", 15//6) #gives int value and ignore the rest value after decimal#floor division
print("5**3 is ", 5**3)#exponenetial 5*5*5
print("5%3 is ", 5%3) #gives remainder

#Assignment Operators
x=5
x+=7
x/=7
x%=7 #x=x%7

#Comparison Operators
i=8
print(i==5)#False
print(i!=5)#True
print(i>5)#True
print(i>=5)
print(i<=5)

#Logical Operators
a=True
b=False

print(a and b)#False
print(a or b)#True

#Identity Operators(is,isnot)
a=True
b=False

print(a is b)#False
print(a is not b)#True

#Membership Operator
list=[76,33,5,3,7,35,75]
print(76 in list)#True
print(76 not in list)#false

#Bitwise Operator(used for competitive fast problems qki machine k sath ye jaldi work krti h
# decimal->binary
# 0      ->00
# 1      ->01
# 2      ->10
# 3      ->11
print(0 & 1) # and o/p-0
print(0 | 1) # or o/p-1



