#!/usr/bin/env python3

import io
import sys
from datetime import datetime


def timestamp_to_seconds(ts):
    dt = datetime.strptime(ts, "%H:%M:%S")

    return dt.hour * 3600 + dt.minute * 60 + dt.second


def get_title_and_duration(part: str):
    try:
        pre, tail = part.split('+ title ', 1)
        title_num, tail = tail.split(':', 1)
        _, duration = tail.split('+ duration: ', 1)
        duration, part = duration.split('\n', 1)
    except:
        return '-1', '', ''

    # print(f'{title_num} {duration}')

    return title_num, duration, part

# _in = sys.argv[1]

# with open(_in) as f:
#     content = f.read()
try:
    content = sys.stdin.read()
except:
    input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='latin-1')
    content = input_stream.read()

titles = {}
content_end = False
while not content_end:
    title_num, duration, content = get_title_and_duration(content)
    if len(content) <= 0:
        content_end = True
    if len(duration) > 0:
        titles[title_num] = duration

# print(titles)


longest_title = -1
pre_duration_sec = -1
for title_num, duration in titles.items():
    duration_sec = timestamp_to_seconds(duration)
    if pre_duration_sec < duration_sec:
        longest_title = title_num
        pre_duration_sec = duration_sec

print(longest_title, end='')

# @TODO convert durations to seconds

