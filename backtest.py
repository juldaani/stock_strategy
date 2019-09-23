#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 22:38:00 2019

@author: juho
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



PATH_DATAFRAME = 'datas/merged'

NUM_BEST, NUM_WORST = 5, 5


df = pd.read_pickle(PATH_DATAFRAME)

shifted = np.full(df.values.shape, np.NaN)
shifted[1:] = df.values[:-1]

monthlyReturns = (df - df.shift(periods=1)) / df.shift(periods=1)

groupedByMonth = [monthlyReturns[monthlyReturns.index.month == i] for i in range(1,13)]
rollingMeans = [groupedByMonth[i].rolling(10).mean().shift(periods=1) for i in range(len(groupedByMonth))]
rollingMeans = [data[~np.all(np.isnan(data),1)] for data in rollingMeans]   # Remove all nan rows



returns = []

#i = 0
#curMeansForMonth = rollingMeans[i]

for curMeansForMonth in rollingMeans:
    
    
    # Get monthly returns for current months
    trueMonthlyReturns = monthlyReturns.loc[curMeansForMonth.index]
    trueMonthlyReturns[np.isnan(curMeansForMonth)] = np.NaN
    
    for curMeans, curTrueReturns in zip(curMeansForMonth.values, trueMonthlyReturns.values):
        sorter = np.argsort(curMeans)
        sortedTrueReturns = curTrueReturns[sorter]
        sortedTrueReturns = sortedTrueReturns[~np.isnan(sortedTrueReturns)]
        
        if(len(sortedTrueReturns) < 5):
            continue
        
        returns.append(sortedTrueReturns[-NUM_BEST:])
#        returns.append(sortedTrueReturns[:NUM_WORST])

#returns = np.array(returns) + 1
returns = np.row_stack(returns) + 1

np.prod(returns,0)

# %%

a = np.argsort(rollingMeans[10].values,1)





# %%