# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 02:22:02 2018

@author: Thomas
"""

import matplotlib.pyplot as plt
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import random
import datetime as dt
import matplotlib.pyplot as plt
from subprocess import check_output
import pickle

import os #change to data

with open('C:\\Users\\Thoams\\Desktop\\MY STUFF\\Projects\\stockOberFlow\\AllData', "rb") as f:
    data = pickle.load(f)

def plotPrice(df):
    plt.plot(df['Price'])
    plt.show()
    
def plotVolume(df):
    plt.plot(df['Volume'])
    plt.show()
    
def plotMomentum(df):
    plt.plot(df['Volume*Price'])
    plt.show()
    
plotPrice(data[1])
plotVolume(data[1])
plotMomentum(data[1])