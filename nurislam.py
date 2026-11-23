# ЗАДАЧА 1
name = input("Введите имя: ")

if name:
    print(f"Привет, {name}! Длина имени: {len(name)}. {name.upper()}")
else:
    print("Имя не введено")


# ЗАДАЧА 2
a = float(input("Введите a: "))
b = float(input("Введите b: "))

print("сумма =", a + b)
print("разность =", a - b)
print("произведение =", a * b)

if b == 0:
    print("деление на ноль")
else:
    print("частное =", round(a / b, 2))
    print("остаток =", a % b)


# ЗАДАЧА 3
number = int(input("Введите число: "))

if number % 2 == 0:
    parity = "чётное"
else:
    parity = "нечётное"

if number > 0:
    sign = "положительное"
elif number < 0:
    sign = "отрицательное"
else:
    sign = "ноль"

if number % 5 == 0:
    multiple = "да"
else:
    multiple = "нет"

print(f"{parity}, {sign}, кратно 5: {multiple}")


# ЗАДАЧА 4
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

numbers = [a, b, c]

print("по возрастанию:", *sorted(numbers))
print("по убыванию:", *sorted(numbers, reverse=True))
print("мин =", min(numbers), "макс =", max(numbers))


# ЗАДАЧА 5
n = int(input("Введите N: "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{i * j:4}", end="")
    print()


# ЗАДАЧА 6
n = int(input("Введите N: "))

total = 0
product = 1
found = False

for i in range(1, n + 1):
    if i % 2 == 0:
        total += i
        product *= i
        found = True

if found:
    print("сумма =", total)
    print("произведение =", product)
else:
    print("чётных чисел нет")


# ЗАДАЧА 7
n = int(input("Введите N: "))

factorial = 1

for i in range(1, n + 1):
    factorial *= i

digit_sum = sum(int(digit) for digit in str(factorial))

print(f"{n}! =", factorial)
print("сумма цифр =", digit_sum)


# ЗАДАЧА 8
text = input("Введите предложение: ")

words = text.split()
words.reverse()

print(" ".join(words))


# ЗАДАЧА 9
text = input("Введите строку: ")

allowed = "abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя"

cleaned = ""

for char in text.lower():
    if char in allowed:
        cleaned += char

print(cleaned == cleaned[::-1])


# ЗАДАЧА 10
text = input("Введите строку: ")

vowels = "аеёиоуыэюя"
vowels_count = 0
consonants_count = 0

for char in text.lower():
    if char in vowels:
        vowels_count += 1
    elif char.isalpha():
        consonants_count += 1

print("гласных =", vowels_count)
print("согласных =", consonants_count)


# ЗАДАЧА 11
numbers = list(map(int, input("Введите числа через пробел: ").split()))

result = []

for number in numbers:
    if number > 0:
        result.append(number ** 2)
    else:
        result.append(0)

print(result)


# ЗАДАЧА 12
numbers = list(map(int, input("Введите числа через пробел: ").split()))

odd_numbers = []

for number in numbers:
    if number % 2 != 0:
        odd_numbers.append(number)

if odd_numbers:
    average = sum(odd_numbers) / len(odd_numbers)
else:
    average = sum(numbers) / len(numbers)

print(average)


# ЗАДАЧА 13
items = input("Введите элементы через пробел: ").split()

unique = []
counts = {}

for item in items:
    if item not in counts:
        counts[item] = 1
        unique.append(item)
    else:
        counts[item] += 1

print(unique)
print(counts)


# ЗАДАЧА 14
numbers = list(map(int, input("Введите числа через пробел: ").split()))

minimum = numbers[0]
maximum = numbers[0]
min_index = 0
max_index = 0

for i in range(1, len(numbers)):
    if numbers[i] < minimum:
        minimum = numbers[i]
        min_index = i

    if numbers[i] > maximum:
        maximum = numbers[i]
        max_index = i

print(f"мин={minimum} (индекс {min_index}), макс={maximum} (индекс {max_index})")


# ЗАДАЧА 15
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

result = even + odd

print(result)


# ЗАДАЧА 16
while True:
    expression = input("Введите выражение или exit: ")

    if expression.lower() == "exit":
        break

    parts = expression.split()

    if len(parts) != 3:
        print("неверный формат")
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
            print("деление на ноль")
            continue
        result = a / b
    else:
        print("неизвестная операция")
        continue

    print(result)


# ЗАДАЧА 17
import random

secret = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Введите число от 1 до 100: "))
    attempts += 1

    if guess < secret:
        print("больше")
    elif guess > secret:
        print("меньше")
    else:
        print(f"угадал за {attempts} попытки")
        break


# ЗАДАЧА 18
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


# ЗАДАЧА 19
phone_book = {}

while True:
    command = input("Введите команду: ")

    if command == "exit":
        break

    parts = command.split()

    if parts[0] == "add":
        name = parts[1]
        phone = parts[2]
        phone_book[name] = phone
        print("добавлено")

    elif parts[0] == "get":
        name = parts[1]

        if name in phone_book:
            print(phone_book[name])
        else:
            print("не найдено")

    elif parts[0] == "del":
        name = parts[1]

        if name in phone_book:
            del phone_book[name]
            print("удалено")
        else:
            print("не найдено")

    elif parts[0] == "list":
        for name, phone in phone_book.items():
            print(f"{name}: {phone}")

    else:
        print("неизвестная команда")


# ЗАДАЧА 20
import string

text = input("Введите строку: ")

for symbol in ".,!?;:":
    text = text.replace(symbol, "")

words = text.lower().split()

word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

for word, count in sorted_words:
    print(f"{word}: {count}")
