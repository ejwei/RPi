#matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
from numpy import *
from numpy.fft import *
from scipy.signal import argrelextrema
from scipy.io import wavfile

# Number of samplepoints
N = 1000
# sample spacing
T = 1.0 / 800.0

# Generated composite sine wave
# x = np.linspace(0.0, N*T, N)
# y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)

# Import audio file into numpy array
fs, data = wavfile.read("rectest.wav")

x = np.linspace(0,data.size/fs,data.size)
y = data 
print(x.size)
print(y.size)
print(fs)

N = x.size
T = 1/fs

yf = fft(y)
xf = np.linspace(0.0, 1.0/(2.0/fs), N/2)
# m =  argrelextrema(2.0/N * np.abs(yf[:N//2]), np.greater)
m = np.argsort(2.0/N * np.abs(yf[:N//2]))[-5:]
print(m)

print(xf[m])
print(np.abs(yf[m]))

fig, ax = plt.subplots(2)
ax[0].plot(x, y)
ax[1].semilogy(xf, 2.0/N * np.abs(yf[:N//2]))
ax[1].plot(xf[m], 2.0/N * np.abs(yf[m]), 'rs')
plt.show()