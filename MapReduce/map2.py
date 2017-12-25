#!/usr/bin/env python
# coding=utf-8
import sys


# filter and move all_data to one reduce
# we output columns: 0,1,11 (antiNucleus, eventFile, Pt)

file_name = 'part-00000'
#'means.csv' - local

 
d = dict() # read_data
data_means = open(file_name, 'r').readlines() 
for line in data_means:
	antiNucleus, mean_time_value = line.split(',')
	d[int(antiNucleus)] = float(mean_time_value)

for line in sys.stdin: 
    data = line.split(',')
    time = float(data[10])
    antiNucleus = int(data[0])
    if time > d[antiNucleus]: # filter data
        print("{0}\t{1},{2}".format(data[0],data[1],data[11]))
  

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
11 - Pt  FLsOAT
12 - runNumber INT
13 - vertexX  FLOAT
14 - vertexY  FLOAT
15 - vertexZ  FLOAT
"""
#OUTPUT
#key - antiNucleus 
#value - eventFile, Pt