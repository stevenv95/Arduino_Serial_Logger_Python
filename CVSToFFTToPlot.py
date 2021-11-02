from scipy.signal import blackman
from scipy.fft import fft, fftfreq, fftshift
from datetime import datetime
import matplotlib.pyplot as plt
from numpy.core.function_base import linspace
import pandas as pd
import numpy as np
import csv
import scipy.fftpack
from scipy.signal.signaltools import detrend
data = pd.read_csv('data.csv')

t = data['x_value'].astype(float).values
data = data['y_value'].astype(float).values
print(data)

# Number of sample points
N = len(t)
# sample spacing
T = 1.0 / 256
x = np.linspace(0.0, N*T, N, endpoint=False)
y = data
y = detrend(y)
#y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
yf = fft(y)
xf = fftfreq(N, T)[:N//2]
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
plt.grid()
plt.show()
