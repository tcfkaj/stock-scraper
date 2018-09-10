from grabber import *

# Location - path to store data
location = 'data/top238_in_top20_industries.h5'

# Start and end of time period in 'YYYY-MM-DD' format
Start = '2016-01-01'
End = '2018-08-31'

# Stock ticker list must be saved as a single column text file in pwd named 'tikz.csv'
# The following block converts this file to a list of strings
with open('tikz.csv') as f:
    reader = csv.reader(f)
    tikz = [r[0] for r in reader]

# Executes function from 'grabber.py' to do the deed
gen_all(tikz, Start, End, location)

