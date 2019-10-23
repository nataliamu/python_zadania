a = [1, 5, 7, 4]
b = [2, 4, 12, 8]

if len(a) == len(b):
    dot = 0
    for i in range(len(a)):
        dot += (a[i]*b[i])
    print("Iloczyn skalarny wektorów a oraz b: " + str(dot))
else:
    print("Wektory mają różną długość!")
