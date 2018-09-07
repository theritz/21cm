# import modules
import numpy as pd
import pandas as pd
import glob
import matplotlib.pyplot as plt

# set some global variables and lists etc.
temp = []
target = pd.DataFrame()
data_folder = '..//21cm//data//*'
# rip the galactic longitude from the 2nd line to use it later on
# to improve I should really use a regex and rip digits after colon...
for f in glob.glob(data_folder):
    with open(f) as file:
        line = file.readlines()[1]
        lon = line[-4:-1]
        check = f + lon
# load all the data files in the list into DataFrame
for data in glob.glob(data_folder):
    with open(data) as file:
        line = file.readlines()[1]
        lon = line[-5:-1]
    temp = pd.read_csv(data, header=13, delim_whitespace=True)
# add the column names
    temp.columns=['frequency power [Hz]','spectral density [dB/Hz]']
# add the longitude column in a not-so-nice way
    temp['longitude'] = lon
# set MultiIndex on longitude and frequency columns
    temp = temp.set_index(['longitude'])
# write-out every spectrum in png format
# still to add: substract baseline, gaussian fit
    temp.plot(x='frequency power [Hz]', y='spectral density [dB/Hz]', kind='scatter', s=2)
    plt.savefig('..//21cm//output//' + lon + '.png')
    plt.close()
#append df temp to df target
    target = target.append(temp)
# sorting on entire index, not sure what this does for frequency so check
    target = target.sort_index()

# calculate the doppler shift, don't know how yet exactly
#target['doppler'] = (target['frequency power [Hz]'] - 1.421402)/1.421402

# write-out to tab-delimited csv
target.to_csv('..//21cm//output//21cmout.csv', sep='\t')

# -------DEV STUFF-------
#print some stats during dev
#print(target.shape)
#print(target.info)
#print(target.columns)
print(target.head())
print(target.tail())
#df.loc[row_indexer,column_indexer]
#print(target.iloc[0:10, :])
#print(target.loc[' 016'])

