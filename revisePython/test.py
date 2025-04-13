# #comments

# #data types


# """
# gdrzgdg
# """

# '''
# kgdrgdg'''

# #datatype

# print(type('hi'))
# print(type(1))
# print(type(1.1))
# print(type(True))
# print(type([1,2,3]))
# print(type((1,2,3)))
# print(type({'name':'john'}))
# print(type(None))
# print(type(1+2j))


# #operators

# #Arithmetic Operators:

# a, b = 1, 3

# print(a + b)  # Addition: 1 + 3 = 4
# print(a - b)  # Subtraction: 1 - 3 = -2
# print(a * b)  # Multiplication: 1 * 3 = 3
# print(a / b)  # Division: 1 / 3 = 0.3333...
# print(a // b) # Floor Division: 1 // 3 = 0
# print(a % b)  # Modulus: 1 % 3 = 1
# print(a ** b) # Exponentiation: 1 ** 3 = 1


# #Comparison Operators:

# print(a == b)  # Equal to: False
# print(a != b)  # Not equal to: True
# print(a > b)   # Greater than: False
# print(a < b)   # Less than: True
# print(a >= b)  # Greater than or equal to: False
# print(a <= b)  # Less than or equal to: True

# #Logical Operators:

# print(a and b)  # Logical AND: 1 (since both are non-zero)
# print(a or b)   # Logical OR: 1 (since 'a' is non-zero)
# print(not a)    # Logical NOT: False (since 'a' is non-zero)

# #Identity Operators:

# print(a is b)       # Identity: False
# print(a is not b)   # Not Identity: True

# #Membership Operators:

# print(a in [1, 2, 3])       # Membership: True
# print(a not in [1, 2, 3])   # Not Membership: False

# #Bitwise Operators:

# print(a & b)   # Bitwise AND: 1 & 3 = 1
# print(a | b)   # Bitwise OR: 1 | 3 = 3
# print(a ^ b)   # Bitwise XOR: 1 ^ 3 = 2
# print(~a)      # Bitwise NOT: ~1 = -2
# print(a << b)  # Bitwise left shift: 1 << 3 = 8
# print(b >> a)  # Bitwise right shift: 3 >> 1 = 1

# #Assignment Operators:

# a = 1
# a += b  # Equivalent to a = a + b; a becomes 4
# a -= b  # Equivalent to a = a - b; a becomes 1
# a *= b  # Equivalent to a = a * b; a becomes 3
# a /= b  # Equivalent to a = a / b; a becomes 1.0
# a //= b # Equivalent to a = a // b; a becomes 0.0
# a %= b  # Equivalent to a = a % b; a becomes 0.0
# a **= b # Equivalent to a = a ** b; a becomes 0.0


# # a = 1
# b = 2.5


# print(a + b)

# userInput = map(int,input("Enter Numbers: ").split(' '))

# print(sum(userInput))

# userInput = int(input("Enter Numbers: "))

# print(userInput * userInput)

# userInput = list(map(float,input("Enter Numbers: ").split(' ')))

# print((userInput[-2] + userInput[-1]) / len(userInput))


# userInput = list(map(int,input("Enter Numbers: ").split(' ')))

# print(userInput[0] >= userInput[1])

# str1 = "Hello"
# str2 = "World"

# print(str1 + ' ' + str2)

# #escape sequence

# print("Hello\nWorld")
# print("Hello\tWorld")

# str3 = "Hello\tWorld"
# print(len("Hello\tWorld"))
# print(len(str3))

# #indexing

# print(str3[10])

# #negative indexing

# print(str3[:-1])

# #slicing

# print(str3[10:12])

# print(str3.replace('Hello','Hi'))

# userInput = input("Enter String: ")

# print(len(userInput))

# print(userInput.count('r'))

# #conditional statements

# import asyncio
# import datetime as dt

# startTime = dt.datetime.now()


# async def my_async_function():
#     await asyncio.sleep(3.5)
#     return "Async function finished!"


# # Running the async function


# print(asyncio.run(my_async_function()))
# endtTime = dt.datetime.now()

# print(endtTime - startTime)

# nesting

# alisAge = 15
# bobAge = 20
# aliBrotherAge = 17

# if alisAge >= bobAge:
#     print("Ali is older than Bob")
#     if aliBrotherAge < alisAge:
#         print("Ali is older than his brother")
#     else:
#         print("Ali is younger than his brother")
# else:
#     print("Bob is older than Ali")


# userInput = int(input("Enter Number: "))

# if userInput % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# one max num
# userInput = list(map(int, input("Enter Number: ").split()))
# max3 = max(userInput)
# print(max3)

# three or many max numbers

# maxNumbers = 3
# unqiueList = []

# while maxNumbers > 0 and userInput:
#     maxValue = max(userInput)
#     if maxValue not in unqiueList:
#         unqiueList.append(maxValue)
#         maxNumbers -= 1
#     userInput = [x for x in userInput if x != maxValue]

# print(unqiueList)

# userInput = list(map(int, input("Enter Number: ").split()))

# a, b, c = userInput
# print(min(a,b,c))
# print(a if a >= b and a >= c else b if b >= a and b >= c else c)

# divisible = []
# for i in userInput:
#     if i % 7 == 0:
#         divisible.append(i)
#     else:
#         pass
# print(divisible)

# list

# lst = [1,2,4,5,55,64,8,89,89,456,4,89,89]

# lst[12] = 100
# #list comprehension

# print(lst)
# removed89 = [x for x in lst if x != 89]

# print(removed89)
# #list slicing

# lst[0:4] = [100,0,15,54]
# print(lst[0:4])

# float1 = 12
# toStr = str(float1)
# toList = list(map(int,[x for x in toStr ]))
# print(toList)

# lst = [1]
# print(lst)
# print(type(lst))

# #tuple

# tup = (1) # not correct , this will be integer as python will consider this as integer
# print(type(tup))
# tup1 = (1,) # correct
# print(type(tup1))

# userInput = list(map(str, input("Enter Three names: ").split()))
# print(userInput)

# userInput = list(input("Enter Three names: ").split())
# print("Yes" if userInput == userInput[::-1] else "No")  # To reverse the list or anything we can use this [::-1]

# w = ""
# for i in userInput:
#     w = i + w

# if (userInput == w):
#     print("Yes")
# else:
#     print("No")

# newInput = []

# for i in userInput:
#     newInput.append(i)
# print(newInput[::-1] == userInput)

# tup = ["C","D", "A", "A", "B", "B", "A"]

# print(tup.count("A"))

# gradesList = sorted(tup)
# print(list(gradesList))c


# integer = 5
# floating = 0.1
# string = "string"
# complex = 2j
# boolean = True
# list1 = [1, 2, 3]
# tuple1 = (1,), (1, 2, 3)
# dictionary = {"name": "Mubarak", "age": 25}
# noneType = None
# set1 = {1, 2, 3}
# frozenset1 = frozenset[{1, 2, 5}]


# for i in range(1,integer + 1):
#     print(i)

# check number is prime or not


# whichOne = ["prime", "armstrong", "palindrome"]

# primes, armstrong, palindrome = [], [], []


# def CheckPAP():
#     checkInput = input("Enter To Check If It is Prime or not : ")

#     userInput = input(
#         "Enter Number To Check If It Is Prime, Armstrong, Palindrom Or not: "
#     )
#     if checkInput == whichOne[0]:
#         for i in range(2, (int(userInput) // 2) + 1):

#             if int(userInput) % i == 0:
#                 print("Not Prime")
#                 break
#             else:
#                 primes.append(i)
#             return primes

#     elif checkInput == whichOne[1]:
#         if userInput == sum([int(userInput) ** 3 for i in userInput]):
#             armstrong.append(i)
#         else:
#             print('Not Armstrong')
#         return armstrong
#     elif checkInput == whichOne[2]:
#         if userInput == userInput[::-1]:
#             palindrome.append(i)
#         else:
#             print("Not Palindrome")
#         return palindrome
#     else:
#         print("Invalid Input")


# print(CheckPAP())

# dictionary

myDetails = {
    "name" : "Mubarak",
    "age" : 25,
    "surname" : "Dalvi",
    "address": "Mumbai",
    "isMale": True,
    "bg": "O+"
}

# for i in myDetails:
#     print(i, myDetails[i])

# myDetails.update({"name": "Mubarak Dalvi"})

# lst = list(myDetails.values())

# var1 = lst[0] = "Mubarak Dalvi"
# print(var1)

# set1 = {1,2,45,4,6,4,8}

# for i in set1:
#     print(i)

# set1.add(100)

# print(set1)

# tolst = list(set1)

# for i in tolst:
#     print(i)


#nested list tuple dict 

# nlst = [1,2,4,5,4,[1,2,5,4,5,5,6,],1424,6,45,]
# print(nlst)
# #to print specific from nested list
# print(nlst[5][-1])

# ntup = (1,2,4,5,4,(1,2,5,4,5,5,6,),1424,6,45)
# print(ntup)

# ndict = {"name" : "Mubarak", "age" : 25, "surname" : "Dalvi", "address": {
#     "city": "Mumbai", "state": "Maharashtra", "country": "India"
# }, "isMale": True, "bg": "O+"}

# print(ndict)

# nset = {1,2,4,5,4,(1,2,5,4,5,5,6,),1424,6,45}
# print(nset)


# print(ndict.get("address").get("city"))

# # match case
# n = 3
# match n:
#     case 1: 
#         print("one")
#     case 2:
#         print("two")
#     case 3:
#         print("three")
#     case _:
#         print("default")


# print(ndict.fromkeys("Mubarak"))

#pract 

# pdict = {}

# pdict["cat"] = "meow"
# print(pdict)

# pdict["table"] = "a peice of furniture", "a table in a database"

# print(pdict)


# print(len({"python","java","c++","python","javascript","java","python","java","c++","c"}))

# dict1 = {}

# userInput = list(input("Enter Subject name followed by its matks obtain: ").split())

# for i in range(0,len(userInput),2):
#     dict1[userInput[i]] = userInput[i+1]

# print(dict1)


# print({("int",9),("float",9.0)})

# num1 = 100
# num2= 1

# while num2 < num1:
#     print(num2)
#     num2 += 1

# print(num2)

# print('-----------------------')

# while num1 > 1:
#     print(num1)
#     num1 -= 1

# print(num1)

# mulnum = int(input('Enter Number: '))

# while mulnum <= mulnum * 10:
#     print(mulnum)
#     mulnum *= 2



#recusive functions 
#factorial
# lst = []

# def fac(num):
#     if num == 1:
#         return 1
#     else:
#         lst.append(num)
#         return num * fac(num - 1)
    
# print(fac(5))
# print(lst)

# n = int(input("Enter Number: "))

# for i in n:
#     summ += i
# print(summ) 

# count = 0
# while count < len(n):
#     summ += n[count]
#     count += 1

# print(summ)

# factorial
# fac = 1
# while n > 1:
#     fac *= n
#     n -= 1
# print(fac)

# fac = 1
# for i in range(1,n+1):
#     fac *= i
# print(fac)

# def calc(*args):
#     return sum(args)

# print(calc(1,2))


def avg (*args):
    return sum(args) / len(args)

print(avg(1,2,3,4,5,6,7,8,9,10))


def convertor(usd):
    inr = 83.5
    return f"${usd * inr}"

print(convertor(100))