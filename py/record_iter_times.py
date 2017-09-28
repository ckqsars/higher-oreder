#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright @2016 R&D, CINS Inc. (cins.com)
#
# Author: chenkaiqi<ckqsars@sina.com>

import scipy.stats as stats


def GetRank(ranklist):
    '''
    change rank to same list, the index is the point the value is rank
    :param ranklist:
    :return: rank
    '''
    rank = [0]*131
    for obj in ranklist:
        rank[int(obj)] = ranklist.index(obj)
    return rank

def read_input(fd, delimiter):
    for obj in fd:
        yield obj.strip().split(delimiter)

def main(data):

    fr = open(data)
    delimiter = '\001'

    motiflist = []
    dictnode = {}
    dictmotif = {}
    motifsValue = {}
    nodesValue = {}
    for obj in read_input(fr,delimiter):
        if obj[0] not in dictnode:

            dictnode[obj[0]] = []
        dictnode[obj[0]].append(obj[1])


        if obj[1] not in dictmotif:
            dictmotif[obj[1]] = []
            motiflist.append(obj[1])
        dictmotif[obj[1]].append(obj[0])

    fr.close()


    motifsValue0 = motifsValue
    nodesValue0 = nodesValue

    oldMotifsValue = motifsValue
    oldNodesValue = nodesValue

    newMotifValue = {}
    newNodeValue = {}

    for i in range(20):
        for index in oldNodesValue:
            # print index+'aa'
            sumdata = 0
            for index1 in oldMotifsValue:

                if index in dictmotif[index1]:
                    # print index1
                    sumdata = (sumdata + oldMotifsValue[index1])
            newNodeValue[index] = 1.0 * sumdata / nodesValue0[index]

        for index in oldMotifsValue:
            sumdata = 0
            for index1 in oldNodesValue:
                if index in dictnode[index1]:
                    sumdata = sumdata + oldNodesValue[index1]
            # newMotifValue[index] = 1.0*sumdata/motifsValue0[index]
            newMotifValue[index] = (1.0 * sumdata / motifsValue0[index]) / \
                                   max(oldNodesValue.items(), key=lambda x: x[1])[1]

        oldMotifsValue = newMotifValue
        oldNodesValue = newNodeValue

    for index in dictnode:
        nodesValue[index] = len(dictnode[index])

    for index in dictmotif:
        temp = 0
        for t in dictmotif[index]:
            temp = 1.0 / len(dictnode[t]) + temp
        motifsValue[index] = temp

    motifsValue0 = motifsValue
    nodesValue0 = nodesValue

    oldMotifsValue = motifsValue
    oldNodesValue = nodesValue

    newMotifValue = {}
    newNodeValue = {}

    for i in range(20):
        for index in oldNodesValue:
            # print index+'aa'
            sumdata = 0
            for index1 in oldMotifsValue:

                if index in dictmotif[index1]:
                    # print index1
                    sumdata = (sumdata + oldMotifsValue[index1])
            newNodeValue[index] = 1.0 * sumdata / nodesValue0[index]

        for index in oldMotifsValue:
            sumdata = 0
            for index1 in oldNodesValue:
                if index in dictnode[index1]:
                    sumdata = sumdata + oldNodesValue[index1]
            # newMotifValue[index] = 1.0*sumdata/motifsValue0[index]
            newMotifValue[index] = (1.0 * sumdata / motifsValue0[index]) / \
                                   max(oldNodesValue.items(), key=lambda x: x[1])[1]


        rankNode = sorted(newNodeValue.items(), key=lambda asd:asd[1], reverse=True)
        oldrankNode = sorted(oldNodesValue.items(), key=lambda asd:asd[1], reverse=True)
        nodeNewlist = [x[0] for x in rankNode]
        nodeOldlist = [x[0] for x in oldrankNode]
        newrank = GetRank(nodeNewlist)
        oldrank = GetRank(nodeOldlist)
        print stats.stats.spearmanr(newrank, oldrank)
        #print nodeNewlist

        oldMotifsValue = newMotifValue.copy()
        oldNodesValue = newNodeValue.copy()



if __name__ == "__main__":
    data = '/home/ckqsars/workspace/high_order/data/graph131_2.txt'
    main(data)