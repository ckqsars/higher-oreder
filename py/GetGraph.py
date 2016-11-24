#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright @2016 R&D, CINS Inc. (cins.com)
#
# Author: chenkaiqi<ckqsars@sina.com>

def main():
    file = '/home/ckqsars/workspace/high_order/data/Florida-bay_6.txt'
    outfile = '/home/ckqsars/workspace/high_order/data/result_Florida-bay_1.txt'
    fr = open(file)
    fp = open(outfile,'w+')
    dictnode = {}
    dictmotif = {}
    k = {}
    l = {}
    M = {}
    for lin in fr:
        lin = lin.strip().split('\001')
        if lin[0] not in dictnode:
            dictnode[lin[0]] = []
        dictnode[lin[0]].append(lin[1])
        
        
        if lin[1] not in dictmotif:
            dictmotif[lin[1]] = []
        dictmotif[lin[1]].append(lin[0])
    
    for index in dictnode:
        k[index] = len(dictnode[index])
        
    for index in dictmotif:
        temp = 0
        for t in dictmotif[index]:
            temp = 1.0/len(dictnode[t])+ temp
        l[index] = temp
         
    
#     print 'the origin node to motif'
#     print '------------------------'
#     print dictnode
#     print '------------------------'
#     
#     print 'the origin motif to node'
#     print '-----------------------'
#     print dictmotif
#     print '----------------------'
#     
#     print 'the origin value of k'
#     print '-------------------'
#     print k
#     print '-------------------'newk
#     
#     print 'the origin value of l'
#     print '-------------------'
#     print l
#     print '-------------------'
    
    k0 = k
    l0 = l
    
    oldK = k
    oldl = l
    newk = {}
    newl = {}
    
    for i in range(20):
        for index in oldK:
            #print index+'aa'
            sum = 0
            for index1 in oldl:
                
                if index in dictmotif[index1]:
                    #print index1
                    sum = sum + oldl[index1]
            newk[index] = 1.0*sum/k0[index]
        
        for index in oldl:
            sum = 0
            for index1 in oldK:
                if index in dictnode[index1]:
                    sum = sum + oldK[index1]
            newl[index] = 1.0*sum/l0[index]
            
        oldK = newk
        oldl = newl
    
#     print 'the result of k'
#     print '--------------'  
#     print newk
#     print '--------------'
#     print 'the result of l'
#     print '--------------'
#     print newl
#     print '--------------'
#     t = 0

#     for index in newk:
#         list = []
#         for index1 in newk:
#             if index != index1 and newk[index] == newk[index1]:
#                 list.append(index1)
#                 t = t + 1
#         if len(list) != 0:
#             print index+'\t'+' '.join(list)
#     print t
    print len(newl)
    print len(newk)
    numk = sorted(newk.items(),key = lambda asd:asd[1],reverse = True)

    boundaryIndex = 0
    print len(numk)
    while(boundaryIndex!=len(numk)-2):
        max = 0
        t = boundaryIndex+1
        for i in range(t,len(numk)-1):
            #fp.write(str(numk[i][0])+'\t')
            boundary=float(numk[i][1]) - float(numk[i+1][1])
            if max < boundary:
                max = boundary
                boundaryIndex = i
        print numk[boundaryIndex][0], max
    for i in range(len(numk)):
            fp.write(str(numk[i][0])+'\t')
#     for i in range(128):
#         if str(i) not in newk:
#             fp.write(str(i)+'\t')
#             
    for i in range(len(numk)):
        print str(numk[i][0])+'\t'+str(numk[i][1])
            
    fp.close()
    
main()    