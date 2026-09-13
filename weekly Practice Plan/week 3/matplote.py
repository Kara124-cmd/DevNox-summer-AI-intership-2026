



# Matplotlib is a low level graph plotting library in python that serves as a visualization utility.


# Pyplot
# Most of the Matplotlib utilities lies under the pyplot submodule, and are usually imported under the plt alias:    import matplotlib.pyplot as plt


import matplotlib.pyplot as plt
x = [0, 1, 2, 3, 4]
y = [1, 4, 8, 5, 19]
plt.plot(x, y)
plt.show()




import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 6])
y = np.array([0, 250])

plt.plot(x, y)
plt.show()




'''Plotting x and y points
The plot() function is used to draw points (markers) in a diagram.
By default, the plot() function draws a line from point to point.
The function takes parameters for specifying points in the diagram.
Parameter 1 is an array containing the points on the x-axis.
Parameter 2 is an array containing the points on the y-axis.
If we need to plot a line from (1, 3) to (8, 10), we have to pass two arrays [1, 8] and [3, 10] to the plot function.'''


# to make many points on the plot we can creat more points 

import matplotlib.pyplot as plt
import numpy as np
x = np.array([1, 2, 6, 8])
y = np.array([3, 8, 1, 10])

plt.plot(x, y, marker = 'o')
plt.show()


# if we do not specify the x points it will take default values of 1, 2, 3 etc on the basis of y axis
import matplotlib.pyplot as plt
import numpy as np
y = np.array([1, 3, 9, 8, 12])

plt.plot(y)
plt.show()
# the default value of the above plot x value are [0.5, 1, 1.0 etc]
















#markers
# use the keyword argument marker to emphasize each point with a specified marker:
import matplotlib.pyplot as plt
import numpy as np
x = np.array([1, 2, 7, 9])
y = np.array([3, 8, 1, 10])

plt.plot(x, y, marker = '*')    # mark each point with start   
plt.show()

'''
chose any of marker
'o'	Circle	
'*'	Star	
'.'	Point	
','	Pixel	
'x'	X	
'X'	X (filled)	
'+'	Plus	
'P'	Plus (filled)	
's'	Square	
'D'	Diamond	
'd'	Diamond (thin)	
'p'	Pentagon	
'H'	Hexagon	
'h'	Hexagon	
'v'	Triangle Down	
'^'	Triangle Up	
'<'	Triangle Left	
'>'	Triangle Right	
'1'	Tri Down	
'2'	Tri Up	
'3'	Tri Left	
'4'	Tri Right	
'|'	Vline	
'_'	Hline

'''




# Format Strings fmt
# You can also use the shortcut string notation parameter to specify the marker.
# This parameter is also called fmt, and is written with this syntax:
# marker|line|color

import matplotlib.pyplot as plt
import numpy as np
y = np.array([3, 8, 1, 10])
plt.plot(y, 'o:r')                         # marker|line|color
plt.show()



# marker / marker size(ms) / markeredgecolor(mec) / markerfacecolor(mfc) / 
import matplotlib.pyplot as plt
import numpy as np
x = np.array([1, 3, 6, 9])
y = np.array([1, 8, 3, 10])

plt.plot(x,y, marker = 'o', ms = '12', mec = 'g', mfc = 'hotpink')   # also use hexadecimal values and color names
plt.legend(title = 'data')
plt.show()









# Matplot Lines styles
# linestyle to change the line / linecolor / linewidth

import matplotlib.pyplot as plt
import numpy as np
x = np.array([1, 3, 6, 9])
y = np.array([1, 8, 3, 10])

plt.plot(x, y, linestyle = "dotted", color = 'g', linewidth = '5.5')
plt.show()






# draw two lines specifying two lines of x and y
import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2, c = 'hotpink', marker = '*', ms = '12', linestyle = 'dotted')
plt.show()







# labels and title in pyplot

import matplotlib.pyplot as plt
import numpy as np
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# set font properties for tittle and labels
font1 = {'family' : 'serif', 'color' : 'blue', 'size' : 15}
font2 = {'family' : 'serif', 'color' : 'red', 'size' : 10}

# position the title to use "loc" parameter
plt.title('Numbers array', fontdict= font1, loc = 'left')                 # use font dict to set font properties 
plt.xlabel('x axis', fontdict= font2, loc= 'center')
plt.ylabel('y axis', fontdict= font2)
plt.plot(x, y)
plt.show()













'''Add Grid Lines to a Plot
With Pyplot, you can use the grid() function to add grid lines to the plot.'''

import matplotlib.pyplot as plt
import numpy as np
x = np.array([1, 3, 5, 7 ,9])
y = np.array([5, 1, 8, 3, 2])

plt.title('Numbers plot')
plt.xlabel('X - Axis')
plt.ylabel('Y - Axis')

plt.plot(x, y)
plt.grid()     
plt.show()



# specify which gird line to display
import matplotlib.pyplot as plt
import numpy as np
x = np.array([1, 3, 5, 7 ,9])
y = np.array([5, 1, 8, 3, 2])

plt.title('Numbers plot')
plt.xlabel('X - Axis')
plt.ylabel('Y - Axis')

plt.plot(x, y)
plt.grid(axis= 'x')     
plt.show()



# set grid line property
import matplotlib.pyplot as plt
import numpy as np
x = np.array([1, 3, 5, 7 ,9])
y = np.array([5, 1, 8, 3, 2])

plt.title('Numbers plot')
plt.xlabel('X - Axis')
plt.ylabel('Y - Axis')

plt.plot(x, y)
plt.grid(color = 'red', linestyle = '--', linewidth = 0.5)     
plt.show()












'''
Display Multiple Plots
With the subplot() function you can draw multiple plots in one figure:

The subplot() function takes three arguments that describes the layout of the figure.
The layout is organized in rows and columns, which are represented by the first and second argument.
The third argument represents the index of the current plot.


'''
# draw 2 plots

import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(1, 2, 1)               # 1 row, 2 columns, and this plot is the first plot.
plt.plot(x,y)


x = np.array([0, 1, 2, 3])
y = np.array([10, 30, 20, 40])
plt.subplot(1, 2, 2)               # 1 row, 2 columns, and this plot is the second plot.
plt.plot(x, y)

plt.show()



# draw two plot top of each other
import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(2, 1, 1)               # 1 row, 2 columns, and this plot is the first plot.
plt.plot(x,y)


x = np.array([0, 1, 2, 3])
y = np.array([10, 30, 20, 40])
plt.subplot(2, 1, 2)               # 1 row, 2 columns, and this plot is the second plot.
plt.plot(x, y)

plt.show()





# draw 6 plots 
import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(2, 3, 1)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(2, 3, 2)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(2, 3, 3)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(2, 3, 4)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(2, 3, 5)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(2, 3, 6)
plt.plot(x,y)

plt.show()







# add supertitle() to entire figure and title and labels to each plot

import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(1, 2, 1)               # 1 row, 2 columns, and this plot is the first plot.
plt.title('sales')
plt.xlabel('X')
plt.ylabel('Y')
plt.plot(x,y)


x = np.array([0, 1, 2, 3])
y = np.array([10, 30, 20, 40])
plt.subplot(1, 2, 2)               # 1 row, 2 columns, and this plot is the second plot.
plt.title('income')
plt.xlabel('X')
plt.ylabel('Y')
plt.plot(x, y)

plt.suptitle("My Shop", color = 'red', fontsize = 20)
plt.show()






'''Line Chart with Annotations
For adding annotations to a line chart you can use the annotate() function. This function allows you to display additional information such as the exact x and y values directly on the data points, improving clarity and data interpretation.'''
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, marker='o')

for xi, yi in zip(x, y):
    plt.text(xi, yi, f'({xi}, {yi})')

plt.title("Line Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid()
plt.show()















'''
Creating Scatter Plots
With Pyplot, you can use the scatter() function to draw a scatter plot.
The scatter() function plots one dot for each observation. It needs two arrays of the same length, one for the values of the x-axis, and one for values on the y-axis:

'''

import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 3, 5, 7, 9])
y = np.array([5, 7, 3, 9, 2])

plt.scatter(x, y)
plt.show()


# draw two plots on same figure
import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([1, 2, 3, 4, 5])
y1 = np.array([5, 7, 2, 8, 1])
colors = np.array(['red', 'green', 'blue', 'orange', 'purple'])     # color each dot
plt.scatter(x1, y1, c = colors)

x2 = np.array([1, 3, 5, 7, 9])
y2 = np.array([8, 3, 7, 1, 4])
plt.scatter(x2, y2, color = 'purple')

plt.show()





# use the color map 'cmap' /  and size of dots /  and tranparency of dots with alpha
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 3, 5, 7, 9])
y = np.array([5, 7, 3, 9, 2])

colors = np.array([9, 11, 40, 37, 22])
sizes = np.array([60, 90, 120, 30, 150])

plt.scatter(x, y,c = colors,cmap = 'rainbow', s = sizes, alpha = 0.4)
plt.colorbar()

plt.show()












'''
Creating Bars
With Pyplot, you can use the bar() function to draw bar graphs: 
'''


import matplotlib.pyplot as plt

fruits = ['Apples', 'Bananas', 'Cherries', 'Dates']
sales = [400, 350, 300, 450]

plt.bar(fruits, sales)
plt.title('Fruit Sales')
plt.xlabel('Fruits')
plt.ylabel('Sales')
plt.show()



import matplotlib.pyplot as plt
import numpy as np

x = np.array(['A', 'B', 'C', 'D', 'E'])
y = np.array([5, 1, 7, 3, 9])

plt.title('Student Records')
plt.xlabel('Students')
plt.ylabel('Marks')

plt.bar(x, y)
plt.show()

# use horizontal bars instead of vertical we use 'barh()'
import matplotlib.pyplot as plt
import numpy as np

x = np.array(['A', 'B', 'C', 'D', 'E'])
y = np.array([5, 1, 7, 3, 9])

plt.barh(x, y, color = 'red', height = 0.3)
plt.show()






# colors  / width
import matplotlib.pyplot as plt
import numpy as np

x = np.array(['A', 'B', 'C', 'D', 'E'])
y = np.array([5, 1, 7, 3, 9])

plt.title('Student Records')
plt.xlabel('Students')
plt.ylabel('Marks')

plt.bar(x, y, color = 'hotpink', width = 0.15)
plt.show()































'''
Histogram
A histogram is a graph showing frequency distributions.
It is a graph showing the number of observations within each given interval.
'''

import matplotlib.pyplot as plt

marks = [10, 15, 18, 22, 25, 28, 31, 35, 40, 42, 45, 48, 50]

plt.hist(marks, bins = 5)        # bins create How many groups/ranges 
plt.xlabel('marks')
plt.ylabel('NO.of Students')
plt.title('Student marks distribution')
plt.show()












'''
Creating Pie Charts
With Pyplot, you can use the pie() function to draw pie charts:
As you can see the pie chart draws one piece (called a wedge).By default the plotting of the first wedge starts from the x-axis and moves counterclockwise
'''

import matplotlib.pyplot as plt

y = [25, 35, 10, 25, 15]
mylabels = ['Usman', 'hamid', 'jawad', 'ali', 'ahmad']
plt.pie(y, labels= mylabels)
plt.show()


# The startangle parameter is defined with an angle in degrees, default angle is 0:
import matplotlib.pyplot as plt

y = [25, 35, 10, 25, 15]
mylabels = ['Usman', 'hamid', 'jawad', 'ali', 'ahmad']
plt.pie(y, labels= mylabels, startangle=180)
plt.show()


# Maybe you want one of the wedges to stand out? The explode parameter allows you to do that. / shadow 
import matplotlib.pyplot as plt

y = [25, 35, 10, 25, 15]

mylabels = ['Usman', 'hamid', 'jawad', 'ali', 'ahmad']
myexplode = [0.0, 0.0, 0.18, 0.0, 0.0]
mycolors = ['black', 'c', 'green', 'blue', 'w']

plt.pie(y, labels= mylabels, explode= myexplode, shadow= True, colors = mycolors)

plt.show()



# To add a list of explanation for each wedge, use the legend() function: / and legend with header title

import matplotlib.pyplot as plt

y = [25, 35, 10, 25, 15]

mylabels = ['Usman', 'hamid', 'jawad', 'ali', 'ahmad']

plt.pie(y, labels= mylabels)
plt.legend(title = 'five student')
plt.show()



nums = [1, 2, 3, 4, 5]
for num in nums:
    if num == 3:
        break

else:
    print('loop completed')













'''
 Box Plot
Box plot is a simple graph that shows how data is spread out. It displays the minimum, maximum, median and quartiles and also helps to spot outliers easily.
Example: This code creates a box plot to show the data distribution and compare three groups using matplotlib'''

import matplotlib.pyplot as plt

data = [ [10, 12, 14, 15, 18, 20, 22],
        [8, 9, 11, 13, 17, 19, 21],
        [14, 16, 18, 20, 23, 25, 27] ]

plt.boxplot(data)
plt.xlabel("Groups")
plt.ylabel("Values")
plt.title("Box Plot")
plt.show()

















# Line Char practice 
# Plot a line chart showing the squares of numbers from 1 to 10.
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

plt.plot(x)
plt.show()


# Plot two lines on the same chart: y1 = x and y2 = x² for x = 0 to 10, with a legend distinguishing them.
import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y1 = x
y2 = x**2

plt.plot(x, y1)
plt.plot(x, y2)

plt.xlabel('x')
plt.ylabel('y')
plt.title('x = y1 and x**2 = y2')
plt.legend()
plt.show()




# Create a line chart of temperature over 7 days, and add axis labels and a title.
import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7]
temp = [23.34, 30.32, 19.4, 40.0, 25.5, 41.3, 33.23]

plt.plot(days, temp, marker = 'o')
plt.xlabel('days')
plt.ylabel('temperature')
plt.title('temperarture of week', fontsize = 15)

plt.show()






# Bar Chart
# Create a bar chart showing the marks of 5 students in a class.
import matplotlib.pyplot as plt

students = ['usman', 'hamid', 'jawad', 'ali', 'ahmad']
marks = [90, 45, 67, 55, 82]

plt.bar(students, marks)
plt.xlabel('students')
plt.ylabel('marks')

plt.show()


# Plot a horizontal bar chart comparing sales of 4 products.

import matplotlib.pyplot as plt

product = ['pensil', 'book', 'bag', 'marker']
sales = [34, 67, 12, 89]

plt.barh(product, sales)

plt.show()


# Create a grouped bar chart comparing marks of 2 students across 3 subjects.

import matplotlib.pyplot as plt 
import numpy as np

subjects = ['math', 'physics', 'computer']
student1 = [80, 70, 90]
student2 = [75, 45, 80]

x = np.arange(3)
width = 0.3

plt.bar(x - width/2, student1, width, label = 'student1')
plt.bar(x + width/2, student2, width, label = 'student2')

plt.xticks(x, subjects)
plt.xlabel('students')
plt.ylabel('marks')
plt.title('student marks')

plt.legend()
plt.show()









# Histogram
# Generate 1000 random numbers (normal distribution) and plot a histogram with 20 bins.
import matplotlib.pyplot as plt
import numpy as np

num = np.random.normal(0, 1, 1000)

plt.hist(num, bins = 20)
plt.show()


# Plot a histogram of ages of 50 people (you can hardcode or randomly generate the list) and change the bar color to green.

import matplotlib.pyplot as plt
import numpy as np

ages = np.array([18, 21, 25, 30, 22,35, 28, 19, 24, 31,27, 40, 23, 29, 33,26, 21, 36, 45, 32, 20, 38, 27, 34, 41,22, 25, 30, 37, 29,18, 26, 43, 31, 35,28, 24, 39, 33, 20,42, 27, 36, 23, 30,25, 44, 32, 21, 38
])

plt.hist(ages, color = 'g')
plt.show()






# Scatter Plot
# Plot a scatter plot of study hours vs. exam scores for 10 students.

import matplotlib.pyplot as plt
import numpy as np

study_hours = np.array([2, 4, 8, 3, 4, 7, 9, 1, 6, 8])
exam_score = np.array([89, 45, 78, 87, 63, 85, 58, 66, 87, 91])

plt.scatter(study_hours, exam_score, color = 'red')
plt.title('students Records')
plt.xlabel('study_hours')
plt.ylabel('exam_scores')
plt.show()



# Create a scatter plot with a third variable represented by point size (e.g., population as bubble size for cities' income vs. happiness score).

import matplotlib.pyplot as plt

income = [20000, 30000, 40000, 50000, 60000]
happines_score = [3, 6, 2, 8, 5]

p_size = [40, 60, 80, 110, 140]
colors = ['red', 'green', 'blue', 'yellow', 'orange']
plt.scatter(income, happines_score, s = p_size, c = colors)
plt.title('population bubble size')
plt.xlabel('income')
plt.ylabel('happines score')
plt.show()





# Pie Chart
# Create a pie chart showing the market share of 5 companies.

import matplotlib.pyplot as plt
import numpy as np

companies = np.array(['tesla', 'microsoft', 'google', 'amazon', 'alibaba'])
market_share = np.array([25, 15, 30, 20, 10])

plt.pie(market_share, labels = companies, autopct = '%1.1f%%')
plt.show()


# Plot a pie chart of your daily time distribution (sleep, study, leisure, work) with percentage labels shown.
import matplotlib.pyplot as plt

daily_routine_time = [8, 7, 4, 5]
routine = ['sleep', 'study', 'leisure', 'work']

plt.pie(daily_routine_time, labels = routine, autopct='%1.1f%%')
plt.show()






# Box Plot
# Create a box plot for a single dataset of exam scores to see its spread and outliers.

import matplotlib.pyplot as plt
import numpy as np

exam_scores = np.array([55, 60, 62, 65, 68, 70, 72, 75, 78, 80, 82, 85, 88, 90, 95])

plt.boxplot(exam_scores)
plt.show()


# Create box plots comparing exam scores of 3 different classes side by side.
import matplotlib.pyplot as plt
import numpy as np

class_A = np.array([55, 60, 65, 70, 75])
class_B = np.array([60, 65, 70, 75, 80])
class_C = np.array([65, 70, 75, 80, 85])

plt.boxplot([class_A, class_B, class_C], tick_labels = ['class_A', 'class_B', 'class_C'])
plt.show()