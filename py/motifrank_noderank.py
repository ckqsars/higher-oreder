#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright @2016 R&D, CINS Inc. (cins.com)
#
# Author: chenkaiqi<ckqsars@sina.com>


from collections import Counter

def read_input(fd,delimiter):
    for obj in fd:
        yield obj.strip().split(delimiter)

def main(indexfile, data, out):
    delimiter1 = '\001'
    delimiter2 = '\t'
    fr = open(data)

    motif_cluster = {}
    node_cluster = {}
    for obj in read_input(fr,delimiter2):
        motif_cluster[obj[0]] = obj[1]

    fr.close()

    fr2 = open(indexfile)
    fp = open(out, 'w+')

    for obj in read_input(fr2, delimiter1):

        if obj[0] not in node_cluster:

            node_cluster[obj[0]] = []

        node_cluster[obj[0]].append(motif_cluster[obj[1]])

    for node in node_cluster:
        node_cluster[node] = int(Counter(node_cluster[node]).most_common(1)[0][0])

    print node_cluster

    for node in node_cluster:
        fp.write("{0}\t{1}\n".format(node, node_cluster[node]))


if __name__ == "__main__":

    indexfile = '/home/ckqsars/workspace/high_order/data/Florida-bay_6.txt'
    data = '/home/ckqsars/workspace/high_order/result/food_web/motif_result_kmeans'
    out = '/home/ckqsars/workspace/high_order/result/food_web/result_node_kmeans.txt'
    main(indexfile, data, out)