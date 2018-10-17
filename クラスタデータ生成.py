import numpy as np
import matplotlib.pyplot as plt

dimension=20
mu=np.array([2.0 for i in range(dimension)])

for i in range(10,dimension,1):
       mu[i]=2.0

conv=np.zeros((dimension,dimension))

for i in range(dimension):
    conv[i,i]=2

box=[]
for i in range(2*10**2):
    hoge=np.random.multivariate_normal(mu,conv)
    hoge=list(hoge)
    box.append(hoge)
box=np.array(box)

plt.scatter(box[:,0],box[:,1])
plt.show()

#np.savetxt("make1.csv",box,delimiter=',') #mu 0~9:2.0 10~:4.0
#np.savetxt("make2.csv",box,delimiter=',') #mu 0~9:4.0 10~:2.0
#np.savetxt("make3.csv",box,delimiter=',') #mu 0~:2.0
#np.savetxt("make2_1.csv",box,delimiter=',') #mu 0~9:2.0 10~:4.0
#np.savetxt("make2_2.csv",box,delimiter=',') #mu 0~9:4.0 10~:2.0
#np.savetxt("make2_3.csv",box,delimiter=',') #mu 0~:2.0
