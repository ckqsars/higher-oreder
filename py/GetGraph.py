#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright @2016 R&D, CINS Inc. (cins.com)
#
# Author: chenkaiqi<ckqsars@sina.com>
import math

def GetVariance(data,average):
    n = len(data)
    Variance = 0
    for obj in data:
        Variance = Variance + math.pow(obj-average,2)
    Variacne = Variance / n

    return Variacne

def main():
    file = '/home/ckqsars/workspace/high_order/data/karate.motif_two'
    outfile = '/home/ckqsars/workspace/high_order/data/karate_result_two.txt'
    variacnfile = '/home/ckqsars/workspace/high_order/data/vvalue.txt'
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
#     print '-------------------'
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
            sumdata = 0
            for index1 in oldl:
                
                if index in dictmotif[index1]:
                    #print index1
                    sumdata = (sumdata + oldl[index1])
            newk[index] = (1.0*sumdata/k0[index])
        
        for index in oldl:
            sumdata = 0
            for index1 in oldK:
                if index in dictnode[index1]:
                    sumdata = sumdata + oldK[index1]
            newl[index] = (1.0*sumdata/l0[index])/max(oldl.items(),key=lambda x:x[1])[1]


        oldK = newk
        oldl = newl
    print len(k)
    print len(l)
    print 'the result of k'
    print '--------------'  
    print newk
    print '--------------'
    print 'the result of l'
    print '--------------'
    print newl
    print '--------------'
    t = 0

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
    for i in range(len(numk)):
        fp.write(str(numk[i][0])+'\t'+str(numk[i][1])+'\n')
        print numk[i][0], numk[i][1]

'''
    boundaryIndex = 62
    print len(numk)
    temp = 0
    while(boundaryIndex!=len(numk)-2):
        max = 0
        #t = boundaryIndex+1
        t = boundaryIndex -1
        #for i in range(t,len(numk)-1):
        for i in range(t):
            #fp.write(str(numk[i][0])+'\t')
            boundary=(float(numk[i][1]) - float(numk[i+1][1]))/numk[i][1]
            if max < boundary:
                max = boundary
                boundaryIndex = i
        #print numk[boundaryIndex][0], max,numk[boundaryIndex][1]
        temp = temp + 1
        if temp == 4:
            break
'''


#     for i in range(128):
#         if str(i) not in newk:
#             fp.write(str(i)+'\t')
#   

'''
    ID_List = []
    value_List = []
    for i in range(len(numk)):
        #print numk[i][0],numk[i][1]/pow(10,16)
        temp = []
        ID_List.append(numk[i][0])
        value_List.append((numk[i][1] - numk[-1][1])/(numk[0][1] - numk[-1][1]))
    
    oldVariance = 0
    t = 0
    for i in range(len(value_List)):
        data = value_List[t:i+1]
            
        average = sum(data)/len(data)
        Variance = GetVariance(data, average)
         
        if oldVariance != 0:
            if Variance > oldVariance:
                t = i
                oldVariance = 0
                print ID_List[t]
             
            else:
                oldVariance = Variance
        #print Variance
           
    fp.close()


'''
main()