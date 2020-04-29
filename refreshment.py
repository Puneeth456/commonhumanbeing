# def f1():
#     return 5
#
#
# a=f1()
# print(a)
#
#
# def f2():
#     return 5
#     return 6
#
#
# b=f2()
# print(b)

#
# def f3():
#     return 5,6
#
#
# c=f3()
# print(c)
# print(type(c))

#
# def f4():
#     yield 5
#     yield 6
#
#
# x,y=f4()
# print(x)
# print(y)
# print(type(x))
#
#
# def f5():
#     yield 5
#     yield 6
#
#
# z=f5()
# print(type(z))

#
#
# def f6():
#     yield 5
#     yield 6
#
#
# g=f6()
# print(next(g))
# print(next(g))


# def f7():
#     yield 5
#     yield 6
#
# a=f7()
# print(a)
#
# for i in a:
#     print(i)

#
#
# def f8():
#     yield 5
#     yield 6
#
#
# b=f8()
# print(next(b))
# print(next(b))


#
# l=[1,2,3,4,5]
# a=iter(l)
#
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
#

#
# s={1,2,3,4,5}
# a=iter(s)
#
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))



# using iterator and generator we can access values only in forward direction.
#

#
# Lambda function are anonymous function
# lambda function will not have a name


#
# def sum(a,b):
#     c=a+b
#     return c
#
# x=sum(1,2)
# print(x)


#
# z=lambda x,y:x+y
# print(z(1,2))

#
# a=lambda x:x%2==0
# print(a(2))
# print(a(3))


# l=[1,2,3,4,5,6,7,8]
#
# a=filter(lambda x:x%2==0,l)
# print(a)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))



# l=[1,2,3,5,6,7,8]
#
# a=list(filter(lambda x:x<6,l ))
# c=iter(a)
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))

#
# def f1():
#     x=20
#     return x
#
#
# c=f1()
# print(c)

#
#
# def f1():
#     def f2():
#         x=20
#         return f2()
#
#
# a=f1()
# print(a)


# def smart_tv():
#     print("smart tv")
#
# def tv():
#     print("tv")
#
#
# tv()
# smart_tv()


# def smart_tv():
#     print("Smart tv")
#
# @tv
# def tv():
#     print("tv")
#
#
# tv()

#
# def smart_tv():
#     print("smart tv")
#
# @smart_tv
# def tv():
#     print("tv")
#
#
# tv()
# smart_tv()
#
#
#
# def smart_tv(tv):
#     print("smart tv")
#
# @smart_tv
# def tv():
#     print("normal tv")
#
#
# tv()
# smart_tv()
#

#
# def smart_tv(tv2009):
#     def waterprooftv(tv2009):
#         print("outside waterproof tv")
#         return waterprooftv()
#
#
# @tv2009
# def tv():
#     print("inside tv")
#
#
# tv()

#
# def smartv(tv):
#     print("inside smart tv")
#
#
# @smarttv
# def tv():
#     print("inside tv")
#
#
# tv()


#
# def smarttv(tv):
#     def waterprooftv(tv):
#         print("inside waterproof tv")
#         return waterprooftv()
#
#
# @smarttv
# def tv():
#     print("inside tv")
#
#
# tv( )
#
# def wtpv(smarttv):
#     print("wtpv")
#
# @wtpv
# def smarttv(tv):
#     print("smart tv")
#
#
# @smarttv
# def tv():
#     print("inside tv")
#
#
# tv()

#
#
# def f1():
#     print("inside f1")
#     return 5
#
# a=f1()
# print(a)


# def f2(a,b):
#     print("inside f1")
#     c=a+b
#     return c
#     return a+b
#
#
# z=f2(1,2)
# print(z)




# def enhancedlogin(func):
#     def loginwithforgot():
#         print("login with forgot")
#         func()
#         return loginwithforgot()
#
#
#
# @enhancedlogin
# def login():
#     print("login with un and pwd")
#
# login()

# def smarttv(jspider):
#     def smartimp():
#         print("smart tv")
#         jspider()
#         return smartimp()
#
#
#
# @smarttv
# def colourtv(qspider):
#     def newimp():
#         print("colour tv implementation")
#         qspider()
#         return newimp()
#
# @colourtv
# def bwtv():
#     print("black and white tv")
#
#
# bwtv()
#
# def againenhancedlogin(func1):
#     def captcha():
#         print("cpatcha")
#         func1()
#         return captcha()
#
#
#
#
# @againenhancedlogin
# def enhancedlogin(func):
#     def loginwithforgot():
#         print("login with forgot")
#         func()
#         return loginwithforgot()
#
#
#
# @enhancedlogin
# def login():
#     print("login with un and pwd")
#
#
# login()
#
#
# l=[1,2,3,"qspiders"]
#
# l[0]=10
# print(l)
# l[10]=100

#
# l=[1,2,3,"qspiders"]
#
# for i in l:
#     print(i)




#
# l=[1,2,3,"qspiders"]
# l1=l.insert(0,"jspiders")

# print(l)

# for var in l1:
#     print(var)

# for var in l:
#     print(var)

#
# l=[1,2,3,"qspiders"]
# l.insert(100,"chumma")
# print(l)

#
#
# l=[1,2,3,"qspiders"]
# l.insert(-10,"tmb")
#
# for var in l:
#     print(var)
#
# l=[1,2,3,"qspiders"]
# l.remove(3)
#
# for var in l:
#     print(var)
#
#
# l=[1,2,3,"qspiders","qspiders"]
# print(l.count("qspiders"))
# print(l.count(3))

#
# l=["python","java","selenium","python","ruby","python"]
# print(l.count("selenium"))



# l=[1,2,3,"q","qspiders"]
# l1=l.append(100)
#
# for var in l:
#     print(var)


#
# l=[1,2,3,"q","q"]
# l1=l.append("chumman")
#
#
# for var in l:
#     print(var)

#
# for var in range(0,102,2):
#     print(var)


# l=[]
# for var in range(2,11,1):
#     j=var**2
#     l.append(j)
#
#
# print(l)
#

#
#
# l=[1,2,3,3,4,4,5]
# l1=[]
#
# for i in l:
#     if i not in l1:
#         l1.append(i)
#
# print(l1)


# l=[1,2,3,3,4,4,5]
# l1=[]
# l2=[]
#
# for i in l:
#     if i not in l1:
#         l1.append(i)
#     else:
#         l2.append(i)
#
#
# print(l1)
# print(l2)
#
# l=[1,2,3,3,4,4,5]
# chumman=list(set(l))
# print(chumman)
#
#
#
# l=[10,20,30,40,50,60]
# print(max(l))

#
# l=[10,20,30,40,50,60]
# l1=[]
#
# max_val=0
# for i in l:
#     if i>max_val:
#         max_val=i
#         l1.append(max_val)
#
# print(l1)

# l=[10,20,30,40,50,60]
# l1=[]
#
# max_val=0
#
# for i in l:
#     if i>max_val:
#         max_val=i
#         l1.append(max_val)
#
# print(l1)

#
# d={'a':1,'b':2,'c':3,'d':4}
# print(d.get('b'))
#
# for i in d.keys():
#     print(i)
#
# for i in d.values():
#     print(i)

#
# for i in d.items():
#     print(i)



# a={'a':1,'c':2,'d':4}
# print(len(a))

# import xlrd
#
# path="G:/My Drive/Partners/FY 20-21/1. April'20/Mid Month/April 20 Payable Mid month.xlsx"
# wb=xlrd.open_workbook(path)
# ws=wb.sheet_by_name("Sheet1")
# var=ws.cell_value(1,1)
# print(var)

# import xlrd
#
# path="G:/My Drive/Partners/FY 20-21/1. April'20/Mid Month/April 20 Payable Mid month.xlsx"
# wb=xlrd.open_workbook(path)
# ws=wb.sheet_by_name("Sheet1")
# var=ws.cell_value(1,1)
# print(var)
#
#
# row_count=ws.nrows
# col_count=ws.ncols
#
# print(col_count)
# print(row_count)

#
# import xlrd
#
# path="G:/My Drive/Partners/FY 20-21/1. April'20/Mid Month/April 20 Payable Mid month.xlsx"
# wb=xlrd.open_workbook(path)
# ws=wb.sheet_by_name("Sheet1")
#
# row_count=ws.nrows
# col_count=ws.ncols
#
# for i in range(row_count):
#     for j in range(col_count):
#         print(ws.cell_value(i,j))


# import xlrd
#
# path="G:/My Drive/Partners/FY 20-21/1. April'20/Mid Month/April 20 Payable Mid month.xlsx"
# wb=xlrd.open_workbook(path)
# ws=wb.sheet_by_name("Sheet1")
#
# row_count=ws.nrows
# col_count=ws.ncols
#
# def read_xl_data(input_val):
#     for i in range(row_count):
#         for j in range(col_count):
#             if (ws.cell_value(i,j)==input_val):
#                 print(ws.cell_value(i+1,j))
#                 break
#
#
# read_xl_data("Amount to be Paid")


# x=20
#
# def f1():
# global x
# x=100
# print("inside f1",x)
#
# def f2():

#
# import logging
#
# logging.debug("debug level information")
# logging.critical("critical value is often")
# logging.error("chumman is very bad")


#
# from selenium import webdrivers
#


# import re
#
# s=input("enter the email Id")
# m=re.fullmatch("[a-zA-Z0-9]*@gmail.com",s)
# if m!=None:
#     print("valid email Id")
# else:
#     print("Invalid email Id")

