# list1=["abc","gcj","gcjhgc","cbjh"]
# #print(list1)
# for i in list1:
#     print(i)
#
# tp=("hdch","dnckn","jbc")
# for j in tp:
#     print(j)
# print(type(tp))

#list of list
l2=[["a",1],["b",2],["c",3]]
# for item in l2:
#     print(item)

# for item,num in l2:
#     print(item,num)#unpcking a list
#
dict1 = dict(l2)
# for item,num in dict:
#     print(item,num)#will through an error

# for item,num in dict1.items():
#     print(item,num)

#only for keys
# for item in dict1:
#     print (item)

#only for values
# for item in dict1:
#     print (dict1[item])

#task - item ko tabhi print kro jab r or y m end hota ho
#quiz-create a list and check whether it is a no and if use check whether it is greater than 6

#my sol(incorrect)
# list3=["jcjsh","djhcks",8,0,2,"jhdck",6,"jd",4]
# for i in list3:
#     if(i>=0 and i>6):
#         print("yes it is a no and greater than 6",i)
#     elif(i>=0 and i<6):
#         print("yes it is a no but not grter than 6",i)
#     else:
#         print("it is a string",i)

#harry's solution
# list4=["jcjsh","djhcks",8,0,2,"jhdck",6,"jd",4]
# for j in list4:
#     #string.isnumeric()
#     #Input : string = '1889345'
#     #Output : True
#     #isnumeric() is a built-in method used for string handling.
#     # The issnumeric() methods returns “True” if all characters in the string are numeric characters,
#     # Otherwise, It returns “False”.
#     if(str(j).isnumeric() and j>6):
#         print(j)
#
#2nd method

ll=["jbj","dhjd",0,8,5,7,"cjk"]
for item in ll:
    if(type(item) == int and item>6):
       print(item)

