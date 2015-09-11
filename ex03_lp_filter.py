import numpy as np
from scipy.io import wavfile
from scipy import signal
import os

os.chdir("C:\KBAudio")
fs, audio = wavfile.read('test2.wav')

passband = 10000. #Hz
stopband= 11000.
nyq = 0.5 * fs

order, normalized_cutoff = signal.buttord(passband/nyq, stopband/nyq, 3, 40)
b, a = signal.butter(order, normalized_cutoff, btype='low')

low_passed = np.zeros_like(audio)

low_passed[:,0] = signal.lfilter(b, a, audio[:,0])
low_passed[:,1] = signal.lfilter(b, a, audio[:,1])

wavfile.write('test2_filtered.wav', fs, low_passed)