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

# Encoding Categorical Variables