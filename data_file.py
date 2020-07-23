# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:21:28 2020

@author: sai_tej
"""
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures   
import pandas as pd
import csv
import matplotlib.pyplot as plt
from datetime import datetime

fmt = '%Y-%m-%d %H:%M:%S'

avg=[]

def file_read(fname):        
        with open(fname) as f:
                for line in f:
                        array.append(line)
healthy=['c_0001.txt','c_0002.txt','c_0003.txt','c_0004.txt','c_0005.txt','c_0006.txt','c_0007.txt','c_0008.txt','c_0009.txt','c_0010.txt','c_0011.txt','c_0012.txt','c_0013.txt','c_0014.txt','c_0015.txt']
parkinson=['p1.txt','p2.txt','p3.txt','p4.txt','p5.txt','p6.txt','p7.txt','p8.txt','p9.txt','p10.txt','p11.txt','p12.txt','p13.txt','p14.txt','p15.txt','p16.txt','p17.txt','p18.txt','p19.txt','p20.txt','p21.txt','p22.txt','p23.txt','p24.txt','p25.txt','H_P000-0001.txt','H_P000-0002.txt','H_P000-0003.txt','H_P000-0004.txt','H_P000-0007.txt','H_P000-0008.txt','H_P000-0010.txt','H_P000-0011.txt','H_P000-0012.txt','H_P000-0013.txt','H_P000-0014.txt','H_P000-0015.txt','H_P000-0016.txt','H_P000-0017.txt','H_P000-0018.txt','H_P000-0019.txt','H_P000-0020.txt','H_P000-0021.txt','H_P000-0022.txt','H_P000-0023.txt.','H_P000-0024.txt','H_P000-0025.txt','H_P000-0028.txt','H_P000-0029.txt','H_P000-0030.txt','H_P000-0031.txt','H_P000-0032.txt','H_P000-0033.txt','H_P000-0034.txt','H_P000-0035.txt','H_P000-0036.txt','H_P000-0037.txt','H_P000-0039.txt','H_P000-0040.txt','H_P000-0041.txt','H_P000-0042.txt','H_P000-0042.txt']
for p in range (0,len(healthy)):
         
    array,ps,gas,pd,gad= [],[],[],[],[]
    file_read(healthy[p])
    
    
    for i in range (0,len(array)):
        if int(array[i].split(';')[6])==0:
            ps.append(int(array[i].split(';')[3]))
            gas.append(int(array[i].split(';')[4]))
            dt_object = datetime.fromtimestamp(int(array[-1].split(';')[5]))
            dt_object1 = datetime.fromtimestamp(int(array[0].split(';')[5]))
            tstamp1 = datetime.strptime(str(dt_object), fmt)
            tstamp2 = datetime.strptime(str(dt_object1), fmt)
            time = (tstamp1 - tstamp2).total_seconds() / 60
            if time < 0:
                time = time *(-1)

        else:
            pd.append(int(array[i].split(';')[3]))
            gad.append(int(array[i].split(';')[4]))
            dt_object = datetime.fromtimestamp(int(array[-1].split(';')[5]))
            dt_object1 = datetime.fromtimestamp(int(array[0].split(';')[5]))
            tstamp1 = datetime.strptime(str(dt_object), fmt)
            tstamp2 = datetime.strptime(str(dt_object1), fmt)
            time = (tstamp1 - tstamp2).total_seconds() / 60
            if time < 0:
                time = time *(-1)


    avg.append({'pressure' : np.average(ps),'grip_angle':np.average(gas),'timestamp': time,'state': 'static' ,'status' : 1 })
    avg.append({'pressure' : np.average(pd),'grip_angle':np.average(gad),'timestamp': time,'state': 'dynamic' ,'status' : 1 })


for p in range (0,len(parkinson)):
    array,ps,gas,pd,gad= [],[],[],[],[]
    file_read(parkinson[p])
    for i in range (0,len(array)):
        if int(array[i].split(';')[6])==0:
            ps.append(int(array[i].split(';')[3]))
            gas.append(int(array[i].split(';')[4]))
            dt_object = datetime.fromtimestamp(int(array[-1].split(';')[5]))
            dt_object1 = datetime.fromtimestamp(int(array[0].split(';')[5]))
            tstamp1 = datetime.strptime(str(dt_object), fmt)
            tstamp2 = datetime.strptime(str(dt_object1), fmt)
            time = ((tstamp1 - tstamp2).total_seconds() / 60)
            if time < 0:
                time = time *(-1)
        else:
            pd.append(int(array[i].split(';')[3]))
            gad.append(int(array[i].split(';')[4]))
            dt_object = datetime.fromtimestamp(int(array[-1].split(';')[5]))
            dt_object1 = datetime.fromtimestamp(int(array[0].split(';')[5]))
            tstamp1 = datetime.strptime(str(dt_object), fmt)
            tstamp2 = datetime.strptime(str(dt_object1), fmt)
            time = (tstamp1 - tstamp2).total_seconds() / 60
            if time < 0:
                time = time *(-1)
    avg.append({'pressure' : np.average(ps),'grip_angle':np.average(gas),'timestamp': time,'state': 'static' ,'status' : 0 })
    avg.append({'pressure' : np.average(pd),'grip_angle':np.average(gad),'timestamp': time,'state': 'dynamic' ,'status' : 0 })


  
import csv
csv_columns = ['pressure','grip_angle','timestamp','state','status']

csv_file = "file.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in avg:
            writer.writerow(data)
except IOError:
    print("I/O error")  

