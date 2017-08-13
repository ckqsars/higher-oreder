#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright @2016 R&D, CINS Inc. (cins.com)
#
# Author: chenkaiqi<ckqsars@sina.com>
import random
import math
import jieba

jieba.cut()


def Get_E(newNodeValue,oldNodesValue):
    '''

    :param newNodeValue: The value of T
    :param oldNodesValue: The value of  T-1
    :return: The distance between use abs
    '''
    E = 0
    for i in oldNodesValue:
        E = abs(oldNodesValue[i] - newNodeValue[i]) + E
    return E/len(oldNodesValue)

def main():
    file = '../data/graph2.txt'
    outfile = '../result/result_11/result_node_08041.txt'
    fr = open(file)
    fp = open(outfile,'w+')
    dictnode = {}
    dictmotif = {}
    motifsValue = {}
    nodesValue = {}
    for lin in fr:
        lin = lin.strip().split('\t')
        if lin[0] not in dictnode: 
            
            dictnode[lin[0]] = []
        dictnode[lin[0]].append(lin[1])
        
        
        if lin[1] not in dictmotif:
            dictmotif[lin[1]] = []
        dictmotif[lin[1]].append(lin[0])
    
    for index in dictnode:
        nodesValue[index] = len(dictnode[index])
        #nodesValue[index] = random.uniform(1,10)
        
    for index in dictmotif:
        # temp = 0
        # for t in dictmotif[index]:
        #     temp = 1.0/len(dictnode[t])+ temp
        motifsValue[index] = 3
        #motifsValue[index] = random.uniform(1, 10)

    print motifsValue
    print nodesValue

         

    
    motifsValue0 = motifsValue.copy()
    nodesValue0 = nodesValue.copy()
    
    oldMotifsValue = motifsValue.copy()
    oldNodesValue = nodesValue.copy()
    
    newMotifValue = {}
    newNodeValue = {}

    Eold_new = 100000
                                                                                  
    while (Eold_new > 0.01):
        for index in oldNodesValue:
            #print index+'aa'
            sumdata = 0
            for index1 in oldMotifsValue:
                               
                if index in dictmotif[index1]:
                    #print index1
                    sumdata = (sumdata + oldMotifsValue[index1])
            newNodeValue[index] = 1.0*sumdata/nodesValue0[index]
                                  #/max(oldMotifsValue.items(),key=lambda x:x[1])[1]
        
        for index in oldMotifsValue:
            sumdata = 0
            for index1 in oldNodesValue:
                if index in dictnode[index1]:
                    sumdata = sumdata + oldNodesValue[index1]
            #newMotifValue[index] = 1.0*sumdata/motifsValue0[index]
            print sumdata
            newMotifValue[index] = 1.0 * sumdata / motifsValue0[index] #/ \
                                  # max(oldNodesValue.items(), key=lambda x: x[1])[1]
        Eold_new = Get_E(newNodeValue,oldNodesValue)
        print newNodeValue
        print newMotifValue
        print oldNodesValue
        print Eold_new
        break
        oldMotifsValue = newMotifValue.copy()
        oldNodesValue = newNodeValue.copy()


    
    rankMotif = sorted(newMotifValue.items(),key = lambda asd:asd[1],reverse = True)
    rankNode = sorted(newNodeValue.items(),key = lambda asd:asd[1],reverse = True)
    print rankNode
    for obj in rankNode:
        #fp.write(obj[0]+'\t'+str((float(obj[1])-float(rankNode[len(rankNode)-1][1]))/(float(rankNode[0][1])-float(rankNode[len(rankNode)-1][1])))+'\n')
        fp.write(obj[0] + '\t' + str(float(obj[1])) + '\n')
    fp.close()

 
main()
