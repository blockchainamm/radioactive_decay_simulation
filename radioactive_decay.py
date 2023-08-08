# Simulation of radioactive istope decay

# import required packages
import numpy as np
import matplotlib.pyplot as plt

# Number of radioactive isotopes
N = 1000000
M = 1000000
counts = [N]
counts1 = [M]

while N > 100 and M > 100:
    probability = np.random.random(N)
    prob = np.random.random(M)
    for p in probability:
        # when probability of occurance > 90%
        if p > 0.9:
            N = N-1
    for pr in prob:
        # when probability of occurance > 80%
        if pr > 0.8:
            M = M-1
    counts.append(N)
    counts1.append(M)

# logarithmic scale
plt.yscale('log')
plt.xscale('log')

# plot the list of radiactive istopes vs decay rate based on probability of occurance
plt.plot(counts)
plt.plot(counts1)

# set x-axis limit
plt.xlim(0, 110)

# set x-axis label
plt.xlabel('Decay rate %')

# set y-axis label
plt.ylabel('Number of radioactive isotopes')

# plot in grid layout
plt.grid(True)

# display plot
plt.show()