import random


# 1. Приветствие с анализом имени
def task_1(name: str):
    if not name or not name.strip():
        print("Имя не введено")
        return
    clean_name = name.strip()
    print(f"Привет, {clean_name}! Длина имени: {len(clean_name)}. {clean_name.upper()}")


# 2. Анализ двух чисел
def task_2(a: float, b: float):
    s = a + b
    d = a - b
    p = a * b
    if b == 0:
        print(f"сумма={s:g}, разность={d:g}, произведение={p:g}, деление на ноль")
    else:
        q = a / b
        rem = a % b
        print(f"сумма={s:g}, разность={d:g}, произведение={p:g}, частное={q:.2f}, остаток={rem:g}")


# 3. Классификация числа
def task_3(n: int):
    parity = "чётное" if n % 2 == 0 else "нечётное"
    if n > 0:
        sign = "положительное"
    elif n < 0:
        sign = "отрицательное"
    else:
        sign = "ноль"
    mult5 = "да" if n % 5 == 0 else "нет"
    print(f"{parity}, {sign}, кратно 5: {mult5}")


# 4. Упорядочить три числа
def task_4(a: int, b: int, c: int):
    asc = sorted([a, b, c])
    desc = sorted([a, b, c], reverse=True)
    print(f"по возрастанию: {' '.join(map(str, asc))}")
    print(f"по убыванию: {' '.join(map(str, desc))}")
    print(f"мин={asc[0]}, макс={asc[-1]}")


# 5. Квадратная таблица умножения
def task_5(n: int):
    max_width = len(str(n * n)) + 1
    for i in range(1, n + 1):
        row = "".join(f"{i * j:<{max_width}}" for j in range(1, n + 1)).rstrip()
        print(row)


# 6. Сумма и произведение чётных чисел
def task_6(n: int):
    evens = [x for x in range(1, n + 1) if x % 2 == 0]
    if not evens:
        print("чётных чисел нет")
        return
    total_sum = sum(evens)
    total_prod = 1
    for x in evens:
        total_prod *= x
    print(f"сумма={total_sum}, произведение={total_prod}")


# 7. Факториал и сумма его цифр
def task_7(n: int):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    digit_sum = sum(int(ch) for ch in str(fact))
    print(f"{n}! = {fact}, сумма цифр = {digit_sum}")


# 8. Реверс слов в предложении
def task_8(text: str) -> str:
    words = text.strip().split()
    return " ".join(reversed(words))


# 9. Палиндром (без учёта регистра и знаков)
def task_9(text: str) -> bool:
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


# 10. Гласные и согласные
def task_10(text: str):
    vowels = set("аеёиоуыэюяaeiou")
    v_count = 0
    c_count = 0
    for ch in text.lower():
        if ch.isalpha():
            if ch in vowels:
                v_count += 1
            else:
                c_count += 1
    print(f"гласных={v_count}, согласных={c_count}")


# 11. Квадраты только положительных чисел
def task_11(nums: list[int]) -> list[int]:
    return [x * x if x > 0 else 0 for x in nums]


# 12. Среднее без чётных
def task_12(nums: list[int]) -> float:
    odds = [x for x in nums if x % 2 != 0]
    target = odds if odds else nums
    return sum(target) / len(target) if target else 0.0


# 13. Удаление дубликатов с подсчётом
def task_13(items: list):
    unique = []
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
        if item not in unique:
            unique.append(item)
    return unique, counts


# 14. Минимум, максимум и их индексы
def task_14(nums: list[int]):
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
    print(f"мин={min_val} (индекс {min_idx}), макс={max_val} (индекс {max_idx})")


# 15. Сортировка по чётности
def task_15(nums: list[int]) -> list[int]:
    evens = sorted(x for x in nums if x % 2 == 0)
    odds = sorted(x for x in nums if x % 2 != 0)
    return evens + odds


# 16. Калькулятор с историей
def task_16(commands: list[str]):
    history = []
    for raw in commands:
        cmd = raw.strip()
        if cmd == "exit":
            print("(выход)")
            break
        parts = cmd.split()
        if len(parts) != 3:
            print("неизвестная операция")
            continue
        left_s, op, right_s = parts
        try:
            a = float(left_s)
            b = float(right_s)
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

        formatted = int(res) if res.is_integer() else res
        history.append((cmd, formatted))
        print(formatted)
    return history


# 17. Угадай число (с подсчётом попыток)
def task_17(guesses: list[int], secret: int | None = None):
    if secret is None:
        secret = random.randint(1, 100)
    attempts = 0
    for guess in guesses:
        attempts += 1
        if guess > secret:
            print("меньше")
        elif guess < secret:
            print("больше")
        else:
            print(f"угадал за {attempts} попытки")
            return attempts


# 18. FizzBuzz с суммой
def task_18(n: int):
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


# 19. Телефонная книга с командами
def run_phonebook(commands: list[str]):
    book: dict[str, str] = {}
    for line in commands:
        parts = line.strip().split()
        if not parts:
            continue
        action = parts[0].lower()
        if action == "add" and len(parts) >= 3:
            name, phone = parts[1], parts[2]
            book[name] = phone
            print("добавлено")
        elif action == "get" and len(parts) >= 2:
            name = parts[1]
            print(book.get(name, "не найдено"))
        elif action == "del" and len(parts) >= 2:
            name = parts[1]
            if name in book:
                del book[name]
                print("удалено")
            else:
                print("не найдено")
        elif action == "list":
            if not book:
                print("(пусто)")
            else:
                for k, v in book.items():
                    print(f"{k}: {v}")


# 20. Частотный анализ слов
def task_20(text: str):
    punct = ".,!?;:—-"
    cleaned = "".join(ch.lower() if ch not in punct else " " for ch in text)
    words = cleaned.split()
    freq: dict[str, int] = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    print(", ".join(f"{k}: {v}" for k, v in sorted_items))


if __name__ == "__main__":
    task_1("Аня")
    task_2(10, 3)
    task_3(10)
    task_4(5, 12, 9)
    task_5(3)
    task_6(10)
    task_7(5)
    print(task_8("я люблю python"))
    print(task_9("А роза упала на лапу Азора"))
    task_10("привет мир")
    print(task_11([1, -2, 3, -4, 0]))
    print(task_12([10, 3, 20, 7]))
    print(task_13([1, 2, 2, 3, 1, 4]))
    task_14([3, 1, 9, 4])
    print(task_15([5, 2, 8, 1, 4, 7]))
    task_16(["10 + 5", "20 / 4", "7 / 0", "7 # 6", "exit"])
    task_17([50, 25, 40, 42], secret=42)
    task_18(15)
    run_phonebook([
        "add Аня +996700111222",
        "add Борис +996700333444",
        "get Аня",
        "get Петя",
        "del Борис",
        "list",
    ])
    task_20("Я люблю Python. Python — это круто!")