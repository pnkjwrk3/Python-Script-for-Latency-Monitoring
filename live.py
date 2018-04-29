# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 01:22:23 2018

@author: Pankaj
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--host", type = str, required=True)
args = parser.parse_args()
host =args.host

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
fig.canvas.set_window_title('%s' %host)

def animate(i):
    pullData = open("records/avg_%s.txt" %host ,"r").read()
    dataArray = pullData.split('\n')
    xar = []
    yar = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            #print(x)
            #print(y)
            xar.append(int(x))
            yar.append(int(y))
    ax1.clear()
    ax1.plot(xar,yar)
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()