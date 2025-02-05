# Задание 2: Калькулятор с использованием цикла
while True:
    # Ввод двух чисел
    num1 = float(input("Введите первое число (или 'q' для выхода): "))
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
            continue  # Повторяем ввод
    else:
        print("Ошибка: Неверная операция.")
        continue  # Повторяем ввод

    # Вывод результата
    print(f"Результат {num1} {operation} {num2} равен: {result}")

    # Проверка на выход
    if input("Хотите продолжить? (y/n): ").lower() != 'y':
        break
