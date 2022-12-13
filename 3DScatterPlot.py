from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

X,Y,Z = [2,7,6,8],[1,2,9,4],[3,6,8,12]

fig = plt.figure()

#To create a 2d scatterplot, remove projection
ax = fig.add_subplot(1,1,1, projection ='3d')

#Giving the plot a title is done by 'ax.set_title()'
ax.set_title("Scatter Plot Title",color='cyan')


#Use '.scatter' to create the scatterplot
ax.scatter(X,Y,Z, c='blue',marker='x')

#Naming the axis is done with 'ax.set_' instead of plt.xlabel because plt only does 2d
ax.set_ylabel('Y-axis',color='red')
ax.set_xlabel("X-axis",color='orange')
ax.set_zlabel('Z-axis',color='green')
plt.show()
