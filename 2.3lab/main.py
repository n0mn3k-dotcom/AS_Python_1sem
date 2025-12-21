if __name__ == "__main__":
    pass

def Transp(A):
    return list(map(list, zip(*A)))


m = int(input("Введите размер матрицы: "))

A = [list(map(int, input().split())) for _ in range(m)]

T = Transp(A)

for row in T:
    print(*row)
