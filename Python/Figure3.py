#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 14:47:42 2019

@author: ep9k
"""

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
import matplotlib.patches as mpatches

import sandbox as sb

filename = '1figr_U_Virginia_Original (1) (1).xlsx'
your_institution = 'UVA'


def figure3c():
    
    cost_data = pd.read_excel('1figr_U_Virginia_edit_Supp_Data.xlsx')
    
    package = cost_data['Package']
    cost_2017 = cost_data['Total cost for 2017']
    
    
    
    
figure3c()