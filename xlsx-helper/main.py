from ics import Calendar, Event
import pandas as pd
import sys

df = pd.read_excel(sys.argv[1])

if len(sys.argv) > 2:
    person_to_filter_for = sys.argv[2]
else:
    person_to_filter_for = None
# breakpoint()

less_data = df.loc[:, ['Bereitschaft', 'Column1', 'Column12']]

calendar= Calendar()

for _, row in less_data.iterrows():
    name = row[0]
    start = row[1]
    end = row[2]
    # add a day since otherwise we do not account for the entirety of the last day
    end += pd.DateOffset(1)

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
    f.write(str(calendar))
    print(f'Wrote file to `{ics_name}`.', file=sys.stderr)

