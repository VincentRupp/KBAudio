import numpy as np
import matplotlib.pyplot as plt

fs = 44100
step_size = 1./fs
t = np.arange(0.0,1.0,step_size)
twotone = np.sin(t*750*2*np.pi) + np.sin(t*1500*2*np.pi)

spectrum = np.fft.rfft(twotone)
freqs = np.fft.rfftfreq(len(twotone),step_size)

plt.plot(freqs,abs(spectrum))