#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright @2016 R&D, CINS Inc. (cins.com)
#
# Author: chenkaiqi<ckqsars@sina.com>

def GetNode(index_nodes):
    node_list = []
    index_nodes.readline()
    index_nodes.readline()
    for obj in read_input(index_nodes, '\t'):
        if len(obj) ==1 :
            break
        node_list.append(str(int(obj[0])-1))
        
    return node_list

def read_input(fd, delimiter):
    for obj in fd:
        yield obj.strip().split(delimiter)

def main(delimiter,data,index_data,out):
    edges = open(data)
    index_nodes = open(index_data)
    nodelist = GetNode(index_nodes)
    nodelist = ['56','57','58','61','63','64','65','67','68','71','90','98','99']
    outfile = open(out,'w+')
    print nodelist
    for obj in read_input(edges,delimiter):
        flag = 0
        for node in obj:           
            if node in nodelist:
                flag = flag + 1
        if flag == 2:
            outfile.write('\t'.join(obj)+'\n')
if __name__=="__main__":
    delimiter = ' '
    data = '/home/ckqsars/workspace/high_order/data/Florida-bay.txt'
    index_data = '/home/ckqsars/workspace/high_order/data/result_node131.txt'
    out = '/home/ckqsars/workspace/high_order/data/edges_Pelagic_Demersal.txt'
    main(delimiter,data,index_data,out)