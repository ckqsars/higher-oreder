#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright @2016 R&D, CINS Inc. (cins.com)
#
# Author: chenkaiqi<ckqsars@sina.com>

file = '/home/ckqsars/workspace/high_order/data/karate.motif3'
outfile = '/home/ckqsars/workspace/high_order/data/karate.motif3_graph.txt'
fp = open(outfile,'w+')
fr = open(file)
t = 0
for lin in fr:
    lin = lin.strip().split('\001')
    for i in range(len(lin)):
        fp.write(lin[i]+'\001'+str(t)+'\n')
    t= t + 1
fp.close()
fr.close()