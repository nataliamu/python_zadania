import os

def parse_folder(path):
    print('Folder:', path)
    for file in os.listdir(path):
        filepath = os.path.join(path, file)
        if os.path.isfile(filepath):
            print(filepath)
    for file in os.listdir(path):
        filepath = os.path.join(path, file)
        if not os.path.isfile(filepath):
            parse_folder(filepath)


path = input('Podaj ścieżkę:') # './'
parse_folder(path)
