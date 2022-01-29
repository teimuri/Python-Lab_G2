#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 23:20:24 2021

@author: hamimehrabi
"""


import numpy as np
import pandas as pd
import math

print("***1***")

dum = np.arange(6)

dum = dum.reshape((3,2))

dum_1 = np.arange(9)

dum_1 = dum_1.reshape((3,3))

res_dum = np.hstack([dum, dum_1])

res = res_dum.ravel()

print(np.argmax(res))



print("***2***")

A = np.mat([[3,1,4],[1,5,9],[2,6,5]])

B = np.mat( [2,4,-1])

print(A.T)

print(np.abs(A))

print(np.linalg.inv(A))

print(np.linalg.eig(A))

print(np.linalg.svd(A))

print(np.linalg.qr(A))

print(np.linalg.solve(A, B.T))

