#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 21:12:30 2021

@author: hamimehrabi
"""


import os

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
        
    
sd = find('data_1.txt', '/Users/hamimehrabi/Desktop/PythonLab/Server/Storage')