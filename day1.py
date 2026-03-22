#STRING
# print('xyz')

# #multiple lines
# print('''multiple
# lines lolsies''')

# #new line
# print('\ntesting new line')

#MATH
# print(50 ** 2)#exponent
# print(50 % 7)#remainder
# print(50/6)#division w remainder
# print(50//6)#division w no remainder


#VARIABLES AND METHODS
# fight = 'Anakin500 this is just a test'

# print(fight.upper())#upper case
# print(fight.lower())#lower case
# print(fight.title())#first letter capital
# print(len(fight))#counts characters including spaces

# print(int(30.9))#only consideres whats on left side


#FUNCTIONS
# def addition(num):
#     num += 100
#     print(num)
# addition(500)

# def addition(num):
#     num += 100
#     return num
# print(addition(500)) 

# def multiple(x,y):
#     print(x+y)
# multiple(5,5)


#BOOLEAN AND RELATIONAL OPERATORS
# bool1 = True
# bool1 = not True
# bool2 = 4 == 5
# print(bool1,bool2)
# print(type(bool1))
# print(bool1)

#CONDITIONAL STATEMENTS
# def food(money):
#     if money > 5:
#         print('Thats a lot of money lol')
    
#     elif money == 5:
#         print('eh thats ok')

#     else:
#         print("Broke ahh")

# food(5)

#LISTS
# letters = ['a','b','c','d','e','f']
# print(letters[0])
# print(letters[1:4])

# print(letters[1:])
# print(letters[:2])
# print(letters[-1])#last item

# print(len(letters))
# letters.append('g')

# print(letters)
# letters.insert(len(letters),'z')
# print(letters)

# letters.pop()
# print(letters)

# numbers = [1,2,3]
# print(letters + numbers)

# Grades = [['abdul',100],['ziyan',0]]
# Ziyan_Marks = Grades[1][1]
# print(Ziyan_Marks)
# Ziyan_Marks = 40#Changeable
# print(Ziyan_Marks)

#TUPLES - immuteable
# grades = ('a','b','c','d','e')

# print(grades[0])

#LOOPS

#FOR LOOP
# grades = ['a','b','c','d','e']
# for marks in grades:
#     if marks == 'b':
#         continue
#     print(marks)

# grades = ['a','b','c','d','e']
# for marks in grades:
#     if marks == 'b':
#         break
#     print(marks)

# grades = ['a','b','c','d','e']
# for x in range(2,11,2):
#     print(x)

# else:
#     print("done")

#WHILE LOOP
# i = 6
# while i >= 1:
#     print(i)
#     i-=1
# else:
#     print('done')


# while i >= 1:
#     if i == 3:
#         break
#     print(i)
#     i-=1
# else:
#     print('done')


# while i >= 1:
#     i-=1
#     if i == 3:
#         continue    
#     print(i)
    
# else:
#     print('done')

# #ADVANCED STRINGS
# my_name = 'Abdulhady Nawab'
# print(my_name[10].lower())
# print(my_name[-1].upper())

# sentence = 'Hi my name is, Abdulhady'
# # print(sentence.split())
# # print(sentence.split(','))
# sentence_split = sentence.split()
# print(sentence_split[0])
# sentence_join = " ".join(sentence_split)
# print(sentence_join)

# # print("He said \"give me all ur money\" ")

# space = '    lol    '
# print(space.strip())

# print("a" in "Apple")#FALSE
# print("A" in "Apple")#TRUE

#DICTIONARIES
# drinks = {
#     'cola': 5, 'dhola': 'Ziyan'
# }
# print(drinks)
# College = {
#     'CSE' : ['abdul','ziyan','himanshu'],
#     'Bio' : ['bingi','aatif'],
#     'Aviation' : ['owais','suwani']
# }
# print(College.keys())
# print(College.values())
# del College['Aviation']
# print(College)
# College['Bio'] = ['bingi','aatif','dingi']#adding or updating stuff in dict
# print(College['Aviation'])
# print(College)

#LOOPING OVER DICTIONARY
# for key in College:
#     print(key)

# for key,value in College.items():
#     print(f'{key} : {value}')

#IMPORTING
# import sys
# from datetime import datetime as dt
# print(sys.version)
# print(dt.now())

#USER INPUT
# name = input("Whats ur name?\n")
# print(name)

# x = float(input('Enter first number: '))
# y = float(input('Enter second number: '))
# o = input('Enter operator to use')

# if o == '+':
#     print(x+y)
# elif o == '-':
#     print(x-y)
# elif o == '/':
#     print(x/y)
# elif o == '*':
#     print(x*y)
# else:
#     print('Not valid')


