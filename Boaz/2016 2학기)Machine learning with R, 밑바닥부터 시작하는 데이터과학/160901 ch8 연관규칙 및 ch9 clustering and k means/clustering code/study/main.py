#-*- coding: utf-8 -*-
from clustering import KMeans
import random
from clustering import squared_clustering_errors
from clustering import *
import matplotlib.pyplot as plt

data = [[-14,-5],[13,13],[20,23],[-19,-11],[-9,-16],[21,27],[-49,15],[26,13],
        [-46,5],[-34,-1],[11,15],[-49,0],[-22,-16],[19,28],[-12,-8],[-13,-19],
        [-41,8],[-11,-6],[-25,-9],[-18,-3]] #20개


"""
#1 MEETSUP
#random.seed(0)
clusterer = KMeans(3)
clusterer.train(data)
print clusterer.means"""


"""
#2 Choosing K
ks = range(1, len(data)+1)
errors = [squared_clustering_errors(data, k) for k in ks]

plt.plot(ks, errors)
plt.xticks(ks)
plt.xlabel("k")
plt.ylabel("total squared error")
plt.title("Total Error vs # of Clusters")
plt.show()"""


#3 IMAGE KMEANS
path_to_png_file = "D:\example_image.png"

recolor_image(data, 5, path_to_png_file)