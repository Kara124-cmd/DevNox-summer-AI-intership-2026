


# statistics two catogoresi discriptive and inferential


# 1 : DISCRIPTIVE STATISTICS 

#============== Measurement of central tendency (mean, median, mode)=================



# mean(average)
import numpy as np
import pandas as pd

arr = np.array([1, 3, 4, 6, 7, 9, 3, 5, 6, 2])


# traditional way to calculate the mean
print(np.sum(arr))
print(len(arr))
print('the mean of this arrays is ', np.sum(arr)/len(arr))

# mean using the fucntion
print(np.mean(arr))



#  calculate mean in the dataset 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('retail_sales.csv')
print(df.head(10))

meanof_sales = np.mean(df['Sales'])
print(meanof_sales)

# show mean on histogram
sns.histplot(x = 'Sales', data = df, bins = 10)
plt.plot([meanof_sales for i in range(0, 400)],[i for i in range(0, 400)], color = 'red')  # mean line

plt.show()





# median 

import numpy as np
import pandas as pd

arr = np.array([1, 3, 4, 6, 7, 9, 3, 5, 6, 2])

print(np.sort(arr))
print(np.median(arr))

# calculate median in dataset
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('retail_sales.csv')
print(df.head(10))

# there are null values in the age column so first we fill this
print(df['Sales'].isnull().sum())
df['Sales'] = df['Sales'].fillna(df['Sales'].mean())
# print(df['Sales'])
md = np.median(df['Sales'])
print(md)
#show median on histogram

sns.histplot(x = 'Sales', data = df, bins = 10)
plt.plot([md for i in range(0, 400)],[i for i in range(0, 400)], color = 'blue')  # median line

plt.show()





# MODE : this is done on categorical data
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('retail_sales.csv')
print(df.head(10))

mod = df['Category'].mode()[0]
print(mod)
count_mod = df['Category'].value_counts()
print(count_mod)

# show the mode on histogram
sns.histplot(x = 'Category', data = df)
plt.plot([mod for i in range(0, 400)], [i for i in range(0, 400)], color = 'brown')
plt.xticks(rotation = 45)
plt.show()








#============== Measurement of variability(range, mean absolute divation, variance, std)=================


# RANGE
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('titanic')
print(df.head(10))
#range of person of what age which travel min to max
min_age = df['age'].min()      # min age
max_age = df['age'].max()      # max age

# now calculate range 
range = max_age - min_age
print('the range of the age between is : ', range)



# MAD(mean absolute diviation) tells how much our data is spread
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class_A = np.array([75, 65, 73, 68, 72, 76])
class_B = np.array([90, 47, 43, 96, 93, 51])
no = np.array([1, 2, 3, 4, 5, 6])

mn = np.mean(class_A)
print(mn)

# calculate the mean aboslute deviation 
mad_A = np.mean(np.abs(class_A - np.mean(class_A)))
mad_B = np.mean(np.abs(class_B - np.mean(class_B)))
print("MAD of Class A:", mad_A)
print("MAD of Class B:", mad_B)


plt.figure(figsize=(8, 4))
plt.scatter(class_A, no, label = 'classA')
plt.scatter(class_B, no, color = 'red', label = 'classB')
plt.plot([mn for i in range(1, 6)], [i for i in range(1, 6)],color = 'brown', label = 'Mean')
plt.legend()
plt.show()






# STANDARD DEVIATION  AND VARIANCE
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class_A = np.array([75, 65, 73, 68, 72, 76])
class_B = np.array([90, 47, 43, 96, 93, 51])
no = np.array([1, 2, 3, 4, 5, 6])

# calculate standard divation
print(np.std(class_A))
print(np.std(class_B))

# calculate variance
print('Variance ==')
print(np.var(class_A))
print(np.var(class_B))



# standard divation and variation on dataset
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

df = pd.read_csv('retail_sales.csv')
print(df.head(10))

# print the standard diviation of quantity
std_df = df['Profit'].std()
print(std_df)

# print the varinace of quantity
var_df = df['Profit'].var()
print(var_df)

# you can also check by describe() methido
detail_df = df['Profit'].describe()
print(detail_df)

# show it on histogrm
sns.histplot(x = 'Profit', data = df)
plt.show()





#PERCENTILES AND QUANTILES
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

dataset = sns.load_dataset('titanic')
print(dataset.head(3))

null_counts = dataset.isnull().sum()  # check for null values
print(null_counts)

dataset['age'] = dataset['age'].fillna(dataset['age'].mean())   # fill null values with mean
print(dataset['age'].isnull().sum())

# calculate the percentiles 
print(np.percentile(dataset['age'], 0))
print(np.percentile(dataset['age'], 25))
print(np.percentile(dataset['age'], 50))
print(np.percentile(dataset['age'], 75))

# show it on the boxplot
sns.boxplot(x = 'age', data = dataset)    # show outliers
plt.show()





# MEasure of shape
# SKEWNESSS using Frequency & Commulative Distribution
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

dataset = sns.load_dataset('titanic')
print(dataset.head(3))

print('mean is : ', dataset['age'].mean(),'median is :', dataset['age'].median(),'mode is :', dataset['age'].mode()[0])

print(dataset['age'].skew())

sns.histplot(x = 'age', data = dataset)     # positive(right) skewness
plt.show()



