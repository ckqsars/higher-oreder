#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright @2016 R&D, CINS Inc. (cins.com)
#
# Author: chenkaiqi<ckqsars@sina.com>

import sys
sys.path.append('/home/ckqsars/anaconda2/pkgs/scikit-learn-0.17.1-np110py27_0/lib/python2.7/site-packages/')
reload(sys)
from sklearn.cluster import KMeans
import numpy as np
from optparse import OptionParser

def read_input(fd, delimiter):
    for obj in fd:
        yield obj.strip().split(delimiter)


def main(delimiter,data,out):
    stdin = sys.stdin if data is None else open(data,'rb')
    stdout = sys.stdout if out is None else open(out,'wb')
    node_id = []
    node_weight = []
    
    for obj in read_input(stdin,delimiter):
        node_id.append(obj[0])

        node_weight.append(map(float,obj[1:]))
    lenNode = len(node_weight)
    x = np.zeros((lenNode,len(node_weight[0])))
    for i in range(len(node_weight)):
        for j in range(len(node_weight[0])):
            x[i][j] = node_weight[i][j]
    #kmeans = KMeans(init='k-means++',n_clusters = 4).fit(x)
    kmeans = KMeans(init='k-means++',n_clusters = 4).fit(x)
    print kmeans.labels_[1],type(kmeans.labels_)
    for i in range(lenNode):
        stdout.write(str(node_id[i])+delimiter+str(kmeans.labels_[i])+'\n')
    stdout.close()
    
    
    
if __name__ == "__main__":
    parser = OptionParser(usage="%prog -s delimiter -d data -o out")

    parser.add_option(
        "-s", "--delimiter",
        help = u"The delimiter between columns, like \t" 
    )

    parser.add_option(
        "-d", "--data",
        help = u"The file (include path) of data"
    )

    parser.add_option(
        "-o", "--out",
        help = u"The file (include path) of result"
    )

    delimiter = ','
    #data = '/home/ckqsars/workspace/high_order/result/nmf/nmf_foodweb_3.txt'
    #out = '/home/ckqsars/workspace/high_order/result/nmf/nmf_foodweb3_kmeans.txt'
    data = '../result/SVD/food_web/node234'
    out = '../result/SVD/food_web/k_means_food_web_svd.txt'
    main(delimiter,data,out)

    # if not sys.argv[1:]:
    #     parser.print_help()
    #     exit(1)
    #
    # (opts, args) = parser.parse_args()
    #
    # main(opts.delimiter, opts.data, opts.out)
