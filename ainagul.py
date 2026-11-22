

# 20 ЗАДАЧ ПО PYTHON



# ЗАДАЧА 1. Приветствие с анализом имени

name = input("Введите имя: ")

if name:
    print(f"Привет, {name}! Длина имени: {len(name)}. {name.upper()}")
else:
    print("Имя не введено")


# ЗАДАЧА 2. Анализ двух чисел

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

n = int(input("Введите число: "))

if n % 2 == 0:
    even = "чётное"
else:
    even = "нечётное"

if n > 0:
    sign = "положительное"
elif n < 0:
    sign = "отрицательное"
else:
    sign = "ноль"

if n % 5 == 0:
    multiple = "да"
else:
    multiple = "нет"

print(f"{even}, {sign}, кратно 5: {multiple}")


# ЗАДАЧА 4. Упорядочить три числа

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

numbers = [a, b, c]

print("По возрастанию:", *sorted(numbers))
print("По убыванию:", *sorted(numbers, reverse=True))
print("Мин =", min(numbers), "Макс =", max(numbers))


# ЗАДАЧА 5. Квадратная таблица умножения

n = int(input("Введите N: "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{i * j:4}", end="")
    print()


# ЗАДАЧА 6. Сумма и произведение чётных чисел

n = int(input("Введите N: "))

even_numbers = [i for i in range(1, n + 1) if i % 2 == 0]

if len(even_numbers) == 0:
    print("Чётных чисел нет")
else:
    total = sum(even_numbers)
    product = 1

    for num in even_numbers:
        product *= num

    print("Сумма =", total)
    print("Произведение =", product)


# ЗАДАЧА 7. Факториал и сумма его цифр

n = int(input("Введите N: "))

factorial = 1

for i in range(1, n + 1):
    factorial *= i

digit_sum = sum(int(digit) for digit in str(factorial))

print(f"{n}! = {factorial}")
print("Сумма цифр =", digit_sum)


# ЗАДАЧА 8. Реверс слов в предложении

text = input("Введите предложение: ")

words = text.split()
words.reverse()

print(" ".join(words))


# ЗАДАЧА 9. Палиндром

text = input("Введите строку: ")

cleaned = "".join(
    char.lower()
    for char in text
    if char.isalnum()
)

print(cleaned == cleaned[::-1])


# ЗАДАЧА 10. Гласные и согласные

text = input("Введите строку: ")

vowels = "аеёиоуыэюя"
vowel_count = 0
consonant_count = 0

for char in text.lower():
    if char in vowels:
        vowel_count += 1
    elif char.isalpha():
        consonant_count += 1

print("Гласных =", vowel_count)
print("Согласных =", consonant_count)


# ЗАДАЧА 11. Квадраты только положительных чисел

numbers = [1, -2, 3, -4, 0]

result = [x ** 2 if x > 0 else 0 for x in numbers]

print(result)


# ЗАДАЧА 12. Среднее без чётных

numbers = [10, 3, 20, 7]

odd_numbers = [x for x in numbers if x % 2 != 0]

if odd_numbers:
    average = sum(odd_numbers) / len(odd_numbers)
elif numbers:
    average = sum(numbers) / len(numbers)
else:
    average = None

print(average)


# ЗАДАЧА 13. Удаление дубликатов с подсчётом

numbers = [1, 2, 2, 3, 1, 4]

unique = []
counts = {}

for num in numbers:
    if num not in counts:
        unique.append(num)
        counts[num] = 1
    else:
        counts[num] += 1

print(unique)
print(counts)


# ЗАДАЧА 14. Минимум, максимум и их индексы

numbers = [3, 1, 9, 4]

if numbers:
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

    print(f"Мин = {min_value} (индекс {min_index})")
    print(f"Макс = {max_value} (индекс {max_index})")
else:
    print("Список пуст")


# ЗАДАЧА 15. Сортировка по чётности

numbers = [5, 2, 8, 1, 4, 7]

even = sorted([x for x in numbers if x % 2 == 0])
odd = sorted([x for x in numbers if x % 2 != 0])

result = even + odd

print(result)


# ЗАДАЧА 16. Калькулятор с историей

history = []

while True:
    expression = input("Введите выражение (или exit): ")

    if expression.lower() == "exit":
        print("Выход")
        break

    try:
        a, operation, b = expression.split()
        a = float(a)
        b = float(b)

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

        print("Результат:", result)
        history.append(expression + " = " + str(result))

    except ValueError:
        print("Ошибка ввода")

print("История вычислений:")
for item in history:
    print(item)


# ЗАДАЧА 17. Угадай число

import random

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

n = int(input("Введите N: "))

fizz_count = 0
buzz_count = 0
fizzbuzz_count = 0

for i in range(1, n + 1):
    if i % 15 == 0:
        print("FizzBuzz", end=", ")
        fizzbuzz_count += 1
    elif i % 3 == 0:
        print("Fizz", end=", ")
        fizz_count += 1
    elif i % 5 == 0:
        print("Buzz", end=", ")
        buzz_count += 1
    else:
        print(i, end=", ")

print("\nFizz:", fizz_count)
print("Buzz:", buzz_count)
print("FizzBuzz:", fizzbuzz_count)


# ЗАДАЧА 19. Телефонная книга с командами

phone_book = {}

while True:
    command = input("Введите команду: ").split()

    if not command:
        continue

    action = command[0].lower()

    if action == "add" and len(command) == 3:
        name = command[1]
        phone = command[2]

        phone_book[name] = phone
        print("Добавлено")

    elif action == "get" and len(command) == 2:
        name = command[1]

        if name in phone_book:
            print(phone_book[name])
        else:
            print("Не найдено")

    elif action == "del" and len(command) == 2:
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

    elif action == "exit":
        print("Выход")
        break

    else:
        print("Неизвестная команда или неправильный формат")


# ЗАДАЧА 20. Частотный анализ слов

text = input("Введите текст: ")

for symbol in ".,!?;:":
    text = text.replace(symbol, "")

words = text.lower().split()

counts = {}

for word in words:
    counts[word] = counts.get(word, 0) + 1

sorted_counts = sorted(
    counts.items(),
    key=lambda item: item[1],
    reverse=True
)

for word, count in sorted_counts:
    print(f"{word}: {count}")

