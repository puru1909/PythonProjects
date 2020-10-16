# f=open("puru2.txt","w")#agr ye file pehle se hogi to uska content replace ho jayega,
# # ar agr nhi hui to new file banega
# f.write("hcisduhis jgjhs hbcjsdhj")
# #f.close()#agr hmlog n galti se v file ko khol diya h to usko close krna ek achi practice h..
# #iss jitni v resource jo file k sath tied up h wo free ho jayengi
#
# #iss code ko agr hm baar baar run karenge to har baar same content write hoga file m isiliye hm
# #append use krte h
#
# ##########################################################################################
# f=open("puru2.txt","rt")
# content=f.read()
# print(content)
# f.close()
########################################################################################
# f=open("puru2.txt","a")
# #f.write("gvdhc jdbvj djhnk")
# a=f.write("gvdhc jdbvj djhnk\n")#agr hm iss code ko baar baar rerun kre to \n lagane k wajh se ye
# #new line m add hota jayega
# print(a)#ye return karega ki hmlogo ne file m kitne characters write kiye h
# f.close()

#w-write mode ka mtlb hota h ki jo v file m h usko khali kr do arjo ab likha ja rha h usko rakho
#a-append mode ka MTLB HOTA H KI jo file m h usko to rakho hi rakho uskebaad m ye jod do
###########################################################################################
#handle read and write both mode(r+)
f=open("puru2.txt","r+")
print(f.read())
f.write("puru is a good singer\n")
print(f.read())
#also if we rerun this code the write content in the file will get appended
##########################################################################################
# f=open("puru2.txt","w")
# f.write("puru is great")
# f.close()
