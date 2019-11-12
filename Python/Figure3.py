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
    
    elsevier_freedom_collection = sb.make_freedom_collection_provider()
    elsevier_subscribed_titles = sb.make_elsevier_subscribed_titles_provider()
    
    elsevier_freedom_jr1_downloads = elsevier_freedom_collection['Downloads JR1 2017'].sum()
    elsevier_subscribed_jr1_downloads = elsevier_subscribed_titles['Downloads JR1 2017'].sum()

    print(elsevier_subscribed_jr1_downloads)
    
    
    cost_data = pd.read_excel('1figr_U_Virginia_edit_Supp_Data.xlsx')
    
    package = cost_data['Package']
    cost_2017 = cost_data['Total cost for 2017']
    
    
    
    
figure3c()