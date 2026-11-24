# 1
name = input()
print("Имя не введено" if not name else f"Привет, {name}! Длина имени: {len(name)}. {name.upper()}")

# 2
a, b = float(input()), float(input())
s, d, p = a + b, a - b, a * b
if b == 0:
    print(f"сумма={s}, разность={d}, произведение={p}, деление на ноль")
else:
    print(f"сумма={s}, разность={d}, произведение={p}, частное={round(a/b, 2)}, остаток={round(a%b, 2)}")

# 3
n = int(input())
p = "чётное" if n % 2 == 0 else "нечётное"
z = "положительное" if n > 0 else ("отрицательное" if n < 0 else "ноль")
k = "да" if n % 5 == 0 else "нет"
print(f"{p}, {z}, кратно 5: {k}")

# 4
a = [int(input()), int(input()), int(input())]
print("по возрастанию:", *sorted(a))
print("по убыванию:", *sorted(a, reverse=True))
print(f"мин={min(a)}, макс={max(a)}")

# 5
n = int(input())
w = len(str(n * n)) + 1
for i in range(1, n + 1):
    print("".join(f"{i*j:<{w}}" for j in range(1, n + 1)).rstrip())

# 6
n = int(input())
ev = [i for i in range(2, n + 1, 2)]
if not ev:
    print("чётных чисел нет")
else:
    m = 1
    for x in ev: m *= x
    print(f"сумма={sum(ev)}, произведение={m}")

# 7
n = int(input())
f = 1
for i in range(2, n + 1): f *= i
print(f"{n}! = {f}, сумма цифр = {sum(int(c) for c in str(f))}")

# 8
print(" ".join(input().split()[::-1]))

# 9
s = "".join(c.lower() for c in input() if c.isalnum())
print(s == s[::-1])

# 10
t = input().lower()
gl = "аеёиоуыэюяaeiouy"
g = sum(1 for c in t if c.isalpha() and c in gl)
s = sum(1 for c in t if c.isalpha() and c not in gl)
print(f"гласных={g}, согласных={s}")

# 11
a = [1, -2, 3, -4, 0]
print([x*x if x > 0 else 0 for x in a])

# 12
a = [10, 3, 20, 7]
b = [x for x in a if x % 2 != 0] or a
print(sum(b) / len(b))

# 13
a = [1, 2, 2, 3, 1, 4]
u = list(dict.fromkeys(a))
c = {x: a.count(x) for x in u}
print(u)
print(c)

# 14
a = [3, 1, 9, 4]
mn = mx = a[0]
mi = ma = 0
for i, x in enumerate(a):
    if x < mn: mn, mi = x, i
    if x > mx: mx, ma = x, i
print(f"мин={mn} (индекс {mi}), макс={mx} (индекс {ma})")

# 15
a = [5, 2, 8, 1, 4, 7]
print(sorted(a, key=lambda x: (x % 2, x)))

# 16
while True:
    s = input().split()
    if s[0] == "exit": break
    x, op, y = float(s[0]), s[1], float(s[2])
    if op == "+": print(x + y)
    elif op == "-": print(x - y)
    elif op == "*": print(x * y)
    elif op == "/": print("деление на ноль" if y == 0 else x / y)
    else: print("неизвестная операция")

# 17
import random
n = random.randint(1, 100)
k = 0
while True:
    g = int(input())
    k += 1
    if g > n: print("меньше")
    elif g < n: print("больше")
    else: print(f"угадал за {k} попытки"); break

# 18
n = int(input())
res = []
f = b = fb = 0
for i in range(1, n + 1):
    if i % 15 == 0: res.append("FizzBuzz"); fb += 1
    elif i % 3 == 0: res.append("Fizz"); f += 1
    elif i % 5 == 0: res.append("Buzz"); b += 1
    else: res.append(str(i))
print(", ".join(res))
print(f"Fizz: {f}, Buzz: {b}, FizzBuzz: {fb}")

# 19
book = {}
while True:
    p = input().split()
    if not p: continue
    if p[0] == "add": book[p[1]] = p[2]; print("добавлено")
    elif p[0] == "get": print(book.get(p[1], "не найдено"))
    elif p[0] == "del": print("удалено" if book.pop(p[1], None) else "не найдено")
    elif p[0] == "list":
        for k, v in book.items(): print(f"{k}: {v}")

# 20
t = input().lower()
for c in ".,!?;:—-": t = t.replace(c, "")
w = t.split()
d = {x: w.count(x) for x in set(w)}
for k, v in sorted(d.items(), key=lambda x: -x[1]):
    print(f"{k}: {v}", end=", ")
