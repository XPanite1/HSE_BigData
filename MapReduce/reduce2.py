#!/usr/bin/env python
# coding=utf-8
import sys

#find result

import sys

count = 0.0
current_key = -1
Pt_sum = 0
event_files = set()
for line in sys.stdin:
    key,value = line.split('\t')
    key = int(key)
    
    if key != current_key:
        if current_key != -1:
            print("{0},{1},{2}".format(current_key, len(event_files), Pt_sum/count))
        current_key = key
        count = 0.0
        Pt_sum = 0.0
        event_files = set()

    event_file, Pt = value.split(',')
    
    event_files.add(int(event_file))
    Pt_sum += float(Pt)
    count += 1.0

print("{0},{1},{2}".format(key,len(event_files),Pt_sum/count))

#INPUT:
"""
key - 
0 - antiNucleus INT
value - 
1 - eventFile UINT
2 - Pt  FLOAT
"""
#OUTPUT:
# antiNucleus, number of eventFiles, mean of Pt