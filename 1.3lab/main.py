import math

n = int(input("Введите n: "))
a = 0
for k in range(1, n + 1):
    a += 1 / math.sin(k)
print("S =", a)
