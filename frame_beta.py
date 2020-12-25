import struct
import numpy as np
import matplotlib.pyplot as plt
import pyaudio

CHUNK = 1024 * 4
FORMAT = pyaudio.paInt16
CHANNEL = 1
RATE = 44100

p=pyaudio.PyAudio()
Stream= p.open(format=FORMAT,
              rate=RATE,
              input=True,
              output=True,
              frames_per_buffer=CHUNK,
              CHANNEL=1
            )
data=Stream.read(CHUNK)
data_int=struct.unpack(str(2*CHUNK) + 'B', data) [::2] +127
data_int
fig, ax=plt.subplots()
ax.plot(data_int, '-')
plt.show()

