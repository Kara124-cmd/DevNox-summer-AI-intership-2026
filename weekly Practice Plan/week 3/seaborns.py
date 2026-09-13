


'''
Visualize Distributions With Seaborn
Seaborn is a library that uses Matplotlib underneath to plot graphs. It will be used to visualize random distributions.
Seaborn is a Python library for creating statistical visualizations. It provides clean default styles and color palettes, making plots more attractive and easier to read. Built on top of Matplotlib and integrated with pandas data structures, Seaborn makes data visualization easier and more consistent.
'''

# Displots
# Displot stands for distribution plot, it takes as input an array and plots a curve corresponding to the distribution of points in the array.

# plotting a displot

import matplotlib.pyplot as plt
import seaborn as sns
sns.displot([0, 1, 2, 3, 4, 5])
plt.show()

# plotting a displot without a histogram
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot([1, 3, 5, 7, 9], kind='kde')
plt.show()








# line graph using seaborn without using the dataframe
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

var_1 = [1, 2, 3, 4, 5, 6, 7]
var_2 = [2, 3, 4, 1, 8, 9, 6]


sns.lineplot(x=var_1, y=var_2)
plt.show()


# line graph using seaborn with dataframe
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

var_1 = [1, 2, 3, 4, 5, 6, 7]
var_2 = [2, 3, 4, 1, 8, 9, 6]

# make dataframe first 
x_1 = pd.DataFrame({'var_1': var_1, 'var_2': var_2})

sns.lineplot(x='var_1', y='var_2', data=x_1)
plt.show()




# work on seaborn datasets on github

# line graph using seaborn
import matplotlib.pyplot as plt
import seaborn as sns

x1 = sns.load_dataset('penguins').head(20)

sns.lineplot(
    x='bill_length_mm',
    y='flipper_length_mm',
    data=x1,
    hue='sex',
    size=10,
    style='sex',
    palette='rocket',
    markers=['o','>'],
    dashes=False
)

plt.title('Python', fontsize = 20)
plt.show()
















# Histogram in seaborn

import matplotlib.pyplot as plt
import seaborn as sns

var = sns.load_dataset('exercise')

sns.displot(var['pulse'], bins=[80, 90, 100, 110, 120, 130, 140, 150], kde = True, rug = True, color = 'g')
plt.show()









# bar plot in seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

var = sns.load_dataset('titanic')
print(var)

sns.barplot(x = 'embarked', y = 'age', data = var, hue='sex')
plt.show()

# make the order of x axis 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

var = sns.load_dataset('titanic')
print(var)

orders = ['S', 'C', 'Q']
sns.barplot(x = 'embarked', y = 'age', data = var, hue='sex')
plt.show()


# we use hue_order to make the element in order 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

var = sns.load_dataset('titanic')
print(var)

sns.barplot(x = 'embarked', y = 'age', data = var, hue='sex', hue_order=['female', 'male'], ci = 90)  # ci make the upper line larger

plt.show()


# make this plot horizontal only work on numerical data not working on the string 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

var = sns.load_dataset('titanic')
print(var)

sns.barplot(x = 'fare', y = 'age', data = var, hue='sex', orient='h', palette='flare')
plt.show()




# colors 
import matplotlib.pyplot as plt
import seaborn as sns

var = sns.load_dataset('titanic')

sns.set(style = 'darkgrid')
sns.barplot(x = 'embarked', y = 'age', data = var, hue='sex', palette='flare', saturation=10, errcolor = 'g', errwidth=2, capsize=0.2, alpha=0.9)
plt.show()
















# scater plot in seaborn

import matplotlib.pyplot as plt
import seaborn as sns

var = sns.load_dataset('penguins').head(50)

m = {'Male': 'o','Female': 's'}
sns.scatterplot(x = 'bill_length_mm', y = 'body_mass_g', data = var, hue = 'sex', style = 'sex', size = 'sex', sizes = (100, 50), palette='deep', alpha = 0.8, markers = m)

plt.show()
















# HeatMap in seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

var = np.linspace(1, 10, 20).reshape(4,5)

sns.heatmap(var)
plt.show()



# import data from dataset and make heatmap
# heatmap words on numerical data so we can drop all others strings columsn
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

var = sns.load_dataset('anagrams').head(5)
x = var.drop(columns = ['attnr'])
print(x)
# print(var)
sns.heatmap(x, vmin = 0, vmax = 12, cmap = "PuOr", annot = True, linewidth = 5, linecolor = 'green')
plt.show()

















# countplot: use for counting the data in plot
# it used the single x axis to count 
import matplotlib.pyplot as plt
import seaborn as sns

dt = sns.load_dataset('tips')

sns.countplot(x = 'sex', data = dt, hue='smoker', palette= 'crest', saturation= 0.5)
plt.show()


# make it horizontal simply chnage x to y

import matplotlib.pyplot as plt
import seaborn as sns

dt = sns.load_dataset('tips')

sns.countplot(y = 'sex', data = dt, hue='smoker')
plt.show()












# voilin plot
# same as box plot distribution of quantitative data across sevral level of one or more 

import matplotlib.pyplot as plt
import seaborn as sns

var = sns.load_dataset('tips')
print(var)

sns.violinplot(x = 'day', y = 'total_bill', data = var, hue = 'time', linewidth = 1.2, palette='Dark2')
plt.show()

# check the total bill according to time like in order of dinner and lunch
import matplotlib.pyplot as plt
import seaborn as sns

var = sns.load_dataset('tips')
print(var)

sns.violinplot(x = 'time', y = 'total_bill', data = var, order = ['Dinner', 'Lunch'], linewidth = 1.2, palette='Dark2', saturaion = 0.5, )
plt.show()


# split data on the basis on sex
import matplotlib.pyplot as plt
import seaborn as sns

var = sns.load_dataset('tips')
print(var)

sns.violinplot(x = 'day', y = 'total_bill', data = var, hue = 'sex',split = True, palette='Dark2')
plt.show()
















# Pair Plot

import matplotlib.pyplot as plt
import seaborn as sns

var = sns.load_dataset('tips')

sns.pairplot(var)
plt.show()


# made only two values 
import matplotlib.pyplot as plt
import seaborn as sns

var = sns.load_dataset('tips')

sns.pairplot(var, vars = ['total_bill', 'tip'], hue = 'sex', hue_order=['Male', 'Female'], palette = 'BuGn')
plt.show()














# strip plot is same as scatter plot
import matplotlib.pyplot as plt
import seaborn as sns

var = sns.load_dataset('tips')
m = {'Male' : 'o', 'Female': '*'}
sns.stripplot(x = 'day', y = 'total_bill', data = var, hue = 'sex', palette = 'rocket_r', markers = m)
plt.show()












# box plot
import matplotlib.pyplot as plt
import seaborn as sns

var = sns.load_dataset('tips')
sns.set(style = 'whitegrid')

sns.boxplot(x = 'day', y = 'total_bill', data = var, hue = 'sex', showmeans = True, palette = 'plasma', linewidth = 2)
plt.show()








# factor plot renamed as catplot

import matplotlib.pyplot as plt
import seaborn as sns

var = sns.load_dataset('tips')

sns.catplot(x = 'size', y = 'tip', data = var, hue = 'sex', kind = 'bar')
plt.show()



# cat plot
import matplotlib.pyplot as plt
import seaborn as sns

var = sns.load_dataset('tips')

var = sns.load_dataset('tips').head(20)

sns.catplot(x = 'tip', y = 'size', data = var, hue = 'sex', palette = 'BuPu', kind = 'point')
plt.show()









# Styling plots in seaborn
import matplotlib.pyplot as plt
import seaborn as sns

var = sns.load_dataset('tips')
sns.set(style = 'darkgrid')
sns.barplot(x= 'day', y = 'total_bill', data = var)
plt.show()


# remove axis line 
import matplotlib.pyplot as plt
import seaborn as sns

var = sns.load_dataset('tips')
sns.set(style = 'whitegrid')
sns.barplot(x= 'day', y = 'total_bill', data = var)
sns.despine()
plt.show()


#changes in figure size and content
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_context('paper', font_scale=1)
plt.figure(figsize = (6,4))

var = sns.load_dataset('tips')
sns.set(style = 'darkgrid')
sns.barplot(x= 'day', y = 'total_bill', data = var, palette = 'cool')
plt.show()






#facetGrid seaborn using this we can create multiple plots 
import matplotlib.pyplot as plt
import seaborn as sns

var = sns.load_dataset('tips')

fg = sns.FacetGrid(var, col = 'day', hue = 'sex')
fg.map(plt.bar, 'total_bill', 'tip').add_legend()
plt.show()



















# practice problems
# displot 
# create a marks list and show it on plot
import matplotlib.pyplot as plt
import seaborn as sns

marks = [45, 55, 60, 65, 70, 72, 75, 80, 85, 90]

sns.displot(marks)
plt.show()

# kde curve on the same plot
import matplotlib.pyplot as plt
import seaborn as sns

marks = [45, 55, 60, 65, 70, 72, 75, 80, 85, 90]

sns.displot(marks, kind='kde')
plt.show()


# Line plot
# create a line plot of day and temperature
import matplotlib.pyplot as plt
import seaborn as sns

days = [1, 2, 3, 4, 5, 6, 7]
temperature = [30, 32, 31, 35, 36, 34, 33]

sns.lineplot(x = days, y = temperature)
plt.show()

# create a dataframe containing student and marks and plot it on line plot
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

student_detail = pd.DataFrame({
    'student' : ['usman', 'ali', 'ahmad', 'jawad',  'khan'],
    'marks' : [89, 56, 76, 92, 67]
})

sns.lineplot(x = 'student', y = 'marks', data = student_detail, marker = 'o')
plt.show()





# load dataset 
import matplotlib.pyplot as plt
import seaborn as sns


data = sns.load_dataset('penguins')
print(data)

sns.lineplot(x = 'bill_length_mm', y = 'flipper_length_mm', data = data, hue = 'sex', style='sex', dashes= False)
plt.show()




import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('exercise')

sns.displot(x = 'pulse', data = df, bins = 20, kde = True, rug = True)
plt.show()




# BARPLOT
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('titanic')
em_order = ['S', 'Q', 'C']
sns.barplot(x = 'embarked', y = 'age', data = df, hue = 'sex', order= em_order)
plt.show()

# make this bar plot horizontal
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('titanic')
em_order = ['S', 'Q', 'C']
sns.barplot(x = 'age', y = 'embarked', data = df, hue = 'sex', order= em_order)
plt.show()







# SCATTERPLOT
import matplotlib.pyplot as plt
import seaborn as sns

penguin = sns.load_dataset('penguins')

sns.scatterplot(x = 'bill_length_mm', y = 'body_mass_g', data = penguin, hue = 'sex', style = 'sex', size = 'sex', alpha = 0.8)
plt.show()



import matplotlib.pyplot as plt
import seaborn as sns

tipps = sns.load_dataset('tips')

sns.scatterplot(x = 'total_bill', y = 'tip', data = tipps, hue = 'sex', style = 'time')
plt.show()



# HEATMAP

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

newarr = pd.DataFrame(arr)
print(newarr)

sns.heatmap(newarr, annot = True)
plt.show()





# countplot
import matplotlib.pyplot as plt
import seaborn as sns

tipps = sns.load_dataset('tips')
print(tipps)
sns.countplot(x = 'sex', data = tipps, hue = 'smoker')
plt.show()


# horizontal couterplot
import matplotlib.pyplot as plt
import seaborn as sns

tipps = sns.load_dataset('tips')
print(tipps)
sns.countplot(y = 'sex', data = tipps, hue = 'smoker')
plt.show()





# voilen plot
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = sns.load_dataset('tips')

sns.violinplot(x = 'day', y = 'total_bill', data = df, hue = 'time', split = True)
plt.show()




#Pair plot
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('tips')
print(df.info())

sns.pairplot(df, vars = ['total_bill', 'tip'], hue ='sex', hue_order = ['Female', 'Male'])
plt.show()




# strip plot
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('tips')

sns.stripplot(x = 'day', y = 'total_bill', data = df, hue = 'sex', marker = '*')
plt.show()




# box Plot
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

var = sns.load_dataset('tips')

sns.boxplot(x = 'day', y = 'total_bill', data = var, hue = 'sex', showmeans = True)
plt.show()



# catplot
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

var = sns.load_dataset('tips')
sns.set(style = 'darkgrid')
sns.despine()

sns.catplot(x = 'size', y = 'tip', data = var, hue = 'sex', kind = 'point')
plt.show()