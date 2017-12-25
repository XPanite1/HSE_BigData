#!/usr/bin/env python
# coding=utf-8
import sys

# just find mean of time for each antiNucleus
# output pairs: antiNucleus, mean_time


sum_times = 0.0
count = 0
last_antiNucleus = -1

for line in sys.stdin:
    antiNucleus,time = line.split('\t')
    
    if antiNucleus != last_antiNucleus:
        if last_antiNucleus != -1: 
            # print data
            mean_time = sum_times/count
            print("{0},{1}".format(last_antiNucleus,mean_time))

        last_antiNucleus = antiNucleus
        sum_times = 0.0
        count = 0

    sum_times += float(time)
    count += 1

mean_time = sum_times/count
print("{0},{1}".format(last_antiNucleus,mean_time))

#INPUT:
#key - antiNucleus INT
#value - Prodtime FLOAT

#OUTPUT:
# antiNucleus, mean_time