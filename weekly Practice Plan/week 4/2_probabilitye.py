

# Coveriance and Correlation
import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np
import pandas as pd

newdf = pd.read_csv('tips.csv')
print(newdf.head(3))

print(newdf.isnull().sum())

print(newdf.info())

data_corr = newdf.select_dtypes(['float64', 'int64']).corr()
print('the correlation in ', data_corr) 

data_cov = newdf.select_dtypes(['float64', 'int64']).cov()
print('the coveriance is ', data_cov) 

# show on heatmap
# sns.heatmap(data_corr, annot = True)
# plt.show()

sns.heatmap(data_cov, annot = True)
plt.show()




# Hypthesis testing (z - test, T - test, chi - Square Test)

#Z_TEST: One-tailed (right-tailed) Z-test for comparing two independent sample means
# Used here to test whether the New Design has a higher mean value than the Old Design

import scipy.stats as st
import numpy as np

import numpy as np

Old_design_data = np.array([45.2, 42.8, 38.9, 43.5, 41.0, 44.6, 40.5, 42.7, 39.8, 41.4, 44.3, 39.7, 42.1, 40.6, 43.0, 42.2, 41.5, 39.6, 44.0, 43.1, 38.7])

New_design_data = np.array([48.5, 49.1, 50.2, 47.8, 48.7, 49.9, 48.0, 50.5, 49.8, 49.6, 48.2, 48.9, 49.7, 50.3, 49.4, 50.1, 48.6, 48.3, 49.0, 50.0, 48.4])

population_std = 2.5
n_sp = len(New_design_data)
apl = 0.05            # Significance level (alpha) — probability of rejecting a true null hypothesis (Type I error)

mean_new = np.mean(New_design_data)
mean_old = np.mean(Old_design_data)

# z_cal calculation
z_cal = (mean_new - mean_old)/(population_std/np.sqrt(n_sp))
print(z_cal)

#z_table
z_table = st.norm.ppf(1 - apl)
print(z_table)


if z_cal > z_table:
    print('ha is right')
else:
    print('ha is not right')