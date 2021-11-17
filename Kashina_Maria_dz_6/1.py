with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print((line.split(' ')[0], line.split('"')[1].split(' ')[0], line.split(' /')[1].split(' ')[0]))
