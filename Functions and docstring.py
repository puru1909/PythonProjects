# a=9
# b=8
# #built in func
# c= sum((a,b))#sum k ander ya to list hona chahiye ya tuple hona chahiye mtlb koi iterable honi chahiye
# print (c)

#user defined func

# def func1():
#     print("hello aapka func1 m swagat h")
# print(func1())
# # o/p
# # hello aapka func1 m swagat h
# # None
# func1()# o/p without print (hello aapka func1 m swagat h)

# def func2(a,b):
#     print("hello u r in func2",a+b)
#
# def fun3(a,b):
#     avg=(a+b)/2
#     print(avg)#o/p-4.5
# #fun3(4,5)
# v=fun3(8,9)
# print(v)#o/p-none because hmlog func m kuch return return nhi kr rhe h

def fun4(a,b):
    """This s the func to calc multiplication of two nos are works best for 2 nos"""
    mul=a*b
    return mul
v2=fun4(7,6)
print(v2)#o/p-42
#return statement in a func is optional
#argument in the input is also optional

#Docstring
#function k ander pehli line k taur pe jo string likhi jati h usko bolte h docstring
print(fun4.__doc__)#O/P This s the func to calc multiplication of two nos
#DOCSTRING HMLOG ISISLIYE LAGATE H qki hamare code m humlog bhot sare functions use krte h
# ar hme yaad nhi h ki kon sa function kya kaam krta h,
# ya ye ho skta h ki hamara code ko koi ar use kr rha h
# to hm docstring m instructions daal skte h ki ye code kaise use kre

