#!/usr/bin/python
import matplotlib.pyplot as plt
#in order: clustering window dt15-df15, prf5, sqrt(prf5), (prf5)^2
#plotted against unclustered results

fig=plt.figure(figsize=(15,10))
#bns waveform
d01= ((1/0.473095*10)) #unclustered value
scale1 = [0.443251,0.356649,0.448163,0.343993]
d1= [(1/a)*10 for a in scale1]  #values with prefactors
f=[i/d01 for i in d1]
plt.scatter(range (1, len(d1)+1), f, color='b')
plt.plot(range (1, len(d1)+1), f, linewidth=2, label='bns')

#sgc100 waveform
d01 = 1.68939
scale3=[1.59094,1.89811,1.79035,2.15523] #values with prefactors
g=[d01/i for i in scale3]
plt.scatter(range (1, len(scale3)+1), g, color='g')
plt.plot(range (1, len(scale3)+1), g, linewidth=2,label='sgc100')
#sgc300 waveform
d01 = 1.63296
scale5=[1.47666,1.87441,1.70946,2.08005] #values with prefactors
h=[d01/i for i in scale5]
plt.scatter(range (1, len(scale5)+1), h, color='r')
plt.plot(range (1, len(scale5)+1), h, linewidth=2,label='sgc300')

#adi-e waveform
d01 = (1./0.315264)*10. #unclustered value
scale7=[0.27014,0.248924,0.26979,0.24805]
d7= [(1/a)*10 for a in scale7]  #values with prefactors
j=[i/d01 for i in d7]
plt.scatter(range (1, len(d7)+1), j, color='cyan')
plt.plot(range (1, len(d7)+1), j, linewidth=2,label='adi-e')

#adi-b waveform
d02= ((1/0.264092)*20) #unclustered value
scale2=[0.246137,0.215717,0.24498,0.215718]
d2= [(1/a)*20 for a in scale2]  #values with prefactors
k=[i/d02 for i in d2]
plt.scatter(range (1, len(d2)+1), k, color='magenta')
plt.plot(range (1, len(d2)+1), k,linewidth=2,label='adi-b')

#adi-c waveform
d02= ((1/0.331693)*10) #unclustered value
scale2=[0.287922,0.264255,0.286525,0.262568]
d2= [(1/a)*10 for a in scale2]  #values with prefactors
k=[i/d02 for i in d2]
plt.scatter(range (1, len(d2)+1), k, color='yellow')
plt.plot(range (1, len(d2)+1), k,linewidth=2,label='adi-c')

#nsbh waveform
d02 = (1./0.332845)*20. #unclustered value
scale4=[0.315666,0.244804,0.317306,0.236154]
d4= [(1/a)*20 for a in scale4]  #values with prefactors
l=[i/d02 for i in d4]
plt.scatter(range (1, len(d4)+1), l, color='k')
plt.plot(range (1, len(d4)+1), l, linewidth=2,label='nsbh')

#adi-d waveform
d02= ((1/0.897992*10)) #unclustered value
scale9=[0.820475,0.75237,0.814261,0.745788]
d9= [(1/a)*10 for a in scale9]  #values with prefactors
z=[i/d02 for i in d9]
plt.scatter(range (1, len(d9)+1), z, color='goldenrod')
plt.plot(range (1, len(d9)+1), z,linewidth=2,label='adi-d', color='goldenrod')

#adi-a waveform
d02= ((1/0.459766)*10) #unclustered value
scale6=[0.40375,0.370457,0.39703,0.368945]
d6= [(1/a)*10 for a in scale6]  #values with prefactors
p=[i/d02 for i in d6]
plt.scatter(range (1, len(d6)+1), p, color='lightcoral')
plt.plot(range (1, len(d6)+1), p,linewidth=2,label='adi-a', color='lightcoral')


plt.xlabel('In order: clustering window dt15-df15, prf5, sqrt(prf5), (prf5)^2')
#plt.yticks([0.2, 0.3, 0.5, 1, 1.1, 1.5, 1.6, 2, 2.5, 2.8, 3, 3.6, 4])
#plt.yticks([0.281,0.282, 0.288, 0.292, 0.295, 0.304, 1.003, 1.0, 1.029, 1.513, 1.522, 1.659,2.856, 2.860, 2.869, 3.58, 3.604,3.663])
plt.ylabel('Ratio values with prefactors over unclustered values')
plt.title('Clustering Window study:\nphysical WFs ratio prefactor/unclustered and sgc WFs ratio hrss unclustered/prefactor at 50% eff\nClustering Window (dt-df): 15-15 and study of Prefactor 5 (linear, square root, squared)')
plt.legend(loc=3, prop={'size':14})
plt.grid()
plt.show()