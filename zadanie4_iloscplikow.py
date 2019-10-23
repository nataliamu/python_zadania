import os

path = './'
file_count = 0
for files in os.listdir(path):
    if os.path.isfile(os.path.join(path, files)):
        file_count +=1

print (file_count)
