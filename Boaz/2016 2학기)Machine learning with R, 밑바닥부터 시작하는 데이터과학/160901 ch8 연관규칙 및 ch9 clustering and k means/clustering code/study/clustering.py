#-*- coding: utf-8 -*-

from __future__ import division
from linear_algebra import squared_distance, vector_mean, distance
import math, random
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

class KMeans:
    """performs k-means clustering"""
    def __init__(self, k):
        self.k = k          # 군집의 개수
        self.means = None   # 군집의 중심
       
    def classify(self, input):
        """입력 데이터에 가장 인접한 군집의 인덱스를 반환"""
        return min(range(self.k), #k개의 array 생성
                   key=lambda i: squared_distance(input, self.means[i])) #유클리드 거리 구하기
                  
    def train(self, inputs):
        self.means = random.sample(inputs, self.k) #임의의 k개 점을 중심점으로 선택. list
        assignments = None
        
        while True:
            # 소속되는 군집을 반복적으로 찾기
            new_assignments = map(self.classify, inputs)
            # 소속되는 군집이 바뀌지 않았다면 종료
            if assignments == new_assignments:               
                return
            # 아니라면 새로운 군집을 찾기
            assignments = new_assignments   
            for i in range(self.k):
                # 군집 i에 속하는 모든 데이터 탐색
                i_points = [p for p, a in zip(inputs, assignments) if a == i]
                # 0으로 나누는 일이 없도록 i_points가 비어 있지 않는지 확인
                if i_points:                               
                    self.means[i] = vector_mean(i_points)   
                    
def squared_clustering_errors(inputs, k):
    #inputs에 대해 k-means 군집화 실행하고 총 오류 제곱 값을 계산
    clusterer = KMeans(k)
    clusterer.train(inputs)
    means = clusterer.means
    assignments = map(clusterer.classify, inputs)
   
    return sum(squared_distance(input,means[cluster])
               for input, cluster in zip(inputs, assignments))

def plot_squared_clustering_errors(plt):
    ks = range(1, len(inputs) + 1)
    errors = [squared_clustering_errors(inputs, k) for k in ks]
    plt.plot(ks, errors)
    plt.xticks(ks)
    plt.xlabel("k")
    plt.ylabel("total squared error")
    plt.show()
#
# using clustering to recolor an image
#
def recolor_image(input_file, k, path_to_png_file):
    img = mpimg.imread(path_to_png_file)
    pixels = [pixel for row in img for pixel in row]

    clusterer = KMeans(k)
    """
    clusterer.train(pixels) # 이 부분이 엄청 오래 걸릴 수 있다
    def recolor(pixel):
        cluster = clusterer.classify(pixel) # 가장 가까운 군집의 인덱스
        return clusterer.means[cluster]     # 가장 가까운 군집의 중심값
    new_img = [[recolor(pixel) for pixel in row] # 해당 픽셀 행을 다시 칠함
               for row in img] # 이미지의 모든 행에 대해
    plt.imshow(new_img)
    plt.axis('off')
    plt.show()"""