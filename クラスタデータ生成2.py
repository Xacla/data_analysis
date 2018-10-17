#ランダムに生成する
import numpy as np
import matplotlib.pyplot as plt
import random as rand

flag=4
dimension=20
if flag==1:
    mu=1
    min_num=2
    max_num=4
elif flag==2:
    mu=4
    min_num=1
    max_num=3
elif flag==3:
    mu=2
    min_num=1
    max_num=4
elif flag==4:
    mu=3
    min_num=1
    max_num=4


box=[]
for i in range(2*10**2):
    hoge=np.zeros(dimension)
    for j in range(dimension):
        if j>=10:
                hoge[j]=float(int(rand.uniform(1,5)))
        elif rand.uniform(0,1)<0.75 and j<10:
            hoge[j]=mu
        else:
            hoge[j]=mu+0.5
            if flag==3 or flag==4:
                while mu<=hoge[j] and mu+1>hoge[j]:
                    hoge[j]=float(int(rand.uniform(1,5)))
            else:
                hoge[j]=float(int(rand.uniform(min_num,max_num)))
    box.append(hoge)
box=np.array(box)

plt.scatter(box[:,0],box[:,1])
#plt.show()

if flag==1:
    np.savetxt("人工データ/rondom_make1.csv",box,delimiter=',') #mu 0~9:1.0
elif flag==2:
    np.savetxt("人工データ/rondom_make2.csv",box,delimiter=',') #mu 0~9:4.0
elif flag==3:
    np.savetxt("人工データ/rondom_make3.csv",box,delimiter=',') #mu 0~9:2.0
elif flag==4:
    np.savetxt("人工データ/rondom_make4.csv",box,delimiter=',') #mu 0~9:2.0
