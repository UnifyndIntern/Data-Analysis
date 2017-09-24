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
r_columns = ['Apr 2013 \nR + RS',
       'May 2013 \nR + RS', 'Jun 2013 \nR + RS', 'Jul 2013 \nR + RS',
       'Aug 2013 \nR + RS', 'Sep 2013 \nR + RS', 'Oct 2013 \nR + RS',
       'Nov 2013 \nR + RS', 'Dec 2013 \nR + RS', 'Jan 2014\n R + RS',
       'Feb 2014\n R + RS', 'Mar 2014\n R + RS', 'Apr 2014\n R + RS',
       'May 2014\n R + RS', 'Jun 2014\n R + RS', 'Jul 2014\n R + RS',
       'Aug 2014\n R + RS', 'Sep 2014\n R + RS', 'Oct 2014\n R + RS',
       'Nov 2014\n R + RS', 'Dec 2014\n R + RS', 'Jan 2015\n R + RS',
       'Feb 2015\n R + RS', 'Mar 2015\n R + RS', 'Apr 2015\n R + RS',
       'May 2015\n R + RS', 'June 2015\n R + RS', 'July 2015\n R + RS',
       'Aug 2015\n R + RS', 'Sep 2015\n R + RS', 'Oct 2015\n R + RS',
       'Nov 2015\n R + RS', 'Dec 2015\n R + RS', 'Jan 2016\n R + RS',
       'Feb 2016\n R + RS', 'Mar 2016\n R + RS', 'Apr 2016\n R + RS',
       'May 2016\n R + RS', 'Jun 2016\n R + RS', 'Jul 2016\n R + RS',
       'Aug 2016\n R + RS', 'Sep 2016\n R + RS', 'Oct 2016\n R + RS',
       'Nov 2016\n R + RS', 'Dec 2016\n R + RS', 'Jan 2017\n R + RS',
       'Feb 2017\n R + RS', 'Mar 2017\n R + RS', 'Apr 2017\n R + RS',
       'May 2017\n R + RS', 'Jun 2017\n R + RS', 'Jul 2017\n R + RS']
old_columns = ['Apr 2013 \nTD', 'May  2013 \nTD', 'Jun  2013 \nTD',
       'Jul  2013 \nTD','Aug 2013 \nTD', 'Sep 2013 \nTD', 'Oct 2013 \nTD',
       'Nov 2013 \nTD', 'Dec 2013 \nTD', 'Jan 2014 \nTD', 'Feb 2014 \nTD',
       'Mar 2014 \nTD', 'Apr 2014 \nTD', 'May 2014 \nTD', 'Jun 2014 \nTD',
       'Jul 2014 \nTD', 'Aug 2014 \nTD', 'Sep 2014 \nTD', 'Oct 2014 \nTD',
       'Nov 2014 \nTD', 'Dec 2014 \nTD', 'Jan 2015 \nTD', 'Feb 2015 \nTD',
       'Mar 2015 \nTD', 'Apr 2015 \nTD', 'May 2015 \nTD', 'June 2015 \nTD',
       'July 2015 \nTD', 'Aug 2015 \nTD', 'Sep 2015 \nTD', 'Oct 2015 \nTD',
       'Nov 2015 \nTD', 'Dec 2015 \nTD', 'Jan 2016 \nTD', 'Feb 2016 \nTD',
       'Mar 2016 \nTD', 'Apr 2016 \nTD', 'May 2016 \nTD', 'Jun 2016 \nTD',
       'Jul 2016 \nTD', 'Aug 2016 \nTD', 'Sep 2016 \nTD', 'Oct 2016 \nTD',
       'Nov 2016 \nTD', 'Dec 2016 \nTD', 'Jan 2017 \nTD', 'Feb 2017 \nTD',
       'Mar 2017 \nTD', 'Apr 2017 \nTD', 'May 2017 \nTD', 'Jun 2017 \nTD',
       'Jul 2017 \nTD']

# Replacing 0 With NaN to avoid 'Divide By Zero Error'    
cleaned_data[old_columns[:]] = cleaned_data[old_columns[:]].replace({0:np.nan})
cleaned_data[r_columns[:]] = cleaned_data[r_columns[:]].replace({0:np.nan})

# TD Calculation
for x in range(0,52):
    cleaned_data[old_columns[x]] = cleaned_data[old_columns[x]] / cleaned_data[r_columns[x]]
