import json
import os

if not os.path.exists('my_project'):
    os.mkdir('my_project')
list_files = ['settings', 'mainapp', 'adminapp', 'athapp']
for el in list_files:
    if not os.path.exists(os.path.join('./my_project', el)):
        os.mkdir(os.path.join('./my_project', el))
with open('config.json', 'x', encoding='utf-8') as f:
    json.dump(os.path.join('my_project'), f)
    for el in list_files:
        json.dump(os.path.join(os.path.join('my_project'), el), f)
