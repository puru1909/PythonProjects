# #Health Management system
# 3 clients-Sonal,Aaman,Guddu
#
# inlog teeno k liye manage krna hoga ki ye kya kha rhe h ar kya kya exercise krte h
#
# hame 3 files banani h unka food log krne k liye
# ar 3 unki exercise log krne k liye
# total - 6 files to be created
#
# Fun1
# #write a function that when executed takes as input client name and
# like press 1 for sonal 2 for aman 3 for guddu
# and like if we select 1 to wo puchega ki sonal ki aap kya log karna chate h exercise ya food
# like 1 for exercise 2 for diet
# ar jo v hmlog denge wo print ho jayega
#
# def getdate():
#     import datetime
#     return datetime.datetime.now() # time return karega
# ye function ko use krna h
#
# i/p- 3 roti,bhindi ki sbji,daal -ye i/p hoga ar phir tym print krna h.. tym pehle v print kr skte h
# o/p [time] roti,bhindi ki sbji,daal ar ek \n v hona chahiye taki file clean dikhe
#     [time] push ups
# Fun2
# #one more function to retrieve exercise or food for any client
# 1.kiska data retrieve krna h
# 2.food/exercise
# fir wo file uthakar de dega.
#
#
# 1st wo puchega log krna h ya retrieve
# fir log h to kiska krna h...n so on
################################################################################
#3 clients-sonal,aman,guddu
#def getdate():
#     import datetime
#     return datetime.datetime.now()
#total 6 files
#write a function that when executed takes an input client name
#one more function to retrieve exercise or food for any client
#
# ######################################################################

def getdate():
    import datetime
    return datetime.datetime.now()

def filelogfood(str,str2):
    f = open(f"{str}food.txt","a")
    f.write(str2 + " " + f"{getdate()}" +"\n")

    f.close()

def fileloggym(str,str2):
    f = open(f"{str}gym.txt","a")
    f.write(str2 + " " + f"{getdate()}"+"\n")

    f.close()

def fileretrieve(str3,str4):
    f = open(f"{str3}{str4}.txt","rt")
    content = f.read()
    print(content)
    f.close()


def logmsg(str):
    print("Press 1 to log efforts for food \n Press 2 to log efforts for gym")
    foodorgym=int(input())

    if(foodorgym==1):
        print("please enter the food")
        food1 = input()
        filelogfood(str, food1)
        print("Congrats your efforts are logged successfully")
    elif(foodorgym==2):
        print("please enter the gym's efforts")
        gym1 = input()
        fileloggym(str, gym1)
        print("Congrats your efforts are logged successfully")
    else:
        print("invalid input")

def retrievemsg(str):
    print("Press 1 to retrieve efforts for food \n Press 2 to retrieve efforts for gym")
    getfoodorgym = int(input())

    if (getfoodorgym == 1):
        fileretrieve(str,"food")
    elif (getfoodorgym == 2):
        fileretrieve(str,"gym")
    else:
        print("invalid input")


print("Select 1 to log \n Select 2 to retrieve")
userin1 = int(input())
if (userin1==1):
    print("For whom you want to log efforts?\n 1.Sonal \n 2.Aman \n 3.Guddu")
    userinlog=int(input())

    if(userinlog == 1):
        logmsg("sonal")
    elif(userinlog == 2):
        logmsg("aman")
    elif(userinlog == 3):
        logmsg("guddu")
    else:
        print("invalid input")

elif(userin1==2):
    print("For whom you want to retrieve efforts?\n 1.Sonal \n 2.Aman \n 3.Guddu")
    userinlog = int(input())
    if (userinlog == 1):
        retrievemsg("sonal")
    elif (userinlog == 2):
        retrievemsg("aman")
    elif (userinlog == 3):
        retrievemsg("guddu")
    else:
        print("invalid input")

else:
    print("invalid input")


