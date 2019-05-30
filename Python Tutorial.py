# birth_year = int(input("Birht year:"))
# age = 2019  - birth_year
# print(age)

# weight_lbs = int(input("weight (lbd):"))
# weight_kq = round(weight_lbs*0.45,0)
# print(type(weight_kq))

# indexing
# name = 'ilham'
# copying
# take_two = name[:]
# print(name[1:-1])
# print(take_two)

# f print
# try:
#     first = str(input("first:"))
#     last = str(input("last:"))
#     print(f'{first} {last}')
# except:
#     print("invalid char")


# string methods
# uni = 'unec'
# print(len(uni))
# print(uni.upper())
# for a in uni:
#     if 'u' in a:
#         print(a.upper())
# uni.upper
# uni.lower
# uni.title
# uni.find
# uni.replace
# '' in uni

# math functions
x = 9
y = -4
# print(round(x))
# print(abs(y))

# import math
# print(int(math.sqrt(x)))


# price = 10000
# has_good_credit =False

# if has_good_credit:
#     down_payment =  0.1 *price
# else:
#     down_payment = 0.2 *price

# print(f"Down_payment: ${down_payment}")

# Conditional Operator AND OR BOTH

"""def conv(num="1 ton = 1000 kq"):
# kq_to_ton = 1
# ton_to_kq = 2
    while True:
        try:
            prompt = int(input("For KQ to TON type 1, for TON to KQ type 2:"))
            if prompt == 1 or 2:
                continue
            else:
                break
        except:
            print("invalid char")

        try:
            num = int(input("number:"))
        except:
            pass
        if prompt == 1:
            return num/1000
        else:
            return num*1000 
        

print(conv())"""

# num = 1

# while num<=5:
#     num+=1

# import random
# pc_num = random.randint(1,10)
# try:
#     for guess in range(5):
#         num = int(input("enter your guess:"))
#         if num == pc_num:
#             print("You were right")
#             break
#         else:
#             print(f'Your guess was {num} but i guessed {pc_num}')

# except:
#     print("Invalid char")

'''
# car game
command = ""
started = False
stopped = False


# while command.upper()!="QUIT"
while command != "quit":
    command = input(">").lower()
    if command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car started!!")
    elif command == "stop":
        if stopped:
            # if not started
            print("Cat is already stopped")
        else:
            stopped = True
            print("Car stopped!")
    elif command == "help":
        print("""
        start - to start the car
        stop - to stop the car
        quit - quit 
        """)
    elif command == "quit":
        break
    else:
        print("Type valid commant")

'''

        
#  for loop
'''
for item in range(1,20,2):
    print(f'{item}\n')

prices = [10, 20, 30]
total = 0
for price in prices:
    total = total+price

print(total)

nested loop
for x in range(4):
    for y in range(3):
        print(f"({x},{y})")
'''


# lists
'''numbers = [3, 6, 2, 8, 4,10]
max_num  = numbers[0]
for number in numbers:
    if number>max_num:
        max_num = number
print(max_num)
'''

#  2D list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

# print(matrix[0][0])
'''for row in matrix:
    for item in row:
        print(item)
        '''


'''
# list methods
numbers = [5, 2, 1,7, 4]
numbers.append(12)
numbers.insert(0,28)
# numbers.clear()
numbers.pop(0)
numbers.index(5)
print(numbers.count(1))
print(numbers.sort())
print(12 in numbers)
print(numbers.reverse)
print(numbers)
new_list =numbers.copy()
numbers.append(10)'''

'''
nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

var1 = []
for num in nums:
    if num not in var1:
        var1.append(num)
print(var1)

'''


# tuple
# nums = (1, 2, 3)
# print(nums.count())

# unpacking
# coordinates = (1, 2, 3)
# x, y, z = coordinates

# dicts

# customer = {
#     "name" : str(input("name:")),
#     "age" : int(input("age:")),
#     "validity" : True
#  }
# print(customer.get("name" , "N"))

# phone = input("Phone")
# num = {
#     "1" : "one",
#     "2" : "two",
#     "3" : "three",
#     "4" : "four",
# }
# output = ""
# for a in phone:
#    output += num.get(a, "error") + ","
# print(f"{output}")

# def square(number):
#     # return number * number
#     print(number*number)
# print(square(3))

# try:
#     number = int(input(">"))
#     print(square(number))
# except:
#     print("error")


# class Point:
#     # pascal naming convention
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def move(self):
#         print("move")   
#     def draw(self):
#         print("draw")

# point1 = Point(10, 20)
# print(point1.x)

# class Person():
#     def __init__(self, name):
#         self.name = name
#     def talk(self):
#         print (f"Hi, {self.name}")

# name = Person(str(input(">")))
# name.talk()


class Mammal:
    def walk(self):
        print("walk")
class Cat(Mammal):
    pass
class Dog(Mammal):
    def bark(self):
        print('bark')

dog1 = Dog()
dog1.bark()
cat1 = Cat()
cat1.walk()