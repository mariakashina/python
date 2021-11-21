import os
import shutil
from pathlib import Path

for root, dirs, files in os.walk('./my_project'):
    for file in dirs:
        if file.endswith('html'):
            name = os.path.split(root)[-1]
            scr = Path(root, file)
            fsrc = Path('./my_project/mainapp/templates', name, file)
            if not os.path.exists(fsrc):
                shutil.copytree(scr, fsrc)
