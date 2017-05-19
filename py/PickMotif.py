#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright @2016 R&D, CINS Inc. (cins.com)
#
# Author: chenkaiqi<ckqsars@sina.com>

import sys


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
        break
        t = head + 1
    return boundaryList

def read_input(fd,delimiter):
    for obj in fd:
        yield obj.strip().split(delimiter)    


def IterationValue(motifDict,nodeDict):
    nodeValue = {}
    motifValue = {}
    
    for index in nodeDict:
        nodeValue[index] = len(nodeDict[index])
        
    for index in motifDict:
        temp = 0
        for t in motifDict[index]:
            temp = 1.0/len(nodeDict[t])+ temp
        motifValue[index] = temp
 
#     print nodeValue
#     print motifValue
    nodeValue0 = nodeValue
    motifValue0 = motifValue
    
    oldNodeValue = nodeValue
    oldMotifValue = motifValue
    newNodeValue = {}
    newMotifValue = {}
    
    for i in range(20):
        for index in oldNodeValue:
            #print index+'aa'
            sumdata = 0.0
            for index1 in oldMotifValue:
                
                if index in motifDict[index1]:
#                     if index == "60":
#                         print index1
                    sumdata = sumdata + oldMotifValue[index1]
            newNodeValue[index] = 1.0*sumdata/nodeValue0[index]
#             if index == "60":
#                 print sumdata
        for index in oldMotifValue:
            sumdata = 0.0
            for index1 in oldNodeValue:
                if index in nodeDict[index1]:
                    sumdata = sumdata + oldNodeValue[index1]
            newMotifValue[index] = 1.0*sumdata/motifValue0[index]

        
        oldNodeValue = newNodeValue
        oldMotifValue = newMotifValue
        
    return newNodeValue,newMotifValue

def RemoveMotif(motifDict,nodeDict,node_list,rm_nodes):
    rm_motif_list = []
    rm_node_list =[]
    for index in motifDict:
        flag = 0
        for node in motifDict[index]:
            if node  in node_list:
                flag = flag + 1
        if flag != 4:
            rm_motif_list.append(index)
                
    for content in rm_motif_list:
        motifDict.pop(content)
        
    for node in nodeDict:
        if node not in node_list:
            rm_node_list.append(node)
            
    for content in rm_node_list:
        nodeDict.pop(content)
        
    
    return motifDict,nodeDict


def GetMotif(index_stdin):
    motifDict = {}
    nodeDict = {}
    
    for obj in read_input(index_stdin,delimiter = '\001'):
        if obj[0] not in nodeDict: 
            
            nodeDict[obj[0]] = []
        nodeDict[obj[0]].append(obj[1])
        
        if obj[1] not in motifDict:
                motifDict[obj[1]] = []
        motifDict[obj[1]].append(obj[0])
    
    return motifDict,nodeDict
    
def main(data,indexdata,index,out):
    stdin = sys.stdin if data is None else open(data)
    index_stdin =  sys.stdin if indexdata is None else open(indexdata)
    stdout = sys.stdout if out is None else open(out,'w+')
    
    for obj in stdin:
        obj = obj.strip().split('\t')
        num_index = obj.index(index)
        print num_index
        data_list = obj[num_index+1:]
        rm_nodes = obj[:num_index+1]

    print len(data_list)
    motifDict,nodeDict = GetMotif(index_stdin)
    print len(nodeDict)
    new_motifDict,new_nodeDict = RemoveMotif(motifDict,nodeDict,data_list,rm_nodes)
    print len(new_motifDict),len(new_nodeDict)
    valueNode,valueMoitf=IterationValue(new_motifDict,new_nodeDict)
    
    #print valueNode
    
    numNode = sorted(valueNode.items(),key = lambda asd:asd[1],reverse = True)
    
    for index in numNode:
        print index[0],index[1]
     
    ranknum = GetTheMax(numNode)
    
    print ranknum
        
    for i in range(len(numNode)):
            stdout.write(str(numNode[i][0])+'\t')  
            
    stdout.close()      
    boundaryIndex = 0
    print len(numNode) 


if __name__ == "__main__":
    data = '/home/ckqsars/workspace/high_order/data/result_node131_temp_9.txt'
    indedata = '/home/ckqsars/workspace/high_order/data/graph131.txt'
    out = '/home/ckqsars/workspace/high_order/data/result_node131_temp_10.txt'
    index = '52'
    main(data,indedata,index,out)