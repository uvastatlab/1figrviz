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
    
    This is counting JR1 downloads by discipline for the subscribed titles and freedom collection providers
    
    Chart Type: Dot Plot/Scatter Plot
    Y-Axis: Discipline
    Y-Axis Data Source: Original 1Figr Dataset, Journals Per Provider, Provider
                        Elsevier_2019, Subscribed Journal List 2019
    X-Axis: Number of JR1 Downloads
    X-Axis Data Source: Original 1Figr Dataset, Journals Per Provider, Provider
                        Elsevier_2019, Subscribed Journal List 2019
    """
    
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
    arrangement = sorted(stats_by_discipline, key=lambda x: (x[1] + x[2])) 
    
    #splitting elements of tuples in arrangement into lists so it is easier to plot
    disciplines_list = [i[0] for i in arrangement]
    subscribed_total = [i[1] for i in arrangement]
    freedom_total = [i[2] for i in arrangement]

    #make plot
    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle(f'JR1 downloads by Discipline')
 
    plot = plt.scatter(subscribed_total, disciplines_list, color='blue')
    plot2 = plt.scatter(freedom_total, disciplines_list, color='orange')

    subscribed_legend_label = mpatches.Patch(color='blue', label='Elsevier Subscribed')
    freedom_legend_label = mpatches.Patch(color='orange', label='Elsevier Freedom')
    plt.xlabel('Number of JR1 Downloads')
    plt.legend(loc='lower right', handles=[subscribed_legend_label, freedom_legend_label])
    
  
    

def figure8f():
    """First creates 'discipline' field for all providers in the Original 1figr dataset.
    Then splits elsevier into elsevier freedom provider and elsevier subscribed titles provider
    
    This is counting JR5 downloads by discipline for the subscribed titles and freedom collection providers
    
    Chart Type: Dot Plot/Scatter Plot
    Y-Axis: Discipline
    Y-Axis Data Source: Original 1Figr Dataset, Journals Per Provider, Provider
                        Elsevier_2019, Subscribed Journal List 2019
    X-Axis: Number of JR5 Downloads
    X-Axis Data Source: Original 1Figr Dataset, Journals Per Provider, Provider
                        Elsevier_2019, Subscribed Journal List 2019
    """
 
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
        subscribed_jr5_downloads = subscribed_subset_by_discipline['Downloads JR5 2017 in 2017'].sum()

        freedom_subset_by_discipline = freedom_collection_provider.loc[freedom_collection_provider['Discipline'] == discipline]
        freedom_jr5_downloads = freedom_subset_by_discipline['Downloads JR5 2017 in 2017'].sum()
        
        stats_by_discipline.append((discipline, subscribed_jr5_downloads, freedom_jr5_downloads))
            
    #sorts disciplines by sum of total # of jr5 downloads
    arrangement = sorted(stats_by_discipline, key=lambda x: (x[1] + x[2])) 
    
    #splitting elements of tuples in arrangement into lists so it is easier to plot
    disciplines_list = [i[0] for i in arrangement]
    subscribed_total = [i[1] for i in arrangement]
    freedom_total = [i[2] for i in arrangement]


    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle(f'JR5 downloads by Discipline')
 
    plot = plt.scatter(subscribed_total, disciplines_list, color='blue')
    plot2 = plt.scatter(freedom_total, disciplines_list, color='orange')

    subscribed_legend_label = mpatches.Patch(color='blue', label='Elsevier Subscribed')
    freedom_legend_label = mpatches.Patch(color='orange', label='Elsevier Freedom')
    plt.xlabel('Number of JR5 Downloads')
    plt.legend(loc='lower right', handles=[subscribed_legend_label, freedom_legend_label])

  

def figure8g():
    """First creates 'discipline' field for all providers in the Original 1figr dataset.
    Then splits elsevier into elsevier freedom provider and elsevier subscribed titles provider
    
    This is counting references by discipline for the subscribed titles and freedom collection providers.
    
    Chart Type: Dot Plot/Scatter Plot
    Y-Axis: Discipline
    Y-Axis Data Source: Original 1Figr Dataset, Journals Per Provider, Provider
                        Elsevier_2019, Subscribed Journal List 2019
    X-Axis: Number of References
    X-Axis Data Source: Original 1Figr Dataset, Journals Per Provider, Provider
                        Elsevier_2019, Subscribed Journal List 2019
    """
   
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
        subscribed_jr5_downloads = subscribed_subset_by_discipline['References'].sum()

        freedom_subset_by_discipline = freedom_collection_provider.loc[freedom_collection_provider['Discipline'] == discipline]
        freedom_jr5_downloads = freedom_subset_by_discipline['References'].sum()
        
        stats_by_discipline.append((discipline, subscribed_jr5_downloads, freedom_jr5_downloads))
            
    #sorts disciplines by sum of total # of jr5 downloads
    arrangement = sorted(stats_by_discipline, key=lambda x: (x[1] + x[2])) 
    
    #splitting elements of tuples in arrangement into lists so it is easier to plot
    disciplines_list = [i[0] for i in arrangement]
    subscribed_total = [i[1] for i in arrangement]
    freedom_total = [i[2] for i in arrangement]


    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle(f'References by Discipline')
 
    plot = plt.scatter(subscribed_total, disciplines_list, color='blue')
    plot2 = plt.scatter(freedom_total, disciplines_list, color='orange')

    subscribed_legend_label = mpatches.Patch(color='blue', label='Elsevier Subscribed')
    freedom_legend_label = mpatches.Patch(color='orange', label='Elsevier Freedom')
    plt.xlabel('Number of References')
    plt.legend(loc='lower right', handles=[subscribed_legend_label, freedom_legend_label])




def figure8h():
    """First creates 'discipline' field for all providers in the Original 1figr dataset.
    Then splits elsevier into elsevier freedom provider and elsevier subscribed titles provider
    
    This is counting papers by discipline for the subscribed titles and freedom collection providers
    
    Chart Type: Dot Plot/Scatter Plot
    Y-Axis: Discipline
    Y-Axis Data Source: Original 1Figr Dataset, Journals Per Provider, Provider
                        Elsevier_2019, Subscribed Journal List 2019
    X-Axis: Number of Papers
    X-Axis Data Source: Original 1Figr Dataset, Journals Per Provider, Provider
                        Elsevier_2019, Subscribed Journal List 2019

    """

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
        subscribed_jr5_downloads = subscribed_subset_by_discipline['Papers'].sum()

        freedom_subset_by_discipline = freedom_collection_provider.loc[freedom_collection_provider['Discipline'] == discipline]
        freedom_jr5_downloads = freedom_subset_by_discipline['Papers'].sum()
        
        stats_by_discipline.append((discipline, subscribed_jr5_downloads, freedom_jr5_downloads))
            
    #sorts disciplines by sum of total # of jr5 downloads
    arrangement = sorted(stats_by_discipline, key=lambda x: (x[1] + x[2])) 
    
    #splitting elements of tuples in arrangement into lists so it is easier to plot
    disciplines_list = [i[0] for i in arrangement]
    subscribed_total = [i[1] for i in arrangement]
    freedom_total = [i[2] for i in arrangement]


    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle(f'Papers (Published Articles) by Discipline')
 
    plot = plt.scatter(subscribed_total, disciplines_list, color='blue')
    plot2 = plt.scatter(freedom_total, disciplines_list, color='orange')

    subscribed_legend_label = mpatches.Patch(color='blue', label='Elsevier Subscribed')
    freedom_legend_label = mpatches.Patch(color='orange', label='Elsevier Freedom')
    plt.xlabel('Number of Papers')
    plt.legend(loc='lower right', handles=[subscribed_legend_label, freedom_legend_label])
    


    
    
    