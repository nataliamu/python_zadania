import os

path = './'
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path, file)):
        if file[-4:] == '.jpg':
            file1 = file[0:-3] + 'png'
            print(file)
            os.rename(file, file1)
            
'''
import os
files = os.listdir()
for file in files:
    name, ext = file.split('.')
    if ext == 'jpg':
        os.rename(file,name + ".png")
        
print(files)'''
