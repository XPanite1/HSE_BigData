#!/usr/bin/env python
# coding=utf-8
import sys

# just find 5 and 95 percentile and filter data
# output all lines with antiNucleus first(as key),
# and all data (eventFile,Pt)


all_times = []
sum_times = 0.0
last_antiNucleus = -1
all_data = []

for line in sys.stdin:
    antiNucleus,time,data = line.split('\t')
    
    antiNucleus = int(antiNucleus)

    if antiNucleus != last_antiNucleus:
        if last_antiNucleus != -1: 
            # print data
            mean_time = sum_times/len(all_times)

            for t,d in zip(all_times,all_data):
                eventFile = int(d.split(',')[0])
                Pt = float(d.split(',')[1])
                if t >= mean_time:
                    print("{0},{1},{2}".format(last_antiNucleus,eventFile,Pt))
        
        last_antiNucleus = antiNucleus
        all_times = []
        all_data = []
        sum_times = 0.0


    all_times.append(float(time))
    all_data.append(data)
    sum_times += float(time)

mean_time = sum_times/len(all_times)

for t,d in zip(all_times,all_data):
            eventFile = int(d.split(',')[0])
            Pt = float(d.split(',')[1])
            if t >= mean_time:
                print("{0},{1},{2}".format(last_antiNucleus,eventFile,Pt))

#key - antiNucleus INT
#data : 
""" 
1 - eventFile UINT
2 - Pt  FLOAT
"""