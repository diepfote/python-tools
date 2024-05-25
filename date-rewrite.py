#!/usr/bin/env python

from datetime import datetime

_in = input()


out = ''
try:
    # e.g. 'June 25, 2023'
    out = datetime.strptime(_in, '%Y%m%dT%H%M%S%z')
except:
    try:
        # e.g. '25 of June, 2023'
        # in order for this to work you have to trim
        # 'st', 'nd', 'rd', 'th' from the number first
        # did this with sed. did not bother to redo it here
        out = datetime.strptime(_in, '%d of %B, %Y')

    except:
        try:
            # e.g. '20250525'
            out = datetime.strptime(_in, '%Y%m%d')
        except:
            # e.g. '2025-05-25T05:24:00+0000'
            out = datetime.strptime(_in, '%Y-%m-%dT%H:%M:%S%z')

# e.g. '2023:12:20 00:02:07'
print(out.strftime("%Y:%m:%d %H:%M:%S"))

