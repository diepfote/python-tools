from ics import Calendar, Event
import pandas as pd
import sys

df = pd.read_excel(sys.argv[1])
person_to_filter_for = sys.argv[2]
# breakpoint()

less_data = df.loc[:, ['Bereitschaft', 'Column1', 'Column12']]

calendar= Calendar()

for _, row in less_data.iterrows():
    name = row[0]
    start = row[1]
    end = row[2]
    # add a day since otherwise we do not account for the entirety of the last day
    end += pd.DateOffset(1)
    if name != person_to_filter_for:
        continue

    print(f'{name}\t\t{start}\t{end}')
    event = Event()
    event.name = 'Bereitschaft'
    event.begin = start
    event.end = end
    calendar.events.add(event)

with open('/tmp/bereitschaft.ics', 'w') as f:
    f.write(str(calendar))

