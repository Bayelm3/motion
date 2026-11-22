
#Задание 1
name = input("Введите имя: ")

if name:
    print(f"Привет, {name}! Длина имени: {len(name)}. {name.upper()}")
else:
    print("Имя не введено")


#Задание 2
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

print("Сумма:", a + b)
print("Разность:", a - b)
print("Произведение:", a * b)

if b != 0:
    print("Частное:", round(a / b, 2))
    print("Остаток:", a % b)
else:
    print("Деление на ноль")


#Задание 3
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


#Задание 4
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

numbers = [a, b, c]
numbers.sort()

print("По возрастанию:", *numbers)
print("По убыванию:", *numbers[::-1])
print("Минимум:", numbers[0])
print("Максимум:", numbers[-1])


#Задание 5
n = int(input("Введите N: "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{i * j:4}", end="")
    print()


#Задание 6
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
    print("Сумма:", total)
    print("Произведение:", product)


#Задание 7
n = int(input("Введите N: "))

factorial = 1

for i in range(1, n + 1):
    factorial *= i

digit_sum = 0

for digit in str(factorial):
    digit_sum += int(digit)

print(f"{n}! =", factorial)
print("Сумма цифр =", digit_sum)


#Задание 8
text = input("Введите предложение: ")

words = text.split()
words.reverse()

result = " ".join(words)

print(result)


#Задание 9
text = input("Введите строку: ").lower()

symbols = " .,!?;:-"

for symbol in symbols:
    text = text.replace(symbol, "")

print(text == text[::-1])


#Задание 10
text = input("Введите строку: ").lower()

vowels = "аеёиоуыэюя"

vowel_count = 0
consonant_count = 0

for letter in text:
    if letter.isalpha():
        if letter in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Гласных =", vowel_count)
print("Согласных =", consonant_count)


#Задание 11
numbers = [1, -2, 3, -4, 0]

result = []

for number in numbers:
    if number > 0:
        result.append(number ** 2)
    else:
        result.append(0)

print(result)


#Задание 12
numbers = [10, 3, 20, 7]

odd_numbers = []

for number in numbers:
    if number % 2 != 0:
        odd_numbers.append(number)

if len(odd_numbers) > 0:
    average = sum(odd_numbers) / len(odd_numbers)
else:
    average = sum(numbers) / len(numbers)

print("Среднее:", average)


#Задание 13
numbers = [1, 2, 2, 3, 1, 4]

result = []
counts = {}

for number in numbers:
    if number not in result:
        result.append(number)

    if number in counts:
        counts[number] += 1
    else:
        counts[number] = 1

print(result)
print(counts)


#Задание 14
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

print("Минимум:", minimum, "индекс:", min_index)
print("Максимум:", maximum, "индекс:", max_index)


#Задание 15
numbers = [5, 2, 8, 1, 4, 7]

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


#Задание 16
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
        print(a + b)
    elif operation == "-":
        print(a - b)
    elif operation == "*":
        print(a * b)
    elif operation == "/":
        if b != 0:
            print(a / b)
        else:
            print("Деление на ноль")
    else:
        print("Неизвестная операция")


#Задание 17
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


#Задание 18
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


#Задание 19
phone_book = {}

while True:
    command = input("Введите команду: ")

    if command == "exit":
        break

    parts = command.split()
    action = parts[0]

    if action == "add":
        name = parts[1]
        phone = parts[2]
        phone_book[name] = phone
        print("Добавлено")

    elif action == "get":
        name = parts[1]

        if name in phone_book:
            print(phone_book[name])
        else:
            print("Не найдено")

    elif action == "del":
        name = parts[1]

        if name in phone_book:
            del phone_book[name]
            print("Удалено")
        else:
            print("Не найдено")

    elif action == "list":
        for name, phone in phone_book.items():
            print(name + ":", phone)

    else:
        print("Неизвестная команда")


#Задание 20
text = input("Введите текст: ").lower()

symbols = ".,!?;:"

for symbol in symbols:
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
    key=lambda item: item[1],
    reverse=True
)

for word, count in sorted_words:
    print(word + ":", count)

