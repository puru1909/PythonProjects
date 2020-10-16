# Lambda functions or anonymous functions
# 1. It is a function without name
# 2.It should have only one expression
# 3.It can take multiple arguments
# def minus(x,y):
#     return x-y
# print(minus(8,7))

# minus = lambda x,y : x-y #one liner function
# print(minus(8,7))

# Both are same only.

##################################################################################################
#Uses of lambda function filter, map and reduce
nums=[4,5,8,2,7,1,6,9,10]
# way 1 :
# def is_even(n):
#     return n%2==0 :
#
# iss func ko bss fiter k sath hmlog ko use krna tha ar khi nhi..so y to write such
# long code jb hame iss reuse nhi krna h to ham lambda func use kr skte h

#way 2:
is_even = lambda n :n%2==0
#program to fetch all the even nos from this list:
#so here we are using an inbuilt method called filter which will take a function (to decide on what basis we need to filter)
#and a iterable it can be list tuple or anything..(to decide on which item we have to apply the filter)
evens=list(filter(is_even,nums))
print(evens)

#or

even=list(filter(lambda n :n%2==0,nums))
print(even)
########################################################################################
# 2.map : lets say we got all the even nos and our job is to double the nos
# in simple words whenever we want to change each value in an iterable(list,tuple..)
# we use
# if map:
#
# #this is same as big data concept we take a chunk of data and we
# filter the data , then we map it and try to reduce it.

