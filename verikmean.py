import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

veriler = pd.read_csv('veri.csv')
print(veriler)

x=veriler.iloc[:,[3,4]].values
wcss=[]
kume_sayisi_listesi=range(1,11)

from sklearn.cluster import KMeans

for i in kume_sayisi_listesi:
    kmeans=KMeans(n_clusters=i, init='k-means++',max_iter=300, n_init=10, random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)

plt.plot(kume_sayisi_listesi,wcss)
plt.title('Chart To Determine The Number Of Sets')
plt.xlabel('Number Of Sets')
plt.ylabel('Within Clusters Sum Of Square (WCSS)')
plt.show()

kmeans=KMeans(n_clusters=4, init='k-means++',max_iter=300, n_init=10, random_state=0)
y_kmeans=kmeans.fit_predict(x)

plt.scatter(x[y_kmeans==0,0],x[y_kmeans==0,1],s=100,c='red',label="Set1")
plt.scatter(x[y_kmeans==1,0],x[y_kmeans==1,1],s=100,c='green',label="Set2")
plt.scatter(x[y_kmeans==2,0],x[y_kmeans==2,1],s=100,c='blue',label="Set3")
plt.scatter(x[y_kmeans==3,0],x[y_kmeans==3,1],s=100,c='magenta',label="Set4")
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=300,c='yellow',label='Centers of Clusters')
plt.title('Customer Segmentation')
plt.xlabel('Annual Income')
plt.ylabel('Expenditure Limit')
plt.legend()
plt.show()
























