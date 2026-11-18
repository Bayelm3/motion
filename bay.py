# задача 1
name = input("Введите имя: ")

if name == "":
    print("Имя не введено")
else:
    print(f"Привет, {name}! Длина имени: {len(name)}. {name.upper()}")


# задача 2
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

print("Сумма:", a + b)
print("Разность:", a - b)
print("Произведение:", a * b)

if b == 0:
    print("Деление на ноль")
else:
    print("Частное:", round(a / b, 2))
    print("Остаток:", a % b)


# задача 3
n = int(input("Введите число: "))

if n % 2 == 0:
    parity = "чётное"
else:
    parity = "нечётное"

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

print(parity, sign, "кратно 5:", multiple)


# задача 4
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

numbers = [a, b, c]

print("По возрастанию:", sorted(numbers))
print("По убыванию:", sorted(numbers, reverse=True))
print("Мин:", min(numbers))
print("Макс:", max(numbers))


# задача 5
n = int(input("Введите N: "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{i * j:4}", end="")
    print()


# задача 6
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


# задача 7
n = int(input("Введите N: "))

factorial = 1

for i in range(1, n + 1):
    factorial *= i

digit_sum = sum(int(x) for x in str(factorial))

print(f"{n}! =", factorial)
print("Сумма цифр =", digit_sum)


# задача 8
text = input("Введите предложение: ")

words = text.split()
words.reverse()

print(" ".join(words))


# задача 9
text = input("Введите строку: ").lower()

for char in " .,!?;:-":
    text = text.replace(char, "")

print(text == text[::-1])


# задача 10
text = input("Введите строку: ").lower()

vowels = "аеёиоуыэюя"
vowel_count = 0
consonant_count = 0

for char in text:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Гласных =", vowel_count)
print("Согласных =", consonant_count)


# задача 11
numbers = list(map(int, input("Введите числа через пробел: ").split()))

result = []

for n in numbers:
    if n > 0:
        result.append(n ** 2)
    else:
        result.append(0)

print(result)


# задача 12
numbers = list(map(int, input("Введите числа через пробел: ").split()))

odd = []

for n in numbers:
    if n % 2 != 0:
        odd.append(n)

if len(odd) > 0:
    print(sum(odd) / len(odd))
elif len(numbers) > 0:
    print(sum(numbers) / len(numbers))
else:
    print("Список пуст")


# задача 13
numbers = list(map(int, input("Введите числа через пробел: ").split()))

unique = []
counts = {}

for n in numbers:
    if n not in counts:
        counts[n] = 0
        unique.append(n)

    counts[n] += 1

print(unique)
print(counts)


# задача 14
numbers = list(map(int, input("Введите числа через пробел: ").split()))

if len(numbers) == 0:
    print("Список пуст")
else:
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

    print("Мин =", minimum, "индекс", min_index)
    print("Макс =", maximum, "индекс", max_index)


# задача 15
numbers = list(map(int, input("Введите числа через пробел: ").split()))

even = []
odd = []

for n in numbers:
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)

even.sort()
odd.sort()

print(even + odd)


# задача 16
while True:
    expression = input("Введите выражение или exit: ")

    if expression == "exit":
        break

    parts = expression.split()

    if len(parts) != 3:
        print("Неверный формат")
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
        if b == 0:
            print("Деление на ноль")
        else:
            print(a / b)
    else:
        print("Неизвестная операция")


# задача 17
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
        print("Угадал за", attempts, "попыток")
        break

# задача 18
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

# задача 19
phone_book = {}

while True:
    command = input("Введите команду: ").split()

    if not command:
        continue

    action = command[0]

    if action == "exit":
        break

    elif action == "add":
        if len(command) == 3:
            name = command[1]
            phone = command[2]
            phone_book[name] = phone
            print("Добавлено")

    elif action == "get":
        name = command[1]
        print(phone_book.get(name, "не найдено"))

    elif action == "del":
        name = command[1]

        if name in phone_book:
            del phone_book[name]
            print("Удалено")
        else:
            print("не найдено")

    elif action == "list":
        for name, phone in phone_book.items():
            print(name + ":", phone)


# задача 20
text = input("Введите строку: ").lower()

for char in ".,!?;:—–-":
    text = text.replace(char, " ")
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