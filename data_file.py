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
string=['c_0001.txt','c_0002.txt','c_0003.txt','c_0004.txt','c_0005.txt','c_0006.txt','c_0007.txt','c_0008.txt','c_0009.txt','c_0010.txt','c_0011.txt','c_0012.txt','c_0013.txt','c_0014.txt','c_0015.txt']
string1=['p1.txt','p2.txt','p3.txt','p4.txt','p5.txt','p6.txt','p7.txt','p8.txt','p9.txt','p10.txt','p11.txt','p12.txt','p13.txt','p14.txt','p15.txt','p16.txt','p17.txt','p18.txt','p19.txt','p20.txt','p21.txt','p22.txt','p23.txt','p24.txt','p25.txt']
for p in range (0,len(string)):
         
    array,ps,gas,pd,gad= [],[],[],[],[]
    file_read(string[p])
    
    
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


for p in range (0,len(string1)):
    array,ps,gas,pd,gad= [],[],[],[],[]
    file_read(string1[p])
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

