#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 19:05:19 2017

@author: dhaval
"""
# For all
def Rent_TD(years):
    # Create a figure instance, and the two subplots
    fig = plt.figure(figsize=(100,20))

    ax1 = fig.add_subplot(211)
    ax1.set_title("Rent for Different Months")
    ax1.set_xlabel("Months")
    ax1.set_ylabel("Rent")
    
    ax2 = fig.add_subplot(212)
    ax2.set_title("Trading Density for Different Months")
    ax2.set_xlabel("Months")
    ax2.set_ylabel("Trading Density")
    
    sns.pointplot(x = r_years[years], y = df_td.iloc[1, years[:]], ax= ax1)
    sns.pointplot(x = td_years[years], y = df_td.iloc[1, years[:]], ax = ax2)
    
def sales_TD(years):
    # Create a figure instance, and the two subplots
    fig = plt.figure(figsize=(100,20))

    ax1 = fig.add_subplot(211)
    ax1.set_title("Sales for Different Months")
    ax1.set_xlabel("Months")
    ax1.set_ylabel("Sales")

    ax2 = fig.add_subplot(212)
    ax2.set_title("Trading Density for Different Months")
    ax2.set_xlabel("Months")
    ax2.set_ylabel("Trading Density")
    
    sns.pointplot(x = s_years[years], y = df_td.iloc[1, years[:]], ax= ax1)
    sns.pointplot(x = td_years[years], y = df_td.iloc[1, years[:]], ax = ax2)
    
# For One 
def Rent_TD():
    # Create a figure instance, and the two subplots
    fig = plt.figure(figsize=(100,20))

    ax1 = fig.add_subplot(211)
    ax1.set_title("Rent for Different Months")
    ax1.set_xlabel("Months")
    ax1.set_ylabel("Rent")
    
    ax2 = fig.add_subplot(212)
    ax2.set_title("Trading Density for Different Months")
    ax2.set_xlabel("Months")
    ax2.set_ylabel("Trading Density")
    
    sns.pointplot(x = r_columns, y = df_td.iloc[1, 57:109], ax= ax1)
    sns.pointplot(x = td_columns, y = df_td.iloc[1, 109:161], ax = ax2)
    
def Sales_TD():
    # Create a figure instance, and the two subplots
    fig = plt.figure(figsize=(100,20))

    ax1 = fig.add_subplot(211)
    ax1.set_title("Sales for Different Months")
    ax1.set_xlabel("Months")
    ax1.set_ylabel("Sales")

    ax2 = fig.add_subplot(212)
    ax2.set_title("Trading Density for Different Months")
    ax2.set_xlabel("Months")
    ax2.set_ylabel("Trading Density")
    
    sns.pointplot(x = s_columns, y = df_td.iloc[1, 5:57], ax= ax1)
    sns.pointplot(x = td_columns, y = df_td.iloc[1, 109:161], ax = ax2)

# Sales Per Year
s_2013 = s_columns[0:9]
s_2014 = s_columns[9:21]
s_2015 = s_columns[21:33]
s_2016 = s_columns[33:45]
s_2017 = s_columns[45:57]
s_years = [s_2013, s_2014, s_2015, s_2016, s_2017]

# Rent Per Year
r_2013 = r_columns[0:9]
r_2014 = r_columns[9:21]
r_2015 = r_columns[21:33]
r_2016 = r_columns[33:45]
r_2017 = r_columns[45:57]
r_years = [r_2013, r_2014, r_2015, r_2016, r_2017]

# Rent Per Year
td_2013 = td_columns[0:9]
td_2014 = td_columns[9:21]
td_2015 = td_columns[21:33]
td_2016 = td_columns[33:45]
td_2017 = td_columns[45:57]
td_years = [td_2013, td_2014, td_2015, td_2016, td_2017]