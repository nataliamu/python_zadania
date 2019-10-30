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



'''
import random
import time
import multiprocessing


array = [ random.randint(0, 10) for i in range(1000000) ]


def count(data):
    result = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0}
    for i in data:
        result[i] += 1
    return result

start_1 = time.perf_counter()
result_1 = count(array)
hist_time_1 = time.perf_counter() - start_1
print(hist_time_1, ' -> ', result_1)


# ----------------------------------------------------
import multiprocessing

if __name__ == '__main__':
    array = [ random.randint(0, 10) for i in range(1000000) ]


    def process_worker(name, data, process_result):
        result = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0}
        for i in data:
            result[i] += 1
        process_result[name] = result

    manager = multiprocessing.Manager()
    process_result = manager.dict()
    jobs = []

    p1 = multiprocessing.Process(target=process_worker, args=(1, array[:200000], process_result))
    p2 = multiprocessing.Process(target=process_worker, args=(2, array[200000:400000], process_result))
    p3 = multiprocessing.Process(target=process_worker, args=(3, array[400000:600000], process_result))
    p4 = multiprocessing.Process(target=process_worker, args=(4, array[600000:800000], process_result))
    p5 = multiprocessing.Process(target=process_worker, args=(5, array[800000:], process_result))
    jobs.append(p1)
    jobs.append(p2)
    jobs.append(p3)
    jobs.append(p4)
    jobs.append(p5)

    for p in jobs: p.start()
    for p in jobs: p.join()
    print(process_result.values())
    '''
