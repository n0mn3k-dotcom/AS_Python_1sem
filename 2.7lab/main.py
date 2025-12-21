if __name__ == "__main__":
    pass

with open("2.7file1.txt", "r", encoding="utf-8") as f1:
    lines1 = f1.readlines()

with open("2.7file2.txt", "r", encoding="utf-8") as f2:
    lines2 = f2.readlines()

new_lines = []
for i in range(len(lines1)):
    line1 = lines1[i].rstrip("\n")
    if i < len(lines2):
        line2 = lines2[i].rstrip("\n")
        new_lines.append(line1 + line2 + "\n")
    else:
        new_lines.append(line1 + "\n")

with open("2.7file1.txt", "w", encoding="utf-8") as f1:
    f1.writelines(new_lines)

print("Файлы объединены: ")
for line in new_lines:
    print(line, end="")
