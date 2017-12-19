#!/usr/bin/env python
# coding=utf-8
import sys

for line in sys.stdin:
    data = line.split(',')  
    print("{0}\t{1},{2}".format(int(data[0]),int(data[1]),float(data[2])))

"""
0 - antiNucleus INT
1 - eventFile UINT
2 - Pt  FLOAT
"""
