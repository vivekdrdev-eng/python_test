# li= ['milk','butter','soda']
# li.pop()
# print(li)
# del li[0]
# print(li)
# print(li)
#assces
# li=['a','b','c']
# print(li[0])
# print(li[-1])
# print(li[-5])
#gengerate
# li=list(filter(lambda x: x % 2 == 1, range(1,100)))
# print(li)
# li=[x ** 2 for x in range(1,11)if x % 2 == 1]
# print(li)
# li=['1','2','8','4','2','6','7','1','9']
# li.sort()
# print(li)
# li=['1','2','8','4','2','6','7','1','9']
# li.reverse()
# print(li)
#count
# li=['1','2','5','4','5','9','7','8','9']
# print(li.count('9'))
# print(li.count('5'))
# loops
# primes=['1','2','3','4','5','6','7','8','9']
# for prime in primes:
#     print(prime)
# animals=['dog','cat','horse','sheep']
# for i,animal in enumerate(animals):
#     print(i,animal)
x=0
# while x<10:
#     print(x)
#     x=x+1
x=0
# for index in range(10):
#     print(index)
#     x=index * 10
#     if index == 6:
#         break
#
#     print(x)
# overdict
# jointdict= {
#     "first_name":"John",
#     "last_name":"Doe",
#     "age":23
# }
# x=jointdict.items()
# print(x)
# for key,value in x:
#     print(f"{key} is {value}")]
#python function
# def hello_world():
#     print("Hello World")
# def add(x,y):
#     print("x is %s and y is %s"%(x,y))
#     return x+y
# add(5,6)
# def varargs(*args):
#     print(args)
#     return args
#
# varargs(1,2,4)
# def keyword_args(**kwargs):
#     print(kwargs)
#
#     return kwargs
# keyword_args(big="foot",  losh="ness")
# pythonfilehandling
# with open("/home/winterfell/pythonwork/mylist.txt.html","r") as file:
#     for line in file:
#         print(line)

# class Animal:
#     def __init__(self, voice):
#         self.voice = voice
#         print(voice)
# cat= Animal("hello")

# cat = Animal('Meow')
# print(cat.voice)    # => Meow
#
# dog = Animal('Woof')
# print(dog.voice)    # => Woof
# import time
#
# def timer(func):
#     def wrapper(*args):
#         start = time.time()
#         result = func(*args)
#         end = time.time()
#         print(f"Took {end-start:2f}s")
#         return result
#     return wrapper
# @timer
# def slow_function():
#     time.sleep(1)
#     return "done!!"
# result = slow_function()


# python utility function

def format_username(first_name,last_name):

    first = first_name.strip().lower()
    last = last_name.strip().lower()
    return f"{first}.{last}"
print(format_username("Vivek","DR"))










