#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright @2016 R&D, CINS Inc. (cins.com)
#
# Author: chenkaiqi<ckqsars@sina.com>


import recursive_motif
from optparse import OptionParser
import settings
import sys


'''
the main is the example of how to use the class recursive_motif
we can use the recursive_motif to get the value of nodes and motifs
then we can use some cluster methods to get the cluster of nodes.
'''

def main(delimiter, data, out, num):
    delimiter = settings.FIELD_DELIMITER[delimiter] if delimiter in settings.FIELD_DELIMITER.keys() else delimiter
    fw = open(out,"w+")
    model = recursive_motif.recursive_motif(datafile= data, delimiter = delimiter,motifEle = 3)
    model.Get_init_value()
    model.Iteration(num)
    nodevalue = model.NodeValue()

    fw.writable(nodevalue)
    print nodevalue


if __name__ == "__main__":
    parser = OptionParser(usage="%prog -d data -s delimiter -o out -n num")
    parser.add_option(
        "-s", "--delimiter",
        help = u"the delimiter between colum 1 and 2"
    )

    parser.add_option(
        "-d", "--data",
        help = u"the name of the data (include the path)"
    )

    parser.add_option(
        "-o", "--out",
        help = u"the out file name(include the path)"
    )

    parser.add_option(
        "-n", "--num",
        help = u"the number of iteration times"
    )

    if not sys.argv[1:]:
        parser.print_help()
        exit(1)
    (opts, args) = parser.parse_args()

    main(delimiter = opts.delimiter, data = opts.data, out = opts.out, num = opts.num)
