#!/usr/bin/env python3

# snatched from https://stackoverflow.com/a/6470135
# and kudos to a LLM
#
# I use this to view ics files in neomutt

import sys
import vobject

with open(sys.argv[1], encoding='utf-8') as f:
    data = f.read()

for cal in vobject.readComponents(data):
    for ev in getattr(cal, 'vevent_list', []):
        print('Summary: ', ev.summary.value if hasattr(ev, 'summary') else '')
        print('Start:   ', ev.dtstart.value)

        if hasattr(ev, 'dtend'):
            print('End:     ', ev.dtend.value)
        elif hasattr(ev, 'duration'):
            print('Duration:', ev.duration.value)

        if hasattr(ev, 'rrule'):
            print('Repeats: ', ev.rrule.value)

        if hasattr(ev, 'description'):
            print('Description:', ev.description.value)
        print()
