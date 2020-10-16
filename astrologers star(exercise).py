# pattern printing
# input: (ek no input lena h) Interger n(0/1) usko type cast krna h
#        ek boolean variable m ar usko set krna h true/false
# True: pattern aesa print hoga
# n=4
# *
# **
# ***
# ****
# False : n=4
# ****
# ***
# **
# *
#
print("please enter a no between 1 to 10")
n = int(input())
print("please enter 0(False) or 1(True)")
b = int(input())
new = bool(b)
print(new)
if(new == True):
    for i in range(1, n+1):
        for j in range(1,i+1):
            print("*", end=" ")
        print("\n")

elif(new == False):
    for i in range(1, n + 1):
         for j in range( n + 1,i,-1):
            print("*", end=" ")
         print("\n")
else:
    print("wrong ip")


# for i in range(1, 5):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print("\n")

# #for i in range(1, 5):
# for j in range(5,0,-1):
#     print("*",end=" ")
#     #print("\n")





