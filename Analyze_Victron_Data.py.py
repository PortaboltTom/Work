import json
import numpy as np 
import os
import pandas as pd
import matplotlib.pyplot as plt
import csv
import os.path
from os import path
from shutil import copyfile
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates

#import data and make simple plot
file_path = 'C:\\Users\\User\\Google Drive\\Circular Energy Solutions\\Victron Data\\Code'
os.chdir(file_path)

data_path = 'C:\\Users\\User\\Google Drive\\Circular Energy Solutions\\Victron Data/Code\\Data_Export\\CircularEnergyrentals01_log_20210220-0000_to_20210227-1008.csv'
data_path2 = 'C:\\Users\\User\\Downloads\\CircularEnergyrentals01_20210305-0000_to_20210305-2300.csv'
data_path3 = 'C:\\Users\\User\\Google Drive\\Circular Energy Solutions\\Klanten\Defensie\\CircularEnergyrentals01_log_20210414-0900_to_20210423-1100.csv' 


all_data = pd.read_csv(data_path3, header=1)
all_data = all_data.rename(columns={'Europe/Berlin (+02:00)': 'Time'})      
ac_out = all_data[['Time','Output power 1', 'Output power 2', 'Output power 3','Input power 1', 'Input power 2', 'Input power 3']]
ac_out = ac_out.dropna()
ac_out = ac_out.apply(pd.to_numeric, errors = 'ignore')
ac_out['Total output power'] =  ac_out['Output power 1'] + ac_out['Output power 2'] + ac_out['Output power 3']
ac_out['Total input power'] = ac_out['Input power 1'] + ac_out['Input power 2'] + ac_out['Input power 3']  
ac_out['Time'] = pd.to_datetime(ac_out['Time'])

fig, ax = plt.subplots(1)
fig.autofmt_xdate()

plt.plot(ac_out['Time'], ac_out['Output power 1'], linewidth=0.2, label='Phase 1') 
plt.plot(ac_out['Time'], ac_out['Output power 2'], linewidth=0.2, label='Phase 2') 
plt.plot(ac_out['Time'], ac_out['Output power 3'], linewidth=0.2, label='Phase 3') 
#plt.plot(ac_out['Time'], ac_out['Total output power'], linewidth=0.2, label='Total output power') 
#plt.plot(ac_out['Time'], ac_out['Total input power'], linewidth=0.2, label='Input power')
''' 
    ac_out['Time'], ac_out['Output power 2'],
    ac_out['Time'], ac_out['Output power 3'], 
    ac_out['Time'], ac_out['Total output power'])
'''
xfmt = mdates.DateFormatter('%d-%m-%y %H:%M')
ax.xaxis.set_major_formatter(xfmt)
plt.xlabel("Date")
plt.ylabel("Output power(Watt)")
#plt.legend(['Phase1', 'Phase2', 'Phase3', 'Total'] )
plt.legend()
plt.title('Power Output')
plt.show()

'add extra text to test github'