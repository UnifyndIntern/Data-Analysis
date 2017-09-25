#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 16:31:39 2017

@author: dhaval
"""    
# Importing Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Importing data
df = pd.read_excel('Master Sales Data July 2017.xlsx')

# Delete Unnecessary Columns in Data
cleaned_data = df.drop(['Sr. No.'], axis = 1)
cleaned_data.drop(['Yardi - Lease Details'], axis = 1, inplace = True)
cleaned_data.drop(['Lease Code'], axis = 1, inplace = True)

# List of columns of Old TD and rent
cleaned_data_columns = list(cleaned_data.columns)
s_columns = cleaned_data_columns[12:64]
r_columns = cleaned_data_columns[276:328]
td_columns = cleaned_data_columns[65:117]

# Replacing 0 With NaN to avoid 'Divide By Zero Error'    
cleaned_data[s_columns[:]] = cleaned_data[s_columns[:]].replace({0:np.nan})
cleaned_data[r_columns[:]] = cleaned_data[r_columns[:]].replace({0:np.nan})
cleaned_data[td_columns[:]] = cleaned_data[td_columns[:]].replace({0:np.nan})

# TD Calculation
for x in range(0,52):
    cleaned_data[td_columns[x]] = cleaned_data[td_columns[x]] / cleaned_data[r_columns[x]]

# New Data Frame for TD analysis
columns = list(cleaned_data.columns)
column_td = ['Brand Name', 'Floor', 'Format', 'Category - New format', 'Carpet Area']

# Added all columns of Sales to column list
for x in range(0,52):
    column_td.append(s_columns[x])
# Added all columns of Rent to column list
for x in range(0,52):
    column_td.append(r_columns[x])
# Added all columns of TD to column list
for x in range(0,52):
    column_td.append(td_columns[x])

df_td = pd.DataFrame(data = cleaned_data, columns = column_td)
df_td = df_td.iloc[0:327,:] # Selected 327 rows as the remaining were blank