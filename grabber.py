import pandas as pd
import pandas_datareader.data as pdr
import tables
import fix_yahoo_finance as yf
import csv as csv

# Pulls data on a single stock from Yahoo API (with fix)
def get_data(tik_, Start_, End_):

    yf.pdr_override()

    df = pdr.get_data_yahoo(tik_, start=Start_, end=End_, as_panel = False)

    return(df)

# Loops through a list of tickers to generate datasets inside location file
def gen_all(tikz_, start_, end_, location_):

    store = pd.HDFStore(location_, 'w', complib=str('zlib'), complevel=5)

    for i in range(len(tikz_)):
        tik = tikz_[i]
        print(tik)
        data = get_data(tik, start_, end_)
        store.put(tik, data, data_columns=data.columns)

    store.close()
