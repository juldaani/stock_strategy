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

NUM_STOCKS = 3
WIN_LEN = 10


df = pd.read_pickle(PATH_DATAFRAME)
df = df[:'2019-8']      # Hack to remove shit from the end of the dataframe

monthlyReturns = df.pct_change(1)
monthlyReturns[np.isnan(df)] = np.NaN
monthlyReturns = monthlyReturns[~np.all(np.isnan(monthlyReturns),1)]

returns = pd.DataFrame(columns = [1]*NUM_STOCKS)
for date in monthlyReturns.index:
#    print(date)
    
    stDate = str(date.year-WIN_LEN) + '-' + str(date.month)
    endDate = str(date.year-1) + '-' + str(date.month)
    win = monthlyReturns[stDate:endDate]
    win = win[win.index.month == date.month]
    
    if(len(win) < WIN_LEN):
        continue
    
    winMean = np.mean(win.values, 0)
    
    sorter = np.argsort(winMean)
    sortedReturns = monthlyReturns.loc[date].values[sorter]
    sortedReturns = sortedReturns[~np.isnan(winMean[sorter])]   # remove nan
    
    returns.loc[date] = sortedReturns[-NUM_STOCKS:]
#    returns.loc[date] = sortedReturns[:NUM_STOCKS]
    
    
returns = returns + 1

a = np.prod(returns['2019'])
#a = np.prod(returns)
print(a)
np.sum(a/len(a))


# %%


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