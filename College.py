#DECORATOR
#PRINT MSG BEFORE AND AFTER EXECUTION
# def decorator(func):
#     def wrapper():
#         print("Before execution")
#         func()
#         print("After execution")
#     return wrapper

# @decorator
# def greet():
#     print("Hello World!!")

# greet()

#CONVERTS RETURN VALUE OF FUNC TO UPPERCASE
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result.upper()
#     return wrapper

# @decorator
# def smth(word):
#     return word

# name = input("What is your name?")
# print(smth(name))

#COUNTS THE NUMBER OF TIMES A FUNCTION IS CALLED
# def counts(func):
#     def wrapper(*args, **kwargs):
#         wrapper.counter += 1#function has variable called counter
#         func(*args, **kwargs)
#         print(f'The function has been called {wrapper.counter} times')

#     wrapper.counter = 0    
#     return wrapper

# @counts
# def greet(name):
#     print(f'Hi {name}')

# names = input("What is your name?\n")
# greet(names)

#LOGS FUNCTION NAME AND ITS ARGUMENTS
# from functools import wraps

# def Log_Info(func):
#     @wraps(func)#TO PRESERVE DATA OF FUNC CUZ WE WANNA PRINT NAME OF FUNC
#     def wrapper(*args,**kwargs):
#         print(f'Name of function is{func.__name__}')
#         print(f'Positional arguments is {args}')
#         print(f'Keyword argument is {kwargs}')
#         print(func(*args,**kwargs))
#     return wrapper

# @Log_Info
# def add(a,b):
#     return a + b

# add(2,3)

#DISPLAY EXECUTION TIME OF FUNCTION
# from functools import wraps
# import time

# def Execution_Time(func):
#     @wraps(func)
#     def wrapper(*args,**kwargs):
#         start_time = time.time()
#         result = func(*args,**kwargs)
#         end_time = time.time()
#         print(f'The execution time is{end_time - start_time}')
#         print(result)
#     return wrapper

# @Execution_Time
# def add(a,b):
#     return a + b

# add(2,3)

#