#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 22:38:00 2019

@author: juho
"""

import numpy as np
import pandas as pd




PATH_DATAFRAME = 'datas/merged'

df = pd.read_pickle(PATH_DATAFRAME)



a = df.loc[str(1800):str(2003)]

stDate = pd.to_datetime(df.first_valid_index())

 + pd.Timedelta(days=365)

a = pd.to_datetime(df.first_valid_index())

df['date'].dt.month==12

df.last_valid_index()


# %%