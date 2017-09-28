#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright @2017 R&D, CINS Inc. (cins.com)
#
# Author: chenkaiqi<ckqsars@sina.com>

import numpy as np
from sklearn.decomposition import NMF

def read_input(fd,delimiter):
    for obj in fd:
        yield obj.strip().split(delimiter)

def main(data, num, out):
    fr = open(data)
    fp = open(out, 'w+')

    delimiter = '\001'
    node_list = []
    motif_list = []
    for obj in read_input(fr,delimiter):
        node = obj[0]
        motif = obj[1]
        if node not in node_list:
            node_list.append(node)
        if motif not in motif_list:
            motif_list.append(motif)
    fr.close()
    node_motif_mat = np.zeros((len(motif_list),len(node_list)))

    fr = open(data)
    for obj in read_input(fr,delimiter):
        node_motif_mat[motif_list.index(obj[1])][node_list.index(obj[0])] = \
            node_motif_mat[motif_list.index(obj[1])][node_list.index(obj[0])] + 1

    nmf = NMF(n_components=num, random_state=1, alpha=0.1, l1_ratio=0.5).fit(node_motif_mat)

    node_dict = {}

    for obj in nmf.components_:
        for i in range(len(obj)):
            if node_list[i] not in node_dict:
                node_dict[node_list[i]] = []
            node_dict[node_list[i]].append(str(obj[i]))

    error_list = [41,99,123,122]

    for index in node_dict:
        if index not in error_list:
            fp.write(str(index)+"\t"+'\t'.join(node_dict[index]))
            fp.write('\n')
    fp.close()

if __name__ == '__main__':
    data = '../data/Florida-bay_6.txt'
    out = '../result/nmf/nmf_foodweb_3.txt'
    num = 83
    main(data, num, out)