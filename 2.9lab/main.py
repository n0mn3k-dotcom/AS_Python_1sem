if __name__ == "__main__":
    pass


f1 = open("2.9file1.txt", "r", encoding="utf-8")
lines1 = f1.readlines()
f1.close()

f2 = open("2.9file2.txt", "r", encoding="utf-8")
lines2 = f2.readlines()
f2.close()

mat1 = []
mat2 = []

mat = []
for line in lines1:
    line = line.strip()
    if line == "":
        if mat != []:
            mat1.append(mat)
            mat = []
    else:
        mat.append([int(x) for x in line.split()])
if mat != []:
    mat1.append(mat)

mat = []
for line in lines2:
    line = line.strip()
    if line == "":
        if mat != []:
            mat2.append(mat)
            mat = []
    else:
        mat.append([int(x) for x in line.split()])
if mat != []:
    mat2.append(mat)

for m in mat1:
    if m not in mat2:
        mat2.append(m)

print("Файл 1:")
for m in mat1:
    for row in m:
        print(" ".join(str(x) for x in row))
    print()

print("Файл 2:")
for m in mat2:
    for row in m:
        print(" ".join(str(x) for x in row))
    print()

f2 = open("2.9file2.txt", "w", encoding="utf-8")
for m in mat2:
    for row in m:
        f2.write(" ".join(str(x) for x in row) + "\n")
    f2.write("\n")
f2.close()
