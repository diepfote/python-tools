import os
import subprocess
from pprint import pprint


files = [f for f in os.listdir() if f.endswith('.mp4')]

ts_files = {}
for f in files:
    ts_files[f] = int(subprocess.check_output(['ffprobe-get-date', f]))

# pprint(ts_files)

inorder = sorted(ts_files, key=ts_files.get)

# pprint(inorder)

for idx, item in enumerate(inorder, start=1):
    new_no = str(idx).zfill(3)
    f_no_num = item.split(' ', 1)[1]
    print(f'{new_no=},{f_no_num=},{item=}')

    os.rename(item, f'{idx} {f_no_num}')

