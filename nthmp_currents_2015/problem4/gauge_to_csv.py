#!/usr/bin/python

from clawpack.visclaw.data import ClawPlotData
# import matplotlib.pyplot as plt
import numpy as np
import os


def process_gauge(gaugeNo, output):
    plotdata = ClawPlotData()
    plotdata.outdir = '_output'   # set to the proper output directory
    g = plotdata.getgauge(gaugeNo)
    # g.t is the array of times
    # g.q is the array of values recorded at the gauges (g.q[m,n] is the m`th variable at time `t[n])
    t = g.t
    h = g.q[0,:]
    u = np.where(h>0.001,g.q[1,:]/h,0.)
    v = np.where(h>0.001,g.q[2,:]/h,0.)
    h = h - h[:10].sum()/10.
    hu2 = h*u**2
    hv2 = h*v**2
    header = "Time (s), water depth (m), u-velocity (m/s), v-velocity (m/s), hu^2 (m^3/s^2), hv^2 (m^3/s^2)"
    if 'data_at_gauges_txt' not in os.listdir('./'):
        os.mkdir('./data_at_gauges_txt')
    result = np.vstack((t, h, u, v, hu2, hv2))
    result = result.transpose()
    np.savetxt('./data_at_gauges_txt/'+output, result, delimiter=',', header=header)

output = 'WG1_geoclaw_for_tecplot.txt'
process_gauge(1, output)
output = 'WG3_geoclaw_for_tecplot.txt'
process_gauge(3, output)


gaugeA_no = [101, 102, 103, 104, 105, 106, 107, 108, 109]
gaugeB_no = [201, 202, 203, 204, 205, 206, 207, 208, 209]
gaugeC_no = [301, 302, 303, 304, 305, 306, 307, 308, 309]
gaugeD_no = [401, 402, 403, 404]
gaugeA = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9']
gaugeB = ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9']
gaugeC = ['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9']
gaugeD = ['d1', 'd2', 'd3', 'd4']
for n, name in zip(gaugeA_no, gaugeA):
    output = name+'_geoclaw_for_tecplot.txt'
    process_gauge(n, output)
for n, name in zip(gaugeB_no, gaugeB):
    output = name+'_geoclaw_for_tecplot.txt'
    process_gauge(n, output)
for n, name in zip(gaugeC_no, gaugeC):
    output = name+'_geoclaw_for_tecplot.txt'
    process_gauge(n, output)
for n, name in zip(gaugeD_no, gaugeD):
    output = name+'_geoclaw_for_tecplot.txt'
    process_gauge(n, output)

