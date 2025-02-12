def generate_squares(N):
    """Генерирует квадраты чисел до N"""
    for i in range(N + 1):
        yield i ** 2

def even_numbers(n):
    """Генерирует чётные числа от 0 до n"""
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

def divisible_by_3_and_4(n):
    """Генерирует числа, делящиеся на 3 и 4, от 0 до n"""
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

def squares(a, b):
    """Генерирует квадраты чисел от a до b"""
    for i in range(a, b + 1):
        yield i ** 2

def countdown(n):
    """Генерирует числа от n до 0"""
    for i in range(n, -1, -1):
        yield i