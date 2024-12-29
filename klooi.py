# import modules
import numpy as np
import pandas as pd
import glob
import matplotlib.pyplot as plt

# set some global variables and lists etc.
temp = []
mw = pd.DataFrame()
target = pd.DataFrame()
data_folder = '..//21cm//data//*'
# rip the galactic longitude from the 2nd line to use it later on
# maybe I'd better use a regex and rip digits after colon?
for data in glob.glob(data_folder):
    with open(data) as file:
        line = file.readlines()[1]
        lon = line[-4:-1]
#load all the data files in the list into temporary DataFrame
    temp = pd.read_csv(data, header=13, delim_whitespace=True)
# add the column names
    temp.columns=['frequency power [Hz]','spectral density [dB/Hz]']
# add the longitude column in a not-so-nice way
    temp['longitude'] = lon
# find the max point and grab the entire row and dump in new df
    mw = pd.DataFrame(temp.loc[temp['spectral density [dB/Hz]'].idxmax()])
    print(mw.head(1))
# calculate mean, std and amplitude
# .....
# fit gaussian using astropy modeling
# ...
# dump it in the mw df
# calculate doppler shift on that one row and add
#   mw['doppler'] = 299792458*((mw['peak'] - 1420.45)/1420.45)
# write-out spectrum in png format, disabled by default
#    plt.xlabel('Doppler shift [??]')
#    plt.ylabel('spectral density [dB/Hz]')
#    temp.plot(x='doppler', y='spectral density [dB/Hz]', kind='scatter', s=2)
#    plt.savefig('..//21cm//output//' + lon + '.png')
#    plt.close()
#append df temp to totals df target
#    target = target.append(temp)
# sorting the totals dataframe on index (but do I need to, really?)
#mw = mw.set_index(['longitude'])
# set MultiIndex on longitude and frequency columns
#target = target.sort_index()
# write-out totals dataframe to tab-delimited csv
#target.to_csv('..//21cm//output//21cmout.csv', sep='\t')


# -------DEV STUFF-------
print(mw.shape)
#print(target)
#print(target.info)
#print(target.columns)
print(target.head())
print(target.tail())
#df.loc[row_indexer,column_indexer]
#print(target.iloc[0:10, :])
#print(target.loc['016'])
#target.loc['016'].plot(x='frequency power [Hz]', y='spectral density [dB/Hz]', kind='scatter', s=2)
#plt.show()

