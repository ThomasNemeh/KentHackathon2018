# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 03:56:10 2018

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

# Dimensions of dataset
#n = data.shape[0]
#p = data.shape[1]
# Make data a numpy array
#data = data.values

print(data[0].iloc[x]['Label'])

