from scipy.io import wavfile
from scipy import signal

this_path = "C:\KBAudio"
fs, audio = wavfile.read(this_path+'audio\distorted.wav')

