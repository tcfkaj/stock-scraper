# This script will convert each dataset within an HDF5 file into seperate
# csv files

import pandas as pd
import tables
import h5py as h
import csv as csv

# Must be path to .h5 file
path_to_h5 = "data/top238_by_industries/top238_in_top20_industries.h5"

# Path to folder where you want all generated csv files
# to end up
csv_folder = "data/top238_by_industries/csv/"

with h.File(path_to_h5, 'r') as hdf:
    ls = list(hdf.keys())

store = pd.HDFStore(path_to_h5)

for tik in ls:
    data = store[tik]
    csv_location = csv_folder + tik + '.csv'
    data.to_csv(csv_location, sep='\t')
