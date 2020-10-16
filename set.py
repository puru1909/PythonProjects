s=set()#empty set
print(type(s))
#creation of set from list
set_from_list=set([1,2,3,4])
print(set_from_list)
print(type(set_from_list))
#we can do like this as well
l=[1,2,3,4]#first create a list
s_from_lst=set(l)#then assign the list to set
print(type(s_from_lst))
# adding elements in the blank set that we have created earlier
s.add(6) #will give 6
s.add(6) #will not get added as 1 is already present in the set
s.add(9)
s1=s.union({6,9,8})
print(s,s1)
s2=s.intersection(s,s1)
print(s2)
#max,min,type,len,difference,symmetric diff,disjoint
s3=s.isdisjoint(s1)
print(s3)
#remove from set
s.remove(6)
print(s)