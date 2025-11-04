if __name__ == "__main__":
    pass

numbers = [3, 7, 2, 8, 5, 1, 4, 6]


for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        print(numbers[i], end='')

print()

for i in range(len(numbers)-1, -1, -1):
    if numbers[i] % 2 == 1:
        print(numbers[i], end='')
