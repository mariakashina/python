import os

struct = {}
n1 = 0
with open('config.yaml', 'r', encoding='utf-8') as f:
    file = str(f.readline())[3:-1]
    if not os.path.exists(file):
        os.mkdir(file)
    root = os.path.abspath(file)
    root1 = root
    for line in f:
        n2 = line.rfind('|')
        file1 = line[n2 + 3:-1]
        if n2 > n1:
            if not os.path.exists(os.path.join(root1, file1)):
                os.mkdir(os.path.join(root1, file1))
            n1 = n2
            root = root1
            root1 = os.path.realpath(os.path.join(root1, file1))
        if n2 == n1:
            if not os.path.exists(os.path.join(root, file1)):
                os.mkdir(os.path.join(root, file1))
                root1 = os.path.realpath(os.path.join(root, file1))
        if n2 < n1:
            if not os.path.exists(os.path.join(os.path.abspath(file), file1)):
                os.mkdir(os.path.join(os.path.abspath(file), file1))
                n1 = n2
                root1 = os.path.realpath(os.path.join(os.path.abspath(file), file1))
