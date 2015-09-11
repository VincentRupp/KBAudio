import numpy as np
import matplotlib.pyplot as plt

A = .8
f = 1000  #1000 Hz
phi = np.pi/2  #initial phase at time zero
fs = 44100
t = np.arange(-.002,.002,1.0/fs) #.004 seconds total length
x = A * np.cos(2*np.pi*f*t+phi)
plt.plot(t,x)

