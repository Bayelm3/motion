

# ЗАДАЧА 1
name = input("Введите имя: ")
if name:
    print(f"Привет, {name}! Длина имени: {len(name)}. {name.upper()}")
else:
    print("Имя не введено")


# ЗАДАЧА 2
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


# ЗАДАЧА 3
n = int(input("Введите число: "))
even = "чётное" if n % 2 == 0 else "нечётное"
if n > 0:
    sign = "положительное"
elif n < 0:
    sign = "отрицательное"
else:
    sign = "ноль"
multiple = "да" if n % 5 == 0 else "нет"
print(even + ", " + sign + ", кратно 5: " + multiple)


# ЗАДАЧА 4
numbers = [int(input("Введите число: ")) for _ in range(3)]
print("По возрастанию:", sorted(numbers))
print("По убыванию:", sorted(numbers, reverse=True))
print("Мин:", min(numbers), "Макс:", max(numbers))


# ЗАДАЧА 5
n = int(input("Введите N: "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{i * j:4}", end="")
    print()


# ЗАДАЧА 6
n = int(input("Введите N: "))
even = [i for i in range(1, n + 1) if i % 2 == 0]
if even:
    total = sum(even)
    product = 1
    for i in even:
        product *= i
    print("Сумма:", total)
    print("Произведение:", product)
else:
    print("Чётных чисел нет")


# ЗАДАЧА 7
n = int(input("Введите N: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
digit_sum = sum(int(digit) for digit in str(factorial))
print(f"{n}! =", factorial)
print("Сумма цифр =", digit_sum)


# ЗАДАЧА 8
text = input("Введите предложение: ")
words = text.split()
print(" ".join(words[::-1]))


# ЗАДАЧА 9
text = input("Введите строку: ").lower()
clean = ""
for char in text:
    if char.isalnum():
        clean += char
print(clean == clean[::-1])


# ЗАДАЧА 10
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


# ЗАДАЧА 11
numbers = [1, -2, 3, -4, 0]
result = [x ** 2 if x > 0 else 0 for x in numbers]
print(result)


# ЗАДАЧА 12
numbers = [10, 3, 20, 7]
odd = [x for x in numbers if x % 2 != 0]
if odd:
    print(sum(odd) / len(odd))
else:
    print(sum(numbers) / len(numbers))


# ЗАДАЧА 13
numbers = [1, 2, 2, 3, 1, 4]
unique = []
count = {}
for x in numbers:
    if x not in unique:
        unique.append(x)
    count[x] = count.get(x, 0) + 1
print(unique)
print(count)


# ЗАДАЧА 14
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
print("Мин:", minimum, "Индекс:", min_index)
print("Макс:", maximum, "Индекс:", max_index)


# ЗАДАЧА 15
numbers = [5, 2, 8, 1, 4, 7]
even = sorted([x for x in numbers if x % 2 == 0])
odd = sorted([x for x in numbers if x % 2 != 0])
print(even + odd)


# ЗАДАЧА 16
while True:
    expression = input("Введите выражение: ")
    if expression == "exit":
        break
    try:
        a, operation, b = expression.split()
        a = float(a)
        b = float(b)
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
    except ValueError:
        print("Ошибка ввода")


# ЗАДАЧА 17
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
        print("Угадали за", attempts, "попытки")
        break


# ЗАДАЧА 18
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
print("\nFizz:", fizz, "Buzz:", buzz, "FizzBuzz:", fizzbuzz)


# ЗАДАЧА 19
phone_book = {}
while True:
    command = input("Введите команду: ").split()
    if not command:
        continue
    action = command[0]
    if action == "add" and len(command) == 3:
        phone_book[command[1]] = command[2]
        print("Добавлено")
    elif action == "get" and len(command) == 2:
        print(phone_book.get(command[1], "Не найдено"))
    elif action == "del" and len(command) == 2:
        if command[1] in phone_book:
            del phone_book[command[1]]
            print("Удалено")
        else:
            print("Не найдено")
    elif action == "list":
        for name, phone in phone_book.items():
            print(name + ":", phone)
    elif action == "exit":
        break
    else:
        print("Неизвестная команда")


# ЗАДАЧА 20
text = input("Введите текст: ").lower()
for char in ".,!?;:":
    text = text.replace(char, "")
words = text.split()
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1
sorted_words = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
for word, count in sorted_words:
    print(word + ":", count)
