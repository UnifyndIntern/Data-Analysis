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
    
    plt.figure(figsize=(26,14))
    plt.title(""+x+" analysis for "+y[0:9])
    plt.ioff()
    sns.barplot(x = df_td[x], y = df_td[y], hue = df_td[hue],ci = None)
    plt.savefig(""+x+"/"+x+"wise wrt "+hue+" "+y+".png")
    plt.close()
plot('Floor','Sep 2016 \nTD','Format')

# Importing data
df = pd.read_excel('TD.xlsx')

plot('Floor','Sep 2016 \nTD','Format')