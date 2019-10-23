import random

print("1. macierz")
size = 8
rows = {}
for i in range(size):
    rows[i] = []
    for _ in range(size):
        rows[i].append(random.randint(0,10))
    print(str(rows[i]))

print("2. macierz")
columns = {}
for i in range(size):
    columns[i] = []
    for _ in range(size):
        columns[i].append(random.randint(0,10))
    print(str(columns[i]))


print("Wynik: ")
rows3 = {}
for i in range(size):
    rows3[i] = []
    for j in range(size):
        rows3[i].append(columns[i][j] + rows[i][j])
    print(str(rows3[i]))
