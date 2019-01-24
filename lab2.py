import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

counts_num = 10000
mu = 0
sigma = 0.25

# generate data
y = np.random.normal(mu, sigma, size=counts_num)
x = np.linspace(0, 0.1, counts_num)
# save data to csv
np.savetxt('14_noise.csv', y, delimiter=',')

# plot
plt.figure(figsize=(15, 10), dpi=300)
plt.plot(x[::10], y[::10], color='g', linewidth=0.5)
plt.title('Noise (10%)')
plt.ylabel('Amplitude, V')
plt.xlabel('Time, sec')
plt.savefig('1.png')
plt.clf()


counter = Counter(y)
expected = 0
for i in y:
    expected += i*counter.get(i)/counts_num
#
var = 0
for i in y:
    var += pow(i - expected, 2) * counter.get(i) / counts_num
print("Expected value = \t\t"+str(expected))
print("Sample variance = \t"+str(var))
