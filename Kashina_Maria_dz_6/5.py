import sys

file1 = sys.argv[-3]
file2 = sys.argv[-2]
file3 = sys.argv[-1]
n = -1
with open(file3, 'x', encoding='utf-8') as f3, \
        open(file1, 'r', encoding='utf-8') as f1, \
        open(file2, 'r', encoding='utf-8') as f2:
    for line in f2:
        hobby = line[:-1]
        users = f1.readline()[:-1]
        n += 1
        if users == '':
            sys.exit(1)
        else:
            f3.writelines(f'{users}: {hobby}\n')
    lines = f1.readlines()[n:]
    for line in lines:
        users = line[:-1]
        f3.writelines(f'{users}: None\n')
