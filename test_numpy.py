# TESTING USE OF NUMPY
import matplotlib.pyplot as plt
import numpy as np

f = open('training.csv','r')
temp = f.read().split('\n')[1:-1]
data = []
for line in temp:
    newLine = [float(x) for x in line.split(',')]
    data.append(newLine)
data = np.array(data)