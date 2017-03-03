#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 10:52:37 2017

@author: traceyvanpuyvelde
"""
import pandas as pd
import numpy as np
import sklearn
import matplotlib.pyplot as plt
import scipy.stats as stats
from sklearn.linear_model import LinearRegression


train_file = 'train.csv'
train = pd.read_csv(train_file)

#clean data
train['LotFrontage'] = train['LotFrontage'].fillna(train['LotFrontage'].median())
train['MasVnrArea'] = train['MasVnrArea'].fillna(0)

features_1 = train[['MSSubClass', 'LotFrontage', 'LotArea', 'OverallQual', 'OverallCond', 'YearBuilt', 'YearRemodAdd', 'MasVnrArea', 'BsmtFinSF1', 'BsmtFinSF2', 'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'LowQualFinSF', 'GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath', 'HalfBath', 'BedroomAbvGr', 'KitchenAbvGr', 'TotRmsAbvGrd', 'Fireplaces', 'GarageCars', 'GarageArea', 'WoodDeckSF', 'OpenPorchSF', 'EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'PoolArea', 'MiscVal', 'MoSold', 'YrSold']]

test_file = 'test.csv'
test = pd.read_csv(test_file)

target = train['SalePrice']
              
              
#create linear regression object
lm = LinearRegression()
lm.fit(features_1, target)
features_1_coeff = pd.DataFrame(list(zip(features_1.columns, lm.coef_)), columns=['features', 'coeffs'])


plt.scatter(train['OverallQual'], train['SalePrice'])
plt.xlabel('Overall Quality')
plt.ylabel('Housing Price')
plt.title('Relationship between quality and price')
plt.show()
