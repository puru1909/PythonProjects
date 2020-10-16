f=open("puru2.txt","rt")#rt mode by default hota h ..hm nhi v likhenge to v ye rahega
print(f.readlines()) #o/p ['puru is greatpuru is a good singer\n', 'puru is a good singer\n', 'puru is a good singer\n', 'puru is a good singer\n', 'puru is a good singer\n', 'puru loves dance\n']
# ek list print hoga ar chunki readlines ne file ko pura read kr liya h to
# 2nd wale "readline" m kuch print nhi hoga,file pointer hamara last tk chala jayega
print(f.readline()) #agr hmlog readlines ko comment krte h tb ye o/p dega ->puru is greatpuru is a good singer

f.close()

###############################################################################

# with open("puru2.txt") as f: is same as  below.. yani ki f=open.. ar f.close()
# k ander jo cheez hm likh skte h wo hm with k ander v likh skte h ar hmko file ko close
#krne ki v zaroorat nhi h with ye khud handle krta h
#
# f=open("puru2.txt","rt")
#
#f.close()

###############################################################################
# with open("puru2.txt") as f:
#    print( f.read(4))

with open("puru2.txt") as f:
    a=readlines()
    print(a)
#
# Question of the day --> agr hmlog with block ko use krke uske bahr aakar
# waps se file ko kholta hu ar usko read krte
# h to kya wo read hogi? yes or no and why
# yha readlines k wajh se file pointer end tk jaa chuka h