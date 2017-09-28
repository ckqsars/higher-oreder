#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright @2016 R&D, CINS Inc. (cins.com)
#
# Author: chenkaiqi<ckqsars@sina.com>


import recursive_motif
from optparse import OptionParser
import sys


def main(delimiter, data, out, num):
    model = recursive_motif.recursive_motif(datafile= data, outfile= out, delimiter = )


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