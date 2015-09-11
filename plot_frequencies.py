import numpy as np
from scipy.io import wavfile
from scipy.fftpack import fft
import os
import matplotlib.pyplot as plt
from pylab import plot, show, title, xlabel, ylabel, subplot

os.chdir("C:\KBAudio")
file_name = "test2.wav"

def plotSpectrum(y,fs):        
    n = len(y)
    k = np.arange(n)
    T = n/float(fs)
    
    frq = k/T  #two sides frequency range
    frq = frq[range(n/2)] #one side frequency range
    
    Y = fft(y)
    Y = Y[range(n/2)]
    
    plot(frq,abs(Y),'r')
    xlabel('Amplitude??')
    ylabel('|Y(freq)|')


fs, y = wavfile.read(file_name)

dur = float(len(y))/float(fs) #length of the audio file in seconds

Ts = 1.0/float(fs)
t = np.arange(0,dur,Ts)

subplot(2,1,1)
plot(t,y)
xlabel("Time")
ylabel("Amplitude")
subplot(2,1,2)
plotSpectrum(y,fs)
show()

#the above doesn't seem super correct
#let's try the shorter method

fs, y = wavfile.read(file_name)
n = len(y)

dur = float(n)/float(fs) #length of the audio file in seconds
step_size = 1./fs

spectrum = np.fft.rfft(y)
freqs = np.fft.rfftfreq(len(y),step_size)

plt.plot(freqs,abs(spectrum[range(n/2+1)]))

plt.plot(freqs,abs(spectrum[]))