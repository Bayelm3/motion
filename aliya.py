


# ЗАДАЧА 1. Приветствие с анализом имени

def task1():
    name = input("Введите имя: ")

    if name == "":
        print("Имя не введено")
    else:
        print(f"Привет, {name}! Длина имени: {len(name)}. {name.upper()}")


# ЗАДАЧА 2. Анализ двух чисел

def task2():
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))

    print("Сумма =", a + b)
    print("Разность =", a - b)
    print("Произведение =", a * b)

    if b == 0:
        print("Деление на ноль")
    else:
        print("Частное =", round(a / b, 2))
        print("Остаток =", a % b)


# ЗАДАЧА 3. Классификация числа

def task3():
    n = int(input("Введите число: "))

    parity = "чётное" if n % 2 == 0 else "нечётное"

    if n > 0:
        sign = "положительное"
    elif n < 0:
        sign = "отрицательное"
    else:
        sign = "ноль"

    multiple = "да" if n % 5 == 0 else "нет"

    print(f"{parity}, {sign}, кратно 5: {multiple}")


# ЗАДАЧА 4. Упорядочить три числа

def task4():
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    c = int(input("Введите третье число: "))

    numbers = [a, b, c]

    print("По возрастанию:", *sorted(numbers))
    print("По убыванию:", *sorted(numbers, reverse=True))
    print("Минимум =", min(numbers))
    print("Максимум =", max(numbers))


# ЗАДАЧА 5. Квадратная таблица умножения

def task5():
    n = int(input("Введите N: "))

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i * j:4}", end="")
        print()


# ЗАДАЧА 6. Сумма и произведение чётных чисел

def task6():
    n = int(input("Введите N: "))

    even_numbers = []

    for i in range(1, n + 1):
        if i % 2 == 0:
            even_numbers.append(i)

    if not even_numbers:
        print("Чётных чисел нет")
    else:
        total = sum(even_numbers)
        product = 1

        for number in even_numbers:
            product *= number

        print("Сумма =", total)
        print("Произведение =", product)


# ЗАДАЧА 7. Факториал и сумма его цифр

def task7():
    n = int(input("Введите N: "))

    if n < 0:
        print("Факториал отрицательного числа не существует")
        return

    factorial = 1

    for i in range(1, n + 1):
        factorial *= i

    digit_sum = 0

    for digit in str(factorial):
        digit_sum += int(digit)

    print(f"{n}! = {factorial}")
    print("Сумма цифр =", digit_sum)


# ЗАДАЧА 8. Реверс слов в предложении

def task8():
    text = input("Введите предложение: ")

    words = text.split()
    words.reverse()

    print(" ".join(words))


# ЗАДАЧА 9. Палиндром

def task9():
    text = input("Введите строку: ").lower()

    clean_text = ""

    for char in text:
        if char.isalnum():
            clean_text += char

    print(clean_text == clean_text[::-1])


# ЗАДАЧА 10. Гласные и согласные

def task10():
    text = input("Введите строку: ").lower()

    vowels = "аеёиоуыэюя"
    vowel_count = 0
    consonant_count = 0

    for char in text:
        if char in vowels:
            vowel_count += 1
        elif char.isalpha():
            consonant_count += 1

    print("Гласных =", vowel_count)
    print("Согласных =", consonant_count)


# ЗАДАЧА 11. Квадраты только положительных чисел

def task11():
    numbers = list(map(int, input("Введите числа через пробел: ").split()))

    result = []

    for number in numbers:
        if number > 0:
            result.append(number ** 2)
        else:
            result.append(0)

    print(result)


# ЗАДАЧА 12. Среднее без чётных

def task12():
    numbers = list(map(int, input("Введите числа через пробел: ").split()))

    if not numbers:
        print("Список пуст")
        return

    odd_numbers = []

    for number in numbers:
        if number % 2 != 0:
            odd_numbers.append(number)

    if odd_numbers:
        average = sum(odd_numbers) / len(odd_numbers)
    else:
        average = sum(numbers) / len(numbers)

    print("Среднее =", average)


# ЗАДАЧА 13. Удаление дубликатов с подсчётом

def task13():
    numbers = list(map(int, input("Введите числа через пробел: ").split()))

    unique = []
    counts = {}

    for number in numbers:
        if number not in unique:
            unique.append(number)

        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1

    print(unique)
    print(counts)


# ЗАДАЧА 14. Минимум, максимум и их индексы

def task14():
    numbers = list(map(int, input("Введите числа через пробел: ").split()))

    if not numbers:
        print("Список пуст")
        return

    min_value = numbers[0]
    max_value = numbers[0]

    min_index = 0
    max_index = 0

    for i in range(1, len(numbers)):
        if numbers[i] < min_value:
            min_value = numbers[i]
            min_index = i

        if numbers[i] > max_value:
            max_value = numbers[i]
            max_index = i

    print(f"Минимум = {min_value} (индекс {min_index})")
    print(f"Максимум = {max_value} (индекс {max_index})")

# ЗАДАЧА 15. Сортировка по чётности

def task15():
    numbers = list(map(int, input("Введите числа через пробел: ").split()))

    even = []
    odd = []

    for number in numbers:
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)

    even.sort()
    odd.sort()

    print(even + odd)


# ЗАДАЧА 16. Калькулятор с историей

def task16():
    history = []

    while True:
        expression = input("Введите выражение (или exit): ")

        if expression.lower() == "exit":
            break

        parts = expression.split()

        if len(parts) != 3:
            print("Неверный формат")
            continue

        try:
            a = float(parts[0])
            b = float(parts[2])
        except ValueError:
            print("Неверный формат чисел")
            continue

        operation = parts[1]

        if operation == "+":
            result = a + b
        elif operation == "-":
            result = a - b
        elif operation == "*":
            result = a * b
        elif operation == "/":
            if b == 0:
                print("Деление на ноль")
                continue
            result = a / b
        else:
            print("Неизвестная операция")
            continue

        print("Результат =", result)
        history.append(f"{expression} = {result}")

    print("\nИстория вычислений:")

    for item in history:
        print(item)


# ЗАДАЧА 17. Угадай число
import random

def task17():
    secret = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Угадайте число от 1 до 100: "))
        attempts += 1

        if guess < secret:
            print("Больше")
        elif guess > secret:
            print("Меньше")
        else:
            print(f"Угадал за {attempts} попыток!")
            break


# ЗАДАЧА 18. FizzBuzz с подсчётом

def task18():
    n = int(input("Введите N: "))

    fizz_count = 0
    buzz_count = 0
    fizzbuzz_count = 0

    result = []

    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
            fizzbuzz_count += 1
        elif i % 3 == 0:
            result.append("Fizz")
            fizz_count += 1
        elif i % 5 == 0:
            result.append("Buzz")
            buzz_count += 1
        else:
            result.append(str(i))

    print(", ".join(result))

    print("Fizz:", fizz_count)
    print("Buzz:", buzz_count)
    print("FizzBuzz:", fizzbuzz_count)


# ЗАДАЧА 19. Телефонная книга с командами

def task19():
    phone_book = {}

    while True:
        command = input("Введите команду: ").split()

        if not command:
            continue

        action = command[0].lower()

        if action == "exit":
            break

        elif action == "add":
            if len(command) != 3:
                print("Формат: add имя телефон")
                continue

            name = command[1]
            phone = command[2]

            phone_book[name] = phone
            print("Добавлено")

        elif action == "get":
            if len(command) != 2:
                print("Формат: get имя")
                continue

            name = command[1]

            if name in phone_book:
                print(phone_book[name])
            else:
                print("Не найдено")

        elif action == "del":
            if len(command) != 2:
                print("Формат: del имя")
                continue

            name = command[1]

            if name in phone_book:
                del phone_book[name]
                print("Удалено")
            else:
                print("Не найдено")

        elif action == "list":
            if phone_book:
                for name, phone in phone_book.items():
                    print(f"{name}: {phone}")
            else:
                print("Телефонная книга пуста")

        else:
            print("Неизвестная команда")


# ЗАДАЧА 20. Частотный анализ слов

def task20():
    text = input("Введите текст: ").lower()

    for char in ".,!?;:":
        text = text.replace(char, "")

    words = text.split()

    counts = {}

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    sorted_words = sorted(
        counts.items(),
        key=lambda item: item[1],
        reverse=True
    )

    for word, count in sorted_words:
        print(f"{word}: {count}")


