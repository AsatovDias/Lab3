# Задание 1: Калькулятор с использованием условных операторов
# Ввод двух чисел
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

# Ввод операции
operation = input("Введите операцию (+, -, *, /): ")

# Выполнение операции
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        print("Ошибка: Деление на ноль недопустимо.")
        result = None
else:
    print("Ошибка: Неверная операция.")
    result = None

# Вывод результата
if result is not None:
    print(f"Результат {num1} {operation} {num2} равен: {result}")
