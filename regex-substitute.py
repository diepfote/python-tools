#!/usr/bin/env python3

import os
import re
import sys


executable_name = os.path.basename(sys.argv[0])
green = os.environ.get('GREEN', '')
red = os.environ.get('RED', '')
yellow = os.environ.get('YELLOW', '')
purple = os.environ.get('PURPLE', '')
no_color = os.environ.get('NC', '')


def _help():
    usage_info = f'''{red}USAGE{no_color}: {executable_name} ORIGINAL PATTERN REPLACEMENT

{purple}Examples{no_color}:
$ {executable_name} {yellow}'__:45:fc:5d:c3:55:48:89:e5:89:7d:fc' '([0-9a-f_]{{2}}):([0-9a-f_]{{2}}):?' '\\1 \\2'{no_color}
original='__:45:fc:5d:c3:55:48:89:e5:89:7d:fc'
pattern='([0-9a-f_]{{2}}):([0-9a-f_]{{2}}):?'
replacement='\\1 \\2'
{green}__ 45fc 5dc3 5548 89e5 897d fc{no_color}

$ {executable_name} {yellow}'__:45:fc:5d:c3:55:48:89:e5:89:7d:fc' '([0-9a-f_]{{2}}):([0-9a-f_]{{2}}):?' '\\1 \\2'{no_color}  2>/dev/null
{green}__ 45fc 5dc3 5548 89e5 897d fc{no_color}

$ {yellow}echo -n '__:45:fc:5d:c3:55:48:89:e5:89:7d:fc'  | regex-sub '([0-9a-f_]{{2}}):([0-9a-f_]{{2}}):?' '\\1 \\2'{no_color}
original='__:45:fc:5d:c3:55:48:89:e5:89:7d:fc'
pattern='([0-9a-f_]{2}):([0-9a-f_]{2}):?'
replacement='\\1 \\2'
{green}__ 45fc 5dc3 5548 89e5 897d fc{no_color}

$ {yellow}echo -en '__:45:fc:5d:c3:55:48:89:e5:89:7d:fc\\n__:45:fc:5d'  | regex-sub '([0-9a-f_]{{2}}):([0-9a-f_]{{2}}):?' '\\1 \\2'{no_color}
original='__:45:fc:5d:c3:55:48:89:e5:89:7d:fc\\n__:45:fc:5d'
pattern='([0-9a-f_]{{2}}):([0-9a-f_]{{2}}):?'
replacement='\\1 \\2'
{green}__ 45fc 5dc3 5548 89e5 897d fc
__ 45fc 5d{no_color}'''

    print(usage_info, file=sys.stderr)


num_args = len(sys.argv)
required_num_args = 3

if num_args < required_num_args:
    _help()
    exit(1)
first_arg = sys.argv[1]
if first_arg == '-h' or first_arg == '--help':
    _help()
    exit(0)

if num_args > required_num_args:
    original = first_arg
    pattern = sys.argv[2]
    replacement = sys.argv[3]
else:
    pattern = first_arg
    replacement = sys.argv[2]
    original = sys.stdin.read()

print(f'{original=}', file=sys.stderr)
print(f'{pattern=}', file=sys.stderr)
print(f'{replacement=}', file=sys.stderr)

print(re.sub(pattern, replacement, original))
