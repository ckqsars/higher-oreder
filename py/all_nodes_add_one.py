#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright @2016 R&D, CINS Inc. (cins.com)
#
# Author: chenkaiqi<ckqsars@sina.com>
'''

all nodes id add one

'''

import sys

def read_input(fd,delimiter):
    for obj in fd:
        yield obj.strip().split(delimiter)    


def main(delimiter,data,out):
    fr = open(data)
    fp = open(out,'w+')
    for obj in read_input(fr,delimiter):
        lenObj = len(obj)
        for i in range(lenObj):
            obj[i] = str(int(obj[i]) + 1)
        fp.write('\t'.join(obj)+'\n')
    fp.close()

if __name__=="__main__":
    delimiter = ' '
    data = "/home/ckqsars/workspace/high_order/data/C-elegans-frontal.txt"
    out = "/home/ckqsars/workspace/high_order/data/C-elegans-frontal_add1.txt"
    main(delimiter,data,out)