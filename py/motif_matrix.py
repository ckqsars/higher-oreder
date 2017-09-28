#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright @2016 R&D, CINS Inc. (cins.com)
#
# Author: chenkaiqi<ckqsars@sina.com>

'''
Get the matrix of motif and node.
calucate the value of  the M
'''

import numpy as np
import jieba

def read_input(fd, delimiter):
    for obj in fd:
        yield obj.strip().split(delimiter)

def Get_Matrix(data, delimiter):
    motif_list = []
    node_list = []
    fr = open(data)
    datalist = list(read_input(fr,delimiter))
    for obj in datalist:
        node = obj[0]
        motif = obj[1]
        if node not in node_list:
            node_list.append(node)
        if motif not in motif_list:
            motif_list.append(motif)

    numNode = len(node_list)
    numMotif = len(motif_list)
    node_motif = np.zeros((numMotif,numNode))


    for obj in datalist:
        node_motif[motif_list.index(obj[1])][node_list.index(obj[0])] = 1
    return node_motif



def main(data, delimiter):
    node_motif = Get_Matrix(data, delimiter)
    print node_motif
    node_motif_T = node_motif.T
    lenRow,lenCol = node_motif.shape
    zero_left = np.zeros((lenCol, lenCol))
    zero_right = np.zeros((lenRow, lenRow))
    M = np.vstack((np.hstack((zero_left,node_motif_T)),np.hstack((node_motif,zero_right))))
    #np.savetxt('../data/food_webM.csv', M, delimiter = ',')
    eigValue,eigVector = np.linalg.eig(M)
    print  max(eigValue)
    print '____'
    #print eigVector[15]
    #print eigVector[13]
    #print eigVector[12]
    for obj in eigValue:
        if int(obj) == 1.0:
            print obj

if __name__ == "__main__":
    data = '../data/Florida-bay_6.txt'
    #data = '../data/graph2.txt'
    delimiter = '\001'
    main(data, delimiter)