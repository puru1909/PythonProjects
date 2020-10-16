#Recursion -> iska mtlb hota h function k ander function ko use krna

# def print2(str):
#     print2(str) #RecursionError: maximum recursion depth exceeded
#     print("This is "+str)
# #print2(puru) #NameError: name 'puru' is not defined
# print2("puru")

#Correct way of using recursion
#factorial
#i/p -> n:Integer
#return : n*n-1*n-2*n-2.....1

#n * n-1 * n-2 * n-3.....1 == n * !(n-1) == n * (n-1) * !(n-2)

# def factorial_iterative(n): #because we have used iteratons to make this code
#     """
#         :param n : Integer-->docstring- always written in the first line of a func
#         :return: n * n-1 * n-2 * n-3.....1---> docstring
#     """
#     fac = 1
#     for i in range(n):
#         fac = fac * (i + 1) # hmlogo ne yha (i+1) isiliye likha h taki fac 0 se multiply naa ho
#     return fac
# n=int(input("Enter the no:"))
# print("factorail using iterative method",factorial_iterative(n))
#
#
# def factorial_rec(n):
#     """
#             :param n : Integer-->docstring- always written in the first line of a func
#             :return: n * n-1 * n-2 * n-3.....1---> docstring
#     """
#     if n==1 or n==0:
#         return 1
#     else:
#         return n * factorial_rec(n-1)
# n=int(input("Enter the no:"))
# print("factorail using recursive method",factorial_rec(n))

# logic of factorial_rec()
# # 5 * factorial_rec(4)
# 5 * 4 * factorial_rec(3)
# .
# .
# .
# 5 * 4 * 3 * 2 * 1


#quiz to cqlculate nth fibonacci no
#0 1 1 2 3 5 8 13

def fibo_rec(f):

    if f == 0 or f == 1:
        return 0
    elif f == 2:
        return 1
    else:
        return (fibo_rec(f-1) + fibo_rec(f-2))

f = int(input("enter the no to calc fibonacci"))
print(fibo_rec(f))

#which one to use recursion or iterative?
# 1. Recursion m debugging krne m problem ho skti h...backtrace krna thoda
# difficult h as compare to iterative

# 2. but iterative m no of lines of code thoda zada hota h,so simple cheeze jaha
# krni h wha recursion use krna best hota h







