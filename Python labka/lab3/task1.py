# 1
class StringHandler:
    def __init__(self):
        self.s = ""
    
    def getString(self):
        self.s = input("Введите строку: ")
    
    def printString(self):
        print(self.s.upper())

# 2
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        return self.length ** 2

# 3
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

# 4
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"({self.x}, {self.y})")
    
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    
    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

#5
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} добавлено. Новый баланс: {self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств!")
        else:
            self.balance -= amount
            print(f"{amount} снято. Новый баланс: {self.balance}")

# 6
is_prime = lambda x: x > 1 and all(x % i != 0 for i in range(2, int(math.sqrt(x)) + 1))

numbers = [10, 15, 17, 19, 21, 23, 29]
prime_numbers = list(filter(is_prime, numbers))
print("Простые числа:", prime_numbers)