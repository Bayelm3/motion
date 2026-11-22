# ЗАДАЧА 1. Приветствие с анализом имени
name = input().strip()
if not name:
    print("Имя не введено")
else:
    print(f"Привет, {name}! Длина имени: {len(name)}. {name.upper()}")


# ЗАДАЧА 2. Анализ двух чисел
a = int(input())
b = int(input())
res = f"сумма={a + b}, разность={a - b}, произведение={a * b}, "
if b == 0:
    res += "деление на ноль"
else:
    res += f"частное={a / b:.2f}, остаток={a % b}"
print(res)


# ЗАДАЧА 3. Классификация числа
n = int(input())
parity = "чётное" if n % 2 == 0 else "нечётное"
sign = "положительное" if n > 0 else ("отрицательное" if n < 0 else "ноль")
mult5 = "да" if n % 5 == 0 else "нет"
print(f"{parity}, {sign}, кратно 5: {mult5}")


# ЗАДАЧА 4. Упорядочить три числа
nums = [int(input()) for _ in range(3)]
asc = sorted(nums)
desc = sorted(nums, reverse=True)
print("по возрастанию:", *asc)
print("по убыванию:", *desc)
print(f"мин={asc[0]}, макс={asc[-1]}")


# ЗАДАЧА 5. Квадратная таблица умножения
n = int(input())
width = len(str(n * n)) + 1
for i in range(1, n + 1):
    row = "".join(f"{i * j:<{width}}" for j in range(1, n + 1))
    print(row.rstrip())


# ЗАДАЧА 6. Сумма и произведение чётных чисел
n = int(input())
evens = [i for i in range(2, n + 1, 2)]
if not evens:
    print("чётных чисел нет")
else:
    prod = 1
    for x in evens:
        prod *= x
    print(f"сумма={sum(evens)}, произведение={prod}")


# ЗАДАЧА 7. Факториал и сумма его цифр
n = int(input())
fact = 1
for i in range(2, n + 1):
    fact *= i
digits_sum = sum(int(d) for d in str(fact))
print(f"{n}! = {fact}, сумма цифр = {digits_sum}")


# ЗАДАЧА 8. Реверс слов в предложении
text = input()
words = text.split()
print(" ".join(words[::-1]))


# ЗАДАЧА 9. Палиндром (без учёта регистра и знаков)
text = input().lower()
cleaned = "".join(ch for ch in text if ch.isalnum())
print(cleaned == cleaned[::-1])


# ЗАДАЧА 10. Гласные и согласные
text = input().lower()
vowels_set = set("аеёиоуыэюяaeiouy")
vowels = sum(1 for ch in text if ch in vowels_set)
consonants = sum(1 for ch in text if ch.isalpha() and ch not in vowels_set)
print(f"гласных={vowels}, согласных={consonants}")


# ЗАДАЧА 11. Квадраты только положительных чисел
def positive_squares(nums):
    return [x ** 2 if x > 0 else 0 for x in nums]


# ЗАДАЧА 12. Среднее без чётных
def odd_average(nums):
    odds = [x for x in nums if x % 2 != 0]
    if not odds:
        return sum(nums) / len(nums) if nums else 0
    return sum(odds) / len(odds)


# ЗАДАЧА 13. Удаление дубликатов с подсчётом
def unique_with_counts(items):
    unique = []
    counts = {}
    for item in items:
        if item not in counts:
            unique.append(item)
            counts[item] = 0
        counts[item] += 1
    print(unique)
    print(counts)


# ЗАДАЧА 14. Минимум, максимум и их индексы
def min_max_indices(nums):
    min_val = max_val = nums[0]
    min_idx = max_idx = 0
    for i in range(1, len(nums)):
        if nums[i] < min_val:
            min_val = nums[i]
            min_idx = i
        if nums[i] > max_val:
            max_val = nums[i]
            max_idx = i
    print(f"мин={min_val} (индекс {min_idx}), макс={max_val} (индекс {max_idx})")


# ЗАДАЧА 15. Сортировка по чётности
def sort_by_parity(nums):
    return sorted(nums, key=lambda x: (x % 2 != 0, x))

    