# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 14:11:29 2021

@author: Vivien
"""

n_traces = 1000
trace = [0]*n_traces
N = 53

#Open trace

for i in range(n_traces):
    file_name = "traces/curve_" + str(i) +".txt"
    curve_file = open(file_name)
    data = curve_file.read()
    trace[i] = data.split(" ")
    

