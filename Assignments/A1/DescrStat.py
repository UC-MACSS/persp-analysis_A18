'''
------------------------------------------------------------------------
This script defines a function DescrStat() that gives descriptive
statistics for a comma delimited text file of one variable in which the
data are in one column and each observation is a row.
------------------------------------------------------------------------
'''

# Import packages
import numpy as np


def DescrStat(datafile):
    data = np.loadtxt(datafile)
    data_mean = data.mean()
    data_std = data.std()
    data_var = data.variance()

    print('Mean of the data is:', data_mean)
    print('Standard deviation of the data is:', data_std)
    print('Variance of the data is:', data_var)

    return data_mean, data_std, data_var
