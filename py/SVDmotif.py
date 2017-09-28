#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright @2017 R&D, CINS Inc. (cins.com)
#
# Author: chenkaiqi<ckqsars@sina.com>

import numpy as np
import Motif



def main(data,delimiter):
    motif = Motif.Motif()
    motif_node, node_list, motif_list = motif.Get_Matrix(data,delimiter)
    #MT = motif.Init_M_MT(motif_node)
    L0, C0 = motif.Inital_C_L(motif_node)
    #print motif.Init_M_MT(motif_node)
    print L0.shape
    E =  np.mat(L0)*motif_node.T

    print E.shape
    U,S,V = motif.calu_SVD(E)

    motif.save_matrix(outpath+'RU.csv',U)
    motif.save_matrix(outpath+'RV.csv', V.T)
    motif.save_matrix(outpath+'RS.csv', S)

    fp = open(outpath+'node','w+')
    fp.write('\n'.join(node_list))
    fp.close()


    #print V


if __name__ == "__main__":
    data = '../data/Florida-bay_6.txt'
    #data = '../data/graph2.txt'
    #outpath = '../result/SVD/11nodes/'
    outpath = '../result/SVD/food_web/'
    delimiter = '\001'
    main(data,delimiter)