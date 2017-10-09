#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright @2016 R&D, CINS Inc. (cins.com)
#
# Author: chenkaiqi<ckqsars@sina.com>

class recursive_motif(object):

    def __init__(self, datafile, delimiter, motifEle):
        self.datafile = datafile
        self.delimiter = delimiter
        self.dictnode = {}
        self.dictmotif = {}
        self.motifsValue0 = {}
        self.nodesValue0 = {}
        self.newMotifValue = {}
        self.newNodeValue = {}
        self.oldNodeValue = {}
        self.oldMotifValue = {}
        self.motifEle = motifEle

    def Read_input(self,fd):

        for obj in fd:
            yield obj.strip().split(self.delimiter)


    def Get_init_value(self):

        fr = open(self.datafile)
        for obj in self.Read_input(fr):
            if obj[0] not in self.dictnode:
                self.dictnode[obj[0]] = []
            self.dictnode[obj[0]].append(obj[1])

            if obj[1] not in self.dictmotif:
                self.dictmotif[obj[1]] = []
            self.dictmotif[obj[1]].append(obj[0])

        for index in self.dictnode:
            self.nodesValue0[index] = len(self.dictnode[index])

        for index in self.dictmotif:
            self.motifsValue0[index] = self.motifEle

        fr.close()

    def Iteration(self, n):
        self.oldNodeValue = self.nodesValue0.copy()
        self.oldMotifValue = self.motifsValue0.copy()
        n = int(n)
        for i in range(n):
            for index in self.oldNodeValue:
                sumdata = 0
                for index1 in self.oldMotifValue:

                    if index in self.dictmotif[index1]:
                        sumdata = (sumdata + self.oldMotifValue[index1])
                self.newNodeValue[index] = (1.0 * sumdata / self.nodesValue0[index])

            for index in self.oldMotifValue:
                sumdata = 0
                for index1 in self.oldNodeValue:
                    if index in self.dictnode[index1]:
                        sumdata = sumdata + self.oldNodeValue[index1]
                self.newMotifValue[index] = 1.0 * sumdata / self.motifsValue0[index]

            self.oldMotifValue = self.newMotifValue.copy()
            self.oldNodeValue = self.newNodeValue.copy()

    def NodeValue(self):

        return self.newNodeValue

    def MotifValue(self):

        return self.newMotifValue



