import os

file_name = input('Введите имя файла в текущей директории: ')
stat = {}
extensions = {}
res = {}
a = os.path.join('./', file_name)
for root, dirs, files in os.walk(os.path.join('./', file_name)):
    for file in files:
        n = 1
        size = os.stat(os.path.join(root, file)).st_size
        while size // 10 > 0:
            n += 1
            size = size // 10
            stat[10 ** n] = 0
            extensions[10 ** n] = []
for root, dirs, files in os.walk(os.path.join('./', file_name)):
    for file in files:
        n = 1
        size = os.stat(os.path.join(root, file)).st_size
        for key in stat:
            if size < int(key):
                stat[key] += 1
                extensions[key].append(os.path.splitext(file)[-1])
                for el in extensions[key][:-1]:
                    if os.path.splitext(file)[-1] == el:
                        extensions[key].remove(el)
                break
for key in stat:
    res[key] = (stat[key], extensions[key])
print(res)
