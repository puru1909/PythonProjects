#Design a calculator which will completely solve all the the problems except the following ones:
#45 * 3 =555, 56+9 = 77 , 56/6 = 4 faulty calculations only for these
#Your pgm shud take operator and the two nos as input from and then return the result

print("Pls enter 2 digits")
a=int(input())
b=int(input())
print("Pls enter the opn u want to perform\n 1.* \n 2.+ \n 3./ \n 4.-")
c=int(input())
if(a==45 and b==3 and c==1):
    print(555)
elif(a==56 and b==9 and c==2):
    print(77)
elif(a==56 and b==6 and c==3):
    print(4)
elif(c==1):
    print(a*b)
elif(c==2):
    print(a+b)
elif(c==3):
    print(a/b)
elif(c==4):
    if(a>b):
        print(a-b)
    else:
        print(b-a)
else:
    print("invalid opn")

