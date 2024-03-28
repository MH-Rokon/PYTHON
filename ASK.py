import numpy as np
import matplotlib.pyplot as plt

# Binary information at transmitter
x = np.array([1, 0, 1, 0, 1, 0, 1, 0, 1])
bp = 0.000001

# Representation of transmitting binary information as digital signal
bit = np.concatenate([np.ones(100) if bit == 1 else np.zeros(100) for bit in x])
t1 = np.arange(bp / 100, 100 * len(x) * (bp / 100) + bp / 100, bp / 100)

# Binary ASK Modulation
A1 = 10
A2 = 5
br = 1 / bp
f = br * 10
t2 = np.arange(bp / 99, bp + bp/99, bp / 99)
m = np.concatenate([A1 * np.cos(2 * np.pi * f * t2) if bit == 1 else A2 * np.cos(2 * np.pi * f * t2) for bit in x])
t3 = np.arange(bp / 99, len(x) * bp, bp / 99)

# Plotting
plt.subplot(211)
plt.plot(t1, bit, linewidth=2.5)
plt.grid(True)
plt.axis([0, bp * len(x), -0.5, 1.5])
plt.ylabel("Amplitude (volt)")
plt.xlabel("Time (sec)")
plt.title("Transmitting Information as Digital Signal")

plt.subplot(212)
plt.plot(t3, m)
plt.grid(True)
plt.xlabel("Time (sec)")
plt.ylabel("Amplitude (volt)")
plt.title("Waveform for binary ASK Modulation Corresponding Binary Information")

plt.tight_layout()
plt.show()
