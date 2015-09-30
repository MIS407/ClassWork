import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss

import pandas as pd
import xlrd

# Make a normal distribution with mean of 18 and standard deviation of 0.09

# ss.norm(loc = 18, scale = 0.09)
# to get the cumulative distribution function
# ss.norm.cdf(x, loc = 18, scale = 0.09)

def f(x):
    return ss.norm.cdf(x, loc = 18, scale = 0.09)

# Read Excel worksheet

wb = xlrd.open_workbook('C:/Users/Desktop/filename.xls')
sheet = wb.sheet_by_index(0)

myList = []
for i in range(sheet.nrows):
    myList.append(int(sheet.cell(i,0).value))
    
def summary(data):
    print('Max: %d' % (np.amax(data)))
    print('Min: %d' % (np.amin(data)))
    print('Mean: %d' % (np.mean(data)))
    print('Stdev: %' % (np.std(data)))

summary(myList)

plt.hist(myList, bins =(30, 40, 50, 60))
