#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 16:31:39 2017

@author: dhaval
"""
def calculate_td(sales,carpet,rent):
    td = (sales/carpet)
    tdr = td/rent
    return tdr
    
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

# List of columns of sales and rent
sales = ['Apr 2013 Sales', 'May 2013 Sales', 'June 2013 Sales', 'July 2013 Sales', 'Aug 2013 Sales', 'Sep 2013 Sales', 'Oct 2013 Sales', 'Nov 2013 Sales', 'Dec 2013 Sales', 'Jan 2014 Sales', 'Feb 2014 Sales', 'Mar 2014 Sales', 'Apr 2014 Sales', 'May 2014 Sales', 'June 2014 Sales', 'July 2014 Sales', 'Aug 2014 Sales', 'Sep 2014 Sales', 'Oct 2014 Sales', 'Nov 2014 Sales', 'Dec 2014 Sales', 'Jan 2015 Sales', 'Feb 2015 Sales', 'Mar 2015 Sales', 'Apr 2015 Sales', 'May 2015 Sales', 'June 2015 Sales', 'July 2015 Sales', 'Aug 2015 Sales', 'Sep 2015 Sales', 'Oct 2015 Sales', 'Nov 2015 Sales', 'Dec 2015 Sales', 'Jan 2016 Sales', 'Feb 2016 Sales', 'Mar 2016 Sales', 'Apr 2016 Sales', 'May 2016 Sales', 'June 2016 Sales', 'July 2016 Sales', 'Aug 2016 Sales', 'Sep 2016 Sales', 'Oct 2016 Sales', 'Nov 2016 Sales', 'Dec 2016 Sales', 'Jan 2017 Sales', 'Feb 2017 Sales', 'Mar 2017 Sales', 'Apr 2017 Sales', 'May 2017 Sales', 'June 2017 Sales', 'July 2017 Sales']
rent = ['Apr 2013 Total (LF+RS)', 'May 2013 Total (LF+RS)', 'Jun 2013 Total (LF+RS)', 'Jul 2013 Total (LF+RS)', 'Aug 2013 Total (LF+RS)', 'Sep 2013 Total (LF+RS)', 'Oct 2013 Total (LF+RS)', 'Nov 2013 Total (LF+RS)', 'Dec 2013 Total (LF+RS)', 'Jan 2014 Total (LF+RS)', 'Feb 2014 Total (LF+RS)', 'Mar 2014 Total (LF+RS)', 'Apr 2014 Total (LF+RS)', 'May 2014 Total (LF+RS)', 'Jun 2014 Total (LF+RS)', 'Jul 2014 Total (LF+RS)' 'Aug 2014 Total (LF+RS)', 'Sep 2014 Total (LF+RS)', 'Oct 2014 Total (LF+RS)', 'Nov 2014 Total (LF+RS)', 'Dec 2014 Total (LF+RS)', 'Jan 2015 Total (LF+RS)', 'Feb 2015 Total (LF+RS)', 'Mar 2015 Total (LF+RS)', 'Apr 2015 Total (LF+RS)', 'May 2015 Total (LF+RS)', 'Jun 2015 Total (LF+RS)', 'Jul 2015 Total (LF+RS)', 'Aug 2015 Total (LF+RS)', 'Sep 2015 Total (LF+RS)', 'Oct 2015 Total (LF+RS)', 'Nov 2015 Total (LF+RS)', 'Dec 2015 Total (LF+RS)', 'Jan 2016 Total (LF+RS)', 'Feb 2016 Total (LF+RS)', 'Mar 2016 Total (LF+RS)', 'Apr 2016 Total (LF+RS)', 'May 2016 Total (LF+RS)', 'Jun 2016 Total (LF+RS)', 'Jul 2016 Total (LF+RS)', 'Aug 2016 Total (LF+RS)', 'Sep 2016 Total (LF+RS)', 'Oct 2016 Total (LF+RS)', 'Nov 2016 Total (LF+RS)', 'Dec 2016 Total (LF+RS)', 'Jan 2017 Total (LF+RS)', 'Feb 2017 Total (LF+RS)', 'Mar 2017 Total (LF+RS)', 'Apr 2017 Total (LF+RS)', 'May 2017 Total (LF+RS)', 'Jun 2017 Total (LF+RS)', 'Jul 2017 Total (LF+RS)']