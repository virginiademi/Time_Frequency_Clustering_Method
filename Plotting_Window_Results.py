import matplotlib.pyplot as plt
#clustering windows: 0.1-0.5; 0.1-5; 0.2-5; 0.5-5; 1-5; 2-5; 5-5; (10-10;15-15)

fig=plt.figure(figsize=(15,10))

#bns waveform
d01= ((1/0.473095)*10) #unclustered value
scale1=[0.471225, 0.470605, 0.471841, 0.473095, 0.469354, 0.4642, 0.459568,0.449939,0.443251,0.454403]
d1= [(1/a)*10 for a in scale1]  #clustered values
f=[i/d01 for i in d1]
plt.scatter(range (1, len(d1)+1), f, color='b')
plt.plot(range (1, len(d1)+1), f, linewidth=2, label='bns')

#sgc100 waveform
d01 = 1.68939
scale3=[1.67969, 1.6741,1.67269,1.67057,1.64952,1.64266,1.63957,1.6197,1.59094,1.57411] #clustered values
g=[d01/i for i in scale3]
plt.scatter(range (1, len(scale3)+1), g, color='g')
plt.plot(range (1, len(scale3)+1), g, linewidth=2,label='sgc100')
#sgc300 waveform
d01 = 1.63296
scale5=[1.61474,1.61276,1.6063,1.60174,1.5782,1.56645,1.55374,1.51093,1.47666, 1.48678] #clustered values
h=[d01/i for i in scale5]
plt.scatter(range (1, len(scale5)+1), h, color='r')
plt.plot(range (1, len(scale5)+1), h, linewidth=2,label='sgc300')

#adi-e waveform
d01 = (1./0.315264)*10. #unclustered value
scale7=[0.312529,0.31122,0.310771,0.312058,0.310234,0.300668,0.285139,0.271709,0.27014,0.26815]
d7= [(1/a)*10 for a in scale7]  #clustered values
j=[i/d01 for i in d7]
plt.scatter(range (1, len(d7)+1), j, color='cyan')
plt.plot(range (1, len(d7)+1), j, linewidth=2,label='adi-e')

#adi-b waveform
d02= ((1/0.264092)*20) #unclustered value
scale2=[0.263958,0.263704,0.263567,0.262492,0.260431,0.258927,0.25827,0.251407,0.246137,0.248097]
d2= [(1/a)*20 for a in scale2]  #clustered values
k=[i/d02 for i in d2]
plt.scatter(range (1, len(d2)+1), k, color='magenta')
plt.plot(range (1, len(d2)+1), k,linewidth=2,label='adi-b')

#adi-c waveform
d02= ((1/0.331693)*10) #unclustered value
scale2=[0.330539, 0.330539, 0.330539, 0.330958, 0.330587, 0.317071, 0.305751,0.291868,0.287922,0.285818]
d2= [(1/a)*10 for a in scale2]  #clustered values
k=[i/d02 for i in d2]
plt.scatter(range (1, len(d2)+1), k, color='yellow')
plt.plot(range (1, len(d2)+1), k,linewidth=2,label='adi-c')

#nsbh waveform
d02 = (1./0.332845)*20. #unclustered value
scale4=[0.331263,0.334105,0.334262,0.331884,0.330778,0.329735,0.329735,0.320141,0.315666,0.323261]
d4= [(1/a)*20 for a in scale4]  #clustered values
l=[i/d02 for i in d4]
plt.scatter(range (1, len(d4)+1), l, color='k')
plt.plot(range (1, len(d4)+1), l, linewidth=2,label='nsbh')

#adi-d waveform
d02= ((1/0.897992)*10) #unclustered value
scale9=[0.897523,0.89676,0.896153,0.900335,0.898467,0.867435,0.848094,0.825823,0.820475,0.808799]
d9= [(1/a)*10 for a in scale9]  #clustered values
z=[i/d02 for i in d9]
plt.scatter(range (1, len(d9)+1), z, color='goldenrod')
plt.plot(range (1, len(d9)+1), z,linewidth=2,label='adi-d', color='goldenrod')

#adi-a waveform
d02= ((1/0.459766)*10) #unclustered value
scale6=[0.457878,0.453117,0.453079,0.454267,0.451207,0.436499,0.421952,0.406447,0.40375,0.400663]
d6= [(1/a)*10 for a in scale6]  #clustered values
p=[i/d02 for i in d6]
plt.scatter(range (1, len(d6)+1), p, color='lightcoral')
plt.plot(range (1, len(d6)+1), p,linewidth=2,label='adi-a', color='lightcoral')


plt.xlabel('Clustering Windows')
#plt.yticks([0.2, 0.3, 0.5, 1, 1.1, 1.5, 1.6, 2, 2.5, 2.8, 3, 3.6, 4])
#plt.yticks([0.281,0.282, 0.288, 0.292, 0.295, 0.304, 1.003, 1.0, 1.029, 1.513, 1.522, 1.659,2.856, 2.860, 2.869, 3.58, 3.604,3.663])
plt.ylabel('Ratio Clustered over Unclustered values')
plt.title('Clustering window study:\nphysical WFs ratio clust/unclust and sgc WFs ratio hrss unclust/clust at 50% eff\nWindows (dt-df): 0.1-0.5; 0.1-5; 0.2-5; 0.5-5; 1-5; 2-5; 5-5; 10-10; 15-15; 20-20')
plt.legend(loc="center left", prop={'size':14})
plt.grid()
plt.show()



