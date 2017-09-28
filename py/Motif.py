#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright @2016 R&D, CINS Inc. (cins.com)
#
# Author: chenkaiqi<ckqsars@sina.com>

import numpy as np
import time

class Motif(object):
    def __init__(self):
        pass

    def read_input(self, fd, delimiter):
        for obj in fd:
            yield obj.strip().split(delimiter)

    def Get_Matrix(self, data, delimiter):
        node_list = []
        motif_list = []
        fr = open(data)
        datalist = list(self.read_input(fr, delimiter))
        for obj in datalist:
            node = obj[0]
            motif = obj[1]
            if node not in node_list:
                node_list.append(node)
            if motif not in motif_list:
                motif_list.append(motif)

        numNode = len(node_list)
        numMotif = len(motif_list)
        node_motif = np.zeros((numMotif, numNode))

        for obj in datalist:
            node_motif[motif_list.index(obj[1])][node_list.index(obj[0])] = 1
        return node_motif, node_list, motif_list


    def Inital_C_L(self,node_motif):
        numMotif, numNode = node_motif.shape
        C0 = np.zeros((numMotif, numMotif))
        L0 = np.zeros((numNode, numNode))
        sum_node = sum(node_motif)
        sum_motif = sum(node_motif.T)


        for i in range(numNode):
            L0[i][i] = 1.0/sum_node[i]

        for j in range(numMotif):
            C0[j][j] = 1.0/sum_motif[j]


        return np.mat(L0), np.mat(C0)

    def Init_M_MT(self, node_motif):
        node_motif_T = node_motif.T
        lenRow, lenCol = node_motif.shape
        zero_left = np.zeros((lenCol, lenCol))
        zero_right = np.zeros((lenRow, lenRow))
        M = np.vstack((np.hstack((zero_left, node_motif_T)), np.hstack((node_motif, zero_right))))

        return M

    def calu_SVD(self, matrix_M):
        U, S, V = np.linalg.svd(matrix_M)
        return U, S, V

    def save_matrix(self,file_name, matrix_name):
        savetime = str(int(time.time()))
        np.savetxt(file_name, matrix_name, delimiter=',')
