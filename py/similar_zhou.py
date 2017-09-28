#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright @2017 R&D, CINS Inc. (cins.com)
#
# Author: chenkaiqi<ckqsars@sina.com>



def GetSimialry(ai, aj, dictmotif, dictnode):
    commlist = [var for var in dictnode[ai] if var in dictnode[aj]]
    sim_sum = 0
    for obj in commlist:
        sim_sum = sim_sum + 1.0 / len(dictmotif[obj])
    sim_sum = sim_sum / len(dictnode[aj])

    return sim_sum


def main(file, outfile, delimiter):
    fr = open(file)

    fp = open(outfile,"w+")
    dictnode = {}
    dictmotif = {}
    nodelist = []
    for obj in fr:
        obj = obj.strip().split(delimiter)
        if obj[0] not in dictnode:
            dictnode[obj[0]] = []
        if obj[0] not in nodelist:
            nodelist.append(obj[0])
        dictnode[obj[0]].append(obj[1])
        if obj[1] not in dictmotif:
            dictmotif[obj[1]] = []
        dictmotif[obj[1]].append(obj[0])
    print dictmotif
    print dictnode

    for ai in nodelist:
        for aj in nodelist:
            if ai != aj:
                sim = GetSimialry(ai, aj, dictmotif, dictnode)
                if sim != 0:
                    item = [ai, aj, str(sim)]
                    fp.write('\t'.join(item)+'\n')





    return 0

if __name__ == "__main__":
   file = "/home/ckqsars/workspace/high_order/data/graph1.txt"  #存储motif-nodes的数据
   outfile = "/home/ckqsars/workspace/high_order/result/result_zhou.txt"
   delimiter = '\t'
   main(file, outfile, delimiter)
