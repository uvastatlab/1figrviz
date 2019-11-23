#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 09:25:35 2019

@author: ep9k
"""

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
import matplotlib.patches as mpatches


import reusable_functions as rf




def figure8e():
    """First creates 'discipline' field for all providers in the Original 1figr dataset.
    Then splits elsevier into elsevier freedom provider and elsevier subscribed titles provider
    
    This is counting JR1 downloads by discipline for the subscribed titles and freedom collection providers"""
    
    original_1figr_data_with_disciplines = rf.make_disciplines_column()
    subscribed_titles_provider = rf.make_elsevier_subscribed_titles_with_disciplines(original_1figr_data_with_disciplines)
    freedom_collection_provider = rf.make_freedom_collection_provider_with_disciplines(original_1figr_data_with_disciplines)
     
    unique_disciplines = original_1figr_data_with_disciplines['Discipline'].unique()

    
    jr1_downloads_by_provider = []
    
    #count of JR1 downloads by discipline for subscribed titles provider
    subscribed_titles_disciplines = subscribed_titles_provider.groupby('Discipline')
    count_list = subscribed_titles_disciplines['Downloads JR1 2017'].sum().tolist()
    jr1_downloads_by_provider.append(count_list)
    
    #count of JR1 downloads by discipline for freedom collection provider
    freedom_collection_disciplines = freedom_collection_provider.groupby('Discipline')
    count_list = freedom_collection_disciplines['Downloads JR1 2017'].sum().tolist()
    jr1_downloads_by_provider.append(count_list)
    
#TODO: get list of disciplines, plot count per discipline
    

def figure8f():
    """First creates 'discipline' field for all providers in the Original 1figr dataset.
    Then splits elsevier into elsevier freedom provider and elsevier subscribed titles provider
    
    This is counting JR5 downloads by discipline for the subscribed titles and freedom collection providers"""
 
    original_1figr_data_with_disciplines = rf.make_disciplines_column()
    subscribed_titles_provider = rf.make_elsevier_subscribed_titles_with_disciplines(original_1figr_data_with_disciplines)
    freedom_collection_provider = rf.make_freedom_collection_provider_with_disciplines(original_1figr_data_with_disciplines)
     
    unique_disciplines = original_1figr_data_with_disciplines['Discipline'].unique()

    
    jr5_downloads_by_provider = []
    
    #count of JR5 downloads by discipline for subscribed titles provider
    subscribed_titles_disciplines = subscribed_titles_provider.groupby('Discipline')
    count_list = subscribed_titles_disciplines['Downloads JR5 2017 in 2017'].sum().tolist()
    jr5_downloads_by_provider.append(count_list)
    
    #count of JR5 downloads by discipline for freedom collection provider
    freedom_collection_disciplines = freedom_collection_provider.groupby('Discipline')
    count_list = freedom_collection_disciplines['Downloads JR5 2017 in 2017'].sum().tolist()
    jr5_downloads_by_provider.append(count_list)

#TODO: get list of disciplines, plot count per discipline

    

def figure8g():
    """First creates 'discipline' field for all providers in the Original 1figr dataset.
    Then splits elsevier into elsevier freedom provider and elsevier subscribed titles provider
    
    This is counting references by discipline for the subscribed titles and freedom collection providers"""
   
    original_1figr_data_with_disciplines = rf.make_disciplines_column()
    subscribed_titles_provider = rf.make_elsevier_subscribed_titles_with_disciplines(original_1figr_data_with_disciplines)
    freedom_collection_provider = rf.make_freedom_collection_provider_with_disciplines(original_1figr_data_with_disciplines)
     
    unique_disciplines = original_1figr_data_with_disciplines['Discipline'].unique()

    
    references_by_provider = []
    
    #count of JR5 downloads by discipline for subscribed titles provider
    subscribed_titles_disciplines = subscribed_titles_provider.groupby('Discipline')
    count_list = subscribed_titles_disciplines['References'].sum().tolist()
    references_by_provider.append(count_list)
    
    #count of JR5 downloads by discipline for freedom collection provider
    freedom_collection_disciplines = freedom_collection_provider.groupby('Discipline')
    count_list = freedom_collection_disciplines['References'].sum().tolist()
    references_by_provider.append(count_list)
    
#TODO: get list of disciplines, plot count per discipline


def figure8h():
    """First creates 'discipline' field for all providers in the Original 1figr dataset.
    Then splits elsevier into elsevier freedom provider and elsevier subscribed titles provider
    
    This is counting papers by discipline for the subscribed titles and freedom collection providers"""
    original_1figr_data_with_disciplines = rf.make_disciplines_column()
    subscribed_titles_provider = rf.make_elsevier_subscribed_titles_with_disciplines(original_1figr_data_with_disciplines)
    freedom_collection_provider = rf.make_freedom_collection_provider_with_disciplines(original_1figr_data_with_disciplines)
     
    unique_disciplines = original_1figr_data_with_disciplines['Discipline'].unique()

    
    papers_by_provider = []
    
    #count of JR5 downloads by discipline for subscribed titles provider
    subscribed_titles_disciplines = subscribed_titles_provider.groupby('Discipline')
    count_list = subscribed_titles_disciplines['Papers'].sum().tolist()
    papers_by_provider.append(count_list)
    
    #count of JR5 downloads by discipline for freedom collection provider
    freedom_collection_disciplines = freedom_collection_provider.groupby('Discipline')
    count_list = freedom_collection_disciplines['Papers'].sum().tolist()
    papers_by_provider.append(count_list)

#TODO: get list of disciplines, plot count per discipline
    



    
    
    