IPs = []
spams = {}
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        IPs.append(line.split(' ')[0])
    set_of_IPs = set(IPs)
    for IP in set_of_IPs:
        spams[IP] = '0'
    for IP in IPs:
        if IP in set_of_IPs:
            spams[IP] = int(spams.get(IP)) + 1
print(max(spams, key=spams.get))
