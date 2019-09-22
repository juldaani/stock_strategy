#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 22:14:01 2019

@author: juho
"""

import numpy as np
import pandas as pd
import os


PATH_DATA = 'datas'


fnames = os.listdir(PATH_DATA)

mergedDf = pd.DataFrame()
for f in fnames:
    print(f)
    
    df = pd.read_pickle(os.path.join(PATH_DATA,f))
    df.rename({'5. adjusted close': f}, axis=1, inplace=True)
    mergedDf = pd.concat([mergedDf,df[f]], axis=1, sort=1)
    
mergedDf.to_pickle(os.path.join(PATH_DATA, 'merged'))

# %%