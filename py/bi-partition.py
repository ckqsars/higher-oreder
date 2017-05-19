#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright @2017 R&D, CINS Inc. (cins.com)
#
# Author: chenkaiqi<ckqsars@sina.com>

def read_input(fd, delimiter):
    datalist = []
    for obj in fd:
        obj = obj.strip().split(delimiter)
        datalist.append(obj)
    return datalist

def main(data, out, k):
    fr = open(data)
    delimiter = '\t'
    fp = open(out,'w+')
    datalist = read_input(fr, delimiter)
    clusterlist = []

    imax = 0
    while(k):
        max = 0
        oldimax = imax
        for i in range(imax,len(datalist) -1):
            if max < float(datalist[i][1]) - float(datalist[i+1][1]):
                max = float(datalist[i][1]) - float(datalist[i+1][1])
                imax = i + 1

        for j in range(oldimax, imax):
            clusterlist.append([datalist[j][0],k])
        k= k -1

    for j in range(imax, len(datalist)):
        clusterlist.append([datalist[j][0], k])
    for obj in clusterlist:
        fp.write(obj[0] + '\t' + str(float(obj[1])) + '\n')

    fp.close()




if __name__ == "__main__":
    data ='../result/food_web/result_.txt'
    out = '../result/food_web/result_bi_partition_7.txt'
    k = 6
    main(data, out , k)