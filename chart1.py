#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 11:20:05 2017

@author: traceyvanpuyvelde
"""
import pandas as pd
import numpy as np
from sklearn import tree
import matplotlib.pyplot as plt
import seaborn as sns

train_file = 'train.csv'
train = pd.read_csv(train_file)

test_file = 'test.csv'
test = pd.read_csv(test_file)

target = train['SalePrice'].values
              
#set Seaborn style - default
sns.set()

#plot relationship              
_ = sns.swarmplot(x=train['MSZoning'], y=target, data=train)
_ = plt.xlabel('MSZoning')
_ = plt.ylabel('Sale Price')
plt.show()