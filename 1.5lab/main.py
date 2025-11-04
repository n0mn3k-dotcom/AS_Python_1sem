if __name__ == "__main__":
    pass

spisok = [42,52,85,33,82,14,164,44335,19,23,78]

new_spisok = sorted([num for num in spisok if num % 2 == 0])

print(new_spisok)
