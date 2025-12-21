if __name__ == "__main__":
    pass


import math

def RingS(R1, R2):
    if R1 < R2:
        R1, R2 = R2, R1

    s = math.pi * (R1 * R1 - R2 * R2)
    return s


r1 = float(input("Введите R1: "))
r2 = float(input("Введите R2: "))

result = RingS(r1, r2)
print("Площадь =", result)
