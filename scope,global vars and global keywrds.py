# l=10 # global variable
# def func1(n):
#     print(l) #o/p-10
#     print(n,"I have printed")
# func1("this is me")
# print(l)#o/p - 10
#######################################################

# l=10 #global variable
# def func1(n):
#     l=5 # local varaible
#     m=8 # local varaible
#     print(l,m) # o/p->5 8
#     print(b,m) # will through error for b as it is not defined anywhere
#     print(n,"I have printed")
# func1("this is me")
# print(l)#o/p->10
 # Pehle local scope m dhunda jata h...wo nhi mila tb global scope m dhunda jata h
 #local global is same as ham sarkar k banaye hue cheezon ko istemaalkr skte h
#(global) par sarkar local insaan ke ghr m ghus kar unki cheeze istemaal nhi kar skte h

###########################################################################
#global keyword
# l=3
# def func2(n):
#     l=l+7 #this will through an error we are trying to change the global variable
#     which is a read- only variable
#     print(l)
#     print(n,"hi there")
# func2("this is me")

#to change a global variable we need to use global keyword inside the func where
# we want to change the global variable as writing global keyword will indicate that
# this func got the permission to change the global variable
#####################################################################
# l=3
# def func2(n):
#     global l
#     l=l+7
#     print(l) #o/p->10
#     print(n,"hi there")
# func2("this is me")
# print(l)#o/p->10
###########################################################################
 #global keyword in nested func

# def sonal():
#      x=90
#      def aman():
#          global x # yha iss point se code executor  sidhe sonal func se bahr
#          # jata h ar x ko search krta h agr wha x hua to uska value wo change krke
#          # x=99 rakh dega but sonal k ander ka x ek local variable hi h to uska
#          #value change nhi hoga
#          x=99
#      print ("before calling aman",x) #o/p -> 90
#      aman()
#      print ("after calling aman",x)  #o/p -> 90
# sonal()
# print(x) #o/p 88
#qki global keyword k wajh se code executor gya sidhe gya bahr ar ek x variable bnake
#uska value 88 set kr diya agr xpehle se hota to usko read krta phir 88 daalta


#quiz:

x=70
def sonal():
    x = 90
    def aman():
        global x
        x = 99
    aman()
    print("after calling aman", x) #o/p after calling aman 90
sonal()
print(x) #o/p->99

