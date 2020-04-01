import matplotlib.pyplot as plt#plotting graph
import matplotlib
import tkinter as tk
#import numpy as np
import math
import random
from matplotlib.pyplot import figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
figure(num=None, figsize=(18, 12), dpi=80, facecolor='w', edgecolor='k')


root = tk.Tk()
root.title("Problem Statement")
text1 = tk.Text(root, height=40, width=100)


text1.pack()
# declaring variables
year = 2011
year_population = 6997990000	
pop_inrease_rate = 0.012
e = 2.71828
yearlist = []
poplist = []

print("Welcome to group 4's Modelling and Simulation Project\nThe year is 2011 and the total world population is 6,997,990,000\n")




for x in range(60):

	yearlist.append(year)
	poplist.append(year_population)
	epidemic = random.uniform(0.1,0.9)
	epidemic_severity = random.uniform(0.1,1)
	world_end_disaster = random.uniform(0,1)
	print ("The population for the year " + str(year) +" is " + str(math.trunc(year_population)))
	year_population = (year_population) * e**(pop_inrease_rate)
	
	text1.insert(tk.INSERT,"The population for the year " + str(year) +" is " + str(math.trunc(year_population))+"\n")
	year = year + 1
	pop_inrease_rate = 0.012



plt.style.use("ggplot")
plt.plot(yearlist,poplist, color='green', linewidth =1)
plt.ylim(6000000000,15000000000)
plt.xlim(2010,2070)
plt.title("year and populace")
plt.xlabel("year")
plt.ylabel("total_population")
plt.grid(True)
plt.show()
root.mainloop()
