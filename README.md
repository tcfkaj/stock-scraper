This repository serves two purposes:

* **Stock Scraper**

Once you have a list of tickers you are interested in, in a txt file line by
line, save them in main
directory as 'tikz.csv'.

Open run.py and adjust the timeframe to desired length. (All stocks on list
must be active during this timeframe or an error will result).

You must also specify a location file to save, eg location =
'data/some_descriptive_name.h5'

This must be an .h5 file.

Once parameters are set, compile and a single HDF5 file will be generated with
a dataset for each ticker containing daily Open, Close, High, Volume data for
each date within the specified timeframe.

The .h5 files in /data folder can be briefly inspected with inspecth5.py
(*filename must be specified in the file*) and compiling will yield a simple
UI.

* **Data Respository**

This is part of a class project for a Machine Learning course and all generated
data will be kept in data/ subfolder.

I will try to be as desriptive as possible in naming the datasets and
eventually, it is my intention, for it to hold some pretty complete HDF5 files
with Groups, Subgroups and Metadata.
