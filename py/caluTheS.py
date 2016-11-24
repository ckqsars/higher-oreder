#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright @2016 R&D, CINS Inc. (cins.com)
#
# Author: chenkaiqi<ckqsars@sina.com>

def GetNodeDict(nodeData):
    '''
    build the dict of nodes connected
    '''
    fr = open(nodeData)
    dict = {}
    for lin in fr:
        lin = lin.strip().split('\t')
        if lin[0] not in dict:
            dict[lin[0]] = []
        dict[lin[0]].append(lin[1])
    
    fr.close()
    
    return dict

def GetMotifDict(motifData):
    '''
    
    build the nodes dict about the information of motifs contained 
    
    '''
    fr = open(motifData)
    dict = {} 
    for lin in fr:
        
        lin = lin.strip().split('\001')
        
        if lin[0] not in dict:
            dict[lin[0]] = []
        dict[lin[0]].append(lin[1])
 
    return dict           
    

def main(data,nodeData, motifData):
    nodeDict = GetNodeDict(nodeData)
    motifDict = GetMotifDict(motifData)
    
    for index in motifDict:
        print index, motifDict[index]

if __name__=='__main__':
    data = '/home/ckqsars/workspace/high_order/data/result8'
    nodeData = '/home/ckqsars/workspace/high_order/data/NodeGraph131.txt'
    motifData = '/home/ckqsars/workspace/high_order/data/graph131_3.txt'
    main(data,nodeData,motifData) 