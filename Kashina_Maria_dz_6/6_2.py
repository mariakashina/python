# простой запуск скрипта
with open('bakery.csv', 'r', encoding='utf-8') as f:
    for line in f:
        print(line[-1])

# запуск скрипта с одним параметром-числом
import sys

with open('bakery.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()[int(sys.argv[-2])-1:]
    for line in lines:
        print(line[:-1])

# запуск скрипта с двум числами
import sys

with open('bakery.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()[int(sys.argv[-2])-1:int(sys.argv[-1])]
    for line in lines:
        print(line[:-1])
