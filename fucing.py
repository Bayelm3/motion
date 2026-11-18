1

name = input("Введите имя: ")

if name == "":
    print("Имя не введено")
else:
    print("Привет,", name)
    print("Длина имени:", len(name))
    print(name.upper())
2

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
3

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
    five = "да"
else:
    five = "нет"

print(even + ", " + sign + ", кратно 5: " + five)
4

a = int(input("Первое число: "))
b = int(input("Второе число: "))
c = int(input("Третье число: "))

numbers = [a, b, c]

print("По возрастанию:", sorted(numbers))
print("По убыванию:", sorted(numbers, reverse=True))
print("Минимум =", min(numbers))
print("Максимум =", max(numbers))
5

n = int(input("Введите N: "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i * j, end="\t")
    print()
6

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
7

n = int(input("Введите N: "))

factorial = 1

for i in range(1, n + 1):
    factorial *= i

digit_sum = 0

for digit in str(factorial):
    digit_sum += int(digit)

print(str(n) + "! =", factorial)
print("Сумма цифр =", digit_sum)
8

text = input("Введите предложение: ")

words = text.split()
words.reverse()

result = " ".join(words)

print(result)
9

text = input("Введите строку: ")

text = text.lower()

for symbol in " .,!?;:-":
    text = text.replace(symbol, "")

if text == text[::-1]:
    print(True)
else:
    print(False)
10

text = input("Введите строку: ").lower()

vowels = "аеёиоуыэюя"
vowel_count = 0
consonant_count = 0

for letter in text:
    if letter in vowels:
        vowel_count += 1
    elif letter.isalpha():
        consonant_count += 1

print("Гласных =", vowel_count)
print("Согласных =", consonant_count)
11

numbers = [1, -2, 3, -4, 0]

result = []

for n in numbers:
    if n > 0:
        result.append(n ** 2)
    else:
        result.append(0)

print(result)
12

numbers = [10, 3, 20, 7]

odd = []

for n in numbers:
    if n % 2 != 0:
        odd.append(n)

if len(odd) > 0:
    average = sum(odd) / len(odd)
else:
    average = sum(numbers) / len(numbers)

print(average)
13

numbers = [1, 2, 2, 3, 1, 4]

unique = []
counts = {}

for n in numbers:
    if n not in unique:
        unique.append(n)

    if n in counts:
        counts[n] += 1
    else:
        counts[n] = 1

print(unique)
print(counts)
14

numbers = [3, 1, 9, 4]

minimum = numbers[0]
maximum = numbers[0]

min_index = 0
max_index = 0

for i in range(len(numbers)):
    if numbers[i] < minimum:
        minimum = numbers[i]
        min_index = i

    if numbers[i] > maximum:
        maximum = numbers[i]
        max_index = i

print("Минимум =", minimum, "индекс", min_index)
print("Максимум =", maximum, "индекс", max_index)
15

numbers = [5, 2, 8, 1, 4, 7]

even = []
odd = []

for n in numbers:
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)

even.sort()
odd.sort()

result = even + odd

print(result)
16

history = []

while True:
    expression = input("Введите выражение: ")

    if expression == "exit":
        break

    parts = expression.split()

    if len(parts) != 3:
        print("Неверное выражение")
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

print("История:")
for item in history:
    print(item)
17

import random

secret = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Угадайте число: "))
    attempts += 1

    if guess < secret:
        print("Больше")
    elif guess > secret:
        print("Меньше")
    else:
        print("Угадал!")
        print("Количество попыток:", attempts)
        break
18

n = int(input("Введите N: "))

fizz = 0
buzz = 0
fizzbuzz = 0

for i in range(1, n + 1):
    if i % 15 == 0:
        print("FizzBuzz", end=", ")
        fizzbuzz += 1
    elif i % 3 == 0:
        print("Fizz", end=", ")
        fizz += 1
    elif i % 5 == 0:
        print("Buzz", end=", ")
        buzz += 1
    else:
        print(i, end=", ")

print()
print("Fizz:", fizz)
print("Buzz:", buzz)
print("FizzBuzz:", fizzbuzz)
19

phonebook = {}

while True:
    command = input("Введите команду: ")

    if command == "exit":
        break

    parts = command.split()

    if parts[0] == "add":
        name = parts[1]
        phone = parts[2]
        phonebook[name] = phone
        print("Добавлено")

    elif parts[0] == "get":
        name = parts[1]

        if name in phonebook:
            print(phonebook[name])
        else:
            print("Не найдено")

    elif parts[0] == "del":
        name = parts[1]

        if name in phonebook:
            del phonebook[name]
            print("Удалено")
        else:
            print("Не найдено")

    elif parts[0] == "list":
        for name, phone in phonebook.items():
            print(name + ":", phone)

    else:
        print("Неизвестная команда")
20

text = input("Введите текст: ").lower()

for symbol in ".,!?;:—":
    text = text.replace(symbol, "")

words = text.split()

counts = {}

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

sorted_words = sorted(
    counts.items(),
    key=lambda x: x[1],
    reverse=True
)

for word, count in sorted_words:
    print(word + ":", count)

