import sys

f1_name = 'users.csv'
f2_name = 'hobby.csv'
f3_name = 'users_hobby.csv'
users_hobby = {}
n = -1
with open(f3_name, 'x', encoding='utf-8') as f3, \
        open(f1_name, 'r', encoding='utf-8') as f1, \
        open(f2_name, 'r', encoding='utf-8') as f2:
    for line in f2:
        hobby = line[:-1]
        users = f1.readline()[:-1]
        n += 1
        if users == '':
            sys.exit(1)
        else:
            users_hobby[users] = hobby
    lines = f1.readlines()[n:]
    for line in lines:
        users = line[:-1]
        users_hobby[users] = None
    f3.write(str(users_hobby))
