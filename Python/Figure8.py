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

    unique_disciplines = original_1figr_data_with_disciplines['Discipline'].unique().tolist()

    for i in unique_disciplines:
        if type(i) == float:
            unique_disciplines.remove(i)
    unique_disciplines.sort()

    stats_by_discipline = []

    for discipline in unique_disciplines:
        
        subscribed_subset_by_discipline = subscribed_titles_provider.loc[subscribed_titles_provider['Discipline'] == discipline]
        subscribed_jr1_downloads = subscribed_subset_by_discipline['Downloads JR1 2017'].sum()

        freedom_subset_by_discipline = freedom_collection_provider.loc[freedom_collection_provider['Discipline'] == discipline]
        freedom_jr1_downloads = freedom_subset_by_discipline['Downloads JR1 2017'].sum()
        
        stats_by_discipline.append((discipline, subscribed_jr1_downloads, freedom_jr1_downloads))
            
    #sorts disciplines by sum of total # of jr1 downloads
    arrangement = sorted(stats_by_discipline, key=lambda x: (x[1] + x[2]), reverse=True) 
    
    #splitting elements of tuples in arrangement into lists so it is easier to plot
    disciplines_list = [i[0] for i in arrangement]
    subscribed_total = [i[1] for i in arrangement]
    freedom_total = [i[2] for i in arrangement]


#####FIX PLOT
    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle(f'JR1 downloads by Discipline')
    plot = plt.bar(disciplines_list, subscribed_total, width=.3, color='green')   
    plt.bar(disciplines_list, freedom_total, width=.3, color='orange')
    
    plt.xticks(rotation=90)
    
    for i in plot:
        score = i.get_height()
        plt.text(i.get_x(),                       #y axis location
                 score,                           #x axis location
                 '{0:g}'.format(float(score)))    #format floats without decimals
    
       

figure8e()

    

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
    



    
    
    