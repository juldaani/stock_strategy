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


#a = df.values
#m = np.all(np.isnan(df.values),1)
#np.sum(m)


monthlyReturns = df.pct_change(1)
monthlyReturns[np.isnan(df)] = np.NaN
monthlyReturns = monthlyReturns[~np.all(np.isnan(monthlyReturns),1)]

predictions, targets = [], []

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
    
    targets.append(monthlyReturns.loc[date].values[sorter])
    predictions.append(winMean[sorter])
    
    if(len(sortedReturns) < 10):
        continue
    
    returns.loc[date] = sortedReturns[-NUM_STOCKS:]
#    returns.loc[date] = sortedReturns[:NUM_STOCKS]

targets, predictions = np.row_stack(targets), np.row_stack(predictions)

    
returns = returns + 1
returnsNp = returns['2019'].values
#returnsNp = returns['2009':].values

ret = 1
for i in range(len(returnsNp)):
    ret = np.sum(returnsNp[i] * (ret/NUM_STOCKS))

print(ret)


# %%

m = ~np.all(np.isnan(predictions),0)
pred, targ = predictions[:,m], targets[:,m]

ii = 3

plt.scatter(targ[:,-ii:].flatten(), pred[:,-ii:].flatten(), alpha=0.9)
s = 0.4
plt.plot(np.arange(-s,s+.001,s), np.arange(-s,s+.001,s))


targ[:,-ii:].flatten()
pred[:,-ii:].flatten()











