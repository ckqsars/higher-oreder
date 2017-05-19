#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright @2016 R&D, CINS Inc. (cins.com)
#
# Author: chenkaiqi<ckqsars@sina.com>

import sys

def ReadData(fr,delimiter):
    '''
    from the file read data 
    
    separator is  delimiter 
    '''
    
    for obj in fr:
        yield obj.strip().split(delimiter)
        
def getcommon(list_1,list_2):
    
    commonlist = list(set(list_1)&set(list_2))
    
    return commonlist

        

def main(NodeFile):
    stdin = sys.stdin if NodeFile is None else open(NodeFile)
    
    
    
    outDict = {}
    splitlist = []
    for obj in ReadData(stdin, '\t'):
        fromNode = obj[0]
        toNode = obj[1]
        if fromNode not in outDict:
            outDict[fromNode] = []
        outDict[fromNode].append(toNode)
    print outDict['94']
    print outDict['95']
    print outDict['67']
    motifDict = {}
    numMotif = 0
    for index in outDict:
        splitlist.append(index)
        for index2 in outDict:
            if index2 not in splitlist:
                outlist = outDict[index]
                outlist2 = outDict[index2]
                commonlist = getcommon(outlist, outlist2)
                lenCommon = len(commonlist)
                for i in range(lenCommon):
                    for j in range(i):
                        numMotif = numMotif + 1
                        motifDict[numMotif]=str(index)+' '+str(index2)+' '+str(commonlist[i])+' '+str(commonlist[j])
    for index in motifDict:
        setmotif = set(motifDict[index].split(' '))
        if setmotif == set([94,95,61,67]):
            print index

    print numMotif

if __name__ =="__main__":
    NodeFile = '/home/ckqsars/workspace/high_order/data/NodeGraph131.txt'
    main(NodeFile)