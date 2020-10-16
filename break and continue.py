# i=0
# while(i<20):
#     print(i+1, end =" ")#if we want that all elements shud get printed in one line
#     i=i+1

#while(1)
#while(True)#both are infinite loops

#break- use of break ye h ki hmlog ko while k ander condition nhi daalni h..
# bt jab whie run ho rha h tb agr hm chahte h ki ek point k baad wo ruk jaye wha break likh skte h
#nhi to while chalta rhe

# i=0
# while(True):
#     print(i=i+1,end=" ")
#     if(i==20):
#         break#stop the loop
#     i=i+1
#break hone k baad yha par aayega.

#continue
# pgm to print all nos between 5 and 45
# i=0
# while(True):
#     if(i+1<5):
#         i=i+1
#         continue #yha ye ander aayega ar niche sbkuch bhulkar ye agli iteration m ghus jayega
#                  # ar agr i+1 5 de bda ho gyatb loop k niche wala stmt chalega
#     print(i+1 , end=" ")
#     if(i==44):
#         break
#     i=i+1

#quiz: user se input lena h no jab tak wo input 100 se km hoga wo lete rahega input
# bt agr 100 se zada dega to wo loop se bahr nikal jayega


while(True):
    # print("ps enter a no")
    # user = int(input())
    user=int(input("ps enter a no\n"))
    if(user<100):
        print("Try Again\n")
        continue
    else:
        print("u hv entered a no greater than 100\n")
        break



