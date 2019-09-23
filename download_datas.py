#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 18:31:30 2019

@author: juho
"""

import numpy as np
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time, os

from params import API_KEY




N_SYMBOLS_TO_GET = 600
SYMBOLS_PATH = 'symbols.csv'
OUT_FOLDER = 'datas'


np.random.seed(1)

if not os.path.exists(OUT_FOLDER):
    os.makedirs(OUT_FOLDER)

symbols = np.genfromtxt(SYMBOLS_PATH, dtype='str')
np.random.shuffle(symbols)

ts = TimeSeries(key=API_KEY, output_format='pandas', indexing_type='date')

c = 0
for i,sym in enumerate(symbols):
    try:
        data, metaData = ts.get_monthly_adjusted(sym)
        data.to_pickle(os.path.join(OUT_FOLDER, metaData['2. Symbol']))
        c += 1
    except:
        print('Error. Cannot fetch symbol: ' + sym)
    
    print(i,sym)

    if(c > N_SYMBOLS_TO_GET):
        break
    
    time.sleep(60/5)    # Because only 5 queries / min allowed    
    



# %%













