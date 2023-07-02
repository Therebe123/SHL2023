import pandas as pd
import numpy as np
import random
from sklearn.preprocessing import OneHotEncoder

from scipy.stats import kurtosis
from scipy.stats import skew

def Sum_dataset(data, cols, window_size):
    
    data[['Sum_' + col for col in cols]] = data[cols].rolling(window_size,center=True,min_periods=1).sum()
    
    # 返回转换后的数据集
    return data

def Mean_dataset(data, cols, window_size):
    
    data[['Mean_' + col for col in cols]] = data[cols].rolling(window_size,center=True,min_periods=1).mean()
    
    # 返回转换后的数据集
    return data

def Var_dataset(data, cols, window_size):
    
    data[['Var_' + col for col in cols]] = data[cols].rolling(window_size,center=True,min_periods=1).var()
    
    # 返回转换后的数据集
    return data

def Max_dataset(data, cols, window_size):
    
    data[['Max_' + col for col in cols]] = data[cols].rolling(window_size,center=True,min_periods=1).max()
    
    # 返回转换后的数据集
    return data

def Min_dataset(data, cols, window_size):
    
    data[['Min_' + col for col in cols]] = data[cols].rolling(window_size,center=True,min_periods=1).min()
    
    # 返回转换后的数据集
    return data

def Kurtosis_dataset(data, cols, window_size):
    
    data[['Kurtosis_' + col for col in cols]] = data[cols].rolling(window_size,center=True,min_periods=1).kurt()
    
    # 返回转换后的数据集
    return data

def Skew_dataset(data, cols, window_size):
    
    data[['Skew_' + col for col in cols]] = data[cols].rolling(window_size,center=True,min_periods=1).skew()
    
    # 返回转换后的数据集
    return data

def Quantile_dataset(data, cols, window_size,quantiles):
    
    data[['Quantile_' + str(quantiles) + '_' + col for col in cols]] = data[cols].rolling(window_size,center=True,min_periods=1).quantile(quantiles)

    
    # 返回转换后的数据集
    return data

# def IQR_dataset(data, cols, window_size): ## 算太慢了，极度不推荐使用
    
#     data[['IQR_' + col for col in cols]] = data[cols].rolling(window_size,center=True,min_periods=1).agg(
#          lambda x:x.quantile(0.75)-x.quantile(0.25)
#     )
    
#     # 返回转换后的数据集
#     return data


