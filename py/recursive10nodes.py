#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright @2016 R&D, CINS Inc. (cins.com)
#
# Author: chenkaiqi<ckqsars@sina.com>
import math


def main():
    file = '../data/graph1.txt'
    outfile = '../result/result_10/result_node_temp.txt'
    #outfile='/home/ckqsars/workspace/high_order/result/result_10/result_motif.txt'
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
        
    for index in dictmotif:
        temp = 0
        for t in dictmotif[index]:
            temp = 1.0/len(dictnode[t])+ temp
        motifsValue[index] = temp
         

    
    motifsValue0 = motifsValue
    nodesValue0 = nodesValue
    
    oldMotifsValue = motifsValue.copy()
    oldNodesValue = nodesValue.copy()
    
    newMotifValue = {}
    newNodeValue = {}
                                                                                  
    for i in range(20):
        for index in oldNodesValue:
            #print index+'aa'
            sumdata = 0
            for index1 in oldMotifsValue:
                               
                if index in dictmotif[index1]:
                    #print index1
                    sumdata = (sumdata + oldMotifsValue[index1])
            #newNodeValue[index] = (1.0*sumdata/nodesValue0[index])/oldNodesValue[index]
            newNodeValue[index] = (1.0 * sumdata / nodesValue0[index])/max(oldMotifsValue.items(),key=lambda x:x[1])[1]
        for index in oldMotifsValue:
            sumdata = 0
            for index1 in oldNodesValue:
                if index in dictnode[index1]:
                    sumdata = sumdata + oldNodesValue[index1]
            newMotifValue[index] = (1.0*sumdata/motifsValue0[index])/max(oldNodesValue.items(),key=lambda x:x[1])[1]
            #newMotifValue[index] = (1.0 * sumdata / motifsValue0[index])
        oldMotifsValue = newMotifValue.copy()
        oldNodesValue = newNodeValue.copy()

        print newNodeValue
    
    rankMotif = sorted(newMotifValue.items(),key = lambda asd:asd[1],reverse = True)
    rankNode = sorted(newNodeValue.items(),key = lambda asd:asd[1],reverse = True)

    print rankMotif
    print rankNode
    for obj in rankNode:
        fp.write(obj[0]+'\t'+str(float(obj[1]))+'\n')
    fp.close()

 
main()