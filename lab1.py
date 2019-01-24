import numpy
import matplotlib.pyplot as plt
amplitude = 1.4
displacement = 0.5
simulation_time = 0.1
frequency = 2 * numpy.pi * 28076.17188
initial_phase = 130
sampling_frequency = 100000
number_of_samples = simulation_time * sampling_frequency
# First plot
t = numpy.linspace(0, 0.1, number_of_samples)
y = amplitude * numpy.cos(frequency * t + initial_phase * numpy.pi/180) + displacement
plt.figure(1)
print y[:3]
plt.title('Digital signal generation')
plt.xlabel('Simulation time, sec')
plt.ylabel('Signal, volt')
plt.axhline(0, color='lightgray')
plt.axvline(0, color='lightgray')
plt.plot(t,y)
plt.show()
# Second plot -> 10%
t1 = numpy.linspace(0, 0.01, number_of_samples * 0.1)
y1 = amplitude * numpy.cos(frequency * t1 + initial_phase * numpy.pi/180) + displacement
plt.figure(2)
plt.title('Digital signal generation')
plt.xlabel('Simulation time, sec')
plt.ylabel('Signal, volt')
plt.axhline(0, color='lightgray')
plt.axvline(0, color='lightgray')
plt.plot(t1, y1)
plt.show()
# Save to csv
numpy.savetxt("lab1_skok.csv", y, delimiter=",")
