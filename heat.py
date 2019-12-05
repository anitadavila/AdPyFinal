# importing the required modules 
import matplotlib.pyplot as plt 
import numpy as np 
from numpy import pi as pie
from matplotlib.animation import FuncAnimation


#setting up plot and data
fig, ax = plt.subplots()
x_data, y_data = [], [] #store our data
ln,= plt.plot([],[],'r') #displays our line red

#function to initialize plot dimensions
def init():
	ax.set_xlim(0,2*pie)
	ax.set_ylim(-1,1)
	return ln,
# function to update frame
def update(frame):
	x_data.append(frame)
	y_data.append(-1*(np.cos(frame)))
	ln.set_data(x_data,y_data)
	return ln,
# animation function
animate = FuncAnimation(fig, update, frames = np.linspace(0,2*pie,128), init_func = init)

plt.show()
