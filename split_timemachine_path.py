#!/usr/bin/env python3

import sys


path=sys.argv[1]
idx=int(sys.argv[2])

# /Volumes/.timemachine/3C72A118-1342-4EBE-8E3B-7252F97963B7/2023-04-27-040313.backup/2023-04-27-040313.backup
if idx == 0:
    # /Volumes/.timemachine/3C72A118-1342-4EBE-8E3B-7252F97963B7
    print(path.rsplit("/", 2)[idx])
else:
    # 2023-04-27-040313.backup/2023-04-27-040313.backup
    print('/'.join(path.rsplit("/", 2)[idx:]))
