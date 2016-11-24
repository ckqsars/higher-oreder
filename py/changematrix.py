#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright @2016 R&D, CINS Inc. (cins.com)
#
# Author: chenkaiqi<ckqsars@sina.com>

import csv

def main(file,outfile):
    fr = open(file)
    fp = open(outfile,'w+')
    data = csv.reader(fr)
    raw = 0
    for content in data:
        raw = raw + 1
        for index in range(len(content)):
            if content[index] == '1':  
                fp.write(str(raw)+'\t'+str(index+1)+'\n')
    fp.close()

if __name__=="__main__":
    file = '/home/ckqsars/workspace/high_order/data/celegans131matrix.csv'
    outfile = '/home/ckqsars/workspace/high_order/data/NodeGraph131.txt'
    main(file,outfile)