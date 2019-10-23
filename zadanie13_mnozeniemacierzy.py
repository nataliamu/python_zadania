import random
size = 8
X = [[random.randint(1,100) for a in range(size)] for a in range(size)]
Y = [[random.randint(1,100) for b in range(size)] for b in range(size)]
result = [[0 for x in range(size)] for y in range(size)]
for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

print('pierwsza macierz:\n', X)
print('\n')
print('druga macierz:\n', Y)
print('Wynik mnożenia:\n')

for r in result:
   print(r)
