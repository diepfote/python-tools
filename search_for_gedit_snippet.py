#!/usr/bin/env python3

from sys import argv
import re

term         = argv[1]
f_path       = argv[2]

matches = []
empty   = ''
content = empty
with open(f_path, 'r') as f:
    content = f.read()
    
regexp = re.compile(u'    <tag>{}.*?</snippet>'.format(term), re.S)
result = regexp.search(content)
replaced_content = re.sub(regexp, empty, content)

if result:
    print ('  <snippet>')
    print(result.group(0))

print(empty)
print('  ' + str(regexp))

