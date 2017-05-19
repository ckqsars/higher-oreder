#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright @2016 R&D, CINS Inc. (cins.com)
#
# Author: chenkaiqi<ckqsars@sina.com>

import copy
import sys
reload(sys)

def read_input(fd, delimiter):
    for obj in fd:
        yield obj.strip().split(delimiter)

def DegreeCentralilty(motifDict,nodeDict):
    degreeMotif = {}
    for motif in motifDict:
        value = 0
        for nodex in motifDict[motif]:
            if nodex in nodeDict:
                for nodey in nodeDict[nodex]:
                    if nodey not in motifDict[motif]:
                        value = value + 1
        
        degreeMotif[motif] = value
    
    return degreeMotif
    
    
def MiddleCentralilty(motifDict,pathdict):
    middleMotif = {}
    t = []
    for index in motifDict:
        print index,motifDict[index]
        st_s = 0
        st = 0
        for node in pathdict :
            if node in motifDict[index]:
                #print node
                
                continue
            
            for node1 in pathdict :
                if node in motifDict[index]:
                    #print node
                    continue
                if len(pathdict[node][node1])!= 0:
                    st = st + 1
                    for node2 in pathdict[node][node1]:
                        if node2 in motifDict[index]:
                            st_s = st_s + 1
                            break
        print 1.0*st_s/st
        4
        
        11
            
                    
        
def main(motifdata,nodedata):
    stdin_motif = sys.stdin if motifdata is None else open(motifdata)
    stdin_node = sys.stdin if nodedata is None else open(nodedata)
    motifDict = {}
    nodeDict = {}
    for lin in read_input(stdin_motif,'\001'):    #建立关于MOTIF的字典
        if lin[1] not in motifDict:
            motifDict[lin[1]] = []
        motifDict[lin[1]].append(lin[0])
            
    for lin in read_input(stdin_node,'\t'):     #建立关于node入的字典，key为nodex value 为对应哪些nodey指向nodex
        if lin[1] not in nodeDict:
            nodeDict[lin[1]] = []
        nodeDict[lin[1]].append(lin[0])
    
    pathdict = {}
    for node in nodeDict:
        if node not in pathdict:
            pathdict[node] = {}
    
    for node in nodeDict:
        nodes = nodeDict[node]
        for node1 in nodes:
            if node1 not in pathdict:
                pathdict[node1][node] = {}
            pathdict[node1][node] = [node]
    for node in pathdict:
        for node1 in pathdict:
            if node1 not in pathdict[node]:
                pathdict[node][node1] = []


#     for index in pathdict:
#         print index,pathdict[index]
        
        
    for node in pathdict:
        dict = {}

        list = []
        for node1 in pathdict[node]:
            if len(pathdict[node][node1]) != 0:

                for node2 in pathdict[node1]:
                    if len(pathdict[node][node2]) ==0 and len(pathdict[node1][node2]) != 0:
                        if node2 not in dict:
                            dict[node2] = []
                        temp1=copy.deepcopy(pathdict[node][node1])
                        dict[node2].append(pathdict[node][node1]+pathdict[node1][node2])
        for index in dict:
            min = 99
            for path in dict[index]:
                if len(path) < min:
                    min = len(path)
                    pathdict[node][index] = path
        
        
#     for index in pathdict:
#         print index,pathdict[index]
    MiddleCentralilty(motifDict,pathdict)
    
    degreeMotif = DegreeCentralilty(motifDict, nodeDict)
    
#     print pathdict 
    print degreeMotif
#     print motifDict
#     print nodeDict
    
if __name__=="__main__":
    motifdata = '/home/ckqsars/workspace/high_order/data/graph131_3.txt'
    nodedata = '/home/ckqsars/workspace/high_order/data/NodeGraph131.txt'
    main(motifdata,nodedata)