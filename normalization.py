#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np

def normalization (fname, attr, normType):
    '''
    Input Parameters:
        fname: Name of the csv file contiaining historical quotes
        attr: The attribute to be normalized 
        normType: The type of normalization 
    Output:
        a dictionary where each key is the original column value and each value is the normalised column value. 
    '''
    result = {}
    
    df = pd.read_csv(fname)
    attr_values = df[attr].values.tolist()
    
    normalized = []
    for val in attr_values:
        if normType == 'min_max':
            min_value = min(attr_values)
            max_value = max(attr_values)
            normalized_value = (val - min_value) / (max_value - min_value)
            normalized.append(normalized_value)
        
        elif normType == 'z_score':
            mean = sum(attr_values) / len(attr_values)
            stdev = df[attr].std()
            normalized_value = (val - mean) / stdev
            normalized.append(normalized_value)
    
    keys_values = zip(attr_values, normalized)
            
    result = dict(keys_values)
            
    return result        

