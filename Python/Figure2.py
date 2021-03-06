
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 14:04:34 2019

@author: ep9k
"""

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
import matplotlib.patches as mpatches

import reusable_functions as rf

#Change these global variables to your corresponding filename and institution name

filename = '1figr_U_Virginia_Original (1) (1).xlsx'
your_institution = 'UVA'


"""
Documentation Format
----------------------------------------------------------------
Summary

Chart Type: Chart Type Name
Y-Axis: Dependent Variable Name
Y-Axis Data Source: SheetName, ColumnName
X-Axis:
X-Axis Data Source:

Supplemental Information
"""

def figure2a():
    """A measurement of currency. Compares JR5 downloads to JR1 downloads for each of the big 7 providers.
    JR5 downloads are 2017 articles downloaded in 2017.
    JR1 downloads are all years articles downloaded in 2017.
    We want to see what % of current articles people are downloading.

    Chart Type: Bar Graph
    Y-Axis: Percent of Total
    Y-Axis Data Source: Original 1Figr Dataset, Journals Per Provider
    X-Axis: Provider Names
    X-Axis Data Source: Original 1Figr Dataset, Journals Per Provider
    """
    
    data = pd.read_excel(filename, sheet_name='Journals per Provider', skiprows=8)
    
    big5 = ['Sage', 'Springer', 'Taylor & Francis', 'Wiley', 'Elsevier']
    
    percent_jr5_of_jr1 = []
    
    for provider_name in big5:
        
        subset_by_provider = data.loc[data['Provider'] == provider_name]

        journals_data = subset_by_provider.groupby('Journal', as_index=False).sum().values.tolist()
        
        for i in journals_data:
            if i[0] == provider_name:
                jr1_total = i[4]
                jr5_total = i[5]
                ratio = jr5_total/jr1_total
                percent_jr5_of_jr1.append(ratio)

    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle(f'Percent JR5 downloads of JR1 downloads (for 2017)')
    plot = plt.bar(big5, percent_jr5_of_jr1, width=.8, color='green')   
    plt.ylabel('Percent of Total')
    plt.ylim(0, 1)  #changes top and bottom limit of y axis in plot
    plt.xticks(rotation=90)

    plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.0%}'))    #formats y axis as %

    for i in plot:
        score = i.get_height()
        
        plt.text(i.get_x() + i.get_width()/2, 
                 1.05 * score, 
                 '{:.1%}'.format(score),
                 ha='center',
                 va='bottom')


def figure2b():
    """A measurement of currency. Compares JR5 downloads to JR1 downloads for each of the big 7 providers.
    JR5 downloads are 2017 articles downloaded in 2017.
    JR1 downloads are all years articles downloaded in 2017.
    We want to see what % of current articles people are downloading.
    Adds the 'Elsevier Freedom Collection' and 'Elsevier Subscribed Titles', making it the big 7 providers

    Chart Type: Bar Graph
    Y-Axis: Percent of Total
    Y-Axis Data Source: Original 1Figr Dataset, Journals Per Provider, Provider
                        Elsevier_2019, Subscribed Journal List 2019
    X-Axis: Provider Names
    X-Axis Data Source: Original 1Figr Dataset, Journals Per Provider, Provider
                        Elsevier_2019, Subscribed Journal List 2019
    
    """
    
    data = pd.read_excel(filename, sheet_name='Journals per Provider', skiprows=8)
    
    big7 = ['Sage', 'Springer', 'Taylor & Francis', 'Wiley', 'Elsevier Freedom Collection', 'Elsevier Subscribed Titles', 'Elsevier Unmatched']
    
    percent_jr5_of_jr1 = []
    
    for provider_name in big7:
        
        subset_by_provider = data.loc[data['Provider'] == provider_name]

        journals_data = subset_by_provider.groupby('Journal', as_index=False).sum().values.tolist()
        
        for i in journals_data:
            if i[0] == provider_name:
                jr1_total = i[4]
                jr5_total = i[5]
                ratio = jr5_total/jr1_total
                percent_jr5_of_jr1.append(ratio)
                
                
    #make ratio of jr5 to jr1 downloads for elsevier freedom collection
    elsevier_freedom_collection = rf.make_freedom_collection_provider()

    elsevier_freedom_jr5_downloads = elsevier_freedom_collection['Downloads JR5 2017 in 2017'].sum()
    elsevier_freedom_jr1_downloads = elsevier_freedom_collection['Downloads JR1 2017'].sum()

    elsevier_freedom_ratio = elsevier_freedom_jr5_downloads/elsevier_freedom_jr1_downloads
    percent_jr5_of_jr1.append(elsevier_freedom_ratio)
    
    #make ratio of jr5 to jr1 downloads for elsevier subscribed titles
    elsevier_subscribed_titles = rf.make_elsevier_subscribed_titles_provider()
    
    elsevier_subscribed_jr5_downloads = elsevier_subscribed_titles['Downloads JR5 2017 in 2017'].sum()
    elsevier_subscribed_jr1_downloads = elsevier_subscribed_titles['Downloads JR1 2017'].sum()

    elsevier_subscribed_ratio = elsevier_subscribed_jr5_downloads/elsevier_subscribed_jr1_downloads
    percent_jr5_of_jr1.append(elsevier_subscribed_ratio)
    
    #make ratio of jr5 to jr1 downloads for elsevier unmatched titles
    elsevier_unmatched_titles = rf.make_elsevier_unmatched_provider()
    
    elsevier_unmatched_jr5_downloads = elsevier_unmatched_titles['Downloads JR5 2017 in 2017'].sum()
    elsevier_unmatched_jr1_downloads = elsevier_unmatched_titles['Downloads JR1 2017'].sum()

    elsevier_unmatched_ratio = elsevier_unmatched_jr5_downloads/elsevier_unmatched_jr1_downloads
    percent_jr5_of_jr1.append(elsevier_unmatched_ratio)

                              
    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle(f'Percent JR5 downloads of JR1 downloads (for 2017)')
    plot = plt.bar(big7, percent_jr5_of_jr1, width=.8, color='green')   
    plt.ylabel('Percent of Total')
    plt.ylim(0, 1)  #changes top and bottom limit of y axis in plot
    plt.xticks(rotation=90)

    plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.0%}'))    #formats y axis as %

    for i in plot:
        score = i.get_height()
        
        plt.text(i.get_x() + i.get_width()/2, 
                 1.05 * score, 
                 '{:.1%}'.format(score),
                 ha='center',
                 va='bottom')



        
        

   
    
    