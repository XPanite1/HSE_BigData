#!/usr/bin/env python
# coding=utf-8
import sys


# just get antiNucleus and prodTime to find mean
# we get columns: 0(antiNucleus), 10(time)

for line in sys.stdin:
    data = line.split(',') 
    print("{0}\t{1}".format(data[0],data[10]))
   
#INPUT 
"""
0 - antiNucleus INT
1 - eventFile UINT
2 - eventNumber INT
3 - eventTime DOUBLE
4 - histFile UINT
5 - multiplicity INT
6 - NaboveLb INT
7 - NbelowLb INT
8 - NLb  INT
9 - primaryTracks INT
10 - prodTime DOUBLE
11 - Pt  FLOAT
12 - runNumber INT
13 - vertexX  FLOAT
14 - vertexY  FLOAT
15 - vertexZ  FLOAT
"""
#OUTPUT 
#key - antiNucleus
#value - prodTime