# This script will convert each dataset within an HDF5 file into seperate
# csv files

import pandas as pd
import tables
import h5py as h

# Must be path to .h5 file
path_to_h5 = "data/sp500/SP500-2011.h5"

# Path to folder where you want all generated csv files
# to end up - must exist
csv_folder = "data/sp500/csv-2011/"

with h.File(path_to_h5, 'r') as hdf:
    ls = list(hdf.keys())

store = pd.HDFStore(path_to_h5)

for tik in ls:
    data = store[tik]
    csv_location = csv_folder + tik + '.csv'
    data.to_csv(csv_location, sep='\t')
