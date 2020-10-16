# open("puru.txt")#ye open() function ek file pointer return krta h
# f=open("puru.txt")#hmlog sbse pehle ek file pointer bnate h fir hm iss file pointer se khilwaad krte h
# content=f.read()
# print(content)
# f.close()#we shud always close the file ye ek good practice h
# #jab v hm kisi file ko open krte h to jo v resources  uss file ko kholne k baad deal krne m lgti h
# # wo ham free krna chahte h ar agr koi dusra pgm uss file ko read krna chahta h to
# # wo usko kr skta h to isiliye hm fle ko close krte h

# f=open("puru.txt","rb")#ye file ko binary format m read krega
# #o/p b'Puru is a good girl\r\nPuru is the queen of this universe\r\nPuru is intelligent'
# content=f.read()
# print(content)
# f.close()

# f=open("puru.txt","rt")#ye default hota h
# # o/p Puru is a good girl
# # Puru is the queen of this universe
# # Puru is intelligent
# content=f.read()
# print(content)
# f.close()

# f=open("puru.txt","rt")
# content=f.read(3) #will give only first 3 chars from the file.
# print(content)
# f.close()
# ##############################################################################################
# f=open("puru.txt","rt")
# content=f.read(3) #now if we rerun this piece of code like this it will give next 3 chars from the file
# print(content)
# content=f.read(3) #will give only first 3 chars from the file.
# print(content)
# f.close()
# #o/p Pur
# #    u i
###############################################################################################
# f=open("puru.txt","rt")
# content=f.read(387989) #since hamare file m itne characters h nhi to ye issi m sare file ko read
#                        # kar dega ar dusre wale part ko ignore karega
# print("1",content)
# content=f.read(387989)
# print("2",content)
# f.close()
#o/p
# 1 Puru is a good girl
# Puru is the queen of this universe
# Puru is intelligent
# 2

##############################################################################################

# f=open("puru.txt","rt")
# content=f.read()
#
# for ch in content:
#     print(ch)#it will print the content of the file character by character
#############################################################################################
# f=open("puru.txt","rt")
# #content=f.read()#iss line ko hatane ka reason ye h ki jb v ham f.read krte h
# # file pointer file ko read kr k khali ho jata h..
# # ar phir kuch print nhi hota
# #to o/p m kuch nhi milega
#
# for line in f:
#     #print(line)#it will print the content of the file line by line
#                #new line character by default file m h already usko rokne k liye we use
#     print(line,end=" ")

# o/p

# Puru is a good girl
#
# Puru is the queen of this universe
#
# Puru is intelligent
###############################################################################################
# f=open("puru.txt","rt")
# print(f.readline())#o/p-Puru is a good girl
# print(f.readline())#o/p- /n Puru is the queen of this universe
#############################################################################################
#realines func to store the content of the file in a list
f=open("puru.txt","rt")
print(f.readlines())
#o/p ['Puru is a good girl\n', 'Puru is the queen of this universe\n', 'Puru is intelligent']
#ek list print hoga ar list k ander sari lines hogi