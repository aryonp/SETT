#!/usr/bin/python
import os
import sys
import csv
import datetime
import time

#SETT = Speedtest automatEd tesT boT

def sett():

        #run speedtest-cli to some server in MUCZ
        print 'Running test'
        a = os.popen("speedtest-cli --server 3578 --simple").read()
        print 'Test completed'
        
	#breakdown result
        lines = a.split('\n')
        print a
        ts = time.time()
        date =datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        
	#if cannot connect
        if "Cannot" in a:
                p = 100
                d = 0
                u = 0
        
	#extract the values for ping down and up values
        else:
                p = lines[0][6:11]
                d = lines[1][10:14]
                u = lines[2][8:12]
       
	print date, p, d, u

        #save data to home
        out_file = open('/home/aryonp/data.csv', 'a')
        writer = csv.writer(out_file)
        writer.writerow((ts*1000,p,d,u))
        out_file.close()

if __name__ == '__main__':
        sett()
        print 'Finished'
