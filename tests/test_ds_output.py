# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 09:30:26 2021

@author: Daniel
"""

import hydrogeosines as hgs
import numpy as np
import pandas as pd

#%%  Testing MVC principal
death_valley = hgs.Site('death valley', geoloc=[-116.471360, 36.408130, 688])
death_valley.import_csv('tests/data/death_valley/Rau_et_al_2021.csv',
                        input_category=["GW","BP","ET"], utc_offset=0, unit=["m","m","nstr"],
                        how="add", check_duplicates=True)

#%%
# tmp = death_valley.data.hgs.get_loc_unit('ET')

#%% Processing
# create Instance of Processing with csiro_site
process = hgs.Processing(death_valley)

# test hals method
hals_results  = process.hals()

# test hals method
fft_results  = process.fft(update=True)

#%%
# test gw_correct
gw_correct_results  = process.GW_correct(lag_h=24, et_method = None, fqs=None)

#%%
# test be method
be_time_results  = process.BE_time(method="all", update=True)
#print(be_time)

#%% frequency domain stuff ...

be_freq_results  = process.BE_freq(method="rau", freq_method='hals', update=True)
#print(be_freq)

#%% Output
csiro_output  = hgs.Output(hals_results) # process.results container or results

# for visualization
csiro_output.plot() # possible different plotting style methods, e.g. simple, report, etc
#csiro_output.plot(method="all",style="simple",loc="all") # possible different plotting style methods, e.g. simple, report, etc

# for export of data into file
#csiro_output.export(exp_format="csv") # different export formats

# for returning a formated table of the results
#csiro_output.table()

#%%
csiro_output2 = hgs.Output(process)
csiro_output2.plot()

