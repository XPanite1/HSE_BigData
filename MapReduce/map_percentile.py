#!/usr/bin/env python
# coding=utf-8
import sys


# filter and move all_data to one reduce
# we get columns: 10(time),0,1,11

for line in sys.stdin:
    data = line.split(',')
    data = line.split(',')  
    print("{0}\t{1}\t{2},{3}".format(data[0],data[10],data[1],data[11]))
    
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