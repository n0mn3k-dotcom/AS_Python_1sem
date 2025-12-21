if __name__ == "__main__":
    pass

with open("f.txt", "r", encoding="utf-8") as f:
    numbers = [float(line.strip()) for line in f if line.strip() != ""]


min_num = min(numbers)
max_num = max(numbers)


sum_min_max = min_num + max_num

print("Минимальное число:", min_num)
print("Максимальное число:", max_num)
print("Сумма минимума и максимума:", sum_min_max)
