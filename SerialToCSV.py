import csv
from datetime import datetime
import time
import serial
import numpy as np
import os
import pandas as pd

ser = serial.Serial('COM8', 115200)
ser.flushInput()
ser.flushOutput()
y_value = 1
x_value = datetime.timestamp(datetime.now())

fieldnames = ["x_value", "y_value"]

with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:

    with open('data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            "x_value": x_value,
            "y_value": y_value,

        }
        readlst = ser.readline().split(b',')
        if readlst[0] == b'<':
            x_value = (datetime.timestamp(datetime.now()))
            y_value = (float(readlst[2])/9.81)
        csv_writer.writerow(info)
