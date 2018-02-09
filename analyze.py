import pandas as pd
import matplotlib.pylab as plt
import os

plt.switch_backend('TkAgg')
trainingFile = 'training.csv'
trainingFile = os.path.join(os.getcwd(), trainingFile)
trainingData = pd.read_csv(trainingFile)
trainingData.drop('Unnamed: 0', axis=1, inplace=True)

trainingData['Volume per Month'] = \
				trainingData['Total Volume Donated (c.c.)'] / \
				trainingData['Months since First Donation']

trainingData.plot(kind = 'scatter', 
	x = 'Months since Last Donation',
	y = 'Volume per Month')
plt.show()

avgData = trainingData.groupby(
	by='Months since Last Donation', as_index = False).mean()
ax = avgData.plot(kind = 'scatter',
	x = 'Months since Last Donation',
	y = 'Volume per Month')
ax.set_xlabel('Months since Last Donation')
ax.set_ylabel('Average Volume per Month')
plt.show()

### average per Month
### last time you came
### first time you came
thisCol = ['Months since Last Donation', 'Made Donation in March 2007']
thisData = trainingData[thisCol]
totData = thisData.groupby(by = 'Months since Last Donation', as_index = False).sum()
countData = thisData.groupby(by = 'Months since Last Donation', as_index = False).count()
thisData = totData.merge(countData, on='Months since Last Donation')
