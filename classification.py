import pandas as pd
import matplotlib.pylab as plt
import os

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

# PLOT 3
# test this update 