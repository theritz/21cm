# import modules
import numpy as np
import pandas as pd
import glob
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from scipy.stats import norm

# set some global variables and lists etc.
mw = []
temp = []
target = pd.DataFrame()
data_folder = '..//21cm//data//*'
# rip the galactic longitude from the 2nd line to use it later on
for data in glob.glob(data_folder):
    with open(data) as file:
        line = file.readlines()[1]
        lon = line[-4:-1]
#load all the data files in the list into temporary DataFrame per file
    temp = pd.read_csv(data, header=13, delim_whitespace=True)
# add the column names
    temp.columns=['frequency power [Hz]','spectral density [dB/Hz]']
# add the longitude column in a not-so-nice way
    temp['longitude'] = lon
# set spectral density to Mhz
    temp['frequency power [Mhz]'] = temp['frequency power [Hz]']/1000000
# fit the data using fit_peak()
#   ...
# print every available spectrum in png format
    plt.xlabel('frequency power [Mhz]')
    plt.ylabel('spectral density [dB/Hz]')
    temp.plot(x='frequency power [Mhz]', y='spectral density [dB/Hz]', kind='scatter', s=2)
    plt.savefig('..//21cm//output//' + lon + '.png')
    plt.close()
#append df temp to totals df target
    target = target.append(temp)
# sorting the totals dataframe on index (but do I need to, really?)
target = target.set_index(['longitude'])
# get max values per longitude from df target and put in df mw
mw = pd.DataFrame(target.max(level=0))
# calculate doppler shift from df mw
mw['doppler'] = ((mw['frequency power [Mhz]'] - 1420.41)/1420.41*299729.46)
# sort df mw for cosmetic purposes
mw = mw.sort_index()
# write-out totals dataframe to tab-delimited csv
mw.to_csv('..//21cm//output//21cmout.csv', sep='\t')

# -------DEV STUFF-------
#print(target.shape)
print(mw.shape)
print(mw.head())
#print(target.info)
#print(target.columns)
#print(target.head())
#print(target.tail())
#print(target.shape)
#df.loc[row_indexer,column_indexer]
#print(target.iloc[0:10, :])
#print(target.loc['244'].head())
#target.loc['016'].plot(x='frequency power [Hz]', y='spectral density [dB/Hz]', kind='scatter', s=2)
#plt.show()