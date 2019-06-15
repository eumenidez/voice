import wave
import pylab as pl
import numpy as np
import math
# ============ test the algorithm =============
# read wave file and get parameters.
fw = wave.open('something.wav','r')
params = fw.getparams()
print(params)
nchannels, sampwidth, framerate, nframes = params[:4]
strData = fw.readframes(nframes)
waveData = np.fromstring(strData, dtype=np.int16)
waveData = waveData*1.0/max(abs(waveData))  # normalization
fw.close()

def calVolume(waveData, frameSize, overLap):
    wlen = len(waveData)
    step = frameSize - overLap
    frameNum = int(math.ceil(wlen*1.0/step))
    volume = np.zeros((frameNum,1))
    for i in range(frameNum):
        curFrame = waveData[np.arange(i*step,min(i*step+frameSize,wlen))]
        curFrame = curFrame - np.median(curFrame) # zero-justified
        volume[i] = np.sum(np.abs(curFrame))
    return volume

# method 2: 10 times log10 of square sum
def calVolumeDB(waveData, frameSize, overLap):
    wlen = len(waveData)
    step = frameSize - overLap
    frameNum = int(math.ceil(wlen*1.0/step))
    volume = np.zeros((frameNum,1))
    for i in range(frameNum):
        curFrame = waveData[np.arange(i*step,min(i*step+frameSize,wlen))]
        curFrame = curFrame - np.mean(curFrame) # zero-justified
        volume[i] = 10*np.log10(np.sum(curFrame*curFrame))
    return volume


# calculate volume
frameSize = 256
overLap = 128
volume11 = calVolume(waveData,frameSize,overLap)
volume12 = calVolumeDB(waveData,frameSize,overLap)

# plot the wave
time = np.arange(0, nframes)*(1.0/framerate)
time2 = np.arange(0, len(volume11))*(frameSize-overLap)*1.0/framerate
pl.figure(figsize=(6,2.5))
pl.ylim((-20,20))
pl.yticks(np.arange(-20,20,10),('20','30','40','50','60','70'))
pl.xticks([0.025, 0.100, 0.250, 0.365, 0.450, 0.540, 0.680,
     0.939, 1.024, 1.150, 1.270, 1.350, 1.408, 1.507, 1.600],[0.025, '0.100', '0.250', 0.365, '0.450', '0.540', '0.680',
     0.939, 1.024, '1.150', '1.270', '1.350', 1.408, 1.507, '1.600'])
pl.tick_params(axis='x', rotation=50)


#pl.plot(time2, volume12, c="g")
pl.plot(time2, volume12)
pl.ylabel("Sound Power Level(dB)",fontsize=11)
pl.xlabel("Time(s)",fontsize=11)
pl.tight_layout()
pl.show()
