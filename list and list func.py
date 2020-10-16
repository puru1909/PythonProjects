market=["soap","surf","glue","pen",9]#mixed list=strings+numbers
print(market)
#print(market[5])#will show error as there is no element in 5th index in this list,index starts from 0
print(market[3])
nos=[7,3,4,6,3]
print(nos)
print(nos[2])
nos.sort()
print(nos)#original list ko sort karke usi ist m store kr deta h
nos.sort()
nos.reverse()#sort k baad reverse likhne pe sorted reverse milega nos.
print(nos)
print(nos.sort())#will return none
#list slicing-it will again return a list bt that list will be the new one
print(nos[0:4])
print(nos[:4])
print(nos[:])
print(nos[1:])
print(nos)#original list will remain as it is, bt in case of sort or reverse original list will get changed
#extended slice
print(nos[::])
print(nos[::2])#skip once
print(nos[::3])#skip twice
print(nos[::-1])
print(nos[::-3])#negative indexing more than 1 tabhi result detah jabhmlog :: k pehle kuch naa likhe
print(nos[1:3:-5])#otherwise it will give blank list
print(nos[1:4:-1])
#list func
#nos.append(76)#add 76 at the end of the list
#nos.insert(1,56)#adds 56 at 1st index
#nos.remove(4)
#nos.pop()#deletes one element from the end
nos[1]=98#we can change the value of list
print(nos)
#mutable-can change(list)
#immutable-cannot change(tuple)

tp=(1,2,3)
print(tp)
#tp[1]=6#gives error as we can't change a tuple once created
tpp=(1)#will give 1 without brackets isiliye ek v element rakhna h tuple m to , lagana hoga
print(tpp)
tpl=(1,)
print(tpl)

# traditional swaping
a=1
b=9
a,b=b,a #swapping in python
#temp=a
#a=b
#b=temp
print(a,b)
#


