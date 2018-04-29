# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 22:50:08 2018

@author: Pankaj
"""

import subprocess
import re
import os
from datetime import datetime
import time


if not os.path.exists("hosts.txt"):
    raise ValueError("No hosts file found.") 
    
hostsFile = open('hosts.txt', "r")
lines = hostsFile.readlines()

if len(lines)==0:
    raise ValueError("Hosts file empty.")
pingtimes=[]

for line in lines:
    line = line.strip( )
    args = ["ping", "-n", "4", "-l", "1", "-w", "100", line]

    ping = subprocess.Popen(
        args,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    )

    time1=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    out, error = ping.communicate()
    #print(out)
    #output=str(out)
    responsetimes = re.findall(r'bytes=1 time=(\d+)ms', str(out))
    average= re.findall(r'Average = (\d+)ms', str(out))
    loss= re.findall(r'Lost = (\d+)', str(out))
    #print(responsetimes)
    pingtimes=pingtimes+responsetimes
    print("Maximum ping time is", max(pingtimes))
    print("Minimum ping time is", min(pingtimes))
    print("Average ping time is", average[0])
    print("Packet Loss:        ", loss[0])
    
    if not os.path.exists('./records'):
        os.makedirs('./records')
    
    f = open('records/%s.txt' %line, 'a')
    f.write("Time:  " + time1 + "\n")
    f.write("Hostname:  " + line + "\n")
    f.write("Minumum Response:  " + min(pingtimes) + "ms" + "\n")
    f.write("Maximum Response:  " + max(pingtimes) + "ms" + "\n")
    f.write("Average Response:  " + average[0] + "ms" + "\n")
    f.write("Packet Loss:  " + loss[0] + " packets" + "\n")
    f.write("\n")
    f.close()
    
    t1=time.time()
    f = open('records/avg_%s.txt' %line, 'a')
    f.write(str(int(t1))+ ','+average[0]+"\n")
    f.close()


hostsFile.close()



