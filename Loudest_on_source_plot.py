import matplotlib.pyplot as plt
#in order: E190216, E191188, E198774, E203926, E215644, EXXXXXX1
x=[93.1922,93.3278,105.118,58.0275,64.8791,84.8321,94.465] #clustered loghbayesian
y=[19.6811,15.2648,21.0836,17.9226,19.6857,16.5495,17.4806] #unclustered loghbayesian
plt.scatter(x,y, marker='x')
plt.xlabel('Clustered value')
plt.ylabel('Unclustered value')
plt.title('Loudest dummy on-source event for clustered against unclustered values\n Type of likelihood: loghbayesian \n In order GRBs: E190216, E191188, E198774, E203926, E215644, EXXXXXX1')
plt.grid()
plt.show()
