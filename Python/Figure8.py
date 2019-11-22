#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 09:25:35 2019

@author: ep9k
"""

import pandas as pd

data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj', 'Ram', 'Vijay', 'Rahim'],  
        'Qualification': ['Msc', 'MA', 'Msc', 'Msc', 'PhD', 'MD', 'PhD']} 

df = pd.DataFrame(data)

address = ['Delhi', 'Delhi', 'Chennai', 'Bangalore', 'Mumbai', 'Bangalore', 'Mumbai'] 

df['Address'] = address 

#df.loc[df['Address'] == 'Delhi', 'Country'] = 'India'

#df.loc[(df['Address'] == 'Delhi') & (df['Qualification'] == 'MA'), 'Country'] = 'India MA'

print(df)
    