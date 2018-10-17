#ランダムに生成する
import numpy as np
import matplotlib.pyplot as plt
import random as rand

flag=3
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
        elif flag==1:
            hoge[j]=0
            while 1>hoge[j]:
                hoge[j]=float(int(rand.gauss(mu,1)))
        elif flag==2:
            hoge[j]=5
            while 4<hoge[j]:
                hoge[j]=float(int(rand.gauss(mu,1)))
        else:
            while hoge[j]<1 or hoge[j]>4:
                hoge[j]=float(int(rand.gauss(mu,1)))
    box.append(hoge)
box=np.array(box)

plt.scatter(box[:,0],box[:,1])
#plt.show()

if flag==1:
    np.savetxt("人工データ/ガウシアン分布/gausian_make1.csv",box,delimiter=',') #mu 0~9:1.0
elif flag==2:
    np.savetxt("人工データ/ガウシアン分布/gausian_make2.csv",box,delimiter=',') #mu 0~9:4.0
elif flag==3:
    np.savetxt("人工データ/ガウシアン分布/gausian_make3.csv",box,delimiter=',') #mu 0~9:2.0
elif flag==4:
    np.savetxt("人工データ/ガウシアン分布/gausian_make4.csv",box,delimiter=',') #mu 0~9:2.0
