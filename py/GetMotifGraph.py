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

def main(data):
    stdin = sys.stdin if data is None else open(data)
    dict = {}
    for obj in ReadData(stdin, '\t'):
        if obj[0] not in dict:
            dict[obj[0]] = []
        dict[obj[0]].append(obj[1])
    
    print dict
if __name__=="__main__":
    data = '/home/ckqsars/workspace/high_order/data/graph1.txt'
    main(data)