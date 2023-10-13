import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
n_samples = 400
n_features = 70
n_clusters = 80
X, _ = make_blobs(n_samples=n_samples, n_features=n_features, centers=n_clusters, 
random_state=42)
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
labels = kmeans.labels_
centers = kmeans.cluster_centers_
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.scatter(centers[:, 0], centers[:, 1], c='red', marker='x', s=200, label='Cluster Centers')
plt.legend()
plt.title('K-Means Clustering')
plt.show()