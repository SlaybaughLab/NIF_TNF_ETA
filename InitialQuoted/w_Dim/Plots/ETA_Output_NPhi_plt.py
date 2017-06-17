#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Allow use of Tex sybols
plt.rc('text', usetex=True)

# Establish list of files to import, labels for each data set, and index
datalist = ['ETA_Output_Full_NPhi.csv']
label=['\\textbf{ETA Spectrum}']

# Initialize variables
j=0
dataX=[]
dataY=[]

# Preset data set format scheme
s=10
linewidth=['1.5','1.5','0.5','0.5']
linestyle=[':', '-', '-', '-']
dashes=[[2, 2, 2, 2],[10, 0.1], [10, 0.1], [10, 0.1]]

# Set up figure
fig = plt.figure()
#ax1 = fig.add_subplot(111)
ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.85])

# Set Line color cycle
ax1.set_color_cycle(['k', 'k', 'k', 'k'])
#ax1.set_color_cycle(['k','b','g','r','c','m','y','w'])

# Set axes	
ax1.axis([1E-3, 20, 1E-4, 5])
ax1.set_xscale('log')
ax1.set_yscale('log')

# Set axes labels and plot title.
# ax1.set_title("Plot title...")    
ax1.set_xlabel('\\textbf{Energy [MeV]}', fontsize=14)	
ax1.set_ylabel('\\textbf{Normalized Flux [n cm$^{-2}$ s$^{-1}$]}', fontsize=14)

# Set minor and major gridlines
ax1.xaxis.grid(b=True, which='major', color='0.3', linestyle='-')
ax1.yaxis.grid(b=True, which='both', color='0.3', linestyle='-')

# Loop over the list of files
for f in datalist:
	f = open(datalist[j], 'r')

	# Reset x and y data lists and index for lists
	x=[]
	y=[]
	i=0

	# Build list of x, y coord pairs from file 
	for line in f: # Iterate over the file handle
     		line = line.rstrip('\n') # Remove the newline, if any
        	row = line.split(',') # Split the line using a comma delimiter
        	x.append(row[0]) # Append first column value to X
        	y.append(row[1]) # Append second column value to y
		i+=1

	# Add data set to scatter plot
#	x=np.float64(x) # Required for scatter plots 
#	y=np.float64(y) # Required for scatter plots
#	ax1.scatter(x[:], y[:], s=s, c=c[0], marker=marker[j], label=label[j]) 

	# Add data set to line plot
 
        if j>1:
            ax1.plot(x, y, linewidth=linewidth[j], linestyle=linestyle[j], 
                dashes=dashes[j]) 
        elif j==1:
            line2=ax1.plot(x, y, linewidth=linewidth[j], linestyle=linestyle[j], 
                label=label[j], dashes=dashes[j]) [0]
        elif j==0:
            line1=ax1.plot(x, y, linewidth=linewidth[j], linestyle=linestyle[j], 
                label=label[j], dashes=dashes[j]) [0]


plt.show()
