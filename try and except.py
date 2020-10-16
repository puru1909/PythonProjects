# #exception handling
# #Example 1
# print("enter num1")
# num1=int(input())#if we put num as "re" we will get an error
# print("enter num2")
# num2=int(input())
# print("sum")
# print(num1+num2)
#
# #Example 2
# print("enter num1")
# num1=input()
# print("enter num2")
# num2=input()
# print("sum")
# print(int(num1)+int(num2))#again if we put "re" in input1 we will get error but in this line we will get error

#Example 3
print("enter num1")
num1=input()
print("enter num2")
num2=input()
try:#isse hm apne pgm ko bolte h ki aesa krne ki koshish kro
    print("the sum of num1 and num2 is ",
          int(num1)+int(num2))#again if we put "re" in input1 we will get error but
                              # in this line we will get error
except Exception as e: # ar agr nhi hota h to
    print(e)#isse jo hamara error msg aa rha tha
    # wo print ho jayega ek string ki taur pe ar baki pgm v aaram se execute karega
    #usko hamne "e" m catch krwa liya ar print krwa diya
print("This line is very imp and mandatory to print")

#Zada tar hmlog iss tarh ki cheeze tab use krte h jab hm internet connectivity se deal krte h
#jaise maan lo hmko koi cheez download krni h ar kisi k comp m internet nhi h to uska pgm wha pe exit ho jayega
#uss situation m hm uska pgm exit hone se bacha skte h taki baki ka code run ho jayear error msg print kr ke dede
#ki bhai aapka internet kharab h ar baki ka code chalta rhe h shi se
