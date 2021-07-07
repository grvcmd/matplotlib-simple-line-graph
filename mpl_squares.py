import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis="both", which="major", labelsize=14)

# set the range for each axis.
# The axis() method requires four values: the min & max for the x-axis and y-axis
# x-axis runs from 0 to 1100 & the y-axis runs from 0 to 1,100,000
ax.axis([0, 1100, 0, 1100000])

# plt.show()
plt.savefig('scatter_squares.png')
# plt.savefig('scatter_squares_tight.png', bbox_inches='tight')
