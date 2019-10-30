import threading
import random


def histogram(lista, macierz):
    for m in macierz:
        lista[m] = lista[m] + 1


zakres = 5
ilosc = 100

lista = []
for i in range(zakres):
    lista.append(0)


macierz = []
for i in range(ilosc):
    macierz.append(int(random.random() * zakres))

p1 = threading.Thread(target=histogram(lista, macierz[0:int(ilosc / 2)]))
p2 = threading.Thread(target=histogram(lista, macierz[int(ilosc / 2):ilosc]))

p1.start()
p2.start()

p1.join()
p2.join()

for i in range(zakres):
    print("%d =\t %d\n\r" % (i, lista[i]))

for i in range(ilosc):
    print("%d\n\r" % macierz[i])
