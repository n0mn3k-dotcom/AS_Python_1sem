if __name__ == "__main__":
    pass



calls = 0

def FibRec(n):
    global calls
    calls += 1
    if n == 1 or n == 2:
        return 1
    else:
        return FibRec(n-1) + FibRec(n-2)

numbers = [5, 6, 7, 8, 9]

for num in numbers:
    calls = 0
    f = FibRec(num)
    print(f"Fib({num}) = {f}, calls = {calls}")
