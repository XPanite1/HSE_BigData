#!/usr/bin/env python
# coding=utf-8
import sys
import numpy as np

# just find 5 and 95 percentile and filter data
# output all lines with antiNucleus first(as key),
# and all data (eventFile,Pt)


all_times = []
last_antiNucleus = -1
all_data = []

for line in sys.stdin:
    antiNucleus,time,data = line.split('\t')
    
    antiNucleus = int(antiNucleus)

    if antiNucleus != last_antiNucleus:
        if last_antiNucleus != -1: 
            # print data
            up_value = np.percentile(all_times,95)
            down_value = np.percentile(all_times,5)

            for t,d in zip(all_times,all_data):
                eventFile = int(d.split(',')[0])
                Pt = float(d.split(',')[1])
                if t >= down_value and t <= up_value:
                    print("{0},{1},{2}".format(last_antiNucleus,eventFile,Pt))
        
        last_antiNucleus = antiNucleus
        all_times = []
        all_data = []


    all_times.append(float(time))
    all_data.append(data)

up_value = np.percentile(all_times,95)
down_value = np.percentile(all_times,5)
for t,d in zip(all_times,all_data):
    eventFile = int(d.split(',')[0])
    Pt = float(d.split(',')[1])
    print t
    if t >= down_value and t <= up_value:
        print("{0},{1},{2}".format(last_antiNucleus,eventFile,Pt))
   

#key - antiNucleus INT
#data : 
""" 
1 - eventFile UINT
2 - Pt  FLOAT
"""