import matplotlib.pyplot as plt
#in order: E190216, E191188, E198774, E203926, E215644, EXXXXXX1
fig1=plt.figure(1)
H1=[0.41197,0.89081,0.011852,0.46113,0.23939,0.28494,0.067697]
L1=[0.29979,0.5752,0.0073377,0.3076,0.16441,0.38794,0.13448]
y=[0.09,0.05,0.16,0.19,0.10,0.06,0.35]
plt.scatter(H1,y, linewidth=2, label='H1 detector', color='red')
plt.scatter(L1,y, linewidth=2, label='L1 detector', color='blue',marker='x')
plt.xticks()
plt.xlabel('Antenna Response')
plt.ylabel('Fractional Increase in Sensitivity')
plt.title('Fractional Increase in Sensitivity for the 50% UL \n against Antenna Response for Hanford (H1) and Livingston (L1) detectors \n NSBH Waveform')
plt.legend(loc="upper right", prop={'size':14})
plt.show()
fig2=plt.figure(2)
y=[0.16,0.14,0.18,0.16,0.12,0.12,0.22]
plt.scatter(H1,y, linewidth=2, label='H1 detector', color='red')
plt.scatter(L1,y, linewidth=2, label='L1 detector', color='blue',marker='x')
plt.xticks()
plt.xlabel('Antenna Response')
plt.ylabel('Fractional Increase in Sensitivity')
plt.title('Fractional Increase in Sensitivity for the 50% UL \n against Antenna Response for Hanford (H1) and Livingston (L1) detectors \n Adi-b Waveform')
plt.legend(loc="upper right", prop={'size':14})
plt.show()
fig3=plt.figure(3)
y=[0.14,0.09,0.15,0.21,0.19,0.11,0.25]
plt.scatter(H1,y, linewidth=2, label='H1 detector', color='red')
plt.scatter(L1,y, linewidth=2, label='L1 detector', color='blue',marker='x')
plt.xticks()
plt.xlabel('Antenna Response')
plt.ylabel('Fractional Increase in Sensitivity')
plt.title('Fractional Increase in Sensitivity for the 50% UL \n against Antenna Response for Hanford (H1) and Livingston (L1) detectors \n Adi-c Waveform')
plt.legend(loc="upper right", prop={'size':14})
plt.show()
fig4=plt.figure(4)
y=[0.23,0.16,0.18,0.26,0.22,0.15,0.28]
plt.scatter(H1,y, linewidth=2, label='H1 detector', color='red')
plt.scatter(L1,y, linewidth=2, label='L1 detector', color='blue',marker='x')
plt.xticks()
plt.xlabel('Antenna Response')
plt.ylabel('Fractional Increase in Sensitivity')
plt.title('Fractional Increase in Sensitivity for the 50% UL \n against Antenna Response for Hanford (H1) and Livingston (L1) detectors \n Adi-e Waveform')
plt.legend(loc="upper right", prop={'size':14})
plt.show()