import sys

from ics import Calendar, Event
import pandas as pd

df = pd.read_excel(sys.argv[1])

if len(sys.argv) > 2:
    person_to_filter_for = sys.argv[2]
else:
    person_to_filter_for = None
# breakpoint()

less_data = df.loc[:, ['On-Call Duty', 'From-Date', 'To-Date']]

calendar = Calendar()

for _, row in less_data.iterrows():
    name, start, end = row.to_list()
    start = str(start)
    end = str(end)


    event = Event()

    if not person_to_filter_for:
        event.name = name
    elif name != person_to_filter_for:
        continue
    elif name == person_to_filter_for:
        event.name = 'Bereitschaft'
    else:
        raise Exception('Unexpected case')

    print(f'{name}\t\t{start}\t{end}')

    event.begin = start
    event.end = end
    calendar.events.add(event)

ics_name = '/tmp/bereitschaft.ics'
with open(ics_name, 'w') as f:
    f.write(calendar.serialize())
    print(f'Wrote file to `{ics_name}`.', file=sys.stderr)

