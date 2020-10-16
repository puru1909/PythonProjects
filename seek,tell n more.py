# f=open("puru2.txt")
# print(f.readline())
# print(f.readline())
# f.close()
#we are running this readline twice and every time when we run this code
#it will fetch the nextline from the file an give it

#ar agr hm ye kisi badi file k sath kr rhe h to hamara file pointer f iski value update
# hoti jati h

#################################################################################
#tell()
#ab muje ye file pointer kha pe maujud h kisi v point of tym m ... ye pta lagane k liye
#hum tell() use krte h
# f=open("puru2.txt")
# print(f.tell())
# print(f.readline())
# print(f.tell())
# print(f.readline())
# print(f.tell())
# o/p 0
# puru is greatpuru is a good singer
#
# 36
# puru is a good singer
#
# 59

##############################################################################
#seek()
#kv kv ham apne file pointer ko reset krna chate h like main chati hu
# ki puru is greatpuru is a good singer (first line) phirse print ho
#f.seek() hamare file pointer ko reset krke  lete aata h waps se uss position
#pe jo hum usko i/p dete h like f.seek(10)

f=open("puru2.txt")
f.seek(11)#atpuru is a good singer
print(f.tell()) #o/p 11
print(f.readline())
f.seek(0)#isse f file k starting m chala jata h
print(f.readline())
#o/p puru is greatpuru is a good singer

#puru is greatpuru is a good singer

###############################################################################

