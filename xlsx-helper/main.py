import sys
import pandas as pd

df = pd.read_excel(sys.argv[1])
person_to_filter_for = sys.argv[2]
# breakpoint()

less_data = df.loc[:, ['Bereitschaft', 'Column1', 'Column12']]

for _, row in less_data.iterrows():
    name = row[0]
    start = row[1]
    end = row[2]
    if name != person_to_filter_for:
        continue

    print(f'{name}\t\t{start}\t{end}')


