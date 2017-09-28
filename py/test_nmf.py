#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright @2017 R&D, CINS Inc. (cins.com)
#
# Author: chenkaiqi<ckqsars@sina.com>

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF
from sklearn.datasets import fetch_20newsgroups
import numpy as np


def print_top_words(model, feature_names, n_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print("Topic #%d:" % topic_idx)
        print(" ".join([feature_names[i]]))

def main():
    num = 4
    outfile = '../result/nmf/mat'+str(num)
    fp = open(outfile,'w+')
    mat_node_motif = np.mat([[1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                            [1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                            [1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                            [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                            [0, 0, 0, 0, 0, 1, 0, 1, 1, 0],
                            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1]]
                            )
    nmf = NMF(n_components=num,random_state=1,alpha=0.1, l1_ratio=0.5).fit(mat_node_motif)
    node_dict = {}
    for obj in nmf.components_:
        for i in range(len(obj)):
            if i+1 not in node_dict:
                node_dict[i+1] = []
            node_dict[i+1].append(str(obj[i]))


    for index in node_dict:
        fp.write(str(index)+"\t"+'\t'.join(node_dict[index]))
        fp.write('\n')
    fp.close()


if __name__ == "__main__":
    main()