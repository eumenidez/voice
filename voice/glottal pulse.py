import numpy as np
from Signal_Analysis.features import signal
import wave
import matplotlib.pyplot as plt

fw = wave.open('u1.wav','r')
params = fw.getparams()
#print(params)
nchannels, sampwidth, framerate, nframes = params[:4]
strData = fw.readframes(nframes)
waveData = np.fromstring(strData, dtype=np.int16)
waveData = waveData*1.0/max(abs(waveData))  # normalization
fw.close()

t = np.arange(0, nframes)*(1.0/framerate)

#plot glottal pulses
pulses=signal.get_Pulses(waveData,framerate)
plt.figure(figsize=(3.5,2.5))
plt.plot(t, waveData,label='signal')
plt.plot([0, 0],[-1, 1],color='r')
plt.plot([0.0081817, 0.0081817],[-1, 1],color='r', label='vibration cycle')
plt.plot([pulses[1], pulses[1]],[-1, 1],color='r')
plt.plot([pulses[2], pulses[2]],[-1, 1],color='r')
plt.plot([pulses[3], pulses[3]],[-1, 1],color='r')
plt.plot([pulses[4], pulses[4]],[-1, 1],color='r')
plt.plot([0.04939, 0.04939],[-1, 1],color='r')

plt.ylabel('Amplitude',fontsize=11)
plt.xlabel('Time(s)',fontsize=11)
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)
plt.tight_layout()

plt.show()


