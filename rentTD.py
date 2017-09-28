def r_TD2013(loc):
	# Year 2013(Sales and TD)
	fig = plt.figure(figsize=(25,15))
	plt.ioff()
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)
    
	a1 = sns.pointplot(x = r_2013, y = df_td.iloc[loc, 57:66], ax= ax1)
	a1.set(ylabel = 'Rent', title = 'Rent for Different Months')
	a2 = sns.pointplot(x = td_2013, y = df_td.iloc[loc, 109:118], ax = ax2)
	a2.set(xticklabels = [], ylabel = 'Trading Density', title = 'Trading Density for Different Months')
	fig.savefig('Results/'+str(brand[loc])+'/2013/r_TD.png')

def r_TD2014(loc):
	# Year 2013(Sales and TD)
	fig = plt.figure(figsize=(25,15))
	plt.ioff()
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)
    
	a1 = sns.pointplot(x = s_2014, y = df_td.iloc[loc, 66:78], ax= ax1)
	a1.set(ylabel = 'Rent', title = 'Rent for Different Months')
	a2 = sns.pointplot(x = td_2014, y = df_td.iloc[loc, 118:130], ax = ax2)
	a2.set(xticklabels = [], ylabel = 'Trading Density', title = 'Trading Density for Different Months')
	fig.savefig('Results/'+str(brand[loc])+'/2014/r_TD.png')

def r_TD2015(loc):
	# Year 2013(Sales and TD)
	fig = plt.figure(figsize=(25,15))
	plt.ioff()

	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)
    
	a1 = sns.pointplot(x = s_2015, y = df_td.iloc[loc, 78:90], ax= ax1)
	a1.set(ylabel = 'Rent', title = 'Rent for Different Months')
	a2 = sns.pointplot(x = td_2015, y = df_td.iloc[loc, 130:142], ax = ax2)
	a2.set(xticklabels = [], ylabel = 'Trading Density', title = 'Trading Density for Different Months')
	fig.savefig('Results/'+str(brand[loc])+'/2015/r_TD.png')

def r_TD2016(loc):
	# Year 2013(Sales and TD)
	fig = plt.figure(figsize=(25,15))
	plt.ioff()
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)
    
	a1 = sns.pointplot(x = s_2016, y = df_td.iloc[loc, 90:102], ax= ax1)
	a1.set(ylabel = 'Rent', title = 'Rent for Different Months')
	a2 = sns.pointplot(x = td_2016, y = df_td.iloc[loc, 142:154], ax = ax2)
	a2.set(xticklabels = [], ylabel = 'Trading Density', title = 'Trading Density for Different Months')
	fig.savefig('Results/'+str(brand[loc])+'/2016/r_TD.png')

def r_TD2017(loc):
	# Year 2013(Sales and TD)
	fig = plt.figure(figsize=(25,15))
	plt.ioff()
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)
    
	a1 = sns.pointplot(x = s_2017, y = df_td.iloc[loc, 102:109], ax= ax1)
	a1.set(ylabel = 'Sales', title = 'Sales for Different Months')
	a2 = sns.pointplot(x = td_2017, y = df_td.iloc[loc, 154:161], ax = ax2)
	a2.set(xticklabels = [], ylabel = 'Trading Density', title = 'Trading Density for Different Months')
	fig.savefig('Results/'+str(brand[loc])+'/2017/s_TD.png')