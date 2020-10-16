#no of guess 9 -limited
#print no of guess left
#game over
#ek no lelo
#phir user ko bolo usko guess krne bt no of attempt limited rkna h lets say 9

n=6
attempts=5
while(attempts>0):
    print("pls guess the no")
    u=input()
    user=int(u)

    if(user==6):
        print("you are correct ,you won")
        break
    elif(user>6):
        print("thoda kam kro")
    elif(user<6):
        print("thoda zada kro")
    attempts=attempts-1

if(attempts==0):
    print("you lose game over")

