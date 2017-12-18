import matplotlib.pyplot as plt
import numpy as np
#in order: E190216, E191188, E198774, E203926, E215644, EXXXXXX1
x=[0.000417,14.4318883033,5.89151084188,0.000528,5.85336655268,8.01145429994,0.030000]
y=[0.09,0.05,0.16,0.19,0.10,0.06,0.35] #nsbh
z=[0.23,0.16,0.18,0.26,0.22,0.15,0.28] #adi-e
w=[0.14,0.09,0.15,0.21,0.19,0.11,0.25] #adi-c
k=[0.13,0.05,0.14,0.15,0.15,0.07,0.33] #bns
plt.scatter(x,y, linewidth=2, label='nsbh waveform', color='red')
plt.scatter(x,z, linewidth=2, label='adi-e waveform', color='blue',marker='x')
plt.scatter(x,w, linewidth=2, label='adi-c waveform', color='green',marker='v')
plt.scatter(x,k, linewidth=2, label='bns waveform', color='black')
fit = np.polyfit(x,z,1)
plt.plot(x,np.poly1d(fit)(x))
fit = np.polyfit(x,y,1)
plt.plot(x,np.poly1d(fit)(x), color='red')
fit = np.polyfit(x,w,1)
plt.plot(x,np.poly1d(fit)(x),color='green')
fit = np.polyfit(x,k,1)
plt.plot(x,np.poly1d(fit)(x),color='black')
plt.xlabel('Sky Position Error')
plt.ylabel('Fractional Increase in Sensitivity')
plt.title('Fractional Increase in Sensitivity for the 50% UL \n against Sky position error(degree) \n NSBH, Adi-e, Adi-c and BNS Waveforms')
plt.legend(loc="upper right", prop={'size':14})
plt.grid()
plt.show()


