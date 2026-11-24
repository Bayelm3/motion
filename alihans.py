
# ================================================================
# 20 ЗАДАЧ ПО PYTHON (НАЧАЛЬНЫЙ УРОВЕНЬ, УСЛОЖНЁННЫЕ)
# ================================================================


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

ascending = sorted(numbers)
descending = sorted(numbers, reverse=True)

print("По возрастанию:", *ascending)
print("По убыванию:", *descending)
print("Мин =", min(numbers), "Макс =", max(numbers))


# ЗАДАЧА 5. Квадратная таблица умножения

n = int(input("Введите N: "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{i * j:4}", end="")
    print()


# ЗАДАЧА 6. Сумма и произведение чётных чисел

n = int(input("Введите N: "))

total = 0
product = 1
count = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        total += i
        product *= i
        count += 1

if count == 0:
    print("Чётных чисел нет")
else:
    print("Сумма =", total)
    print("Произведение =", product)


# ЗАДАЧА 7. Факториал и сумма его цифр

n = int(input("Введите N: "))

factorial = 1

for i in range(1, n + 1):
    factorial *= i

digit_sum = sum(int(digit) for digit in str(factorial))

print(f"{n}! =", factorial)
print("Сумма цифр =", digit_sum)


# ЗАДАЧА 8. Реверс слов в предложении

text = input("Введите предложение: ")

words = text.split()
words.reverse()

result = " ".join(words)

print(result)


# ЗАДАЧА 9. Палиндром

text = input("Введите строку: ")

cleaned = ""

for char in text.lower():
    if char.isalnum():
        cleaned += char

if cleaned == cleaned[::-1]:
    print("True")
else:
    print("False")


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

result = []

for num in numbers:
    if num > 0:
        result.append(num ** 2)
    else:
        result.append(0)

print(result)


# ЗАДАЧА 12. Среднее без чётных

numbers = [10, 3, 20, 7]

odd_numbers = []

for num in numbers:
    if num % 2 != 0:
        odd_numbers.append(num)

if len(odd_numbers) > 0:
    average = sum(odd_numbers) / len(odd_numbers)
elif len(numbers) > 0:
    average = sum(numbers) / len(numbers)
else:
    average = 0

print("Среднее =", average)


# ЗАДАЧА 13. Удаление дубликатов с подсчётом

numbers = [1, 2, 2, 3, 1, 4]

unique = []
counts = {}

for num in numbers:
    if num not in unique:
        unique.append(num)

    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1

print(unique)
print(counts)


# ЗАДАЧА 14. Минимум, максимум и их индексы

numbers = [3, 1, 9, 4]

if len(numbers) == 0:
    print("Список пуст")
else:
    min_value = numbers[0]
    max_value = numbers[0]

    min_index = 0
    max_index = 0

    for i in range(len(numbers)):
        if numbers[i] < min_value:
            min_value = numbers[i]
            min_index = i

        if numbers[i] > max_value:
            max_value = numbers[i]
            max_index = i

    print(f"Мин = {min_value} (индекс {min_index})")
    print(f"Макс = {max_value} (индекс {max_index})")


# ЗАДАЧА 15. Сортировка по чётности

numbers = [5, 2, 8, 1, 4, 7]

even_numbers = []
odd_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

even_numbers.sort()
odd_numbers.sort()

result = even_numbers + odd_numbers

print(result)


# ЗАДАЧА 16. Калькулятор с историей

history = []

while True:
    expression = input("Введите выражение (или exit): ")

    if expression.lower() == "exit":
        break

    parts = expression.split()

    if len(parts) != 3:
        print("Неверный формат")
        continue

    a = float(parts[0])
    operation = parts[1]
    b = float(parts[2])

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
    history.append(expression + " = " + str(result))

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
        print(f"Угадал за {attempts} попытки!")
        break


# ЗАДАЧА 18. FizzBuzz с подсчётом

n = int(input("Введите N: "))

fizz_count = 0
buzz_count = 0
fizzbuzz_count = 0

for i in range(1, n + 1):

    if i % 15 == 0:
        print("FizzBuzz", end=" ")
        fizzbuzz_count += 1

    elif i % 3 == 0:
        print("Fizz", end=" ")
        fizz_count += 1

    elif i % 5 == 0:
        print("Buzz", end=" ")
        buzz_count += 1

    else:
        print(i, end=" ")

print()

print("Fizz:", fizz_count)
print("Buzz:", buzz_count)
print("FizzBuzz:", fizzbuzz_count)


# ЗАДАЧА 19. Телефонная книга с командами

phonebook = {}

while True:
    command = input("Введите команду: ").split()

    if not command:
        continue

    action = command[0]

    if action == "add":
        name = command[1]
        phone = command[2]

        phonebook[name] = phone
        print("Добавлено")

    elif action == "get":
        name = command[1]

        if name in phonebook:
            print(phonebook[name])
        else:
            print("Не найдено")

    elif action == "del":
        name = command[1]

        if name in phonebook:
            del phonebook[name]
            print("Удалено")
        else:
            print("Не найдено")

    elif action == "list":
        if len(phonebook) == 0:
            print("Телефонная книга пуста")
        else:
            for name, phone in phonebook.items():
                print(f"{name}: {phone}")

    elif action == "exit":
        break

    else:
        print("Неизвестная команда")


# ЗАДАЧА 20. Частотный анализ слов

text = input("Введите текст: ")

text = text.lower()

for char in ".,!?;:":
    text = text.replace(char, "")

words = text.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

sorted_words = sorted(
    word_count.items(),
    key=lambda item: item[1],
    reverse=True
)

for word, count in sorted_words:
    print(f"{word}: {count}")

