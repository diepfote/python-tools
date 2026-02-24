#!/usr/bin/env python

from sys import argv
from datetime import datetime


# valid input for exiftool
date_format = '%Y:%m:%d %H:%M:%S'  # '2023:12:20 00:02:07'
if len(argv) > 1:
    # alternate input date formats
    date_format=argv[1]

_in = input().strip()


# rewrites a date for exiftool
# exiftool -'ContentCreateDate'='2018:02:02 00:00:00' asdf.mp4

out = ''
formats_to_try = [
        # e.g. 'June 25, 2023'
        '%Y%m%dT%H%M%S%z',

        # e.g. '25 of June, 2023'
        # in order for this to work you have to trim
        # 'st', 'nd', 'rd', 'th' from the number first
        # did this with sed. did not bother to redo it here
        '%d of %B, %Y',

        # e.g. '20250525'
        '%Y%m%d',

        # e.g. '2025-05-25T05:24:00+0000'
        '%Y-%m-%dT%H:%M:%S%z',

        # e.g. 2026:01:15 03:00:00
        '%Y:%m:%d %H:%M:%S',

        # e.g. 'October 31, 2025 at 2:00 PM UTC'
        '%B %d, %Y at %H:%M %p %Z'
        ]
for f in formats_to_try:
    try:
        out = datetime.strptime(_in, f)
        # only continue the loop if we hit an exception
        # this way we will try all specified formats if necessary
        break
    except:
        pass


print(out.strftime(date_format))

