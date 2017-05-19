#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright @2016 R&D, CINS Inc. (cins.com)
#
# Author: chenkaiqi<ckqsars@sina.com>

import xlrd

def main(data):
    datalist = xlrd.open_workbook(data)
    table = datalist.sheets()[3]
    nrows = table.nrows
    ncols = table.ncols
    for i in range(nrows):
        print table.row_values(i)

if __name__ == "__main__":
    data = '/home/ckqsars/workspace/high_order/data/statistics.xlsx'
    main(data)