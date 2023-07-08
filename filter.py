
import matplotlib.pyplot as plt
import numpy as np
from IIR2Filter import IIR2Filter

GAZE_CSV = "../20220715_mainMsSeki/gaze.csv"

gaze_xs = np.loadtxt(GAZE_CSV, usecols=[1], skiprows=1, delimiter=",")
gaze_ys = np.loadtxt(GAZE_CSV, usecols=[2], skiprows=1, delimiter=",")
N = len(gaze_xs)
dt = 0.04
t = np.arange(0, N * dt, dt)

plt.figure("gaze x")
plt.plot(t, gaze_xs)
plt.figure("gaze y")
plt.plot(t, gaze_ys)

fs = 200

# freqx = np.linspace(0, 1.0/dt, N)
# Fx = np.fft.fft(gaze_xs)
# Fx = Fx / (N/2)
# Fx[0] = Fx[0] / 2
# plt.figure("fft x")
# plt.plot(freqx, np.abs(Fx))

# FilterMains = IIR2Filter(3, [20,80], 'bandpass', design='butter', fs=200)
FilterX = IIR2Filter(10, [40, 60], 'bandpass', design='butter', fs=200)
FilterY = IIR2Filter(10, [40, 60], 'bandpass', design='butter', fs=200)

for i, gaze_x in enumerate(gaze_xs):
    gaze_xs[i] = FilterX.filter(gaze_x)
for i, gaze_y in enumerate(gaze_ys):
    gaze_ys[i] = FilterY.filter(gaze_y)

gaze_xs = np.abs(gaze_xs)
gaze_ys = np.abs(gaze_ys)

for i, gaze_x in enumerate(gaze_xs):
    with open("./smoothed_gaze.csv", "a") as f:
        np.savetxt(f, np.array([[i+1, gaze_x, gaze_ys[i]]]), delimiter=",")
# Fx = np.fft.fft(gaze_xs)
# Fx = Fx / (N/2)
# Fx[0] = Fx[0] / 2
# plt.figure("fft x_after")
# plt.plot(freqx, np.abs(Fx))

plt.figure("filtered gaze_x")
plt.plot(gaze_xs)
plt.figure("filtered gaze_y")
plt.plot(gaze_ys)
plt.show()

# --/--/--/--/--/--/--/--/--/--/--/--/--

impulse = np.zeros(1000)
impulse[0] = 1
impulseResponse = np.zeros(len(impulse))

for i in range(len(impulse)):
    impulseResponse[i] = FilterX.filter(impulse[i])

freqResponse = np.fft.fft(impulseResponse)
freqResponse = abs(freqResponse[0:int(len(freqResponse)/2)])
xfF = np.linspace(0, fs/2, len(freqResponse))

plt.figure("Frequency_Response")
plt.plot(xfF,np.real(freqResponse))
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude")
plt.title("lowpass")
plt.show()
