#!/usr/bin/env python3

# snatched from https://stackoverflow.com/a/6470135
#
# I use this to view ics files in neomutt

import sys
import vobject


data = open(sys.argv[1]).read()

# parse the top-level event with vobject
cal = vobject.readOne(data)

print('Summary: ', cal.vevent.summary.valueRepr())
print('')

print('Start:   ', cal.vevent.dtstart.value)
print('End:     ', cal.vevent.dtend.value)
try:
    print('Repeats: ', cal.vevent.rrule)
except:
    pass
print('')
print('Description: ', cal.vevent.description.valueRepr())

