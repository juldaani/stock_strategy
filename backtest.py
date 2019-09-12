#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 18:31:30 2019

@author: juho
"""

import numpy as np
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time

from params import API_KEY



# %%

allSymbols = np.genfromtxt('symbols.csv', dtype='str')
ts = TimeSeries(key=API_KEY)

# Pick random subset
symbols = allSymbols[np.random.choice(len(allSymbols), size=100, replace=False)]

datas, metaDatas = [], []
for sym in symbols:
    data, metaData = ts.get_monthly_adjusted(symbols[56])
    datas.append(data)
    metaDatas.append(metaData)
    
    time.sleep(60/5)
    print(sym)
    
np.save('datas', datas)
np.save('meta_datas', metaDatas)



# %%

a = np.load('datas.npy')














