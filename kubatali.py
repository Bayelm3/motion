# ЗАДАЧА 1. Приветствие с анализом имени
name = input("Введите имя: ").strip()
if not name:
    print("Имя не введено")
else:
    print(f"Привет, {name}! Длина имени: {len(name)}. {name.upper()}")


# ЗАДАЧА 2. Анализ двух чисел
a = float(input("Введите a: "))
b = float(input("Введите b: "))
if a.is_integer():
    a = int(a)
if b.is_integer():
    b = int(b)

s = a + b
diff = a - b
prod = a * b

if b == 0:
    print(f"сумма={s}, разность={diff}, произведение={prod}, деление на ноль")
else:
    quot = a / b
    rem = a % b
    quot_str = f"{quot:.2f}".rstrip("0").rstrip(".") if isinstance(quot, float) else str(quot)
    rem_str = f"{rem:.2f}".rstrip("0").rstrip(".") if isinstance(rem, float) else str(rem)
    print(f"сумма={s}, разность={diff}, произведение={prod}, частное={quot_str}, остаток={rem_str}")


# ЗАДАЧА 3. Классификация числа
n = int(input("Введите число: "))
parity = "чётное" if n % 2 == 0 else "нечётное"
if n > 0:
    sign = "положительное"
elif n < 0:
    sign = "отрицательное"
else:
    sign = "ноль"
mult5 = "да" if n % 5 == 0 else "нет"
print(f"{parity}, {sign}, кратно 5: {mult5}")


# ЗАДАЧА 4. Упорядочить три числа
x = int(input("Введите 1-е число: "))
y = int(input("Введите 2-е число: "))
z = int(input("Введите 3-е число: "))

asc = sorted([x, y, z])
desc = sorted([x, y, z], reverse=True)
print("по возрастанию:", *asc)
print("по убыванию:", *desc)
print(f"мин={min(asc)}, макс={max(asc)}")


# ЗАДАЧА 5. Квадратная таблица умножения
n = int(input("Введите N: "))
max_width = len(str(n * n)) + 1
for i in range(1, n + 1):
    row = "".join(f"{i * j:<{max_width}}" for j in range(1, n + 1)).rstrip()
    print(row)


# ЗАДАЧА 6. Сумма и произведение чётных чисел
n = int(input("Введите N: "))
evens = [i for i in range(2, n + 1, 2)]
if not evens:
    print("чётных чисел нет")
else:
    even_sum = sum(evens)
    even_prod = 1
    for num in evens:
        even_prod *= num
    print(f"сумма={even_sum}, произведение={even_prod}")


# ЗАДАЧА 7. Факториал и сумма его цифр
n = int(input("Введите N: "))
fact = 1
for i in range(2, n + 1):
    fact *= i
digit_sum = sum(int(ch) for ch in str(fact))
print(f"{n}! = {fact}, сумма цифр = {digit_sum}")


# ЗАДАЧА 8. Реверс слов в предложении
text = input("Введите строку: ")
words = text.split()
print(" ".join(reversed(words)))


# ЗАДАЧА 9. Палиндром (без учёта регистра и знаков)
def is_palindrome(s: str) -> bool:
    punct = set(".,!?;:-")
    cleaned = "".join(ch.lower() for ch in s if ch not in punct and not ch.isspace())
    return cleaned == cleaned[::-1]

s = input("Введите строку: ")
print(is_palindrome(s))


# ЗАДАЧА 10. Гласные и согласные
text = input("Введите строку: ")
vowels = set("аеёиоуыэюя")
vowel_count = 0
consonant_count = 0

for ch in text.lower():
    if ch.isalpha():
        if ch in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print(f"гласных={vowel_count}, согласных={consonant_count}")


# ЗАДАЧА 11. Квадраты только положительных чисел
def square_positives(nums: list[int]) -> list[int]:
    return [x * x if x > 0 else 0 for x in nums]

print(square_positives([1, -2, 3, -4, 0]))
print(square_positives([-5, -1]))


# ЗАДАЧА 12. Среднее без чётных
def avg_without_evens(nums: list[int]) -> float:
    odds = [x for x in nums if x % 2 != 0]
    target = odds if odds else nums
    return sum(target) / len(target)

print(avg_without_evens([10, 3, 20, 7]))
print(avg_without_evens([2, 4, 6]))
print(avg_without_evens([1, 2, 3]))


# ЗАДАЧА 13. Удаление дубликатов с подсчётом
def unique_with_counts(items: list) -> tuple[list, dict]:
    counts = {}
    unique = []
    for item in items:
        counts[item] = counts.get(item, 0) + 1
        if item not in unique:
            unique.append(item)
    return unique, counts

u1, c1 = unique_with_counts([1, 2, 2, 3, 1, 4])
print(u1)
print(c1)

u2, c2 = unique_with_counts(["a", "b", "a"])
print(u2)
print(c2)


# ЗАДАЧА 14. Минимум, максимум и их индексы
def min_max_with_indices(nums: list[int]) -> str:
    min_val = nums[0]
    min_idx = 0
    max_val = nums[0]
    max_idx = 0

    for i in range(1, len(nums)):
        if nums[i] < min_val:
            min_val = nums[i]
            min_idx = i
        if nums[i] > max_val:
            max_val = nums[i]
            max_idx = i

    return f"мин={min_val} (индекс {min_idx}), макс={max_val} (индекс {max_idx})"

print(min_max_with_indices([3, 1, 9, 4]))
print(min_max_with_indices([-5, 0, 5]))
print(min_max_with_indices([42]))


# ЗАДАЧА 15. Сортировка по чётности
def sort_by_parity(nums: list[int]) -> list[int]:
    evens = sorted(x for x in nums if x % 2 == 0)
    odds = sorted(x for x in nums if x % 2 != 0)
    return evens + odds

print(sort_by_parity([5, 2, 8, 1, 4, 7]))
print(sort_by_parity([3, -1, 0, 10]))
print(sort_by_parity([1, 3, 5]))


# ЗАДАЧА 16. Калькулятор с историей
history = []
while True:
    expr = input().strip()
    if expr == "exit":
        print("(выход)")
        break

    parts = expr.split()
    if len(parts) != 3:
        print("неизвестная операция")
        continue

    try:
        a = float(parts[0])
        op = parts[1]
        b = float(parts[2])
    except ValueError:
        print("неизвестная операция")
        continue

    if op == "+":
        res = a + b
    elif op == "-":
        res = a - b
    elif op == "*":
        res = a * b
    elif op == "/":
        if b == 0:
            print("деление на ноль")
            continue
        res = a / b
    else:
        print("неизвестная операция")
        continue

    if isinstance(res, float) and res.is_integer():
        res = int(res)
    history.append((expr, res))
    print(res)


# ЗАДАЧА 17. Угадай число (с подсчётом попыток)
import random

secret = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Введите число: "))
    attempts += 1
    if guess < secret:
        print("больше")
    elif guess > secret:
        print("меньше")
    else:
        print(f"угадал за {attempts} попытки" if attempts in (2, 3, 4) else f"угадал за {attempts} попыток")
        break


# ЗАДАЧА 18. FizzBuzz с суммой
n = int(input("Введите N: "))
out = []
counts = {"Fizz": 0, "Buzz": 0, "FizzBuzz": 0}

for i in range(1, n + 1):
    if i % 15 == 0:
        out.append("FizzBuzz")
        counts["FizzBuzz"] += 1
    elif i % 3 == 0:
        out.append("Fizz")
        counts["Fizz"] += 1
    elif i % 5 == 0:
        out.append("Buzz")
        counts["Buzz"] += 1
    else:
        out.append(str(i))

print(", ".join(out))
print(f"Fizz: {counts['Fizz']}, Buzz: {counts['Buzz']}, FizzBuzz: {counts['FizzBuzz']}")


# ЗАДАЧА 19. Телефонная книга с командами
phonebook = {}

while True:
    line = input().strip()
    if not line:
        continue
    parts = line.split()
    cmd = parts[0].lower()

    if cmd == "add" and len(parts) >= 3:
        name = parts[1]
        phone = parts[2]
        phonebook[name] = phone
        print("добавлено")
    elif cmd == "get" and len(parts) == 2:
        name = parts[1]
        print(phonebook.get(name, "не найдено"))
    elif cmd == "del" and len(parts) == 2:
        name = parts[1]
        if name in phonebook:
            del phonebook[name]
            print("удалено")
        else:
            print("не найдено")
    elif cmd == "list":
        if not phonebook:
            print("(пусто)")
        else:
            for name, phone in phonebook.items():
                print(f"{name}: {phone}")
    elif cmd == "exit":
        break
    else:
        print("неизвестная команда")


# ЗАДАЧА 20. Частотный анализ слов
import re

text = input("Введите строку: ").lower()
# Удаляем знаки препинания (.,!?;:) и разбиваем на слова
cleaned = re.sub(r"[.,!?;:]", " ", text)
words = cleaned.split()

freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1

sorted_freq = sorted(freq.items(), key=lambda item: (-item[1], item[0]))
print(", ".join(f"{word}: {count}" for word, count in sorted_freq))

