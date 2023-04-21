#!/usr/bin/env python3

# Usage:
# $ urldecode 'asdf%20' | hexdump -C
# 00000000  61 73 64 66 20                                    |asdf |
# 00000005
# $ urlencode 'asdf ' | hexdump -C
# 00000000  61 73 64 66 25 32 30                              |asdf%20|
# 00000007

import os
import re
import sys

from urllib.parse import unquote, quote

operations = {'urldecode': unquote, 'urlencode': quote}
op = operations[os.path.basename(sys.argv[0])]

if len(sys.argv) > 2 and sys.argv[1] == '--oauth2':
    url = sys.argv[2]
    # TODO refactor these procedures require unquote
    url = unquote(url)
    url = url.split('&g0.tab=1')[0]
    url = re.sub('/oauth2/[^/]+/', '/', url)
else:
    url = sys.argv[1]
    url = op(url)

print(url, end='')
