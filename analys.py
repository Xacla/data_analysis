from sklearn import decomposition
from sklearn import manifold
import numpy as np
import matplotlib.pyplot as plt
flag=3
if flag==0:
    data1=np.loadtxt('make1.csv',delimiter=",")
    data2=np.loadtxt('make2.csv',delimiter=',')
    #data3=np.loadtxt('make3.csv',delimiter=',')
elif flag==1:
    data1=np.loadtxt('make2_1.csv',delimiter=",")
    data2=np.loadtxt('make2_2.csv',delimiter=',')
    data3=np.loadtxt('make2_3.csv',delimiter=',')
elif flag==2 :
    data1=np.loadtxt('人工データ/rondom_make1.csv',delimiter=",")
    data2=np.loadtxt('人工データ/rondom_make2.csv',delimiter=',')
    data3=np.loadtxt('人工データ/rondom_make3.csv',delimiter=',')
    data4=np.loadtxt('人工データ/rondom_make4.csv',delimiter=',')
    data=np.vstack((data1,data2,data3,data4))
elif flag==3 :
    data1=np.loadtxt('人工データ/ガウシアン分布/gausian_make1.csv',delimiter=",")
    data2=np.loadtxt('人工データ/ガウシアン分布/gausian_make2.csv',delimiter=',')
    data3=np.loadtxt('人工データ/ガウシアン分布/gausian_make3.csv',delimiter=',')
    data4=np.loadtxt('人工データ/ガウシアン分布/gausian_make4.csv',delimiter=',')
    data=np.vstack((data1,data2,data3,data4))
    #data=np.vstack((data3,data4))
#print(data1.shape,data2.shape)
#data=np.vstack((data1,data2,data3))
#data=np.vstack((data1,data2))


tsne=manifold.TSNE(perplexity=5,init='pca',learning_rate=100,early_exaggeration=10,n_iter=10000)
result=tsne.fit_transform(data)

#pca=decomposition.PCA()
#result=pca.fit_transform(data)
'''
for i in range(200):
    if result[200+i,0]<0:
        print(data2[i,:])
'''
plt.scatter(result[0:200,0],result[0:200,1],c='r')
plt.scatter(result[200:400,0],result[200:400,1],c='g')
plt.scatter(result[400:600,0],result[400:600,1],c='y')
plt.scatter(result[600:800,0],result[600:800,1],c='w')
plt.show()
