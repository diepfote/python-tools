#!/usr/bin/env python

# THIS IS A TEST SCRIPT TO INTERACT WITH NVIM's
# PYTHON INTEGRATION

from pynvim import attach
nvim = attach('socket', path='/tmp/tmp.nvim')


start = nvim.current.buffer.mark('<')[0]
end = nvim.current.buffer.mark('>')[0]

buffer_range = nvim.current.buffer[start:end]
line_count_initial = len(buffer_range)


# TODO DEBUG
print(f'{start=}, {end=}')

content = '\n'.join(buffer_range)

# ---------------------
# regex hokuspokus
# content = content.replace('asdf', 'ptsd')
import re

#yml_array_elem_regex = re.compile("^  -.*?(?=(^  -)|(^\s*$)|\Z)", (re.S|re.M|re.DEBUG))
yml_array_elem_regex = re.compile("(?=^  -)", (re.S|re.M))
# print(yml_array_elem_regex)

yaml_array = yml_array_elem_regex.split(content)

for index, element in enumerate(yaml_array):
    print(f'{element=}')
    yaml_array[index] = element.replace('\n', '')
    # print(f'{yaml_array[index]=}')

line_count_after_hokuspokus = len(yaml_array)

# ---------------------


# replace buffer content with hokuspokus
nvim.current.buffer[start:end] = yaml_array


# sort hokuspokused selection
sort_command = f'{start},{end-line_count_after_hokuspokus+1}sort'
print(f'{sort_command=}')
nvim.command(sort_command)


# refresh content
buffer_range = nvim.current.buffer[start:end-line_count_after_hokuspokus+1]
content = '\n'.join(buffer_range)
yaml_array = content.splitlines()
yaml_array.append('')
if not yaml_array[0]:
  del yaml_array[0]
yaml_array.append('')


# --------------------------
# undo regex hokuspokus


yml_sub_elem_regex = re.compile("(?=\s{4,})", (re.S|re.M))

print(f'before {yaml_array=}')
yaml_array_new = []
for index, element in enumerate(yaml_array):

    sub_array = yml_sub_elem_regex.split(element)
    if len(sub_array) > 1:
        for subelement in sub_array:
            yaml_array_new.append(subelement)
    else:
        yaml_array_new.append(element)


print(f'after {yaml_array_new=}')

# replace buffer, undo hokuspokus
# TODO this adds an empty line at the top and removes a line at the bottom
nvim.current.buffer[start:end-line_count_after_hokuspokus+1] = yaml_array_new

# --------------------------

