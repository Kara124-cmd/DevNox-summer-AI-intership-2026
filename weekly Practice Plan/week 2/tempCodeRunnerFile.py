import matplotlib.pyplot as plt
name = ['usman', 'hassan', 'khan','ali']
marks = [89, 56, 78, 56]
plt.xlabel("name")
plt.ylabel('marks')
plt.title('StudentRecord', fontsize = 20)
c = ['m', 'y', 'g', 'b']
plt.bar(name, marks, width = 0.3, color = c, label = 'studentdata')
plt.legend()
plt.show()


