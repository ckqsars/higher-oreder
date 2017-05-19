#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright @2016 R&D, CINS Inc. (cins.com)
#
# Author: chenkaiqi<ckqsars@sina.com>
import math



def GetTheMax(rankNode):
    boundaryList = []
    boundaryIndex = 0
    t = 0
    while(t!=len(rankNode)-1):
        max = 0    
        for i in range(t,len(rankNode)-1):
    
            boundary=(float(rankNode[i][1]) - float(rankNode[i+1][1]))
            if max < boundary:
                max = boundary
                boundaryIndex = rankNode[i][0]
                head = i
        print boundaryIndex
        boundaryList.append(boundaryIndex)
        t = head + 1
    return boundaryList
def main():
    file = '/home/ckqsars/workspace/high_order/data/graph131_2.txt'
    outfile = '/home/ckqsars/workspace/high_order/data/result_node131_temp.txt'
    motifile = "/home/ckqsars/workspace/high_order/result/result_131/motif_result"
    fr = open(file)
    fp = open(outfile,'w+')
    fp2 = open(motifile,'w+')
    dictnode = {}
    dictmotif = {}
    motifsValue = {}
    nodesValue = {}
    for lin in fr:
        lin = lin.strip().split('\001')
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
    
    oldMotifsValue = motifsValue
    oldNodesValue = nodesValue
    
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
            newNodeValue[index] = 1.0*sumdata/nodesValue0[index]
        
        for index in oldMotifsValue:
            sumdata = 0
            for index1 in oldNodesValue:
                if index in dictnode[index1]:
                    sumdata = sumdata + oldNodesValue[index1]
            #newMotifValue[index] = 1.0*sumdata/motifsValue0[index]
            newMotifValue[index] = (1.0 * sumdata / motifsValue0[index]) / \
                                   max(oldNodesValue.items(), key=lambda x: x[1])[1]
            
        oldMotifsValue = newMotifValue
        oldNodesValue = newNodeValue
    
    rankMotif = sorted(newMotifValue.items(),key = lambda asd:asd[1],reverse = True)
    rankNode = sorted(newNodeValue.items(),key = lambda asd:asd[1],reverse = True)
    
    maxIndex = GetTheMax(rankNode)
    print rankMotif

    for obj in rankNode:
        fp.write(obj[0]+'\t'+str(float(obj[1]))+'\n')
#         if obj[0] in maxIndex:
#             fp.write('********'+'\n')
    for obj in rankNode:
        fp2.write(obj[0]+'\t'+str(float(obj[1]))+'\n')

    fp.close()
    fp2.close()
 
main()