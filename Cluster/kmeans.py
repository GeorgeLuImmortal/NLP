#Taken from https://datasciencelab.wordpress.com/2013/12/12/clustering-with-k-means-in-python/
# Just added plotting for 3-k cases

import numpy as np
import random
import matplotlib.pyplot as plt

def init_board(N):
    X = np.array([(random.uniform(-1, 1), random.uniform(-1, 1)) for i in range(N)])
    return X

def cluster_points(X, mu):
    clusters  = {}
    for x in X:
        bestmukey = min([(i[0], np.linalg.norm(x-mu[i[0]])) \
                    for i in enumerate(mu)], key=lambda t:t[1])[0]
        try:
            clusters[bestmukey].append(x)
        except KeyError:
            clusters[bestmukey] = [x]
    return clusters

def reevaluate_centers(mu, clusters):
    newmu = []
    keys = sorted(clusters.keys())
    for k in keys:
        newmu.append(np.mean(clusters[k], axis = 0))
    return newmu

def has_converged(mu, oldmu):
    return (set([tuple(a) for a in mu]) == set([tuple(a) for a in oldmu]))

def find_centers(X, K):
    # Initialize to K random centers
    oldmu = random.sample(X, K)
    mu = random.sample(X, K)
    while not has_converged(mu, oldmu):
        oldmu = mu
        # Assign all points in X to clusters
        clusters = cluster_points(X, mu)
        # Reevaluate centers
        mu = reevaluate_centers(oldmu, clusters)
    return(mu, clusters)

def change_coords(array):
    return list(map(list, zip(*array)))

def parse_output(data):
    clusters = data[1]
    points1 = change_coords(clusters[0])
    plt.plot(points1[0], points1[1], 'ro')
    points2 = change_coords(clusters[1])
    plt.plot(points2[0], points2[1], 'g^')
    points3 = change_coords(clusters[2])
    plt.plot(points3[0], points3[1], 'ys')
    centroids = change_coords(data[0])
    plt.plot(centroids[0], centroids[1], 'kx')
    plt.axis([-1.0, 1, -1.0, 1])
    print(centroids[0],centroids[1])
    plt.show()

#data = init_board(15)
#data = np.array([[0.5,0.5],[0.6,0.6],[-0.5,-0.5], [-0.6,-0.6],[0.124,0.124], [0.135,0.135]])
#data = np.array([[-0.75481481,-0.65939385],[ 0.9609946,-0.45210792],[ 0.03132103,-0.46177143],[-0.83049319,0.86988309],[-0.6564483,-0.62849243],[-0.74457841,-0.84889699],[ 0.52991612,0.22131933],[0.95501368,0.75731765],[-0.1588455,-0.59022394],[-0.48827274,0.4756018 ],[ 0.08457099 ,0.74903366],[ 0.15248698,-0.49186275],[-0.31785017, 0.86374679],[ 0.27915881 ,0.15606388],[ 0.65861993,0.60586763]])
data = np.array([[-0.71,-0.65],[ -0.72,-0.66],[ -0.70,-0.67],[-0.73,-0.64],[-0.74,-0.62],[ 0.52,0.22],[0.53,0.23],[0.525,0.20],[0.54,0.21],[ 0.55 ,0.26],[ 0.15,-0.49],[0.16, -0.50],[ 0.14 ,-0.48],[ 0.17,-0.47],[0.13,-0.44]])

print(data)
print(type(data))
out = find_centers(list(data), 3)

parse_output(out)