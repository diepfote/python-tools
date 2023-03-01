#!/usr/bin/env python3

import sys
import re
from urllib.parse import unquote

if len(sys.argv) > 2 and sys.argv[1] == '--oauth2':
    url = sys.argv[2]
    url = unquote(url)
    url = url.split('&g0.tab=1')[0]
    url = re.sub('/oauth2/[^/]+/', '/', url)
else:
    url = sys.argv[1]
    url = unquote(url)

print(url)
