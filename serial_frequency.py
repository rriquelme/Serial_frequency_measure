# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 15:59:54 2020

@author: rers9
"""

import serial
import time

# open serial port
ser = serial.Serial('COM4', 115200)  
# check which port was really used
print(ser.name)
#Clear buffer
print(ser.readline()) # write a string

#Start counting for 'sec' seconds, for 3 times:
# 1.-
count = 0
sec = 20
t_end = time.time() + sec
while time.time() < t_end:
    ser.readline()
    count+=1
print(count/sec)
# 2.-
count = 0
t_end = time.time() + sec
while time.time() < t_end:
    ser.readline()
    count+=1
print(count/sec)
# 3.-
count = 0
t_end = time.time() + sec
while time.time() < t_end:
    ser.readline()
    count+=1
print(count/sec)

# close port
ser.close()   