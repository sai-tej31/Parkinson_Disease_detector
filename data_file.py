# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:21:28 2020

@author: sai_tej
"""

import numpy as np
import csv
from datetime import datetime
import os
import math
import time

fmt = '%Y-%m-%d %H:%M:%S'


def findtime(a,b):
    time = (a - b).total_seconds()/60
    if time < 0:
        time = time *(-1)
    return time

avg=[]

def file_read(fname):        
        with open(fname) as f:
                for line in f:
                        array.append(line)


healthy=['C_0001.txt','C_0002.txt','C_0003.txt','C_0004.txt','C_0005.txt','C_0006.txt','C_0007.txt','C_0008.txt','C_0009.txt','C_0010.txt','C_0011.txt','C_0012.txt','C_0013.txt','C_0014.txt','C_0015.txt']
parkinson=['p1.txt','p2.txt','p3.txt','p4.txt','p5.txt','p6.txt','p7.txt','p8.txt','p9.txt','p10.txt','p11.txt','p12.txt','p13.txt','p14.txt','p15.txt','p16.txt','p17.txt','p18.txt','p19.txt','p20.txt','p21.txt','p22.txt','p23.txt','p24.txt','p25.txt','H_P000-0001.txt','H_P000-0002.txt','H_P000-0003.txt','H_P000-0004.txt','H_P000-0007.txt','H_P000-0008.txt','H_P000-0010.txt','H_P000-0011.txt','H_P000-0012.txt','H_P000-0013.txt','H_P000-0014.txt','H_P000-0015.txt','H_P000-0016.txt','H_P000-0017.txt','H_P000-0018.txt','H_P000-0019.txt','H_P000-0020.txt','H_P000-0021.txt','H_P000-0022.txt','H_P000-0023.txt.','H_P000-0024.txt','H_P000-0025.txt','H_P000-0028.txt','H_P000-0029.txt','H_P000-0030.txt','H_P000-0031.txt','H_P000-0032.txt','H_P000-0033.txt','H_P000-0034.txt','H_P000-0035.txt','H_P000-0036.txt','H_P000-0037.txt','H_P000-0039.txt','H_P000-0040.txt','H_P000-0041.txt','H_P000-0042.txt','H_P000-0042.txt']


for p in range (0,len(healthy)):
         
    array,ps,gas,pd,gad,pc,gac= [],[],[],[],[],[],[]
    dr_dt_s,dr_dtheta_s,dr_dt_d,dr_dtheta_d = [],[],[],[]
    time_s,time_d,time_c =[],[],[]
    radius_s,radius_d=[],[]
    x_s,y_s,x_d,y_d =[],[],[],[]
    
    file_read(healthy[p])
    
    for i in range (0,len(array)):
        if int(array[i].split(';')[6])==0:
            ps.append(int(array[i].split(';')[3]))
            gas.append(int(array[i].split(';')[4]))
            x_s.append(int(array[i].split(';')[0]))
            y_s.append(int(array[i].split(';')[1]))
            radius_s.append(math.sqrt(int(array[i].split(';')[0]) **2 + int(array[i].split(';')[1])**2))
            dt_object = datetime.fromtimestamp(int(array[i].split(';')[5]))
            time_s.append(datetime.strptime(str(dt_object), fmt))
        
        
        
        elif int(array[i].split(';')[6])==1:
            pd.append(int(array[i].split(';')[3]))
            gad.append(int(array[i].split(';')[4]))
            x_d.append(int(array[i].split(';')[0]))
            y_d.append(int(array[i].split(';')[1]))
            radius_d.append(math.sqrt(int(array[i].split(';')[0]) **2 + int(array[i].split(';')[1])**2))
            dt_object = datetime.fromtimestamp(int(array[i].split(';')[5]))
            time_d.append(datetime.strptime(str(dt_object), fmt))
                       
            
    if len(radius_s) != 0:
        for i in range(int(len(x_s)/10)-1):
            if time.mktime(time_s[i+1].timetuple())-time.mktime(time_s[i].timetuple()) !=0: 
                dr_dt_s.append((radius_s[i+1]-radius_s[i])/(time.mktime(time_s[i+1].timetuple())-time.mktime(time_s[i].timetuple()))/60)
            else:
                dr_dt_s.append(0)
            if math.atan(y_s[i+1]/x_s[i+1])-math.atan(y_s[i]/x_s[i]) != 0:
                dr_dtheta_s.append((radius_s[i+1]-radius_s[i])/(math.atan(y_s[i+1]/x_s[i+1])-math.atan(y_s[i]/x_s[i])))
            else:
                dr_dtheta_s.append(0)
        avg.append({'pressure' : np.average(ps),'grip_angle':np.average(gas),'timestamp': findtime(time_s[-1],time_s[0]),'state': 'static','dr/dt-std':np.std(dr_dt_s),'dr/dt-mean':np.average(dr_dt_s),'dr/dtheta-std':np.std(dr_dtheta_s),'dr/dtheta-mean':np.average(dr_dtheta_s),'max-radius':np.max(radius_s),'status' : 1 })
        
    if len(radius_d) != 0:
        for i in range(int(len(radius_d)/10) -1):
            if time.mktime(time_d[i+1].timetuple())-time.mktime(time_d[i].timetuple()):
                dr_dt_d.append((radius_d[i+1]-radius_d[i])/(time.mktime(time_d[i+1].timetuple())-time.mktime(time_d[i].timetuple()))/60)
            else:
                dr_dt_d.append(0)
            if math.atan(y_d[i+1]/x_d[i+1])-math.atan(y_d[i]/x_d[i]) != 0:
                dr_dtheta_d.append((radius_d[i+1]-radius_d[i])/(math.atan(y_d[i+1]/x_d[i+1])-math.atan(y_d[i]/x_d[i])))
            else:
                dr_dtheta_d.append(0)
        avg.append({'pressure' : np.average(pd),'grip_angle':np.average(gad),'timestamp': findtime(time_d[-1],time_d[0]),'state': 'dynamic','dr/dt-std':np.std(dr_dt_d),'dr/dt-mean':np.average(dr_dt_d),'dr/dtheta-std':np.std(dr_dtheta_d),'dr/dtheta-mean':np.average(dr_dtheta_d),'max-radius':np.max(radius_d),'status' : 1 })

        
        

for p in range (0,len(parkinson)):
         

    array,ps,gas,pd,gad,pc,gac= [],[],[],[],[],[],[]
    dr_dt_s,dr_dtheta_s,dr_dt_d,dr_dtheta_d = [],[],[],[]
    time_s,time_d,time_c =[],[],[]
    radius_s,radius_d=[],[]
    x_s,y_s,x_d,y_d =[],[],[],[]
        
    
    
    file_read(parkinson[p])
    
    for i in range (0,len(array)):
        if int(array[i].split(';')[6])==0:
            ps.append(int(array[i].split(';')[3]))
            gas.append(int(array[i].split(';')[4]))
            x_s.append(int(array[i].split(';')[0]))
            y_s.append(int(array[i].split(';')[1]))          
            radius_s.append(math.sqrt(int(array[i].split(';')[0]) **2 + int(array[i].split(';')[1])**2))
            dt_object = datetime.fromtimestamp(int(array[i].split(';')[5]))
            time_s.append(datetime.strptime(str(dt_object), fmt))
          
        
        elif int(array[i].split(';')[6])==1:
            pd.append(int(array[i].split(';')[3]))
            gad.append(int(array[i].split(';')[4]))            
            x_d.append(int(array[i].split(';')[0]))
            y_d.append(int(array[i].split(';')[1]))
            radius_d.append(math.sqrt(int(array[i].split(';')[0]) **2 + int(array[i].split(';')[1])**2))
            dt_object = datetime.fromtimestamp(int(array[i].split(';')[5]))
            time_d.append(datetime.strptime(str(dt_object), fmt))
           
    if len(radius_s) != 0:
        for i in range(int(len(x_s)/10)-1):
            if time.mktime(time_s[i+1].timetuple())-time.mktime(time_s[i].timetuple()) !=0: 
                dr_dt_s.append((radius_s[i+1]-radius_s[i])/(time.mktime(time_s[i+1].timetuple())-time.mktime(time_s[i].timetuple()))/60)
            else:
                dr_dt_s.append(0)
            if math.atan(y_s[i+1]/x_s[i+1])-math.atan(y_s[i]/x_s[i]) != 0:
                dr_dtheta_s.append((radius_s[i+1]-radius_s[i])/(math.atan(y_s[i+1]/x_s[i+1])-math.atan(y_s[i]/x_s[i])))
            else:
                dr_dtheta_s.append(0)
        avg.append({'pressure' : np.average(ps),'grip_angle':np.average(gas),'timestamp': findtime(time_s[-1],time_s[0]),'state': 'static','dr/dt-std':np.std(dr_dt_s),'dr/dt-mean':np.average(dr_dt_s),'dr/dtheta-std':np.std(dr_dtheta_s),'dr/dtheta-mean':np.average(dr_dtheta_s),'max-radius':np.max(radius_s),'status' : 0 })
        
    if len(radius_d) != 0:
        for i in range(int(len(radius_d)/10) -1):
            if time.mktime(time_d[i+1].timetuple())-time.mktime(time_d[i].timetuple()):
                dr_dt_d.append((radius_d[i+1]-radius_d[i])/(time.mktime(time_d[i+1].timetuple())-time.mktime(time_d[i].timetuple()))/60)
            else:
                dr_dt_d.append(0)
            if math.atan(y_d[i+1]/x_d[i+1])-math.atan(y_d[i]/x_d[i]) != 0:
                dr_dtheta_d.append((radius_d[i+1]-radius_d[i])/(math.atan(y_d[i+1]/x_d[i+1])-math.atan(y_d[i]/x_d[i])))
            else:
                dr_dtheta_d.append(0)
        avg.append({'pressure' : np.average(pd),'grip_angle':np.average(gad),'timestamp': findtime(time_d[-1],time_d[0]),'state': 'dynamic','dr/dt-std':np.std(dr_dt_d),'dr/dt-mean':np.average(dr_dt_d),'dr/dtheta-std':np.std(dr_dtheta_d),'dr/dtheta-mean':np.average(dr_dtheta_d),'max-radius':np.max(radius_d),'status' : 0 })

    

    

    

csv_columns = ['pressure','grip_angle','timestamp','state','dr/dt-std','dr/dt-mean','dr/dtheta-std','dr/dtheta-mean','max-radius','status']

csv_file = "dataset_file.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in avg:
            writer.writerow(data)
except IOError:
    print("I/O error")  

