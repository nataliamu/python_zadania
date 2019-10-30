import random
from multiprocessing import Pool, Process, Array

data_range = 40


def generate_list(size):
    return [random.randint(0, data_range - 1) for _ in range(size)]


def generate_hist(size):
    return [0]*size


def fill_hist(hist, tab):
    for i in tab:
        hist[i] = hist[i] + 1
    return hist


pool = Pool(processes=4)
data = generate_list(100)
histogram = generate_hist(data_range)
fill_hist(histogram, data)
result = Array('i', range(data_range))
for j in range(data_range):
    result[j] = 0


proc1 = Process(target=fill_hist, args=(result, data[0:25]))
proc2 = Process(target=fill_hist, args=(result, data[25:50]))
proc3 = Process(target=fill_hist, args=(result, data[50:75]))
proc4 = Process(target=fill_hist, args=(result, data[75:100]))

proc1.start()
proc2.start()
proc3.start()
proc4.start()

proc1.join()
proc2.join()
proc3.join()
proc4.join()

printable_result = generate_hist(data_range)

print(histogram)
for i in range(data_range):
    printable_result[i] = result[i]
print(printable_result)
print([i for i in range(data_range)])



'''
import random
from multiprocessing import Pool

def create_histogram(size):
    l = []
    for i in range(0, size):
        l.append(random.randint(0, 100))

    histogram = [0] * (size + 1)
    for j in l:
        histogram[j] = histogram[j] + 1
    return histogram


p = Pool()
hist = p.map(create_histogram, (500000,) )
'''
