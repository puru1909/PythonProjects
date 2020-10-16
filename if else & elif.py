#max min
# print("enter 2 nos")
# a=input()
# b=input()
#
# if(int(a)>int(b)):#iss colon ka mtlb h ki hmlog iss if statement k ander ghusna chante h
#     print("a is max")
# elif(int(a)==int(b)):#we use elif because agr 1st if stmt true hota to hmnhi chahte h ki wo next if m jaye isiliye we use krte h elif, ki agr if wala stsmt true nhi h tbhi wo elif m jaye warna naa jaye
#     print("a is equal to b")
# else:
#     print("b is max")

lst=[8,7,3,4]
#IN Keyword
#print(4 in lst)#will give true
# if 6 in lst:
#     print("yes")
# else:
#     print("no")
#print(4 in lst)#will give true
#NOT IN Keyword
# 2

#quiz-
print("Pls enter ur age")
age=int(input())
if(age>18 and age<101):
    print("yes u r eligible for driving")
elif(age==18):
    print("we can't decide ,pls visit our driving school and get urself tested")
elif(age>7 and age<18):
    print("ur age is less than 18")
else:
    print("illogical age")

