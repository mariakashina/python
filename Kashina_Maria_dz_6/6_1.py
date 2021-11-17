import sys

f_name = 'bakery.csv'
with open(f_name, 'a+', encoding='utf-8') as f:
    print(sys.argv[-1], file=f)
