import os

file_name = input('Введите имя папки в текущей директории: ')
stat = {}
a = os.path.join('./', file_name)
for root, dirs, files in os.walk(os.path.join('./', file_name)):
    for file in files:
        n = 1
        size = os.stat(os.path.join(root, file)).st_size
        while size // 10 > 0:
            n += 1
            size = size // 10
            stat[10 ** n] = 0
for root, dirs, files in os.walk(os.path.join('./', file_name)):
    for file in files:
        n = 1
        size = os.stat(os.path.join(root, file)).st_size
        for key in stat:
            if size < int(key):
                stat[key] += 1
                break
print(stat)
