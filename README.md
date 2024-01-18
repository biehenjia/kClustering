# kClustering
A list of various clustering algorithms built from scratch. 
# kMeans
kMeans clustering is a machine learning algorithm that aims to minimize the following expression, where $k$ is the number of clusters, $c_{i}$ represents each cluster, and $C_i$ represents the centroid representing cluster $c_{i}$
```math
$$\sum\limits^k_{i=1}\sum\limits^{|c_{i}|}_{j=1}|c_{i}[j]-C_{i}|^{2}$$
```
This algorithm works by attributing a set of points to a cluster $c$, calculating the _variance_ of the cluster, i.e., the squared distance of each one of the points and the centroid, and shifting the cluster to incorporate points that have lesser _variance_ against the centroid. 

Here is a visualisation of the algorithm across $k=10$

![](kmeans.gif)

## Complexity analysis
The naive implementation of kMeans clustering under $2$ dimensions and $k$ clusters is $O(n^{2k+1})$. For each point among $n$ points,

# kMeans with lloyd's optimization
Lloyd's algorithm is an implementation 

# DBSCAN

