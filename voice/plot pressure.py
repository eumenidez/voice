import numpy
import matplotlib.pyplot as plt

a = numpy.loadtxt('pressure1.txt')
#a = numpy.loadtxt('2.txt')
#x=a[:,0]

x=numpy.arange(1491)
y=a[:,1]

fig,ax=plt.subplots(figsize=(5.5,3))
ax.plot(x, y, '-', label='original pressure signal')

plt.xticks([31, 102, 235, 328, 390, 462, 582, 806, 877,
            986, 1087, 1158, 1208, 1293, 1373],[0.025, '0.100', '0.250', 0.365, '0.450', '0.540', '0.680',
     0.939, 1.024, '1.150', '1.270', '1.350', 1.408, 1.507, '1.600'])

ax.tick_params(axis='x', rotation=50)

c='forestgreen'
plt.plot([31,31],[-5,29.967],':',color=c, label='time stamp')
plt.plot([102,102],[-5,1.3],':',color=c)
plt.plot([235,235],[-5,7.283],':',color=c)
plt.plot([328,328],[-5,0.383],':',color=c)
plt.plot([390,390],[-5,1.55],':',color=c)
plt.plot([462,462],[-5,3.85],':',color=c)
plt.plot([582,582],[-5,0.083],':',color=c)
plt.plot([806,806],[-5,28.317],':',color=c)
plt.plot([877,877],[-5,2.4],':',color=c)
plt.plot([986,986],[-5,4.883],':',color=c)
plt.plot([1087,1087],[-5,0.233],':',color=c)
plt.plot([1158,1158],[-5,6.25],':',color=c)
plt.plot([1208,1208],[-5,66.217],':',color=c)
plt.plot([1293,1293],[-5, 0.417],':',color=c)
plt.plot([1373,1373],[-5,0.05],':',color=c)

ax.plot([31, 102, 235, 328, 390, 462, 582, 806, 877,
            986, 1087, 1158, 1208, 1293, 1373],[29.967, 1.3, 7.283, 0.383, 1.55, 3.85,
                                                0.083, 28.317, 2.4, 4.883, 0.233, 6.25,
                                                66.217, 0.417, 0.05],'o',color='r', label='sampled data point')

ax.plot([31, 102, 235, 328, 390, 462, 582, 806, 877,
            986, 1087, 1158, 1208, 1293, 1373],[29.967, 1.3, 7.283, 0.383, 1.55, 3.85,
                                                0.083, 28.317, 2.4, 4.883, 0.233, 6.25,
                                                66.217, 0.417, 0.05],'-',color='r',label='reconstructed pressure signal')

plt.ylim(-5,70)
plt.ylabel('Differential Pressure (Pa)', fontsize=11)
plt.xlabel('Time(s)',fontsize=11)
plt.legend()
plt.tight_layout()
plt.show()
