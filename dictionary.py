#dictionary is a key value pairs
d1={}
print(type(d1))
d2=[]
print(type(d2))
d3=()
print(type(d3))
d4=(1)#even if we are keeping one element in tuple we have to add ,
print(type(d4))
d5={"aman":"games","sonal":"ladai","guddu":"sutai"}
print(d5)
print(d5["aman"])#give the value for aman key
d6={"aman":"games","sonal":"ladai","guddu":"sutai","mummy":{"morng":"brkfast","noon":"lunch","nyt":"dinner"}}#dictionary ka value ham dictionary daal skte h(nested dictionary
print(d6)
print(d6["mummy"])
print(d6["mummy"]["nyt"])#mummy ka nyt ka value print hoga
#dictionary k values list v ho skte h,tuple v ho skte h ar dictionary v ho skte h but keys immutable type ki honi chahiye it can v nos or string bt it shud be immutable
#adding a key in dictionary
d5["papa"]="work"
print(d5)
d5["kutu"]="bhaw bhaw"
print(d5)
# if the name of kutu gets changed to tiger old one will not get override but a new key will get generated
d5["tiger"]="bhaw bhaw"
print(d5)
#deleting elements from a dictionary
del d5["kutu"]
print(d5)
#dictionary functions
d7={"a":"aa","b":"bb"}
d8=d7#d8 will not create a new copy of d7,will simply refer to d7 so if we delete any key from d8, that key will get deleted from d7 as well
#print(d8)
del d8["a"]
print(d7)
#to avoid this we use copy func,it will return a shallow copy
d9=d7.copy()
print(d9)
del d9["b"]
print(d9)#empty
print(d7)
print(d5.get("sonal"))#gives the value for sonal
d5.update({"kuchu":"puchu"})
print(d5)
print(d5.keys())
print(d5.items())


#Create a dic and take input from the user and return the meaning if the word from the dic.

mydict={"soap":"used for bathing","towel":"to wipe water","glass":"to drink water","chips":"fast food"}
print(type(mydict))
print("Please enter a string to find is meaning")
x=input()
#print(mydict[x])
print(mydict.get(x)) #both are correct
