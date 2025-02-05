import math
import random
from itertools import permutations

# 1. Конвертация граммов в унции
def grams_to_ounces(grams):
    return grams * 28.3495231

# 2. Конвертация температуры из Фаренгейта в Цельсий
def fahrenheit_to_celsius(f):
    return (5 / 9) * (f - 32)

# 3. 
def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if 2 * chickens + 4 * rabbits == numlegs:
            return chickens, rabbits
    return None

# 4. Фильтрация простых чисел
def filter_prime(numbers):
    is_prime = lambda x: x > 1 and all(x % i != 0 for i in range(2, int(math.sqrt(x)) + 1))
    return list(filter(is_prime, numbers))

# 5. 
def string_permutations(s):
    return [''.join(p) for p in permutations(s)]

# 6. Разворот слов в строке
def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])

# 7. Проверка на наличие 3 рядом с 3
def has_33(nums):
    return any(nums[i] == nums[i + 1] == 3 for i in range(len(nums) - 1))

# 8. Проверка наличия 007 в списке
def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if not code:
            return True
    return False

# 9. Вычисление объема сферы
def sphere_volume(radius):
    return (4/3) * math.pi * radius ** 3

# 10. Уникальные элементы списка
def unique_elements(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

# 11. Проверка на палиндром
def is_palindrome(word):
    return word == word[::-1]

# 12. Вывод гистограммы
def histogram(lst):
    for num in lst:
        print('*' * num)

# 13. Игра "Угадай число"
def guess_the_number():
    name = input("Hello! What is your name? ")
    number = random.randint(1, 20)
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    guesses = 0
    while True:
        guess = int(input("Take a guess.\n"))
        guesses += 1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break

# 14. Импорт функций в другой файл
if __name__ == "__main__":
    print("Простые числа из списка: ", filter_prime([10, 15, 17, 19, 21, 23, 29]))
