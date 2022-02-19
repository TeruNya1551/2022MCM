#=============================================================================
# Name        : Harbin.py
# Description : Draw the line chart of Harbin's annual average temperature
#=============================================================================

import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('C:\\Users\\Repen\\Desktop\\Harbin.txt')

# plt.rcParams['lines.linewidth'] = 2
# plt.rcParams['figure.figsize'] = (12.0, 6.0) #inches
# plt.plot(data[:,0],data[:,1])

# linear_model=np.polyfit(data[:,0],data[:,1],1)
# linear_model_fn=np.poly1d(linear_model)
# x_s=np.arange(1961,2010)
# plt.plot(x_s,linear_model_fn(x_s),color="green")

# plt.show()

print(np.mean(data[:,1]))
print(np.var(data[:,1]))