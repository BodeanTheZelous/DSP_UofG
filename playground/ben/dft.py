#!/usr/bin/env ipython

import numpy as np
import matplotlib.pyplot as plt
import wave as wave

pi = np.pi

Ts = 0.05
fs = 1/Ts
t = np.arange(0, 10, Ts)

fl = fs/len(t)
fln = fl/fs

f1n = 0.4
f2n = 0.005*2
f1 = f1n*fs
f2 = f2n*fs

IN = np.sin(f1*2*pi*t) + np.sin(f2*2*pi*t)

plt.subplot(2, 1, 1)
plt.plot(t, IN,marker='o')

plt.xlabel("time(s)")
plt.ylabel("Amp")

plt.show()



#plt.axvline()
