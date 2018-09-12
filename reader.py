# import modules
import numpy as np
import pandas as pd
import glob
import matplotlib.pyplot as plt

# set some global variables and lists etc.
temp = []
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
# substract baseline using polynomial fit
# ...
# calculate velocity of source (but this is WRONG right now!)
    temp['velocity'] = 299792458*((temp['frequency power [Hz]'] - 1420.45)/1420.45)
# write-out spectrum in png format, disabled by default
#    temp.plot(x='frequency power [Hz]', y='spectral density [dB/Hz]', kind='scatter', s=2)
#    plt.savefig('..//21cm//output//' + lon + '.png')
#    plt.close()
#append df temp to totals df target
    target = target.append(temp)
# sorting the totals dataframe on index (but do I need to, really?)
target = target.set_index(['longitude'])
# set MultiIndex on longitude and frequency columns
#target = target.sort_index()
# write-out totals dataframe to tab-delimited csv
#target.to_csv('..//21cm//output//21cmout.csv', sep='\t')


# -------DEV STUFF-------
print(target.shape)
#print(target)
#print(target.info)
#print(target.columns)
#print(target.head())
#print(target.tail())
#df.loc[row_indexer,column_indexer]
#print(target.iloc[0:10, :])
print(target.loc['016'])
target.loc['016'].plot(x='frequency power [Hz]', y='spectral density [dB/Hz]', kind='scatter', s=2)
target.loc['016'].plot(x='frequency power [Hz]', y='velocity', kind='scatter', s=2)
plt.show()

