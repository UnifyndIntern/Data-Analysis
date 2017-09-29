#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 17:03:12 2017

@author: dhaval
"""

# Importing Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot(x,y,hue):
    x = str(x)
    y = str(y)
    hue = str(hue)
    sns.barplot(x = df[x], y = df[y], hue = df[hue])

# Importing data
df = pd.read_excel('TD.xlsx')

plot('Format','Nov 2016 \nTD','Floor')