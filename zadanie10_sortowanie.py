import random
unsorted_list = []
sorted_list = []
python_sorted_list = []
for x in range(50):
    unsorted_list.append(random.randrange(100))
print ('unsorted:', unsorted_list)
while unsorted_list:
    biggest = unsorted_list[0]
    for index in range(len(unsorted_list)):
        if unsorted_list[index]>biggest:
            biggest = unsorted_list[index]
    unsorted_list.remove(biggest)
    sorted_list.append(biggest)
print('sorted:', sorted_list)
