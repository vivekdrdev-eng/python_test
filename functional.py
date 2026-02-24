# lambda function
def square(x):
    return x * x
print(square(3))
add = lambda x : x*x
print(add(3))
def myfunction(n):
    return lambda x : a * n
my_dubbler = myfunction(3)
print(my_dubbler(5))
# map function
# to find the sqrs of this numbers
my_numbers =[]
n = int (input("enter your numbers"))
for i in range(n):
    numbers = int(input(f"enter your numbers:{i+1}:"))
    my_numbers.append(numbers)
    print(my_numbers)
square = list(map(lambda x: x ** 2,my_numbers))
print(square)

def squares(number):
    squared = []
    for num in number:
        square.append(num*num)
    return squared
my_numbers = []
n = int (input("enter your numbers"))
for i in range(n):
    numbers = int(input(f"enter your numbers:{i+1}:"))
    my_numbers.append(numbers)

result = squares(my_numbers)
print(my_numbers)
print(result)

# filter function
my_age = [20,12,32,26,18,50,23]

adults = list(filter(lambda x : x>= 18,my_age))
print(adults)

languages = ["Python", "Java", "C++"]
for l,a in enumerate(languages):
    print(l,a)

names = ["Vivek", "Anu", "Rahul"]
scores = [85, 90, 78]
z = zip(names, scores)
print(tuple(z))


















