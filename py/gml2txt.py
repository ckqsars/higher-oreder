#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright @2017 R&D, CINS Inc. (cins.com)
#
# Author: chenkaiqi<ckqsars@sina.com>


import networkx as nx
import scipy.stats as stats



def read_input(fd,delimiter):
    for obj in fd:
        yield obj.strip().split(delimiter)


def GetRank(ranklist):
    '''
    change rank to same list, the index is the point the value is rank
    :param ranklist:
    :return: rank
    '''
    rank = [0]*34
    for obj in ranklist:
        rank[obj] = ranklist.index(obj)
    return rank

def main(data, outfile, indexfile):
    fr = open(data)
    indexfr = open(indexfile)

    ranklist1 = []
    ranklist2 = []
    for obj in read_input(indexfr, '\t'):
        ranklist1.append(int(obj[0]))
    print ranklist1

    fp = open(outfile,'w+')
    g = nx.karate_club_graph()
    eigen_cen =  nx.eigenvector_centrality(g)
    between_cen = nx.betweenness_centrality(g)
    eigen_cen = sorted(eigen_cen.items(), key=lambda asd: asd[1], reverse=True)

    for obj in eigen_cen:
        ranklist2.append(int(obj[0]))
    print  ranklist2
    rank1 = GetRank(ranklist1)
    rank2 = GetRank(ranklist2)
    print rank1
    print rank2

    listlen = len(rank1)
    print listlen

    sum = 0
    for i in range(listlen):
        sum = abs(rank1[i]-rank2[i]) + sum

    sum = 1.0*sum/listlen

    print sum

    print stats.stats.spearmanr(rank1,rank2)
    print stats.stats.spearmanr(ranklist2,ranklist1)
    # for obj in g.edges():
    #     fp.write("{0} {1}\n".format(obj[0],obj[1]))
    # fp.close()
    # g_degree = g.degree()
    # degreesort = sorted(g_degree.items(), key=lambda asd: asd[1], reverse=True)
    #print degreesort

if __name__ == "__main__":
    data = '/home/ckqsars/workspace/high_order/data/football.gml'
    indexfile = '../data/karate_result_two.txt'
    outfile = '/home/ckqsars/workspace/high_order/data/football.txt'
    main(data, outfile, indexfile)