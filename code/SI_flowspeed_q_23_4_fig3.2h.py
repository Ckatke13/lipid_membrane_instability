#This code plots the flow speed profile in the lipid membrane at different times(t =0, 0.00035 and 0.0005s/0, 350 and 500 in dimensionless time)for q = q_c = (3/\beta)^(1/4).
#To obtain the flow speed profile, the "velocity.pvd" generated from solving the equation(linear_instabilities_q_23_4_cos.py) which stores the data for the dimensionless flow speed was loaded into Paraview. 
#Then using the calculator filter,flow speed in real units was calculated using the formula v = U_0*v (units = micrometer/s). Here U_0(10 micrometer/sec) is the velocity scale.
#Each ".csv" file containing the data for the flow speed over the entire domain corrsponding to particular time instant is generated by visualizing calculated flow speed in previous step in the spreadsheet view



import matplotlib.pyplot as plt
import numpy as np

x1, y1 = np.loadtxt('flowspeed_q_23_4_t_0.csv', delimiter=',', unpack=True)
x2, y2 = np.loadtxt('flowspeed_q_23_4_t_350.csv', delimiter=',', unpack=True)
x3, y3 = np.loadtxt('flowspeed_q_23_4_t_500.csv', delimiter=',', unpack=True)

plt.figure(figsize=(6.68,3.01))
ax = plt.subplot(111)

#axis linewidth
for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(2)

#plotting
ax.plot(x1,y1,linewidth = 4,color='0.1')
ax.plot(x2,y2,linewidth = 4,color='0.6')
ax.plot(x3,y3,linewidth = 4,color='0.8')

#tick parameters
ax.tick_params(axis="x", direction = "in", length=10, width=2, labelsize=19)
ax.tick_params(axis="y", direction = "in", length=10, width=2, labelcolor="white")

#tick labels
ax.xaxis.set_ticks(np.arange(0.,1.1,0.5))
ax.yaxis.set_ticks(np.arange(-10,10.1,10))

#axes labels
csfont = {'fontname':'Calibri'}


# Hide the right and top spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Only show ticks on the left and bottom spines
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')

#axis range
plt.xlim([0,1])
plt.ylim([-10.5,10])



plt.savefig('SI_flowspeed_23_4.eps', format='eps', dpi = 300)
