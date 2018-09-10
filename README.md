This repository serves two purposes:

* **Stock Scraper**

	1. Once you have a list of tickers you are interested in, in a text file line by line, save them in main directory as 'tikz.csv'.

	2. Open run.py

	3. Adjust the timeframe to desired length. *All stocks on list must be active during this timeframe or an error will result.*

	4. Set location variable, location='some_descriptive_name.h5'. *This must be a .h5 file.*

	5. Save in-file changes and compile and a single HDF5 file will be
	   generated with a dataset for each ticker containing daily Open,
Close, High, Volume data for each date within the specified timeframe. The
datasets within the file generated is extractable as a Pandas dataframe.

	6. The .h5 files in /data folder can be briefly inspected with inspecth5.py (*filename must be specified in the file*) and compiling will yield a simple UI. Although you will be able to explore better with an HDF5 viewer.

* **Data Respository**

This is part of a class project for a Machine Learning course and all generated
data will be kept in data/ subfolder.

I will try to be as desriptive as possible in naming the datasets and
eventually, it is my intention, for it to hold some pretty complete HDF5 files
with Groups, Subgroups and Metadata.
