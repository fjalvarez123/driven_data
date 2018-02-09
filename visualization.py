import pandas as pd
import matplotlib.pylab as plt
import os

# columns:
# 0 - Months since Last Donation
# 1 - Number of Donations
# 2 - Total Volume Donated (c.c.)
# 3 - Months since First Donation
# 4 - Made Donation in March 2007

plt.switch_backend('TkAgg')
trainingFile = 'training.csv'
trainingFile = os.path.join(os.getcwd(), trainingFile)
trainingData = pd.read_csv(trainingFile)
trainingData.drop('Unnamed: 0', axis=1, inplace=True)

flag = 'Made Donation in March 2007'
yesData = trainingData.loc[trainingData[flag] == 1]
noData = trainingData.loc[trainingData[flag] == 0]

# PLOT 1
x_label = 'Total Volume Donated (c.c.)'
y_label = 'Months since First Donation'
myPlot = yesData.plot(kind='scatter', x=x_label, y=y_label, color='Blue')
noData.plot(kind='scatter', x=x_label, y=y_label, ax=myPlot, color='Red')
myPlot.set_xlabel(x_label)
myPlot.set_ylabel(y_label)
plt.show()

# PLOT 2
x_label = 'Total Volume Donated (c.c.)'
y_label = 'Months since First Donation'
myPlot = yesData.plot(kind='scatter', x=x_label, y=y_label, color='Blue')
noData.plot(kind='scatter', x=x_label, y=y_label, ax=myPlot, color='Red')
myPlot.set_xlabel(x_label)
myPlot.set_ylabel(y_label)
myPlot.set_xlabel(x_label)
myPlot.set_ylabel(y_label)
plt.show()

# PLOT 3 -
x_label = 'Number of Donations'
y_label = 'Months since Last Donation'
myPlot = yesData.plot(kind='scatter', x=x_label, y=y_label, color='Blue')
noData.plot(kind='scatter', x=x_label, y=y_label, ax=myPlot, color='Red')
myPlot.set_xlabel(x_label)
myPlot.set_ylabel(y_label)
myPlot.set_xlabel(x_label)
myPlot.set_ylabel(y_label)
plt.show()

# PLOT 4 -
x_label = 'Number of Donations'
y_label = 'Months since First Donation'
myPlot = yesData.plot(kind='scatter', x=x_label, y=y_label, color='Blue')
noData.plot(kind='scatter', x=x_label, y=y_label, ax=myPlot, color='Red')
myPlot.set_xlabel(x_label)
myPlot.set_ylabel(y_label)
myPlot.set_xlabel(x_label)
myPlot.set_ylabel(y_label)
plt.show()

# PLOT 3 - Months since First Donation
count = trainingData.groupby(by='Months since First Donation', as_index=False)['Made Donation in March 2007'].count()
sum = trainingData.groupby(by='Months since First Donation', as_index=False)['Made Donation in March 2007'].sum()
data = count.merge(right=sum, how='inner', on='Months since First Donation')
data['pct_attended'] = data['Made Donation in March 2007_y'] / data['Made Donation in March 2007_x']
data.plot(kind='scatter', x='Months since First Donation', y='pct_attended')
plt.xlabel('Months since First Donation')
plt.ylabel('Percent made Donation in March')
plt.show()
plt.clf()

# PLOT 4 - * this one is pretty interesting
count = trainingData.groupby(by='Number of Donations', as_index=False)['Made Donation in March 2007'].count()
sum = trainingData.groupby(by='Number of Donations', as_index=False)['Made Donation in March 2007'].sum()
data = count.merge(right=sum, how='inner', on='Number of Donations')
data['pct_attended'] = data['Made Donation in March 2007_y'] / data['Made Donation in March 2007_x']
data.plot(kind='scatter', x='Number of Donations', y='pct_attended')
plt.xlabel('Number of Donations')
plt.ylabel('Percent made Donation in March')
plt.show()
plt.clf()


# PLOT 5 - Number of Donations
count = trainingData.groupby(by='Months since First Donation', as_index=False)['Made Donation in March 2007'].count()
sum = trainingData.groupby(by='Months since First Donation', as_index=False)['Made Donation in March 2007'].sum()
data = count.merge(right=sum, how='inner', on='Months since First Donation')
data['pct_attended'] = data['Made Donation in March 2007_y'] / data['Made Donation in March 2007_x']
data.plot(kind='scatter', x='Months since First Donation', y='pct_attended')
plt.xlabel('Months since First Donation')
plt.ylabel('Percent made Donation in March')
plt.show()
plt.clf()
#
# # PLOT 6 - histograms
plt.hist(trainingData['Months since First Donation'], bins=15)
plt.show()
plt.clf()
plt.hist(trainingData['Months since Last Donation'], bins=20)
plt.show()
plt.clf()

# PLOT 7
data = trainingData
data['rate_of_donation'] = data['Total Volume Donated (c.c.)'] / data['Months since First Donation']
yesData = data.loc[data[flag] == 1]
noData = data.loc[data[flag] == 0]
x_label = 'Months since First Donation'
y_label = 'rate_of_donation'
myPlot = yesData.plot(kind='scatter', x=x_label, y=y_label, color='Blue')
noData.plot(kind='scatter', x=x_label, y=y_label, ax=myPlot, color='Red')
myPlot.set_xlabel(x_label)
myPlot.set_ylabel(y_label)
myPlot.set_xlabel(x_label)
myPlot.set_ylabel(y_label)
plt.show()
plt.clf()

# PLOT 8
myPlot = plt.hist(yesData['rate_of_donation'],color='Blue',alpha=.5)
plt.hist(noData['rate_of_donation'],color='Red',alpha=.5)
plt.xlabel('Rate of Donation (cc/month)')
plt.show()

# PLOT 9
data = trainingData
data['frequency'] = data['Number of Donations'] / data['Months since First Donation']
yesData = data.loc[data[flag] == 1]
noData = data.loc[data[flag] == 0]
x_label = 'Months since First Donation'
y_label = 'frequency'
myPlot = yesData.plot(kind='scatter', x=x_label, y=y_label, color='Blue')
noData.plot(kind='scatter', x=x_label, y=y_label, ax=myPlot, color='Red')
myPlot.set_xlabel(x_label)
myPlot.set_ylabel(y_label)
myPlot.set_xlabel(x_label)
myPlot.set_ylabel(y_label)
plt.show()
plt.clf()
