import csv

# Compares two single-column CSV files

with open('tikz.csv') as f:
    reader = csv.reader(f)
    tikz = [r[0] for r in reader]

with open('tik240.csv') as f:
    reader = csv.reader(f)
    tik240 = [r[0] for r in reader]

for i in range(len(tik240)):
    if tik240[i] not in tikz:
        print(tik240[i])

