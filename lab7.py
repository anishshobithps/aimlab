import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture
from sklearn.cluster import KMeans

data = pd.read_csv('datasets/7.csv')
X = np.array(data[['x1', 'x2']])

plt.scatter(X[:, 0], X[:, 1], c = 'black')
plt.show()

kmeans = KMeans(n_clusters=2)
k_labels = kmeans.fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c = k_labels)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], marker='*', c='red')
plt.show()

gmm = GaussianMixture(n_components=2)
g_labels = gmm.fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c = g_labels)
plt.show()