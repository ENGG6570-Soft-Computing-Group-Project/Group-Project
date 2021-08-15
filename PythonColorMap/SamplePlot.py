from matplotlib import pyplot as plt
# data to be plotted
x = [0.1,0.2,0.3,0.6,0.9]
y = [16,13,7,5,1]

# plotting
plt.rcParams["figure.figsize"] = (3,3)
plt.plot(x, y, color="green", marker='o')
plt.xlabel('alpha', fontsize=18)
plt.ylabel('Convergence Epoch Num ', fontsize=16)
title = "Convergence Epoch Num vs learning rate"
plt.title(title, fontsize = 18)
plt.show()