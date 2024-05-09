#!/usr/bin/env python3

import sys
import re

with open(sys.argv[1], 'r') as f:
    content = f.read()

oneline_matches = 'pkg(ver|rel)=[^\n]+'
multiline_matches = '(sha256|md5)sums[^\\s]*=\\([^)]+\\)'
regexp = re.compile('^(' + oneline_matches + '|' + multiline_matches + ')', re.MULTILINE)

print(regexp.sub('', content))

