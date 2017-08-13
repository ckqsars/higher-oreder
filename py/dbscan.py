#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright @2016 R&D, CINS Inc. (cins.com)
#
# Author: chenkaiqi<ckqsars@sina.com>

import sys
sys.path.append('/home/ckqsars/anaconda2/pkgs/scikit-learn-0.17.1-np110py27_0/lib/python2.7/site-packages/')
reload(sys)
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
import numpy as np

def read_input(fd, delimiter):
    for obj in fd:
        yield obj.strip().split(delimiter)


def main(delimiter,data,out,eps, min_samples):
    stdin = sys.stdin if data is None else open(data,'rb')
    stdout = sys.stdout if out is None else open(out,'wb')
    node_id = []
    node_weight = []
    
    for obj in read_input(stdin,delimiter):
        node_id.append(obj[0])
        node_weight.append(map(float, obj[1:]))
    lenNode = len(node_weight)
    x = np.zeros((lenNode,len(node_weight[0])))
    for i in range(len(node_weight)):
        for j in range(len(node_weight[0])):
            x[i][j] = node_weight[i][j]
    #kmeans = KMeans(init='k-means++',n_clusters = 4).fit(x)
    kmeans = DBSCAN(eps,min_samples).fit(x)
    print kmeans.labels_[1],type(kmeans.labels_)
    for i in range(lenNode):
        stdout.write(str(node_id[i])+delimiter+str(kmeans.labels_[i])+'\n')
    stdout.close()
    
    
    
if __name__=="__main__":
    eps = 0.002
    min_samlpes = 3
    delimiter = ','
    # data = '../result/food_web/result_temp_4.txt'
    # out = '../result/food_web/result_temp_4_0727.txt'
    data = '../result/SVD/food_web/node_foodRu'
    out = '../result/SVD/food_web/dbscan_food_web_svdRU.txt'
    main(delimiter,data,out, eps , min_samlpes)
     
