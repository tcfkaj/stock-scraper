import pandas as pd
import tables
import h5py as h

# Location of h5 file to inspect, must be changed in file
location = 'data/top238_in_top20_industries_R-friendly.h5'

# Provides a simple UI to see the head() of desired datasets in h5 file
with h.File(location, 'r') as hdf:
    ls = list(hdf.keys())

store = pd.HDFStore(location)

b = True

while b == True:

    print('List of datasets in the file ',location,':\n', ls)
    print('Number of datasets in this file \n', len(ls))

    ds = input('Pick a dataset to see (q to quit): ')

    if ds == 'q':
        b = False;

    elif ds not in ls:
        print("Sorry try again.");

    else:
        n = int(input("How many rows would you like to see? "))
        stock = store[ds]
        print(stock.head(n))
        stop = input("Would you like to see another (y/n)? ")
        if stop != 'y':
            b = False
