#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright @2016 R&D, CINS Inc. (cins.com)
#
# Author: chenkaiqi<ckqsars@sina.com>

file = '/home/ckqsars/workspace/high_order/data/Florida-bay.motif6'
outfile = '/home/ckqsars/workspace/high_order/data/Florida-bay_6.txt'
fp = open(outfile,'w+')
fr = open(file)
for lin in fr:
    lin = lin.strip().split('\001')
    for i in range(len(lin)-1):
        fp.write(lin[i+1]+'\001'+lin[0]+'\n')
fp.close()
fr.close()